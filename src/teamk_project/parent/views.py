from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parent/index.html', context_dict, context)

def bookings(request):
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

def editProfile(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parent/editProfile.html', context_dict, context)


