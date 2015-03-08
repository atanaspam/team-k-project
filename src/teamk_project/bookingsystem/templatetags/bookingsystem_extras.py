from django import template
from bookingsystem.models import Client, Session, UserSelectsSession
from datetime import timedelta
from django.db.models import Q
import datetime, time, re

register = template.Library()
ageGroups = ['7-10', '10-12', '12-15', '15-21']

def getAgeGroup(age):
	global ageGroups
	for group in ageGroups:
		temp = group.split('-')
		if (age in range(int(temp[0]), int(temp[1]))):
			return group
	return NULL

@register.filter
def is_manager(value):
    return value.groups.filter(name='Manager').exists()

@register.filter
def is_coach(value):
    return value.groups.filter(name='Coach').exists()

@register.filter
def is_parent(value):
    return value.groups.filter(name='Parent').exists()

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})

@register.filter
def orderby(data, field):
    return data.order_by(field)

@register.filter(name='nonEmpty')
def nonEmpty(block, childID):
	child = Client.objects.get(uid=childID)
	age = datetime.date.today() - child.dateofbirth
	booked = UserSelectsSession.objects.filter(user_uid=child.uid)
	available = Session.objects.filter(~Q(sessionid__in=[session.session_sessionid.sessionid for session in booked]) )
 	sessions = available.filter((Q(begintime__gte=datetime.datetime.now()) & Q(begintime__gte=block.begindate)) & Q(begintime__lte=block.enddate)  & Q(agegroup=getAgeGroup(age.days/365)) & Q(isfull=0))# & Q(block_blockid=block.blockid))
	return sessions.exists()

@register.filter
def is_anonymous(value):
    return value.is_anonymous()
