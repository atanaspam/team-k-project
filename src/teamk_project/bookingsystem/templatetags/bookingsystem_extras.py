from bookingsystem.models import Client, Session, UserSelectsSession
from django import template
from django.forms.fields import CheckboxInput
from django.db.models import Q
from datetime import timedelta
import datetime, time, re

register = template.Library()

ageGroups = ['7-10', '10-12', '12-15', '15-21']

def getAgeGroup(age):
	global ageGroups
	for group in ageGroups:
		temp = group.split('-')
		if (age in range(int(temp[0]), int(temp[1]))):
			return group
	return -1

# Check if certain type

@register.filter
def is_manager(value):
    return value.groups.filter(name='Manager').exists()

@register.filter
def is_coach(value):
    return value.groups.filter(name='Coach').exists()

@register.filter
def is_parent(value):
    return value.groups.filter(name='Parent').exists()

# Check if field is a checkbox

@register.filter(name='is_checkbox')
def is_checkbox(value):
    print value.name
    return isinstance(value, CheckboxInput)

# Check if block is not empty

@register.filter(name='nonEmpty')
def nonEmpty(block, childID):
    # Get child
	child = Client.objects.get(uid=childID)
    # Get age of child
	age = datetime.date.today() - child.dateofbirth
    # Get booked sessions
	booked = UserSelectsSession.objects.filter(user_uid=child.uid)
    # Get available session (excluding already booked sessions)
	available = Session.objects.filter(~Q(sessionid__in=[
                                       session.session_sessionid.sessionid 
                                       for session in booked]))
    # Get age group
	agegroupp=getAgeGroup(age.days/365)
 	if not agegroupp==-1:
        # Filter available sessions
		sessions = available.filter((Q(begintime__gte=datetime.datetime.now())
                                    & Q(begintime__gte=block.begindate)) & 
                                    Q(begintime__lte=block.enddate) & 
                                    Q(agegroup=agegroupp) & Q(isfull=0))
	else:
		sessions = Session.objects.none()
	return sessions.exists()

# Allows to add classes to a field

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})

# Order data by fields

@register.filter
def orderby(data, field):
    return data.order_by(field)

# Not Used / Not working

@register.filter
def is_anon(value):
	print value.is_anonymous()
	return value.is_anonymous()