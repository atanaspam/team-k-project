from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from bookingsystem.models import Client
from django.contrib.auth.decorators import login_required, user_passes_test

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

def is_manager(user):
    return user.groups.filter(name='Manager').exists()

def is_coach(user):
    return user.groups.filter(name='Coach').exists()

def is_parent(user):
    return user.groups.filter(name='Parent').exists()

@login_required
@user_passes_test(is_coach)
def coachIndex(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('coach/index.html', context_dict, context)

@login_required
@user_passes_test(is_coach)
def sessions(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('coach/sessions.html', context_dict, context)

@login_required
@user_passes_test(is_coach)
def attendance(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('coach/attendance.html', context_dict, context)

@login_required
@user_passes_test(is_coach)
def coachEditProfile(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('coach/editProfile.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def managerIndex(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('manager/index.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def loggedin(request):
	context = RequestContext(request)
	# Here we have some interaction with the model
	# We then plug the results of the interaction in the dictionary..
	return render_to_response('manager/loggedin.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def managerBookings(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('manager/bookings.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def confirmbooking(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('manager/confirmbooking.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def coaches(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('manager/coaches.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def coachProfile(request):
 	context = RequestContext(request)
 	context_dict={}
 	return render_to_response('manager/coachProfile.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def members(request):
    context = RequestContext(request)
    context_dict={}
    return render_to_response('manager/members.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def audit(request):
 	context = RequestContext(request)
 	context_dict={}
 	return render_to_response('manager/audit.html', context_dict, context)
 	
@login_required
@user_passes_test(is_parent)
def parentIndex(request):
	context = RequestContext(request)
	parent = request.user
	### This query gets all the "Children" of the user with UiD 1 ###
	children = Client.objects.filter(belongsto='1')
	### This just gets the current user (if he is not logged in he is Anonymous)
	context_dict = {'children': children}
	context_dict['parent'] = parent
	return render_to_response('parent/index.html', context_dict, context)

@login_required
@user_passes_test(is_parent)
def parentBookings(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parent/bookings.html', context_dict, context)

@login_required
@user_passes_test(is_parent)
def childrenList(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parent/childrenList.html', context_dict, context)

@login_required
@user_passes_test(is_parent)
def childProfile(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parent/childProfile.html', context_dict, context)

@login_required
@user_passes_test(is_parent)
def addNewChild(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parent/addNewChild.html', context_dict, context)

@login_required
@user_passes_test(is_parent)
def payments(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parent/payments.html', context_dict, context)

@login_required
@user_passes_test(is_parent)
def parentEditProfile(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parent/editProfile.html', context_dict, context)





