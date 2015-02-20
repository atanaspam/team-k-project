from django import forms
from bookingsystem.models import Block, Session, Client
from django.forms import widgets
from datetime import date, time, timedelta
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User

import re
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import Widget, Select, MultiWidget
from django.utils.safestring import mark_safe

#from django.forms import MultiWidget

# Source: https://djangosnippets.org/snippets/1202/
################################################################################
__all__ = ('SelectTimeWidget', 'SplitSelectDateTimeWidget')

# Attempt to match many time formats:
# Example: "12:34:56 P.M."  matches:
# ('12', '34', ':56', '56', 'P.M.', 'P', '.', 'M', '.')
# ('12', '34', ':56', '56', 'P.M.')
# Note that the colon ":" before seconds is optional, but only if seconds are omitted
time_pattern = r'(\d\d?):(\d\d)(:(\d\d))? *([aApP]\.?[mM]\.?)?$'

RE_TIME = re.compile(time_pattern)
# The following are just more readable ways to access re.matched groups:
HOURS = 0
MINUTES = 1
SECONDS = 3
MERIDIEM = 4

class SelectTimeWidget(Widget):

    hour_field = '%s_hour'
    minute_field = '%s_minute'
    #second_field = '%s_second'
    meridiem_field = '%s_meridiem'
    twelve_hr = False # Default to 24hr.

    def __init__(self, attrs=None, hour_step=None, minute_step=None, second_step=None, twelve_hr=False):

        self.attrs = attrs or {}

        if twelve_hr:
            self.twelve_hr = True # Do 12hr (rather than 24hr)
            self.meridiem_val = 'a.m.' # Default to Morning (A.M.)

        if hour_step and twelve_hr:
            self.hours = range(1,13,hour_step)
        elif hour_step: # 24hr, with stepping.
            self.hours = range(0,24,hour_step)
        elif twelve_hr: # 12hr, no stepping
            self.hours = range(1,13)
        else: # 24hr, no stepping
            self.hours = range(0,24)
            minute_step = 10
        if minute_step:
            self.minutes = range(0,60,minute_step)
        else:
            self.minutes = range(0,60)

        #if second_step:
        #    self.seconds = range(0,60,second_step)
        #else:
        #    self.seconds = range(0,60)

    def render(self, name, value, attrs=None):
        try: # try to get time values from a datetime.time object (value)
            hour_val, minute_val = value.hour, value.minute
            if self.twelve_hr:
                if hour_val >= 12:
                    self.meridiem_val = 'p.m.'
                else:
                    self.meridiem_val = 'a.m.'
        except AttributeError:
            hour_val = minute_val = 0
            if isinstance(value, basestring):
                match = RE_TIME.match(value)
                if match:
                    time_groups = match.groups();
                    hour_val = int(time_groups[HOURS]) % 24 # force to range(0-24)
                    minute_val = int(time_groups[MINUTES])
                   # if time_groups[SECONDS] is None:
                   #     selfecond_val = 0
                   # else:
                   #     second_val = int(time_groups[SECONDS])

                    # check to see if meridiem was passed in
                    if time_groups[MERIDIEM] is not None:
                        self.meridiem_val = time_groups[MERIDIEM]
                    else: # otherwise, set the meridiem based on the time
                        if self.twelve_hr:
                            if hour_val >= 12:
                                self.meridiem_val = 'p.m.'
                            else:
                                self.meridiem_val = 'a.m.'
                        else:
                            self.meridiem_val = None


        # If we're doing a 12-hr clock, there will be a meridiem value, so make sure the
        # hours get printed correctly
        if self.twelve_hr and self.meridiem_val:
            if self.meridiem_val.lower().startswith('p') and hour_val > 12 and hour_val < 24:
                hour_val = hour_val % 12
            elif hour_val == 0:
                hour_val = 12

        output = []
        if 'id' in self.attrs:
            id_ = self.attrs['id']
        else:
            id_ = 'id_%s' % name

        # For times to get displayed correctly, the values MUST be converted to unicode
        # When Select builds a list of options, it checks against Unicode values
        hour_val = u"%.2d" % hour_val
        minute_val = u"%.2d" % minute_val
        #second_val = u"%.2d" % second_val

        hour_choices = [("%.2d"%i, "%.2d"%i) for i in self.hours]
        local_attrs = self.build_attrs(id=self.hour_field % id_)
        select_html = Select(choices=hour_choices).render(self.hour_field % name, hour_val, local_attrs)
        output.append(select_html)

        minute_choices = [("%.2d"%i, "%.2d"%i) for i in self.minutes]
        local_attrs['id'] = self.minute_field % id_
        select_html = Select(choices=minute_choices).render(self.minute_field % name, minute_val, local_attrs)
        output.append(select_html)

        ########################################################################
        ##################      SECONDS GO HERE         ########################
        ########################################################################

        #second_choices = [("%.2d"%i, "%.2d"%i) for i in self.seconds]
        #local_attrs['id'] = self.second_field % id_
        #select_html = Select(choices=second_choices).render(self.second_field % name, second_val, local_attrs)
        #output.append(select_html)

        if self.twelve_hr:
            #  If we were given an initial value, make sure the correct meridiem gets selected.
            if self.meridiem_val is not None and  self.meridiem_val.startswith('p'):
                    meridiem_choices = [('p.m.','p.m.'), ('a.m.','a.m.')]
            else:
                meridiem_choices = [('a.m.','a.m.'), ('p.m.','p.m.')]

            local_attrs['id'] = local_attrs['id'] = self.meridiem_field % id_
            select_html = Select(choices=meridiem_choices).render(self.meridiem_field % name, self.meridiem_val, local_attrs)
            output.append(select_html)

        return mark_safe(u'\n'.join(output))

    def id_for_label(self, id_):
        return '%s_hour' % id_
    id_for_label = classmethod(id_for_label)

    def value_from_datadict(self, data, files, name):
        #print name
        # if there's not h:m:s data, assume zero:
        h = data.get(self.hour_field % name, 0) # hour
        m = data.get(self.minute_field % name, 0) # minute
        #s = data.get(self.second_field % name, 0) # second
        meridiem = data.get(self.meridiem_field % name, None)
        #print 'AAAA'
        #print maridiem
        #NOTE: if meridiem is None, assume 24-hr
        if meridiem is not None:
            if meridiem.lower().startswith('p') and int(h) != 12:
                h = (int(h)+12)%24
            elif meridiem.lower().startswith('a') and int(h) == 12:
                h = 0
        s = 0
        if (int(h) == 0 or h) and m and s:
           # print h + m + s + 'AAA'
            return '%s:%s:%s' % (h, m, s)
        #print '%s:%s:%s' % (h, m, s)
        #print str(time(int(h), int(m)))
        #return str(time(int(h), int(m)))
        #print data.get(name, None)
        return data.get(name, None)

class DateSelectorWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):

        years = [(year, year) for year in (2014, 2015, 2016)] #### RED ALERT !!! THIS IS HARDOCDED !
        days = [(day, day) for day in range(1, 31)]
        months = [(1,'January'),(2,'February'),(3,'March'),(4,'April'),(5,'May'),(6,'June'),(7,'July'),(8,'August'),(9,'September'),(10,'October'),(11,'November'),(12,'December')]
        _widgets = (
            widgets.Select(attrs=attrs, choices=days),
            widgets.Select(attrs=attrs, choices=months),
            widgets.Select(attrs=attrs, choices=years),
        )
        super(DateSelectorWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            #print value
            return value
        return [None, None, None]

    def format_output(self, rendered_widgets):
        return u''.join(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        datelist = [
            widget.value_from_datadict(data, files, name + '_%s' % i)
            for i, widget in enumerate(self.widgets)]
        try:
            D = date(day=int(datelist[0]), month=int(datelist[1]),
                    year=int(datelist[2]))
        except ValueError:
            return ''
        else:
            return str(D)

class BlockForm(forms.ModelForm):

    #blockid = forms.IntegerField()
    begindate = forms.DateField(widget=DateSelectorWidget(), help_text="Beginning of the block")
    enddate = forms.DateField(widget=DateSelectorWidget(), help_text="End of the block")
    label = forms.CharField(max_length=40, help_text="User Friendly name.")
    type = forms.Select()
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Block
        fields = ('begindate', 'enddate', 'label', 'type')

class WeekBlockForm(forms.ModelForm):

    # Get the next Monday
    today = date.today()
    today += timedelta(days=-today.weekday())

    WEEK_CHOICES = []
    # Get the next 20 Mondays and add them to the select Field
    for i in range(0,20):
        today += timedelta(weeks=1)
        WEEK_CHOICES += [(today, today.strftime("%d/%m/%y"))]
    #print WEEK_CHOICES

    #blockid = forms.IntegerField()
    begindate = forms.DateField(widget=forms.Select(choices=WEEK_CHOICES), help_text="Beginning of the block")
    label = forms.CharField(max_length=40, help_text="User Friendly name.")
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Block
        fields = ('begindate', 'label')

class SplitSelectDateTimeWidget(widgets.MultiWidget):

    def __init__(self, attrs=None, hour_step=None, minute_step=None, second_step=None, twelve_hr=None, years=None):

        widgets = (SelectDateWidget(attrs=attrs, years=years), SelectTimeWidget(attrs=attrs, hour_step=hour_step, minute_step=minute_step, second_step=second_step, twelve_hr=twelve_hr))
        super(SplitSelectDateTimeWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.date(), value.time().replace(microsecond=0)]
        return [None, None]

    def format_output(self, rendered_widgets):

        rendered_widgets.insert(-1, '<br/>')
        return u''.join(rendered_widgets)

################################################################################
#### TO BE REMOVED.
################################################################################
class SessionForm(forms.ModelForm):

    duration = forms.Select()
    begintime = forms.DateTimeField(widget=SplitSelectDateTimeWidget(), help_text="Beginning of the session")
    endtime = forms.DateTimeField(widget=SplitSelectDateTimeWidget(), help_text="End of the session")
    block_blockid = forms.IntegerField(help_text="Which block it belongs to")
    capacity = forms.IntegerField(help_text="Capacity of the session")
    agegroup = forms.CharField(help_text="Associated age group")
    skillgroup = forms.CharField(help_text="Associated skill group")
    class Meta:
        model = Session


class SessionForm1(forms.ModelForm):

    #duration = forms.Select()
    begindate = forms.DateField(widget=DateSelectorWidget(), help_text="Beginning of the session")
    begintime = forms.TimeField(widget=SelectTimeWidget(), help_text="When the session begins")
    endtime = forms.TimeField(widget=SelectTimeWidget(), help_text="When the session ends")
    #block_blockid = forms.IntegerField(help_text="Which block it belongs to")
    capacity = forms.IntegerField(help_text="Capacity of the session")
    agegroup = forms.CharField(help_text="Associated age group")
    skillgroup = forms.CharField(help_text="Associated skill group")
    class Meta:
        model = Session
        fields = ('begindate', 'begintime', 'endtime', 'capacity', 'agegroup', 'skillgroup')

class RegisterForm(forms.ModelForm):
    username = forms.CharField(help_text="Username:")
    first_name = forms.CharField(help_text="First Name:")
    last_name = forms.CharField(help_text="Last Name:")
    email = forms.CharField(help_text="Email:")
    password = forms.PasswordInput()
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class EditPersonalDetailsForm(forms.ModelForm):
    email = forms.EmailField(help_text="Email:")
    telephone = forms.IntegerField(help_text="Telephone:")
    class Meta:
        model = Client
        fields = ('email', 'telephone')

class CreateChildForm(forms.ModelForm):
    firstname = forms.CharField(help_text="First Name:")
    lastname = forms.CharField(help_text="Surname:")
    email = forms.CharField(help_text="Email:")
    telephone = forms.IntegerField(help_text="Telephone:")
    age = forms.IntegerField
    genderid = forms.Select()
    class Meta:
        model = Client
        fields = ('firstname', 'lastname', 'email', 'telephone', 'age', 'genderid')




