from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('bookingsystem/index.html', context_dict, context)

def sessions(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('bookingsystem/sessions.html', context_dict, context)

def attendance(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('bookingsystem/attendance.html', context_dict, context)

def editProfile(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('bookingsystem/editProfile.html', context_dict, context)





