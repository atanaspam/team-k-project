from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from bookingsystem.models import Client, Session
from bookingsystem.models import Block
from bookingsystem.models import UserSelectsSession
from bookingsystem.models import Payment
from django.contrib.auth.decorators import login_required, user_passes_test
import datetime

@login_required
def index(request):
	return render('index.html')

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
	parent = request.user
	##			PENDING SESSIONS RETRIEVAL		##
	sessions = UserSelectsSession.objects.filter(status = 'P').values_list('user_uid')
	sessions1 = UserSelectsSession.objects.filter(status = 'P').values_list('session_sessionid')
	users = Client.objects.filter(uid__in=sessions) 
	sessionDetails = Session.objects.filter(sessionid__in = sessions1)
	pendingSessions = UserSelectsSession.objects.filter(status = 'P')
	##			PENDING PAYERS RETRIEVAL		##
	nonPaidUsers = Payment.objects.filter(haspayed = '0').values_list('usertopay')
	pendingUsers = Client.objects.filter(uid__in=nonPaidUsers)
	paymentInfo = Payment.objects.filter(haspayed = '0')
	## 			DATA COMMUNICATION				##
	context_dict={'parent':parent}
	context_dict['pending'] = pendingSessions
	context_dict['users'] = users
	context_dict['sessions'] = sessionDetails
	context_dict['pendingusers'] = pendingUsers
	context_dict['pendingpayments'] = paymentInfo
	return render_to_response('manager/index.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def loggedin(request):
	context = RequestContext(request)
	# Here we have some interaction with the model7
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
def managerSessions(request):
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
	user = request.user
	### This query gets all the "Children" of the user with UiD 1 ###
	children = Client.objects.filter(belongsto=user.id)
	### This just gets the current user (if he is not logged in he is Anonymous)
	moneyToPay = Payment.objects.filter(usertopay__in=children)
	context_dict = {'children': children}
	context_dict['parent'] = user
	context_dict['payments'] = moneyToPay
	return render_to_response('parent/index.html', context_dict, context)

@login_required
@user_passes_test(is_parent)
def parentBookings(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parent/bookings.html', context_dict, context)

@login_required
@user_passes_test(is_parent)
def childSessions(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parent/childSessions.html', context_dict, context)

@login_required
@user_passes_test(is_parent)
def bookSessions(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parent/bookSessions.html', context_dict, context)

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
	child = request.user
	today = datetime.datetime.today()
	print 'No Argument'
	### This query gets all the "Children" of the user with UiD 1 ###
	children = Client.objects.filter(belongsto='1')
	### This just gets the current user (if he is not logged in he is Anonymous)
	context_dict = {'children': children}
	#context_dict['parent'] = parent
	return render_to_response('parent/childProfile.html', context_dict, context)

login_required
@user_passes_test(is_parent)
def childProfile1(request, num):
	context = RequestContext(request)
	child = Client.objects.get(uid = num)
	today = datetime.datetime.now()
	### This query gets all the "Children" of the user with UiD 1 ###
	#Sessions = Block.objects.filter(blockid = '40')
	sessions = Session.objects.filter(begintime__range = ['2015-01-25', '2015-01-31'])
	print '1 Argument' 
	### This just gets the current user (if he is not logged in he is Anonymous)
	context_dict = {'dbsessions': sessions}
	#context_dict['parent'] = parent
	return render_to_response('parent/childProfile.html', context_dict, context)

login_required
@user_passes_test(is_parent)
def childProfile2(request, num):
	context = RequestContext(request)
	child = Client.objects.get(uid = num)
	today = datetime.datetime.now()
	### This query gets all the "Children" of the user with UiD 1 ###
	#Sessions = Block.objects.filter(blockid = '40')
	sessions = Session.objects.filter(begintime__range = ['2015-01-25', '2015-01-31'])
	print '2 Arguments' 
	### This just gets the current user (if he is not logged in he is Anonymous)
	context_dict = {'dbsessions': sessions}
	#context_dict['parent'] = parent
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

@login_required
@user_passes_test(is_parent)
def sessionsTimetable(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('coach/sessionsTimetable.html', context_dict, context)


def applicationApproved(request):
	print 'AAA'
	context = RequestContext(request)
	sessionID = None
	if request.method == 'GET':
		sessionID = request.GET['session_sessionid']
		print 'AAA'

		if sessionID:
			session = Category.objects.get(sessionid = int(sessionID))
	    	if session:
	    		flag = 'C'
	    		session.status = flag
	    		session.save()
	return HttpResponse('Success!')


	









