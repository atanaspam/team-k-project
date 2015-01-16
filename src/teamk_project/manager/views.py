from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('manager/index.html', context_dict, context)

def bookings(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('manager/bookings.html', context_dict, context)

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
	context_dict={}
	return render_to_response('manager/members.html', context_dict, context)

def confirmbooking(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('manager/confirmbooking.html', context_dict, context)

def audit(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('manager/audit.html', context_dict, context)



