from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.db.models import Q, Sum
from bookingsystem.models import Client, Session, Block, UserSelectsSession, Payment, SubvenueUsedforSession, sessionCoachedBy
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.contrib.auth import logout
from django.db import models
from django.db.models import Max
from bookingsystem.forms import BlockFormMore, SessionForm, EditPersonalDetailsForm, CreateChildForm, WeekBlockForm ##########################
from datetime import timedelta
import datetime, time


approvalHistory = []
i = 0
lastSessionID = -1
lastID = -1
lastBlockID = -1
ageGroups = ['7-10','10-12', '12-15', '15-19']

def getDayOfWeek(n):
	daysOfWeek = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thurday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
	return daysOfWeek[n]

def getLastID():
	global lastID
	if (lastID == -1):
		lastID = Client.objects.all().aggregate(Max('uid')).get("uid__max")
		if lastID is None:
			lastID = 1
			return lastID
	#print lastID +1
	return ++lastID

def getLastSessionID():
	global lastSessionID
	if (lastSessionID == -1):
		lastSessionID = Session.objects.all().aggregate(Max('sessionid')).get("sessionid__max")
		if lastSessionID is None:
			lastSessionID = 1
			return lastSessionID
	lastSessionID += 1
	return lastSessionID

def getLastBlockID():
	global lastBlockID
	if (lastBlockID == -1):
		lastBlockID = Block.objects.all().aggregate(Max('blockid')).get("blockid__max")
		if lastBlockID is None:
			print 'noBlock'
			lastBlockID = 1
			return lastBlockID
	lastBlockID += 1
	return lastBlockID



@login_required
def index(request):
	return render('index.html')

def is_manager(user):
    return user.groups.filter(name='Manager').exists()

def is_coach(user):
    return user.groups.filter(name='Coach').exists()

def is_parent(user):
    return user.groups.filter(name='Parent').exists()

###############################################################################
#									Coach 					   				  #
###############################################################################


@login_required
@user_passes_test(is_coach)
def coachIndex(request):
	context = RequestContext(request)
	today = datetime.date.today()
	userID = request.user.id
	todaySessions = Session.objects.filter(Q(begintime__year=today.year, begintime__month=today.month, begintime__day=today.day)).values_list('sessionid')
	todayAssignedSessions = sessionCoachedBy.objects.filter(Q(session_id__in=todaySessions) & Q(user_id=userID))
	futureAssignedSessions = sessionCoachedBy.objects.filter(user_id=userID)
	context_dict={'todayAssignedSessions':todayAssignedSessions}
	context_dict['futureAssignedSessions'] = futureAssignedSessions
	return render_to_response('coach/index.html', context_dict, context)

@login_required
@user_passes_test(is_coach)
def attendance(request, id):
	context = RequestContext(request)
	context_dict={}
	unattendedSessionObjects = UserSelectsSession.objects.filter(session_sessionid = id, status = 'C',hasattended = 0)
	attendedSessionObjects = UserSelectsSession.objects.filter(session_sessionid = id, status = 'C',hasattended = 1)

	context_dict = {'unattendedSessionObjects':unattendedSessionObjects}
	context_dict['attendedSessionObjects'] = attendedSessionObjects
	context_dict['s'] = Session.objects.get(sessionid = id)
	return render_to_response('coach/attendance.html', context_dict, context)

@login_required
@user_passes_test(is_coach)
def attended(request,id,sid):

	attendance = UserSelectsSession.objects.get(user_uid=id, session_sessionid = sid)

	currentAttendance = (not attendance.hasattended)

	attendance.hasattended = currentAttendance

	attendance.save()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#					 			NOT REQUIRED 								  #

@login_required
@user_passes_test(is_coach)
def submitAttendance(request):
	context = RequestContext(request)
	context_dict={}
	sessionID = request.POST['sessionID']
	for key in request.POST:
		if (key.startswith('attendance')):
			childID = request.POST[key]
			child = UserSelectsSession.objects.get(user_uid=childID, session_sessionid = sessionID)
			child.hasattended = 1
			child.save()
	return  redirect("index.html")

@login_required
@user_passes_test(is_coach)
def sessions(request, id):
	context = RequestContext(request)
	context_dict={}
	# today = datetime.date.today()
	# assignedSessions = Session.objects.filter(begintime__gte=today)
	# context_dict={'assignedSessions':assignedSessions}
	return render_to_response('coach/sessions.html', context_dict, context)


@login_required
@user_passes_test(is_coach)
def coachEditProfile(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('coach/editProfile.html', context_dict, context)


###############################################################################
#								End of Coach 					   			  #
###############################################################################


@login_required
@user_passes_test(is_manager)
def managerIndex(request):
	context = RequestContext(request)
	manager = request.user
	##			PENDING SESSIONS RETRIEVAL		##
	pendingSessions = UserSelectsSession.objects.filter(status = 'P')
	##			PENDING PAYERS RETRIEVAL		##
	pendingPayments = Payment.objects.filter(haspayed=0)
	pendingUsers = pendingPayments.values_list('usertopay')
	nextArrivalDay = UserSelectsSession.objects.filter(user_uid__in=pendingUsers)
		#pendingUsers = Client.objects.filter(payment__usertopay=nonPaidUsers).select_related()
		#paymentInfo = Payment.objects.filter(haspayed = '0')
	## 			DATA COMMUNICATION				##
	context_dict={'manager':manager}
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

		context_dict['paymentMade'] = True
	##			PENDING SESSIONS RETRIEVAL		##
	pendingSessions = UserSelectsSession.objects.filter(status = 'P')
	##			PENDING PAYERS RETRIEVAL		##
	pendingPayments = Payment.objects.filter(haspayed=0)
	pendingUsers = pendingPayments.values_list('usertopay')
	nextArrivalDay = UserSelectsSession.objects.filter(user_uid__in=pendingUsers)
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

################################  Block Info Pages #############################

@login_required
@user_passes_test(is_manager)
def blockInfo(request, bid):
	context = RequestContext(request)
	context_dict={}
	blocks = Block.objects.get(blockid = bid)
	blockSessions = Session.objects.filter(block_blockid = bid)

	context_dict['blocks'] = blocks
	context_dict['blockSessions'] = blockSessions

	print context_dict
	return render_to_response('manager/blockInfo.html', context_dict, context)

################################################################################
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



###################### Add block id query in context detail#####################

@login_required
@user_passes_test(is_manager)
def managerBlocks(request):
	context = RequestContext(request)
	blockInfo = Block.objects.all()
	#venueInfo = SubvenueUsedforSession.objects.filter(session_sessionid__in=sessionInfo.values_list('sessionid'))
	#info = sessionInfo | venueInfo
	context_dict={'blocks':blockInfo}
	return render_to_response('manager/blocks.html', context_dict, context)

################################################################################


@login_required
@user_passes_test(is_manager)
def confirmbooking(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('success.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def coaches(request):
	context = RequestContext(request)
	context_dict={}

	coacheGroups = Group.objects.get(name='Coach')
	allCoaches = User.objects.filter(Q(groups=coacheGroups))

	notCoaches = User.objects.filter(~Q(id__in = allCoaches))

	context_dict['allCoaches'] = allCoaches
	context_dict['notCoaches'] = notCoaches
	return render_to_response('manager/coaches.html', context_dict, context)


@login_required
@user_passes_test(is_manager)
def addNewCoach(request):
	context = RequestContext(request)
	user = request.user
	context_dict={}

	for key in request.POST:
		if (key.startswith('notCoach')):
			userID = request.POST[key]
			userObject = User.objects.get(id = userID)
			g = Group.objects.get(name='Coach')
			g.user_set.add(userObject)

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
@user_passes_test(is_manager)
def coachProfile(request, id):
 	context = RequestContext(request)
 	context_dict={}
 	coacheGroups = Group.objects.get(name='Coach')
	allCoaches = User.objects.filter(Q(groups=coacheGroups))
	userObject = User.objects.get(id = id)
	if (userObject in allCoaches):
	 	context_dict['userObject'] = userObject
	 	return render_to_response('manager/coachProfile.html', context_dict, context)
	else:
		return redirect('/bookingsystem/manager/coaches.html')

@login_required
@user_passes_test(is_manager)
def removeCoach(request, id):
	context = RequestContext(request)
 	context_dict={}
	sessionCoachedByObjects = sessionCoachedBy.objects.filter(user_id = id)
	print sessionCoachedByObjects.values_list()
	print context_dict
	if sessionCoachedByObjects:
		context_dict = {'sessionCoachedByObjects':sessionCoachedByObjects}
		context_dict['coachid'] = id
		return render_to_response('manager/removeCoach.html', context_dict, context)
	else:
		confirmRemoveCoachFunction(id)
 		return redirect('/bookingsystem/manager/coaches.html')

@login_required
@user_passes_test(is_manager)
def confirmRemoveCoach(request, id):
 	confirmRemoveCoachFunction(id)
	return redirect('/bookingsystem/manager/coaches.html')

def confirmRemoveCoachFunction(id):
 	userObject = User.objects.get(id = id)
	g = Group.objects.get(name='Coach')
	g.user_set.remove(userObject)
	sessionCoachedBy.objects.filter(user_id = id).delete()


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

    #for i in clients:
    #	print i.amount

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
	weeks = Block.objects.filter(((Q(type='Week') & Q(begindate__gte=monday))) | (Q(type='Season')))
	context_dict = {'blocks': weeks}
	context_dict['child'] = child
	return render_to_response('parent/userBookings.html', context_dict, context)

@login_required
@user_passes_test(is_parent)
def userBookings1(request, num):
	child = Client.objects.get(uid=num)
	context = RequestContext(request)
	today = datetime.date.today()
	monday = today - datetime.timedelta(days=today.weekday())
 	context_dict = {'sessions': sessions}
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
	return render_to_response('successEmb.html', context_dict, context)


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

def bookSeason(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('parameterent/bookSeason.html', context_dict, context)

def bookSeason1(request, blockID, uID):
 	context = RequestContext(request)
 	child = Client.objects.get(uid=uID)
	owner = Block.objects.get(blockid=blockID)
 	sessions = Session.objects.filter( Q(begintime__gte=datetime.datetime.now() ) & Q(begintime__lte=owner.enddate))
 	context_dict = {'sessions': sessions}
 	context_dict['child'] = child
 	return render_to_response('parent/bookSeason.html', context_dict, context)

# @login_required
# @user_passes_test(is_parent)
# def childProfile(request, id):
# 	context = RequestContext(request)
# 	context_dict = {}
# 	parentid = request.user.id
# 	child = Client.objects.get(uid=id)

# 	if request.method == 'POST':
# 		form = EditPersonalDetailsForm(request.POST)
# 		# Have we been provided with a valid form?
# 		if form.is_valid():
# 			info=form.save(commit=False)
# 			child.telephone = info.telephone
# 			child.email = info.email
# 			child.save()
# 			# Redirect on success
# 			return redirect('/success.html')
# 		else:
# 			# The supplied form contained errors - just print them to the terminal.
# 			print form.errors
# 	else:
# 		# If the request was not a POST, display the form to enter details.
# 		form = EditPersonalDetailsForm()
# 		context_dict['form'] = form
# 		context_dict['child'] = child
# 		return render_to_response('parent/childProfile.html', context_dict, context)


@login_required
@user_passes_test(is_parent)
def childProfile(request, id):
	context = RequestContext(request)
	context_dict = {}
	parentid = request.user.id
	child = Client.objects.get(uid=id)
	sessions = UserSelectsSession.objects.filter(user_uid=child.uid)
 	if request.method == 'POST':
 		form = EditPersonalDetailsForm(request.POST)
 		#If the request was not a POST, display the form to enter details.
 	else:
 		form = EditPersonalDetailsForm()
 		context_dict['form'] = form
		context_dict['sessions'] = sessions
 		context_dict['child'] = child
 	return render_to_response('parent/childProfile.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def managerChildProfile(request, id):
	context = RequestContext(request)
	context_dict = {}
	print id
	parentid = request.user.id
	child = Client.objects.get(uid=id)
	sessions = UserSelectsSession.objects.filter(user_uid=child.uid)
 	if request.method == 'POST':
 		form = EditPersonalDetailsForm(request.POST)

 		#If the request was not a POST, display the form to enter details.
 	else:
 		form = EditPersonalDetailsForm()
 		context_dict['form'] = form
		context_dict['sessions'] = sessions
 		context_dict['child'] = child
 	return render_to_response('manager/childProfile.html', context_dict, context)

# @login_required
# @user_passes_test(is_parent)
# def changeChild(request):
# 	f_uid = request.POST.get("uid", "")
# 	parentid = request.user.id

# 	child = Client.objects.get(uid=f_uid, belongsto=parentid)
# 	if child:
# 		child.firstname = request.POST.get("firstname", "")
# 		child.lastname = request.POST.get("lastname", "")
# 		child.genderid = int(request.POST.get("genderid", ""))
# 		child.dateofbirth = request.POST.get("dateofbirth", "")
# 		child.telephone = request.POST.get("telephone", "")
# 		child.email = request.POST.get("email", "")
# 		child.save()

# 	return redirect('/bookingsystem/parent/childrenList.html')

################################################################################
####												Adding new Child	 															 ###
################################################################################

@login_required
@user_passes_test(is_parent)
def addNewChild(request):
	context = RequestContext(request)
	#context_dict={}
	context_dict = {'parent': request.user}
	#print lastID
	if request.method == 'POST':
		form = CreateChildForm(request.POST)
		# Have we been provided with a valid form?
		if form.is_valid():
			info=form.save(commit=False)
			info.uid = getLastID
			info.ismember = 0
			info.belongsto = request.user
			print info
			# info.save()
			# Redirect on success
			return redirect('/success.html')
		else:
			# The supplied form contained errors - just print them to the terminal.
			print form.errors
	else:
		# If the request was not a POST, display the form to enter details.
		form = CreateChildForm()
		context_dict['form'] = form
		return render_to_response('parent/addnewChild.html', context_dict, context)

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

@login_required
@user_passes_test(is_manager)
def sessionInfo(request, sessionID):
	context = RequestContext(request)

	userSelectSessionObjects = UserSelectsSession.objects.filter(Q(session_sessionid = sessionID))
	context_dict = {'userSelectSessionObjects': userSelectSessionObjects}

	childrenNot = Client.objects.filter(~Q(uid__in = userSelectSessionObjects.values('user_uid')))
	context_dict['childrenNot'] = childrenNot

	sessionDetails = Session.objects.get(sessionid=sessionID)
	context_dict['details'] = sessionDetails

	sessionCoachedByObjects = sessionCoachedBy.objects.filter(session_id = sessionID)

	coacheGroups = Group.objects.get(name='Coach')
	allCoaches = User.objects.filter(Q(groups=coacheGroups))
	assignedCoaches = allCoaches.filter(Q(id__in = sessionCoachedByObjects.values('user_id')))
	unassignedCoaches = allCoaches.filter(~Q(id__in = sessionCoachedByObjects.values('user_id')))

	context_dict['assignedCoaches'] = assignedCoaches
	context_dict['unassignedCoaches'] = unassignedCoaches
	return render_to_response('manager/sessionInfo.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def addCoachToSession(request):
	context = RequestContext(request)
	context_dict={}

	SessionID = request.POST['sessionID']
	sessionObject = Session.objects.get(sessionid = SessionID)
	for key in request.POST:
		if (key.startswith('coachID')):
			userID = request.POST[key]
			userObject = User.objects.get(id = userID)
			add = sessionCoachedBy.objects.get_or_create(session_id = sessionObject, user_id = userObject)

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
@user_passes_test(is_manager)
def removeCoachFromSession(request, id, sid):

	sessionCoachedBy.objects.filter(session_id = sid, user_id = id).delete()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
@user_passes_test(is_manager)
def addChildToSession(request):
	context = RequestContext(request)
	context_dict={}

	SessionID = request.POST['sessionID']
	sessionObject = Session.objects.get(sessionid = SessionID)
	for key in request.POST:
		if (key.startswith('notInSession')):
			childID = request.POST[key]
			clientObject = Client.objects.get(uid = childID)
			add = UserSelectsSession.objects.get_or_create(session_sessionid = sessionObject, user_uid = clientObject)

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
@user_passes_test(is_manager)
def removeChildFromSession(request, id, sid):

	UserSelectsSession.objects.filter(user_uid = id, session_sessionid = sid).delete()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
@user_passes_test(is_manager)
def addSession(request):
	context = RequestContext(request)
	context_dict={}

	# A HTTP POST?
	if request.method == 'POST':
		form = SessionForm(request.POST)
		# Have we been provided with a valid form?
		if form.is_valid():
			session=form.save(commit=False)
			session.sessionid = getLastSessionID()
			print session.sessionid, session.begintime, session.endtime, session.block_blockid
			session.save()
			# Now save to the DB block.save()
			# Redirect on success
			return redirect('/success.html')
		else:
			# The supplied form contained errors - just print them to the terminal.
			#print form.begintime
			print form.errors
	else:
		# If the request was not a POST, display the form to enter details.
		form = SessionForm()
	return render_to_response('manager/addSession.html', {'form': form}, context)

@login_required
@user_passes_test(is_manager)
def removeSession(request,sid):
	context = RequestContext(request)
	context_dict={}

	userSelectSessionObjects = UserSelectsSession.objects.filter(session_sessionid = sid)
	sessionCoachedByObjects = sessionCoachedBy.objects.filter(session_id = sid)

	print sessionCoachedByObjects

	context_dict['userSelectSessionObjects'] = userSelectSessionObjects
	context_dict['sessionCoachedByObjects'] = sessionCoachedByObjects
	context_dict['sessionid'] = sid

	print context_dict

	if userSelectSessionObjects or sessionCoachedByObjects:
		return render_to_response('manager/removeSession.html', context_dict, context)
	else:
		confirmRemoveSessionFunction(sid)
		return redirect('/bookingsystem/manager/sessions.html')

@login_required
@user_passes_test(is_manager)
def confirmRemoveSession(request,sid):
	confirmRemoveSessionFunction(sid)
	return redirect('/bookingsystem/manager/sessions.html')

def confirmRemoveSessionFunction(sid):
	UserSelectsSession.objects.filter(session_sessionid = sid).delete()
	sessionCoachedBy.objects.filter(session_id = sid).delete()
	Session.objects.get(sessionid = sid).delete()


@login_required
@user_passes_test(is_manager)
def addBlock(request):
	global ageGroups
	context = RequestContext(request)
	# A HTTP POST?
	if request.method == 'POST':
		if 'submit_week' in request.POST:

			form = WeekBlockForm(request.POST)
			# Have we been provided with a valid form?
			if form.is_valid():
				block=form.save(commit=False)
				block.blockid = getLastBlockID()
				print 'Week block ID:', block.blockid
				block.enddate = block.begindate + timedelta(days = 6)
				block.type = 'Week'
				block.save()
				for i in range(0,5):
					# Create the morning Block
					b = Block(blockid=getLastBlockID(), begindate=block.begindate + timedelta(days = i), enddate=block.begindate + timedelta(days = i), label=getDayOfWeek(i) + ' Morning', type='Morning')
					print 'Morning Block:', b
					b.save()
					# Create all the sessions for the morning block
					for age in ageGroups:
						# Generate the time
						sessionTime = datetime.datetime.strptime('08:00', '%H:%M').time() # generate a 8:00 time
						sessionBegTime = datetime.datetime.combine(block.begindate+timedelta(days = i), sessionTime)
						s = Session(sessionid=getLastSessionID(), duration=1, begintime=sessionBegTime, endtime=(sessionBegTime+timedelta(hours=1)), block_blockid=b, capacity=10, agegroup=age, skillgroup='RANDOM', isfull=0)
						#print s.sessionid , s.begintime, s.endtime, s.agegroup
						s.save()
					# Create the afternoon block
					b1 = Block(blockid=getLastBlockID(), begindate=block.begindate + timedelta(days = i), enddate=block.begindate + timedelta(days = i), label=getDayOfWeek(i) + ' Afternoon', type='Afternoon')
					print 'Afternoon Block:',  b1
					b1.save()
					for age in ageGroups:
						# Generate the time
						sessionTime = datetime.datetime.strptime('13:00', '%H:%M').time() # generate a 8:00 time
						sessionBegTime = datetime.datetime.combine(block.begindate+timedelta(days = i), sessionTime)
						s = Session(sessionid=getLastSessionID(), duration=1, begintime=sessionBegTime, endtime=(sessionBegTime+timedelta(hours=1)), block_blockid=b1, capacity=10, agegroup=age, skillgroup='RANDOM', isfull=0)
						#print s.sessionid , s.begintime, s.endtime, s.agegroup
						s.save()
				# Redirect on success
				return redirect('/success.html')
			else:
				# The supplied form contained errors - just print them to the terminal.
				print form.errors
		if 'submit_season' in request.POST:
			print 'AAAAAAAAAAAAAAAAA'
			form = BlockFormMore(request.POST)
			# Have we been provided with a valid form?
			if form.is_valid():
				block=form.save(commit=False)
				block.blockid = getLastBlockID()
				block.type = 'Season'
				block.save()
				print form.cleaned_data['begintime']
				days = []
				for data in form.cleaned_data['weekdays']:
					days.append(int(data))
				print days
				delta = datetime.timedelta(days=1)
				day = block.begindate
				while day <= block.enddate:
					if day.weekday() in days:
						#sessionTime = datetime.datetime.strptime('13:00', '%H:%M').time() # generate a 8:00 time
						sessionTime = form.cleaned_data['begintime']
						sessionBegTime = datetime.datetime.combine(day, sessionTime)
						s = Session(sessionid=getLastSessionID(), duration=1, begintime=sessionBegTime, endtime=(sessionBegTime+timedelta(hours=1)), block_blockid=block, capacity=10, agegroup='13-23', skillgroup='RANDOM', isfull=0)
						print s.sessionid , s.begintime, s.endtime, s.agegroup, s.block_blockid.blockid
						s.save()
					day += delta
				print Session.objects.filter(block_blockid=block.blockid)
				return redirect('/success.html')
			else:
				# If error
				print form.errors
				return redirect('/fail.html')
		else:
			# if unrecognised
			return redirect('/fail.html')
	else:
		# If the request was not a POST, display the form to enter details.
		form = WeekBlockForm()
		sform = BlockFormMore()
	return render_to_response('manager/addBlock.html', {'form': form, 'sform': sform}, context)

@login_required
@user_passes_test(is_manager)
def removeBlock(request,bid):
	context = RequestContext(request)
	context_dict={}
	sessionsInBlock = Session.objects.filter(block_blockid = bid)
	UserSelectsSessionObjects = UserSelectsSession.objects.filter(session_sessionid__in = sessionsInBlock.values('sessionid'))
	sessions1 = Session.objects.filter(Q(block_blockid = bid) & Q(sessionid__in = UserSelectsSessionObjects.values('session_sessionid') ))
	sessionCoachedByObjects = sessionCoachedBy.objects.filter(session_id__in = sessionsInBlock.values('sessionid'))
	sessions2 = Session.objects.filter(Q(block_blockid = bid) & Q(sessionid__in = sessionCoachedByObjects.values('session_id') ))

	context_dict = {'sessionsInBlock' : sessions1}
	context_dict['UserSelectsSessionObjects'] = UserSelectsSessionObjects

	context_dict['sessionWithCoach'] = sessions2
	context_dict['sessionCoachedByObjects'] = sessionCoachedByObjects

	context_dict['blockid'] = bid

	if UserSelectsSessionObjects:
		return render_to_response('manager/removeBlock.html', context_dict, context)
	else:
		confirmRemoveBlockFunction(bid)
	return redirect('/bookingsystem/manager/blocks.html')


@login_required
@user_passes_test(is_manager)
def confirmRemoveBlock(request,bid):
	confirmRemoveBlockFunction(bid)
	return redirect('/bookingsystem/manager/blocks.html')

def confirmRemoveBlockFunction(bid):
	sessionsInBlock = Session.objects.filter(block_blockid = bid)
	UserSelectsSessionObjects = UserSelectsSession.objects.filter(session_sessionid__in = sessionsInBlock.values('sessionid')).delete()
	sessionCoachedByObjects = sessionCoachedBy.objects.filter(session_id__in = sessionsInBlock.values('sessionid')).delete()
	sessionsInBlock.delete()
	Block.objects.get(blockid = bid).delete()





