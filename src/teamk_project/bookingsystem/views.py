from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q, Sum
from bookingsystem.models import Client, Session, Block, UserSelectsSession, Payment, SubvenueUsedforSession
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.contrib.auth import logout
from django.db import models
from django.db.models import Max
import datetime

approvalHistory = []
i = 0

lastID = -1

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
		#sessions = UserSelectsSession.objects.filter(status = 'P').values_list('user_uid')
		#sessions1 = UserSelectsSession.objects.filter(status = 'P').values_list('session_sessionid')
		#users = Client.objects.filter(uid__in=sessions)
		#sessionDetails = Session.objects.filter(sessionid__in = sessions1)
	pendingSessions = UserSelectsSession.objects.filter(status = 'P')
	##			PENDING PAYERS RETRIEVAL		##
	pendingPayments = Payment.objects.filter(haspayed=0)
	pendingUsers = pendingPayments.values_list('usertopay')
	nextArrivalDay = UserSelectsSession.objects.filter(user_uid__in=pendingUsers)
		#pendingUsers = Client.objects.filter(payment__usertopay=nonPaidUsers).select_related()
		#paymentInfo = Payment.objects.filter(haspayed = '0')

	## 			DATA COMMUNICATION				##
	context_dict={'parent':parent}
	context_dict['pending'] = pendingSessions
	context_dict['nextarrivalday'] = nextArrivalDay
	context_dict['payments'] = pendingPayments
	return render_to_response('manager/index.html', context_dict, context)


@login_required
@csrf_exempt
@user_passes_test(is_manager)
def markPaid(request):
	context = RequestContext(request)
	parent = request.user
	context_dict = {}


	if request.method == 'POST':
		for i in request.POST.getlist('kidPaid'):
			Payment.objects.filter(usertopay=i).update(haspayed=True)
			print i


		context_dict['paymentMade'] = True;


	##			PENDING SESSIONS RETRIEVAL		##
		#sessions = UserSelectsSession.objects.filter(status = 'P').values_list('user_uid')
		#sessions1 = UserSelectsSession.objects.filter(status = 'P').values_list('session_sessionid')
		#users = Client.objects.filter(uid__in=sessions)
		#sessionDetails = Session.objects.filter(sessionid__in = sessions1)
	pendingSessions = UserSelectsSession.objects.filter(status = 'P')
	##			PENDING PAYERS RETRIEVAL		##
	pendingPayments = Payment.objects.filter(haspayed=0)
	pendingUsers = pendingPayments.values_list('usertopay')
	nextArrivalDay = UserSelectsSession.objects.filter(user_uid__in=pendingUsers)
		#pendingUsers = Client.objects.filter(payment__usertopay=nonPaidUsers).select_related()
		#paymentInfo = Payment.objects.filter(haspayed = '0')

	## 			DATA COMMUNICATION				##
	context_dict['parent'] = parent
	context_dict['pending'] = pendingSessions
	context_dict['nextarrivalday'] = nextArrivalDay
	context_dict['payments'] = pendingPayments
	checked = request.POST.getlist("checked")




	return render_to_response('manager/index.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def loggedin(request):
	context = RequestContext(request)
	return render_to_response('manager/loggedin.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def managerBookings(request):																	#### WARNING: Repetitive code:Line 51
	context = RequestContext(request)
	parent = request.user
	##			PENDING SESSIONS RETRIEVAL		##
	pendingSessions = UserSelectsSession.objects.filter(status = 'P')
	declinedSessions = Session.objects.filter(sessionid__in=UserSelectsSession.objects.filter(status = 'R').values_list('session_sessionid'))

	## 			DATA COMMUNICATION				##
	context_dict={'parent':parent}
	context_dict['pending'] = pendingSessions
	context_dict['history'] = approvalHistory
	context_dict['declined'] = declinedSessions
	return render_to_response('manager/bookings.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def managerSessions(request):
	context = RequestContext(request)
	sessionInfo = Session.objects.all()
	venueInfo = SubvenueUsedforSession.objects.filter(session_sessionid__in=sessionInfo.values_list('sessionid'))
	#info = sessionInfo | venueInfo
	context_dict={'sessions':sessionInfo}
	return render_to_response('manager/sessions.html', context_dict, context)

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
    #clients = Client.objects.select_related('payment__usertopay')
    clients = Client.objects.raw('''
    	SELECT client.*, payment.amount 
    	FROM client 
    	LEFT JOIN payment
    	ON client.uID = payment.usertopay;
    	''')
    #print clients.query, "\n"
    context_dict={'clients':clients}

    for i in clients:
    	print i.amount

    #print clients.values_list()
    #context_dict['payments'] = Payment.objects.filter(haspayed=0)
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
	context_dict['totalDue'] = moneyToPay.filter(haspayed=False).aggregate(Sum('amount'))['amount__sum']
	return render_to_response('parent/index.html', context_dict, context)


@login_required
@user_passes_test(is_parent)
def paypalConfirm(request):
	context = RequestContext(request)
	user = request.user
	context_dict = {}

	### This query gets all the "Children" of the user with UiD 1 ###
	children = Client.objects.filter(belongsto=user.id)
	### This just gets the current user (if he is not logged in he is Anonymous)
	context_dict['children']= children
	context_dict['parent'] = user



	## !!!!!kick any user out that shouldn't be here
	#if request.META['HTTP_REFERER'] != "paypal.com":
	#	logout(request)
	#	return redirect("/")
	## !!!!!!!!!!!!!!!disabled for the demo #################

	if request.method == 'GET':
		#for i in request.GET.getlist('kidPaid'):
		i = Client.objects.filter(belongsto=request.GET['id'])
		if i:
			Payment.objects.filter(usertopay__in=i).update(haspayed=True)
			return render_to_response('parent/index.html', context_dict, context)




	moneyToPay = Payment.objects.filter(usertopay__in=children)

	context_dict['payments'] = moneyToPay
	context_dict['totalDue'] = moneyToPay.filter(haspayed=False).aggregate(Sum('amount'))['amount__sum']


	return render_to_response('parent/index.html', context_dict, context)

@login_required
@user_passes_test(is_parent)
def childrenList(request):
	context = RequestContext(request)
	user = request.user
	### This query gets all the "Children" of the user with UiD 1 ###
	children = Client.objects.filter(belongsto=user.id)
	### This just gets the current user (if he is not logged in he is Anonymous)
	moneyToPay = Payment.objects.filter(usertopay__in=children)
	context_dict = {'children': children}
	context_dict['parent'] = user
	context_dict['payments'] = moneyToPay
	return render_to_response('parent/childrenList.html', context_dict, context)

@login_required
@user_passes_test(is_parent)
def parentBookings(request):
	context = RequestContext(request)
	user = request.user
	children = Client.objects.filter(belongsto=user.id)
	context_dict = {'children': children}
	return render_to_response('parent/bookings.html', context_dict, context)


@login_required
@user_passes_test(is_parent)
def userBookings(request, num):
	context = RequestContext(request)
	child = Client.objects.get(uid=num)
	today = datetime.date.today()
	monday = today - datetime.timedelta(days=today.weekday())
	blocks = Block.objects.filter(Q(type='Week') & Q(begindate__gte=monday))
	context_dict = {'blocks': blocks}
	context_dict['child'] = child
	return render_to_response('parent/userBookings.html', context_dict, context)

@login_required
@user_passes_test(is_parent)
def userBookings1(request, num):
	child = Client.objects.get(uid=num)
	context = RequestContext(request)
	today = datetime.date.today()
	monday = today - datetime.timedelta(days=today.weekday())
	blocks = Block.objects.filter(Q(type='Week') & Q(begindate__gte=monday))
	context_dict = {'blocks': blocks}
	context_dict['child'] = child
	return render_to_response('parent/userBookings.html', context_dict, context)


@login_required
@user_passes_test(is_parent)
def confirmBookings(request, uID):
	context = RequestContext(request)
	checked = request.POST.getlist("checked")
	if checked: 
		for item in checked:
			#print item
			user = Client.objects.get(uid=uID)
			session = Session.objects.get(sessionid=item)
			t = UserSelectsSession(
				session_sessionid=session,
				user_uid=user,
				status='P'
				)
			t.save()
	context_dict = {'checked': checked}
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
	return render_to_response('parameterent/bookSessions.html', context_dict, context)

def bookSessions1(request, blockID, uID):
 	context = RequestContext(request)
 	child = Client.objects.get(uid=uID)
	owner = Block.objects.get(blockid=blockID)
 	sessions = Session.objects.filter( Q(begintime__gte=datetime.datetime.now() ) & Q(begintime__lte=owner.enddate))
 	context_dict = {'sessions': sessions}
 	context_dict['child'] = child
 	return render_to_response('parent/bookSessions.html', context_dict, context)

# def bookSessions2(request, num):
# 	context = RequestContext(request)
# 	owner = Block.objects.get(blockid=num)
# 	sessions = Session.objects.filter( Q(begintime__gte=datetime.datetime.now() ) & Q(begintime__lte=owner.enddate))
# 	context_dict = {'sessions': sessions}
# 	return render_to_response('parent/bookSessions.html', context_dict, context)

###################################################################################
####				Child Profiles depening on the uid passed					###
###################################################################################

@login_required
@user_passes_test(is_parent)
def childProfile(request, id):
	context = RequestContext(request)
	context_dict = {}
	parentid = request.user.id
	try:
		child = Client.objects.get(uid=id, belongsto=parentid)
		if child:
			context_dict['child'] = child
			return render_to_response('parent/childProfile.html', context_dict, context)
	except:
		return redirect('/bookingsystem/parent/childrenList.html')

@login_required
@user_passes_test(is_parent)
def changeChild(request):
	f_uid = request.POST.get("uid", "")
	parentid = request.user.id

	child = Client.objects.get(uid=f_uid, belongsto=parentid)
	if child:
		child.firstname = request.POST.get("firstname", "")
		child.lastname = request.POST.get("lastname", "")
		child.genderid = int(request.POST.get("genderid", ""))
		child.age = request.POST.get("age", "")
		child.telephone = request.POST.get("telephone", "")
		child.email = request.POST.get("email", "")
		child.save()

	return redirect('/bookingsystem/parent/childrenList.html')

###################################################################################
####							Adding new Child								###
###################################################################################

@login_required
@user_passes_test(is_parent)
def addNewChild(request):
	context = RequestContext(request)
	context_dict={}
	context_dict = {'parent': request.user}
	#print lastID
	return render_to_response('parent/addnewChild.html', context_dict, context)

@login_required
@user_passes_test(is_parent)
def addChild(request):
	if request.method == "POST":
		global lastID

		# THIS NEED TO BE CHANGED TO AUTOINCREMENT IN THE DATABASE!
		if (lastID == -1):
			lastID = Client.objects.all().aggregate(Max('uid')).get("uid__max")

		lastID = lastID + 1

		f_uid = lastID
		f_firstname = request.POST.get("firstname", "")
		f_lastname = request.POST.get("lastname", "")
		f_genderid = int(request.POST.get("genderid", ""))
		f_age = request.POST.get("age", "")
		f_telephone = request.POST.get("telephone", "")
		f_email = request.POST.get("email", "")
		f_medicalconditions = request.POST.get("medicalconditions", "")
		f_belongsto = request.user.id

		# VALIDATION HERE!!!

		p = Client.objects.get_or_create(uid=f_uid, firstname=f_firstname, lastname=f_lastname, genderid=f_genderid, age=f_age, telephone=f_telephone, email=f_email, belongsto=f_belongsto, experiencelevel=0, managedby=0, ismember=0)
	return redirect('/bookingsystem/parent/childrenList.html')

###################################################################################

@login_required
@user_passes_test(is_parent)
def payments(request):
	context = RequestContext(request)
	context_dict={}
	
	user = request.user
	### This query gets all the "Children" of the user with UiD 1 ###
	children = Client.objects.filter(belongsto=user.id)
	### This just gets the current user (if he is not logged in he is Anonymous)
	moneyToPay = Payment.objects.filter(usertopay__in=children)

	context_dict['children'] = children
	context_dict['parent'] = user
	context_dict['payments'] = moneyToPay
	context_dict['totalDue'] = moneyToPay.filter(haspayed=False).aggregate(Sum('amount'))['amount__sum']
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

@user_passes_test(is_manager)
def applicationApproved(request):
	global i
	context = RequestContext(request)
	sessionID = None
	if request.method == 'GET':
		sessionID = request.GET['session_sessionid']
		user = request.GET['userid']
		#print user
		if sessionID:
			session = UserSelectsSession.objects.get( Q(session_sessionid = sessionID) & Q(user_uid = user) )
	    	if session:
	    		#print session.session_sessionid
	    		approvalHistory.insert(i, session)
	    		i=(i+1)%10
	    		session.status = 'C' # set from pending to confirmed
	    		session.save()
	return HttpResponse('Success!')

################################################################################
#													Not Yet Working																			 #
################################################################################
@user_passes_test(is_manager)
def sessionInfo(request, sessionID):
	#print sessionID
	context = RequestContext(request)
	user = request.user
	# sessionID = None
	# if request.method == 'GET':
	# 	sessionID = request.GET['session_sessionid']
	# 	#print sessionID
	# 	if sessionID:
	# 		session = Session.objects.get(sessionid=sessionID)
	# 		print session
	#     	if session:
	#     		#print session.session_sessionid
	#     		context_dict={'session':session}
	sessionDetails = Session.objects.get(sessionid=sessionID)
	sessionUsers = UserSelectsSession.objects.filter(session_sessionid=sessionDetails.sessionid)
	context_dict={'details': sessionDetails}
	context_dict['users'] = sessionUsers
	return render_to_response('manager/sessionInfo.html', context_dict, context)












