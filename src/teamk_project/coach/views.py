from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
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

def editProfile(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('coach/editProfile.html', context_dict, context)





