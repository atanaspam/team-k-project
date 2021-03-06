from django import forms
from datetime import date, time, timedelta
from django.contrib import auth
from django.contrib.auth.models import User, Group
from django.utils.safestring import mark_safe
from django.core.exceptions import ObjectDoesNotExist
from django.forms import widgets
from django.forms.widgets import Widget, Select, MultiWidget, CheckboxSelectMultiple, CheckboxInput, TextInput, NumberInput, EmailInput
from django.forms.extras.widgets import SelectDateWidget
from bookingsystem.models import Block, Session, Client, GENDER_CHOICES, DefaultCoaches
import re


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
	second_field = '%s_second'
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

		if minute_step:
			self.minutes = range(0,60,minute_step)
		else:
			self.minutes = range(0,60)

		if second_step:
			self.seconds = range(0,60,second_step)
		else:
			self.seconds = range(0,60)

	def render(self, name, value, attrs=None):
		try: # try to get time values from a datetime.time object (value)
			hour_val, minute_val, second_val = value.hour, value.minute, value.second
			if self.twelve_hr:
				if hour_val >= 12:
					self.meridiem_val = 'p.m.'
				else:
					self.meridiem_val = 'a.m.'
		except AttributeError:
			hour_val = minute_val = second_val = 0
			if isinstance(value, basestring):
				match = RE_TIME.match(value)
				if match:
					time_groups = match.groups();
					hour_val = int(time_groups[HOURS]) % 24 # force to range(0-24)
					minute_val = int(time_groups[MINUTES])
					if time_groups[SECONDS] is None:
						second_val = 0
					else:
						second_val = int(time_groups[SECONDS])
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
		second_val = u"%.2d" % second_val
		hour_choices = [("%.2d"%i, "%.2d"%i) for i in self.hours]
		local_attrs = self.build_attrs(id=self.hour_field % id_)
		select_html = Select(choices=hour_choices).render(self.hour_field % name, hour_val, local_attrs)
		output.append(select_html)

		minute_choices = [("%.2d"%i, "%.2d"%i) for i in self.minutes]
		local_attrs['id'] = self.minute_field % id_
		select_html = Select(choices=minute_choices).render(self.minute_field % name, minute_val, local_attrs)
		output.append(select_html)

		# second_choices = [("%.2d"%i, "%.2d"%i) for i in self.seconds]
		# local_attrs['id'] = self.second_field % id_
		# select_html = Select(choices=second_choices).render(self.second_field % name, second_val, local_attrs)
		# output.append(select_html)

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
		# if there's not h:m:s data, assume zero:
		h = data.get(self.hour_field % name, 0) # hour
		m = data.get(self.minute_field % name, 0) # minute
		#s = data.get(self.second_field % name, 0) # second
		meridiem = data.get(self.meridiem_field % name, None)

		#NOTE: if meridiem is None, assume 24-hr
		if meridiem is not None:
			if meridiem.lower().startswith('p') and int(h) != 12:
				h = (int(h)+12)%24
			elif meridiem.lower().startswith('a') and int(h) == 12:
				h = 0

		if (int(h) == 0 or h) and m:# and s:
			return '%s:%s' % (h, m)

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
			D = date(day=int(datelist[0]), month=int(datelist[1]), year=int(datelist[2]))
		except ValueError:
			return ''
		else:
			return str(D)

class DateSelectorWidget1(widgets.MultiWidget):
	def __init__(self, attrs=None):
		years = [(year, year) for year in range(date.today().year-30, date.today().year)]
		days = [(day, day) for day in range(1, 31)]
		months = [(1,'January'),(2,'February'),(3,'March'),(4,'April'),(5,'May'),(6,'June'),(7,'July'),(8,'August'),(9,'September'),(10,'October'),(11,'November'),(12,'December')]
		_widgets = (
			widgets.Select(attrs=attrs, choices=days),
			widgets.Select(attrs=attrs, choices=months),
			widgets.Select(attrs=attrs, choices=years),
		)
		super(DateSelectorWidget1, self).__init__(_widgets, attrs)

	def decompress(self, value):
		if value:
			#print value
			return value
		return [None, None, None]

	def format_output(self, rendered_widgets):
		return u''.join(rendered_widgets)

	def value_from_datadict(self, data, files, name):
		datelist = [widget.value_from_datadict(data, files, name + '_%s' % i)
		for i, widget in enumerate(self.widgets)]
		try:
			D = date(day=int(datelist[0]), month=int(datelist[1]), year=int(datelist[2]))
		except ValueError:
			return ''
		else:
			return str(D)

class BlockForm(forms.ModelForm):
	begindate = forms.DateField(widget=DateSelectorWidget(attrs={'style': 'width:33.3%'}), help_text="Beginning of the block")
	enddate = forms.DateField(widget=DateSelectorWidget(attrs={'style': 'width:33.3%'}), help_text="End of the block")
	label = forms.CharField(max_length=40, help_text="User Friendly name.")
	# An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Block
		fields = ['begindate', 'enddate', 'label']

class BlockFormMore(BlockForm):
	num_choices = ( (0, "Monday"), (1, "Tuesday"), (2, "Wednesday"), (3, "Thursday"), (4, "Friday"), (5, "Saturday"), (6, "Sunday"))
	begintime = forms.TimeField(widget=SelectTimeWidget(minute_step=10, twelve_hr=True, attrs={'style': 'width:33.3%', 'class': 'form-control col-xs-1 col-sm-1 col-md-1'}), label="Session begintime")
	agegroup = forms.ChoiceField(choices=[('7-10', '7-10'), ('10-12', '10-12'), ('12-15', '12-15'), ('15-21', '15-21')])
	weekdays = forms.MultipleChoiceField(choices=num_choices, required=True, widget=forms.CheckboxSelectMultiple(), label='Select Day')
	coachGroups = Group.objects.filter(id=3)
	coachChoices = User.objects.filter(groups=coachGroups).values_list('id','first_name', 'last_name')
	COACH_CHOICES = ( )
	for item in coachChoices:
		temp = (item[0], str(item[1] + ' ' + item[2]),)
		COACH_CHOICES += (temp,)
	coachedby = forms.ChoiceField(choices=COACH_CHOICES)
	class Meta(BlockForm.Meta):
		fields = BlockForm.Meta.fields + ['weekdays', 'coachedby']

class WeekBlockForm(forms.ModelForm):
	# Get the next Monday
	today = date.today()
	today += timedelta(days=-today.weekday())
	WEEK_CHOICES = []
	# Get the next 20 Mondays and add them to the select Field
	for i in range(0,20):
		today += timedelta(weeks=1)
		WEEK_CHOICES += [(today, today.strftime("%d/%m/%y"))]
	begindate = forms.DateField(widget=forms.Select(choices=WEEK_CHOICES, attrs={'style': 'max-width:300px'}), help_text="Beginning of the block")
	label = forms.CharField(max_length=40, help_text="User Friendly name.", widget=forms.TextInput(attrs={'style': 'max-width:300px'}))
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

class SessionForm(forms.ModelForm):
	begintime = forms.DateTimeField(widget=SplitSelectDateTimeWidget(attrs={'style': 'width:33.3%', 'class': 'form-control col-xs-1 col-sm-1 col-md-1'}), label="Beginning of the session")
	endtime = forms.DateTimeField(widget=SplitSelectDateTimeWidget(attrs={'style': 'width:33.3%', 'class': 'form-control col-xs-1 col-sm-1 col-md-1'}), label="End of the session")
	block_blockid = forms.Select()
	capacity = forms.IntegerField(label="Capacity of the session")
	agegroup = forms.CharField(label="Associated age group")
	skillgroup = forms.CharField(label="Associated skill group")
	class Meta:
		model = Session
		fields = ['begintime', 'endtime', 'block_blockid', 'capacity', 'agegroup', 'skillgroup']

class SessionEditForm(SessionForm):
	isfull = forms.BooleanField(required=False)
	block_blockid = forms.Select()
	agegroup = forms.CharField(label="Associated age group", widget=TextInput(attrs={'size':8}))
	skillgroup = forms.CharField(label="Associated skill group", widget=TextInput(attrs={'size':10}))
	capacity = forms.IntegerField(label="Capacity of the session", widget=NumberInput(attrs={'style': 'width:50px'}))
	class Meta(SessionForm.Meta):
		fields = SessionForm.Meta.fields +['isfull']

class SessionFormMore(SessionForm):
	venue_choices = ((1, "Court 1"), (2, "Court 2"), (3, "Court 3"), (4, "Court 4"), (5, "Court 5"), (6, "Court 6"))
	subvenue = forms.MultipleChoiceField(choices=venue_choices, required=True, widget=forms.SelectMultiple(), label='Venue:')
	coachGroups = Group.objects.filter(id=3)
	coachChoices = User.objects.filter(groups=coachGroups).values_list('id','first_name', 'last_name')
	COACH_CHOICES = ((0, 'None'), )
	for item in coachChoices:
		temp = (item[0], str(item[1] + ' ' + item[2]),)
		COACH_CHOICES += (temp,)
	coachedby = forms.ChoiceField(choices=COACH_CHOICES, label="Coach:")
	class Meta(SessionForm.Meta):
		fields = SessionForm.Meta.fields + ['subvenue', 'coachedby']

################################################################################
#### TO BE REMOVED.
################################################################################

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
################################################################################
class loginForm(forms.ModelForm):
	username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'style': 'max-width:200px'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'max-width:200px'}))
	class Meta:
		model = User
		fields = ('username', 'password')

	def clean(self):
		cleaned_data = self.cleaned_data
		if 'username'  in cleaned_data:
			username = cleaned_data['username']
		else:
			raise forms.ValidationError("Please enter a username")
		if 'password'  in cleaned_data:
			password = cleaned_data['password']
		else:
			raise forms.ValidationError("Please enter a password")
		username = cleaned_data['username']
		password = cleaned_data['password']
		user = auth.authenticate(username=username, password=password)
		if user:
			return cleaned_data
		else:
			print 'AAAA'
			raise forms.ValidationError("Invalid username/password combination.")

class RegisterForm(forms.ModelForm):
	username = forms.CharField(label="Username")
	first_name = forms.CharField(label="First Name")
	last_name = forms.CharField(label="Last Name")
	email = forms.CharField(label="Email")
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')

# This form is responsible for changing the personal data of Clients
class EditPersonalDetailsForm(forms.ModelForm):
	email = forms.EmailField(label="Email:")
	telephone = forms.IntegerField(label="Telephone:")
	class Meta:
		model = Client
		fields = ['email', 'telephone']
YES_OR_NO = (
	(1, 'Yes'),
	(0, 'No')
)
class ManagerEditPersonalDetailsForm(EditPersonalDetailsForm):
	ismember = forms.ChoiceField(choices=YES_OR_NO, widget=forms.Select(attrs={'class':'form-control'}))
	class Meta(EditPersonalDetailsForm.Meta):
		fields = EditPersonalDetailsForm.Meta.fields + ['ismember']

class CreateChildForm(forms.ModelForm):
	firstname = forms.CharField(label="First Name")
	lastname = forms.CharField(label="Surname")
	email = forms.EmailField(label="Email")
	telephone = forms.IntegerField(label="Telephone")
	dateofbirth = forms.DateField(widget=DateSelectorWidget1(attrs={'style': 'width:33.3%'}), label="Date Of Birth")
	genderid = forms.ChoiceField(initial="Select", label="Gender",choices=GENDER_CHOICES)
	class Meta:
		model = Client
		fields = ('firstname', 'lastname', 'email', 'telephone', 'dateofbirth', 'genderid')

# This form is responsible for changing the personal data of django contrib auth users
class EditUserPersonalDetailsForm(forms.ModelForm):
	email = forms.EmailField(label="Email:")
	password = forms.PasswordInput()
	class Meta:
		model = User
		fields = ['email', 'password']

class UserEditDetailsForm(forms.ModelForm):
	#firstName = forms.CharField(max_length=20, help_text='Your new name')
	email = forms.EmailField(label="New Email:", widget=EmailInput(attrs={'size':25}))
	telephone = forms.IntegerField(label="New Telephone:")
	class Meta:
		model = User
		fields = ['email', 'telephone']

class DefaultCoachesForm(forms.ModelForm):
	coachGroups = Group.objects.filter(id=3)
	coachChoices = User.objects.filter(groups=coachGroups)
	COACH_CHOICES = ((0, 'None'), )
	for item in coachChoices:
		temp = (item, str(item.first_name + ' ' + item.last_name),)
		COACH_CHOICES += (temp,)
	monMor = forms.ChoiceField(choices=COACH_CHOICES, label="Morning:")
	monAft = forms.ChoiceField(choices=COACH_CHOICES, label="Afternoon:")
	tueMor = forms.ChoiceField(choices=COACH_CHOICES, label="Morning:")
	tueAft = forms.ChoiceField(choices=COACH_CHOICES, label="Afternoon:")
	wedMor = forms.ChoiceField(choices=COACH_CHOICES, label="Morning:")
	wedAft = forms.ChoiceField(choices=COACH_CHOICES, label="Afternoon:")
	thuMor = forms.ChoiceField(choices=COACH_CHOICES, label="Morning:")
	thuAft = forms.ChoiceField(choices=COACH_CHOICES, label="Afternoon:")
	friMor = forms.ChoiceField(choices=COACH_CHOICES, label="Morning:")
	friAft = forms.ChoiceField(choices=COACH_CHOICES, label="Afternoon:")

	def clean_monMor(self):
		data = self.cleaned_data["monMor"]
		if User.objects.filter(username=data).exists():
			return User.objects.get(username=data)
		else:
			raise forms.ValidationError("This is not a valid user")

	def clean_monAft(self):
		data = self.cleaned_data["monAft"]
		if User.objects.filter(username=data).exists():
			return User.objects.get(username=data)
		else:
			raise forms.ValidationError("This is not a valid user")

	def clean_tueMor(self):
		data = self.cleaned_data["tueMor"]
		if User.objects.filter(username=data).exists():
			return User.objects.get(username=data)
		else:
			raise forms.ValidationError("This is not a valid user")

	def clean_tueAft(self):
		data = self.cleaned_data["tueAft"]
		if User.objects.filter(username=data).exists():
			return User.objects.get(username=data)
		else:
			raise forms.ValidationError("This is not a valid user")

	def clean_wedMor(self):
		data = self.cleaned_data["wedMor"]
		if User.objects.filter(username=data).exists():
			return User.objects.get(username=data)
		else:
			raise forms.ValidationError("This is not a valid user")

	def clean_wedAft(self):
		data = self.cleaned_data["wedAft"]
		if User.objects.filter(username=data).exists():
			return User.objects.get(username=data)
		else:
			raise forms.ValidationError("This is not a valid user")

	def clean_thuMor(self):
		data = self.cleaned_data["thuMor"]
		if User.objects.filter(username=data).exists():
			return User.objects.get(username=data)
		else:
			raise forms.ValidationError("This is not a valid user")

	def clean_thuAft(self):
		data = self.cleaned_data["thuAft"]
		if User.objects.filter(username=data).exists():
			return User.objects.get(username=data)
		else:
			raise forms.ValidationError("This is not a valid user")

	def clean_friMor(self):
		data = self.cleaned_data["friMor"]
		if User.objects.filter(username=data).exists():
			return User.objects.get(username=data)
		else:
			raise forms.ValidationError("This is not a valid user")

	def clean_friAft(self):
		data = self.cleaned_data["friAft"]
		if User.objects.filter(username=data).exists():
			return User.objects.get(username=data)
		else:
			raise forms.ValidationError("This is not a valid user")

	def clean(self):
		cleaned_data = self.cleaned_data
		# data = [
		# 	cleaned_data["monMor"],
		# 	cleaned_data["monAft"],
		# 	cleaned_data["tueMor"],
		# 	cleaned_data["tueAft"],
		# 	cleaned_data["wedMor"],
		# 	cleaned_data["wedAft"],
		# 	cleaned_data["thuMor"],
		# 	cleaned_data["thuAft"],
		# 	cleaned_data["friMor"],
		# 	cleaned_data["friAft"]
		# 	]
		# try:
		# 	for i in range(0,10):
		# 		User.objects.get(username=data[i])
		# except:
		# 	#self.add_error('monMor', "Something went wrong")
		# 	raise forms.ValidationError("An error occurred")
		return cleaned_data

	def save(self, commit=True):
		data = self.clean()
		print data
		try:
			a = DefaultCoaches.objects.get(id=1)
			a.monMor = User.objects.get(username=data["monMor"])
			a.monAft = User.objects.get(username=data["monAft"])
			a.tueMor = User.objects.get(username=data["tueMor"])
			a.tueAft = User.objects.get(username=data["tueAft"])
			a.wedMor = User.objects.get(username=data["wedMor"])
			a.wedAft = User.objects.get(username=data["wedAft"])
			a.thuMor = User.objects.get(username=data["thuMor"])
			a.thuAft = User.objects.get(username=data["thuAft"])
			a.friMor = User.objects.get(username=data["friMor"])
			a.friMor = User.objects.get(username=data["friAft"])
		except ObjectDoesNotExist:
			a = DefaultCoaches.objects.create(id=1,
					monMor=User.objects.get(username=data["monMor"]),
					monAft=User.objects.get(username=data["monAft"]),
					tueMor=User.objects.get(username=data["tueMor"]),
					tueAft=User.objects.get(username=data["tueAft"]),
					wedMor=User.objects.get(username=data["wedMor"]),
					wedAft=User.objects.get(username=data["wedAft"]),
					thuMor=User.objects.get(username=data["thuMor"]),
					thuAft=User.objects.get(username=data["thuAft"]),
					friMor=User.objects.get(username=data["friMor"]),
					friAft=User.objects.get(username=data["friAft"])
					)
		if commit:
			a.save()
		return a
	class Meta:
		model = DefaultCoaches
		exclude = ('',)


