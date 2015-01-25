from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from bookingsystem.models import Client
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	context = RequestContext(request)
	### This query gets all the "Children" of the user with UiD 1 ###
	children = Client.objects.filter(belongsto='1')
	### This just gets the current user (if he is not logged in he is Anonymous)
	parent = request.user
	context_dict = {'children': children}
	context_dict['parent'] = parent
	return render_to_response('index.html', context_dict, context)

def coachIndex(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('coach/index.html', context_dict, context)

def sessions(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('coach/sessions.html', context_dict, context)

def attendance(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('coach/attendance.html', context_dict, context)

def coachEditProfile(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('coach/editProfile.html', context_dict, context)

def managerIndex(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('manager/index.html', context_dict, context)

def loggedin(request):
	context = RequestContext(request)
	# Here we have some interaction with the model
	# We then plug the results of the interaction in the dictionary..
	return render_to_response('manager/loggedin.html', context_dict, context)

def managerBookings(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('manager/bookings.html', context_dict, context)

def confirmbooking(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('manager/confirmbooking.html', context_dict, context)

def coaches(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('manager/coaches.html', context_dict, context)

def coachProfile(request):
 	context = RequestContext(request)
 	context_dict={}
 	return render_to_response('manager/coachProfile.html', context_dict, context)

def members(request):
    context = RequestContext(request)
    users = User.objects.all()
    context_dict={'users':users}
    return render_to_response('manager/members.html', context_dict, context)

def audit(request):
 	context = RequestContext(request)
 	context_dict={}
 	return render_to_response('manager/audit.html', context_dict, context)

def parentIndex(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parent/index.html', context_dict, context)

def parentBookings(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parent/bookings.html', context_dict, context)

def childrenList(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parent/childrenList.html', context_dict, context)

def childProfile(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parent/childProfile.html', context_dict, context)

def addNewChild(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parent/addNewChild.html', context_dict, context)

def payments(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parent/payments.html', context_dict, context)

def parentEditProfile(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parent/editProfile.html', context_dict, context)





