from django import forms
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from bookingsystem.models import *
from bookingsystem.forms import BlockFormMore, EditPersonalDetailsForm, CreateChildForm, WeekBlockForm, SessionFormMore, ManagerEditPersonalDetailsForm, EditUserPersonalDetailsForm, DefaultCoachesForm, EditPersonalDetailsForm, SessionEditForm
from django.db.models import Q, F, Sum, Min, Max, Count
from itertools import chain
from datetime import timedelta, date, datetime
import time, re, pytz

###
### Depreciated To be removed with the new Approved page
### Complexity to be moved to DB
approvalHistory = []



### This is bad and you should feel bad...
i = 0
### Hardcoded price per session
PRICE = 25

def addPayment(user, session, type):
	try:
		payment = Payment.objects.get(usertopay=Client.objects.get(uid=user))
	except Payment.DoesNotExist:
		payment = None
	if payment:
		payment.amount += PRICE
		string = payment.label
		payment.label = string + ", " + str(session.session_sessionid.sessionid)
		payment.save()
	else:
		id ="Sessions: " + str(session.session_sessionid.sessionid)
		payType = Paymenttype.objects.get(typeid=type)
		payment = Payment(usertopay=Client.objects.get(uid=user), paymenttype=payType, amount=PRICE, label=id, haspayed=0, duedate=date.today())
		payment.save()
	#print payment.paymentid, payment.amount, payment.label


# This field is also referred to in the forms BlockFormMore
ageGroups = ['7-10', '10-12', '12-15', '15-21']

def getDayOfWeek(n):
	daysOfWeek = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thurday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
	return daysOfWeek[n]

def getAgeGroup(age):
	global ageGroups
	for group in ageGroups:
		temp = group.split('-')
		if (age in range(int(temp[0]), int(temp[1]))):
			return group
	return -1


## days can be 0 to 5
## morOrAft can be 0 for Morning and 1 for Afternoon
def getCoach(day, morOrAft):

	try:
			data = DefaultCoaches.objects.get(id=1)
	except ObjectDoesNotExist:
		return -1
	info = [
			[data.monMor, data.monAft],
			[data.tueMor, data.tueAft],
			[data.wedMor, data.wedAft],
			[data.thuMor, data.thuAft],
			[data.friMor, data.friAft]
			]
	return info[day][morOrAft]



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
#																	Coach 																			#
###############################################################################


@login_required
@user_passes_test(is_coach)
def coachIndex(request):
	context = RequestContext(request)
	today = date.today()
	userID = request.user.id
	todaySessions = Session.objects.filter(Q(begintime__year=today.year, begintime__month=today.month, begintime__day=today.day)).values_list('sessionid')
	todayAssignedSessions = Session.objects.filter(Q(coachedby=request.user) & Q(sessionid__in=todaySessions))
	futureAssignedSessions = Session.objects.filter(Q(coachedby=request.user) & Q(begintime__gte=date.today() + timedelta(days=1)))

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

@login_required
@user_passes_test(is_coach)
def printScheduleCoach(request):
	context = RequestContext(request)
	today = date.today()
	userID = request.user.id
	todaySessions = Session.objects.filter(Q(begintime__year=today.year, begintime__month=today.month, begintime__day=today.day)).values_list('sessionid')
	todayAssignedSessions = Session.objects.filter(Q(coachedby=request.user) & Q(sessionid__in=todaySessions))
	futureAssignedSessions = Session.objects.filter(Q(coachedby=request.user) & Q(begintime__gte=date.today() + timedelta(days=1)))

	context_dict={'todayAssignedSessions':todayAssignedSessions}
	context_dict['futureAssignedSessions'] = futureAssignedSessions
	return render_to_response('coach/printSchedule.html', context_dict, context)

@login_required
@user_passes_test(is_coach)
def printAttendance(request, id):
	context = RequestContext(request)
	context_dict={}
	unattendedSessionObjects = UserSelectsSession.objects.filter(session_sessionid = id, status = 'C',hasattended = 0)
	attendedSessionObjects = UserSelectsSession.objects.filter(session_sessionid = id, status = 'C',hasattended = 1)

	context_dict = {'unattendedSessionObjects':unattendedSessionObjects}
	context_dict['attendedSessionObjects'] = attendedSessionObjects
	context_dict['s'] = Session.objects.get(sessionid = id)
	return render_to_response('coach/printAttendance.html', context_dict, context)

#					 			NOT REQUIRED 								  #
# 							DEPRECIIATED									#
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
	return render_to_response('coach/sessions.html', context_dict, context)

###############################################################################
#																	Manager 																		#
###############################################################################

# @login_required
# def editProfile(request):
# 		############################################################################
# 		### 						HAS TO BE REFACTORED TO INCLUDE A FORM 										 #
# 		############################################################################
# 		## PENDING HTML CHANGE
#     context = RequestContext(request)
#     user = request.user

#     if request.method == 'POST':
#     	userID = request.POST.get('id', '')
#     	userObject = User.objects.get(id = userID)
#     	userObject.email = request.POST.get('email', '')
#     	userObject.additionalinfo.telephone = request.POST.get('telephone', '')
#     	userObject.save()

#     	# if not re.match(r"[^@]+@[^@]+\.[^@]+", userObject.email):
#     	# 	print "valid!"

#     	# additionalinfo = additionalinfo.objects.get_or_create(user_id = userID)
#     	# additionalinfo.telephone = request.POST.get('telephone', '')

#         # form = EditUserPersonalDetailsForm(request.POST)
#         # Have we been provided with a valid form?
#         # if form.is_valid():
#         # print form
#     # else:
#         # If the request was not a POST, display the form to enter details.
#         # form = EditUserPersonalDetailsForm()
#         # context['form'] = form

#     user = User.objects.get(id = user.id)
#     context_dict = {'user':user}
#     context_dict['form'] = EditPersonalDetailsForm()
#     try:
#         context_dict['telephone'] = user.additionalinfo.telephone
#     except:
#         pass

#     if request.META.get('HTTP_REFERER') is not None:
# 	    if "bookingsystem/manager/" in request.META.get('HTTP_REFERER'):
# 	    	context_dict['menu'] = "manager"
# 	    elif "bookingsystem/coach/" in request.META.get('HTTP_REFERER'):
# 	    	context_dict['menu'] = "coach"
# 	    elif "bookingsystem/parent/" in request.META.get('HTTP_REFERER'):
# 	    	context_dict['menu'] = "parent"
# 	    else:
# 	    	context_dict['menu'] = "error"
# 	    return render_to_response('editProfile.html', context_dict, context)
#     else:
# 		return redirect(request.path.split("/editProfile.html", 1)[0])

@login_required
@user_passes_test(is_manager)
def managerIndex(request):
	context = RequestContext(request)
	manager = request.user
	##			PENDING SESSIONS RETRIEVAL		##
	pendingSessions = UserSelectsSession.objects.filter(status = 'P')
	result = {}
	list_result = UserSelectsSession.objects.filter(status='P')  # converts ValuesQuerySet into Python list
	for item in list_result:
		if item.user_uid in result:
			result[item.user_uid].append(item)
		else:
			result[item.user_uid] = []
			result[item.user_uid].append(item)

	##			PENDING PAYERS RETRIEVAL		##
	pendingPayments = Payment.objects.filter(haspayed=0)
	pendingUsers = pendingPayments.values_list('usertopay')
	#print UserSelectsSession.objects.all().session_sessioni
	UserSelectsSession.objects.extra(select={'dayDiff':"(session_sessionid__begintime.date() - date.today()).days"})
	nextArrivalDay = UserSelectsSession.objects.filter(user_uid__in=pendingUsers).select_related('session_sessionid')
	nextArrivalDay1 = nextArrivalDay.filter(session_sessionid__begintime__gte=datetime.now())
	for item in nextArrivalDay1:
		dayDiff = (item.session_sessionid.begintime.date() - date.today()).days
		item.__dict__['dayDiff'] = dayDiff
		#print item.session_sessionid.begintime.date(), date.today(), dayDiff

	######for payer in pendingPayments:
		#print payer.userselectssession_set.all().aggregate(Min('begindate'))
		######payer.usertopay.nextDate = payer.usertopay.nextArrivalDate
		#print payer.usertopay.nextArrivalDate

	#
	#	SELECT id
	#	FROM UserSelectsSession NATURAL JOIN Session,
	#	GROUP BY user_uid
	# HAVING MIN(julianday(begintime) - julianday(SELECT date('now')))
	#
	#
	#


	pendingSessions = UserSelectsSession.objects.filter(status = 'P')
	declinedSessions = UserSelectsSession.objects.filter(status = 'D')
	## 			DATA COMMUNICATION				##
	context_dict={'manager':manager}
	context_dict['data'] = result
	context_dict['pending'] = pendingSessions
	context_dict['declined'] = declinedSessions
	#context_dict['nextarrivalday'] = nextArrivalDay
	context_dict['history'] = approvalHistory
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

	context_dict['details'] = blocks
	context_dict['blockSessions'] = blockSessions
	context_dict['blockid'] = bid

	if request.META.get('HTTP_REFERER') is not None:
		if "/bookingsystem/manager/sessionInfo" in request.META.get('HTTP_REFERER'):
			context_dict['previous'] = "/bookingsystem/manager/blocks"
		else:
			context_dict['previous'] = request.META.get('HTTP_REFERER')
	else:
		context_dict['previous'] = "/"

	return render_to_response('manager/blockInfo.html', context_dict, context)

################################################################################
@login_required
@user_passes_test(is_manager)
def managerBookings(request):
	context = RequestContext(request)
	parent = request.user
	##			PENDING SESSIONS RETRIEVAL		##
	pendingSessions = UserSelectsSession.objects.filter(status = 'P')
	declinedSessions = UserSelectsSession.objects.filter(status = 'D')

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
	#sessionInfo.extra('coachedBy': )
	context_dict={'sessions':sessionInfo}
	return render_to_response('manager/sessions.html', context_dict, context)



##################### Add block id query in context detail #####################

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

# @login_required
# @user_passes_test(is_manager)
# def confirmbooking(request):
# 	context = RequestContext(request)
# 	context_dict={}
# 	return render_to_response('success.html', context_dict, context)



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
		history={}
		beginning = date.today() - timedelta(days=7*5)
		coachingHistory = Session.objects.filter(Q(coachedby=userObject) & Q(begintime__gte=beginning) )
		#for session in coachingHistory:
		i = 5
		while i > 0:
			beginning = datetime.now(pytz.utc) - timedelta(days=7*i)
			history["Week Beginning: " + beginning.strftime("%d/%m/%y")] = userObject.session_set.filter( Q(begintime__gte=beginning) & Q(begintime__lte=beginning + timedelta(days=7)) ).aggregate(Sum('duration'))

	#userObject.session_set.filter( Q(begintime__gte=beginning) & Q(begintime__lte=beginning + datetime.timedelta(days=7)) ).annotate(total_hours=Sum('duration'))




			i -= 1
		print history
			#print session.total_hours
		today = date.today()
		userID = request.user.id
		todaySessions = Session.objects.filter(Q(begintime__year=today.year, begintime__month=today.month, begintime__day=today.day)).values_list('sessionid')
		todayAssignedSessions = Session.objects.filter(Q(coachedby=request.user) & Q(sessionid__in=todaySessions))
		futureAssignedSessions = Session.objects.filter(Q(coachedby=request.user) & Q(begintime__gte=date.today() + timedelta(days=1)))
		context_dict['history']= history
		context_dict['todayAssignedSessions'] = todayAssignedSessions
		context_dict['futureAssignedSessions'] = futureAssignedSessions

	 	return render_to_response('manager/coachProfile.html', context_dict, context)
	else:
		return redirect('/bookingsystem/manager/coaches.html')

@login_required
@user_passes_test(is_manager)
def removeCoach(request, id):
	context = RequestContext(request)
 	context_dict={}
	sessionCoachedByObjects = sessionCoachedBy.objects.filter(user_id = id)
	context_dict = {'coachid' : id}
	if sessionCoachedByObjects:
		context_dict['sessionCoachedByObjects'] = sessionCoachedByObjects
		return render_to_response('manager/removeCoach.html', context_dict, context)
	else:
 		return render_to_response('manager/removeCoach.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def confirmRemoveCoach(request, id):
 	userObject = User.objects.get(id = id)
	g = Group.objects.get(name='Coach')
	g.user_set.remove(userObject)
	sessionCoachedBy.objects.filter(user_id = id).delete()
	return redirect('/bookingsystem/manager/coaches.html')

@login_required
@user_passes_test(is_manager)
def managers(request):
	context = RequestContext(request)
	context_dict={}

	managerGroups = Group.objects.get(name='Manager')
	allManagers = User.objects.filter(Q(groups=managerGroups) & ~Q(id = request.user.id))

	notManager = User.objects.filter(~Q(id__in = allManagers) & ~Q(id = request.user.id))

	context_dict['allManagers'] = allManagers
	context_dict['notManager'] = notManager
	context_dict['user'] = request.user
	return render_to_response('manager/managers.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def managerProfile(request, id):
 	context = RequestContext(request)
 	context_dict={}
 	coacheGroups = Group.objects.get(name='Coach')
	allCoaches = User.objects.filter(Q(groups=coacheGroups))
	userObject = User.objects.get(id = id)
	if (userObject in allCoaches):
	 	context_dict['userObject'] = userObject

	 	today = date.today()
		userID = request.user.id
		todaySessions = Session.objects.filter(Q(begintime__year=today.year, begintime__month=today.month, begintime__day=today.day)).values_list('sessionid')
		todayAssignedSessions = Session.objects.filter(Q(coachedby=request.user) & Q(sessionid__in=todaySessions))
		futureAssignedSessions = Session.objects.filter(Q(coachedby=request.user) & Q(begintime__gte=date.today() + timedelta(days=1)))
		context_dict['todayAssignedSessions'] = todayAssignedSessions
		context_dict['futureAssignedSessions'] = futureAssignedSessions

	 	return render_to_response('manager/coachProfile.html', context_dict, context)
	else:
		return redirect('/bookingsystem/manager/coaches.html')

@login_required
@user_passes_test(is_manager)
def addNewManager(request):
	context = RequestContext(request)
	user = request.user
	context_dict={}

	for key in request.POST:
		if (key.startswith('notManager')):
			userID = request.POST[key]
			userObject = User.objects.get(id = userID)
			g = Group.objects.get(name='Manager')
			g.user_set.add(userObject)

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
@user_passes_test(is_manager)
def removeManager(request, id):
	context = RequestContext(request)
 	context_dict={}

 	print "---"
 	print request.user.id
 	print int(id)

 	if (request.user.id != int(id)):
		context_dict = {'managerid' : id}
 	return render_to_response('manager/removeManager.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def confirmRemoveManager(request, id):
 	userObject = User.objects.get(id = id)
	g = Group.objects.get(name='Manager')
	g.user_set.remove(userObject)
	return redirect('/bookingsystem/manager/managers.html')



@login_required
@user_passes_test(is_manager)
def members(request):
    context = RequestContext(request)
    clients = Client.objects.all()
    #for client in clients:
    #	print client.payment_set.all()
    #clients = Payment.objects.select_related('usertopay__uid')


    # clients = Client.objects.raw('''
    # 	SELECT client.*, payment.amount
    # 	FROM client
    # 	LEFT JOIN payment
    # 	ON client.uID = payment.usertopay;
    # 	''')


    #print clients.query, "\n"
    #print clients
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
@user_passes_test(is_manager)
def managerChildProfile(request, id):
	context = RequestContext(request)
	context_dict = {}
	child = Client.objects.get(uid=id)
	sessions = UserSelectsSession.objects.filter(user_uid=child.uid)
	parent = User.objects.get(id=child.belongsto_id)

	try:
		telephone = parent.additionalinfo.telephone
	except:
		telephone = ""

	if request.method == 'POST':
		form = ManagerEditPersonalDetailsForm(request.POST)

		#If the request was not a POST, display the form to enter details.
	else:
		form = ManagerEditPersonalDetailsForm()
		print parent
		context_dict['parentInfo'] = parent
		context_dict['telephone'] = telephone
		context_dict['form'] = form
		context_dict['sessions'] = sessions
		context_dict['child'] = child

	if request.META.get('HTTP_REFERER') is not None:
		context_dict['previous'] = request.META.get('HTTP_REFERER')
	else:
		context_dict['previous'] = "/"

	return render_to_response('manager/childProfile.html', context_dict, context)

@login_required
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
				session.session_sessionid.capacity -= 1
				if session.session_sessionid.capacity == 0:
					session.session_sessionid.isfull=1
				#session.session_sessionid.save()
				#session.save()
				addPayment(user, session, 1)

	return HttpResponse('Approved!')

###############################################################################
#																	Parent 																			#
###############################################################################

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
	today = date.today()
	monday = today - timedelta(days=today.weekday())
	weeks = Block.objects.filter(((Q(type='Week') & Q(begindate__gte=monday))) | (Q(type='Season')))
	print weeks
	context_dict = {'blocks': weeks}
	context_dict['child'] = child
	return render_to_response('parent/userBookings.html', context_dict, context)


@login_required
@user_passes_test(is_parent)
def confirmBookings(request, uID):
	context = RequestContext(request)
	checked = chain(request.POST.getlist("morning"),request.POST.getlist("afternoon"))
	if checked:
		for item in checked:
			user = Client.objects.get(uid=uID)
			session = Session.objects.get(sessionid=item)
			t = UserSelectsSession(
				session_sessionid=session,
				user_uid=user,
				status='P',
				hasattended=0
				)
			#print t.session_sessionid, user_uid, status, hasattended
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
	age = date.today() - child.dateofbirth
	preSelectedSessions = UserSelectsSession.objects.filter(user_uid=child.uid)
	seasonSessions = Session.objects.filter(block_blockid__in=Block.objects.filter(type="Season"))
	availableSessions = Session.objects.filter(~Q(sessionid__in=[session.session_sessionid.sessionid for session in preSelectedSessions]) & ~Q(sessionid__in=seasonSessions))
	agegroupp=getAgeGroup(age.days/365)
	if agegroupp == -1:
		sessions = Session.objects.none()
	else:
		sessions = availableSessions.filter((Q(begintime__gte=datetime.now()) & Q(begintime__gte=owner.begindate)) & Q(begintime__lte=owner.enddate)  & Q(agegroup=agegroupp) & Q(isfull=0))

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
	age = date.today() - child.dateofbirth
	agegroupp=getAgeGroup(age.days/365)
 	if not agegroupp==-1:
		sessions = Session.objects.filter( Q(block_blockid=blockID) & Q(begintime__gte=datetime.now() ) & Q(begintime__lte=owner.enddate) & Q(agegroup=agegroupp) & Q(isfull=0))
	else:
		sessions = Session.objects.none()
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

	belongsto = child.belongsto
	if belongsto.id == parentid:
		sessions = UserSelectsSession.objects.filter(user_uid=child.uid)

		try:
			Medical = Medicalcondition.objects.get(ownerid = child.uid)
			context_dict['medical'] = Medical
		except:
			pass

		context_dict['sessions'] = sessions
		context_dict['child'] = child
		print context_dict

	 	if request.method == 'POST':
	 		child.telephone = request.POST.get('telephone', '')
	 		child.email = request.POST.get('email', '')
			child.save()

	 		if 'Medical' in locals():
	 			Medical.condition = request.POST.get('medicalconditions', '')
	 			Medical.save()
	 		else:
	 			Medicalcondition.objects.create(ownerid = id, condition = request.POST.get('medicalconditions', ''))

	 	else:
	 		form = EditPersonalDetailsForm()
	 		context_dict['form'] = form
	 	return render_to_response('parent/childProfile.html', context_dict, context)
	else:
		return redirect('/bookingsystem/parent/')

			# form = EditPersonalDetailsForm(request.POST)
	 		# if form.is_valid():
	 		# 	newinfo = form.save(commit=False)
	 		# 	print newinfo
	 		#If the request was not a POST, display the form to enter details.


@login_required
@user_passes_test(is_parent)
def printSchedule(request, uid):
	context = RequestContext(request)
	context_dict = {}
	parentid = request.user.id
	child = Client.objects.get(uid=uid)
	context_dict['child'] = child
	belongsto = child.belongsto

	if belongsto.id == parentid:
		sessions = UserSelectsSession.objects.filter(user_uid=child.uid)
		context_dict['sessions'] = sessions
		print context_dict
	 	return render_to_response('parent/printSchedule.html', context_dict, context)



@login_required
@user_passes_test(is_parent)
def removeChild(request, uid):
	context = RequestContext(request)
	context_dict = {}
	sessions = UserSelectsSession.objects.filter(user_uid=uid)
 	context_dict = {"childid" : uid}

 	if sessions:
 		context_dict['sessions'] = sessions

 	return render_to_response('parent/removeChild.html', context_dict, context)

@login_required
@user_passes_test(is_parent)
def confirmRemoveChild(request, uid):
	context = RequestContext(request)
	context_dict = {}
	UserSelectsSession.objects.filter(user_uid=uid).delete()
 	Client.objects.get(uid = uid).delete()

 	return redirect('/bookingsystem/parent/')


################################################################################
####												Adding new Child	 															 ###
################################################################################

@login_required
@user_passes_test(is_parent)
def addNewChild(request):
	context = RequestContext(request)
	form = CreateChildForm(initial={})
	context_dict = {'parent': request.user}
	#print lastID
	if request.method == 'POST':
		form = CreateChildForm(request.POST)
		# Have we been provided with a valid form?
		if form.is_valid():
			child=form.save(commit=False)
			#child.uid = getLastID()
			child.ismember = 0
			child.belongsto = request.user
			child.experiencelevel=0
			child.save()
			# Redirect on success
			return redirect('/success.html')
	# If the request was not a POST, display the form to enter details.
	context_dict['form'] = form
	return render_to_response('parent/addNewChild.html', context_dict, context)

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
def removeSelection(request):
	context = RequestContext(request)
	sessionID = None
	if request.method == 'GET':
		sessionID = request.GET['session_sessionid']
		user = request.GET['userid']
		#print user
		if sessionID:
			session = UserSelectsSession.objects.get( Q(session_sessionid = sessionID) & Q(user_uid = user)).delete()
			print session
 	return HttpResponse('Success!')

###############################################################################
#																		Misc 																			#
###############################################################################

@login_required
@user_passes_test(is_manager)
def applicationDeclined(request):
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
				#approvalHistory.insert(i, session)
				#i=(i+1)%10
				session.status = 'D' # set from pending to declined
				session.save()
	return HttpResponse('Declined!')

@login_required
@user_passes_test(is_manager)
def sessionInfo(request, sessionID, type):
	context = RequestContext(request)

	userSelectSessionObjects = UserSelectsSession.objects.filter(Q(session_sessionid = sessionID))
	childrenNot = Client.objects.filter(~Q(uid__in = userSelectSessionObjects.values('user_uid')))
	sessionDetails = Session.objects.get(sessionid=sessionID)
	allCoaches = User.objects.filter(Q(groups=Group.objects.get(name='Coach')))
	assignedCoaches = sessionDetails.coachedby.all()
	unassignedCoaches = allCoaches.filter(~Q(id__in = assignedCoaches.values('id')))

	context_dict = {'userSelectSessionObjects': userSelectSessionObjects}
	context_dict['childrenNot'] = childrenNot
	context_dict['details'] = sessionDetails
	context_dict['assignedCoaches'] = assignedCoaches
	context_dict['unassignedCoaches'] = unassignedCoaches

	if request.META.get('HTTP_REFERER') is not None:
		if "/bookingsystem/manager/managerChildProfile/" in request.META.get('HTTP_REFERER'):
			context_dict['previous'] = "/bookingsystem/manager/sessions"
		else:
			context_dict['previous'] = request.META.get('HTTP_REFERER')
	else:
		context_dict['previous'] = "/"

	if request.method == 'POST':
		form = SessionEditForm(request.POST)
		# Have we been provided with a valid form?
		if form.is_valid():
			session=form.save(commit=False)
			session.sessionid = sessionDetails.sessionid
			if not form.cleaned_data['isfull']:
				session.isfull = False;
			session.duration = (session.endtime-session.begintime)
			session.save()
			print session.sessionid
			context_dict['success'] = 1
			return redirect('manager/sessionInfo.html')
		else:
			return redirect('fail.html')
	else:
		if int(type) == 1:
			print sessionDetails.isfull
			form = SessionEditForm(initial={'isfull' : sessionDetails.isfull,
																			'begintime' : sessionDetails.begintime,
																			'endtime' : sessionDetails.endtime,
																			'block_blockid' : sessionDetails.block_blockid,
																			'capacity' : sessionDetails.capacity,
																			'agegroup' : sessionDetails.agegroup,
																			'skillgroup' : sessionDetails.skillgroup
				})
			context_dict['form'] = form
			return render_to_response('manager/sessionInfoEdit.html', context_dict, context)
		else:
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
			coach = User.objects.get(id = userID)
			sessionObject.coachedby.add(coach)

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
@user_passes_test(is_manager)
def removeCoachFromSession(request, id, sid):
	sessionDetails = Session.objects.get(sessionid=sid)
	coaches = sessionDetails.coachedby.all().get(id=id)
	a = coaches.session_set.remove(sessionDetails)
	#sessionDetails.coaches.clear()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
@user_passes_test(is_manager)
def addChildToSession(request):
	context = RequestContext(request)
	context_dict={}
	SessionID = request.POST['sessionID']
	session = Session.objects.get(sessionid = SessionID)
	for key in request.POST:
		if (key.startswith('notInSession')):
			childID = request.POST[key]
			clientObject = Client.objects.get(uid = childID)
			add = UserSelectsSession.objects.get_or_create(session_sessionid = session, user_uid = clientObject, status='C', hasattended=0)
			session.capacity -= 1
			if session.capacity == 0:
				session.isfull=1
			session.save()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
@user_passes_test(is_manager)
def removeChildFromSession(request, id, sid):
	UserSelectsSession.objects.filter(user_uid = id, session_sessionid = sid).delete()
	session = Session.objects.get(sessionid=sid)
	session.capacity += 1
	if session.capacity > 0:
		session.isfull=0
	session.save()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
@user_passes_test(is_manager)
def addSession(request):
	context = RequestContext(request)
	context_dict={}

	# A HTTP POST?
	if request.method == 'POST':
		form = SessionFormMore(request.POST)
		# Have we been provided with a valid form?
		if form.is_valid():
			session=form.save(commit=False)
			session.duration = (session.endtime-session.begintime)
			session.isfull=0
			if form.cleaned_data['coachedby'][0] != 0:
				session.coachedby.add(User.objects.get(id=form.cleaned_data['coachedby'][0]))
			session.save()
			#sessionCoachedBy(session_id=session, user_id=User.objects.get(id=form.cleaned_data['coachedby'][0])).save()
			# Redirect on success
			return redirect('/success.html')
		#else:
			# The supplied form contained errors - just print them to the terminal.
	else:
		# If the request was not a POST, display the form to enter details.
		form = SessionFormMore()
	return render_to_response('manager/addSession.html', {'form': form}, context)

@login_required
@user_passes_test(is_manager)
def removeSession(request,sid):
	context = RequestContext(request)

	userSelectSessionObjects = UserSelectsSession.objects.filter(session_sessionid = sid)
	sessionCoachedByObjects = Session.objects.get(sessionid=sid).coachedby.all()
	context_dict = {'sessionid' : sid}
	if userSelectSessionObjects or sessionCoachedByObjects:
		context_dict['userSelectSessionObjects'] = userSelectSessionObjects
		context_dict['sessionCoach'] = sessionCoachedByObjects
		return render_to_response('manager/removeSession.html', context_dict, context)
	else:
		return render_to_response('manager/removeSession.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def confirmRemoveSession(request,sid):
	UserSelectsSession.objects.filter(session_sessionid = sid).delete()
	sessionDetails = Session.objects.get(sessionid=sid)
	coaches = sessionDetails.coachedby.clear()
	Session.objects.get(sessionid = sid).delete()
	return redirect('/bookingsystem/manager/sessions.html')

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
				#block.blockid = getLastBlockID()
				print 'Week block ID:', block.blockid
				block.enddate = block.begindate + timedelta(days = 6)
				block.type = 'Week'
				block.save()
				for i in range(0,5):
					# Create the morning Block
					b = Block(begindate=block.begindate + timedelta(days = i), enddate=block.begindate + timedelta(days = i), label=getDayOfWeek(i) + ' Morning', type='Morning')
					print 'Morning Block:', b
					b.save()
					# Create all the sessions for the morning block
					for age in ageGroups:
						# Generate the time
						sessionTime = datetime.strptime('08:00', '%H:%M').time() # generate a 8:00 time
						sessionBegTime = datetime.combine(block.begindate+timedelta(days = i), sessionTime)
						s = Session(duration=1, begintime=sessionBegTime, endtime=(sessionBegTime+timedelta(hours=1)), block_blockid=b, capacity=10, agegroup=age, skillgroup='RANDOM', isfull=0)
						s.save()
						if (getCoach(i,0) != (-1 & 0)):
							s.coachedby.add(getCoach(i,0))
						print s.sessionid , s.begintime, s.endtime, s.agegroup, s.coachedby
						s.save()
					# Create the afternoon block
					b1 = Block(begindate=block.begindate + timedelta(days = i), enddate=block.begindate + timedelta(days = i), label=getDayOfWeek(i) + ' Afternoon', type='Afternoon')
					print 'Afternoon Block:',  b1
					b1.save()
					for age in ageGroups:
						# Generate the time
						sessionTime = datetime.strptime('13:00', '%H:%M').time() # generate a 8:00 time
						sessionBegTime = datetime.combine(block.begindate+timedelta(days = i), sessionTime)
						s = Session(duration=1, begintime=sessionBegTime, endtime=(sessionBegTime+timedelta(hours=1)), block_blockid=b1, capacity=10, agegroup=age, skillgroup='RANDOM', isfull=0)
						s.save()
						if (getCoach(i,1) != (-1 & 0)):
							s.coachedby.add(getCoach(i,1))
						#print s.sessionid , s.begintime, s.endtime, s.agegroup, s.coachedby
						s.save()
				# Redirect on success
				return redirect('/success.html')
			else:
				sform = BlockFormMore()


		if 'submit_season' in request.POST:
			form = BlockFormMore(request.POST)
			# Have we been provided with a valid form?
			if form.is_valid():

				block=form.save(commit=False)
				#block.blockid = getLastBlockID()
				block.type = 'Season'
				block.save()
				#print form.cleaned_data['begintime']
				days = []
				for data in form.cleaned_data['weekdays']:
					days.append(int(data))
				delta = timedelta(days=1)
				day = block.begindate
				while day <= block.enddate:
					if day.weekday() in days:
						#sessionTime = datetime.datetime.strptime('13:00', '%H:%M').time() # generate a 8:00 time
						sessionTime = form.cleaned_data['begintime']
						sessionBegTime = datetime.combine(day, sessionTime)
						s = Session(duration=1, begintime=sessionBegTime, endtime=(sessionBegTime+timedelta(hours=1)), block_blockid=block, capacity=10, agegroup=form.cleaned_data['agegroup'], skillgroup='RANDOM', isfull=0)
						print s.sessionid , s.begintime, s.endtime, s.agegroup, s.block_blockid.blockid
						s.save()
					day += delta
				print Session.objects.filter(block_blockid=block.blockid)
				return redirect('/success.html')
			else:
				print form.errors
				form = WeekBlockForm()
				sform = BlockFormMore()
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
	#sessionCoachedByObjects = sessionCoachedBy.objects.filter(session_id__in = sessionsInBlock.values('sessionid'))
	sessionCoachedByObjects = Session.objects.filter(sessionid__in=sessionsInBlock.values('sessionid'))
	sessions2 = Session.objects.filter(Q(block_blockid = bid) & Q(sessionid__in = sessionCoachedByObjects.values('sessionid') ))

	context_dict = {'blockid' : bid}
	for session in sessionCoachedByObjects:
		print session.coachedby.all(), session
	# 		print coach, session
	if sessions1 or sessions2:
		context_dict['sessionsInBlock'] = sessions1
		context_dict['UserSelectsSessionObjects'] = UserSelectsSessionObjects
		context_dict['sessionWithCoach'] = sessions2
		context_dict['sessionCoachedByObjects'] = sessionCoachedByObjects
		return render_to_response('manager/removeBlock.html', context_dict, context)
	else:
		return render_to_response('manager/removeBlock.html', context_dict, context)


@login_required
@user_passes_test(is_manager)
def confirmRemoveBlock(request,bid):
	sessionsInBlock = Session.objects.filter(block_blockid = bid)
	UserSelectsSessionObjects = UserSelectsSession.objects.filter(session_sessionid__in = sessionsInBlock.values('sessionid')).delete()
	#sessionCoachedByObjects = sessionCoachedBy.objects.filter(session_id__in = sessionsInBlock.values('sessionid')).delete()
	sessionCoachedByObjects = Session.objects.filter(sessionid__in=sessionsInBlock.values('sessionid'))
	for session in sessionCoachedByObjects:
		session.coachedby.clear()
	sessionsInBlock.delete()
	Block.objects.get(blockid = bid).delete()
	return redirect('/bookingsystem/manager/blocks.html')

@login_required
@user_passes_test(is_manager)
def setDefaultCoaches(request):
	context = RequestContext(request)
	context_dict={}
	# A HTTP POST?
	if request.method == 'POST':
		form = DefaultCoachesForm(request.POST)
		# Have we been provided with a valid form?
		if form.is_valid():
			#print form.cleaned_data
			a = form.save(commit = False)
			#print a.monMor
			#a.save

			return redirect('/success.html')
		else:
			return redirect('/fail.html')

	else:
		# If the request was not a POST, display the form to enter details.
		try:
			a = DefaultCoaches.objects.get(id=1)
			default_data = {
			'monMor': a.monMor, 'monAft': a.monAft,
			'tueMor': a.tueMor, 'tueAft': a.tueAft,
			'wedMor': a.wedMor, 'wedAft': a.wedAft,
			'thuMor': a.thuMor, 'thuMon': a.thuAft,
			'friMor': a.friMor, 'friAft': a.friAft
			}
			form = DefaultCoachesForm(default_data)
			print form
		except ObjectDoesNotExist:
			form = DefaultCoachesForm()

	if request.META.get('HTTP_REFERER') is not None:
		context_dict = {'previous' : request.META.get('HTTP_REFERER')}
	else:
		context_dict = {'previous' : "/"}

	context_dict['form'] = form


	return render_to_response('manager/setDefaultCoaches.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def applicationAllApproved(request):
	global i
	context = RequestContext(request)
	sessionID = None
	if request.method == 'GET':
		user = request.GET['userid']
		sessions = UserSelectsSession.objects.filter(Q(user_uid = user) & Q(status='P'))
		if sessions:
			for session in sessions:
				approvalHistory.insert(i, session)
				i=(i+1)%25
				session.status = 'C' # set from pending to confirmed
				session.session_sessionid.capacity -= 1
				if session.session_sessionid.capacity == 0:
					session.session_sessionid.isfull=1
				#print session.session_sessionid, session.status
				session.session_sessionid.save()
				session.save()
				addPayment(user, session, 1)
	return HttpResponse('Approved!')

@login_required
@user_passes_test(is_manager)
def applicationAllDeclined(request):
	global i
	context = RequestContext(request)
	sessionID = None
	if request.method == 'GET':
		user = request.GET['userid']
		sessions = UserSelectsSession.objects.filter(Q(user_uid = user) & Q(status='P'))
		if sessions:
			for session in sessions:
				session.status = 'D' # set from pending to confirmed
				#print session.session_sessionid, session.status
				session.save()
	return HttpResponse('Declined!')
