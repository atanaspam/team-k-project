from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from manager.models import User
# From the model we import the User table
# See http://www.tangowithdjango.com/book/chapters/models_templates.html

def index(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('index.html', context_dict, context)

def loggedin(request):
	context = RequestContext(request)
	# Here we have some interaction with the model
	user = User.objects.get(uid='4')
	# We then plug the results of the interaction in the dictionary..
	context_dict={'users':user}
	return render_to_response('loggedin.html', context_dict, context)

def bookings(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('manager/bookings.html', context_dict, context)

def coaches(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('manager/coaches.html', context_dict, context)

def members(request):
    context = RequestContext(request)
    users = User.objects.all()
    context_dict={'users':users}
    return render_to_response('members.html', context_dict, context)

# def coachProfile(request):
# 	context = RequestContext(request)
# 	context_dict={}
# 	return render_to_response('manager/coachProfile.html', context_dict, context)

# def confirmbooking(request):
# 	context = RequestContext(request)
# 	context_dict={}
# 	return render_to_response('manager/confirmbooking.html', context_dict, context)

# def audit(request):
# 	context = RequestContext(request)
# 	context_dict={}
# 	return render_to_response('manager/audit.html', context_dict, context)



