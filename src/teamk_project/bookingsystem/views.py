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
from bookingsystem.forms import BlockForm, SessionForm1, EditPersonalDetailsForm, CreateChildForm ##########################
import datetime

approvalHistory = []
i = 0
lastSessionID = -1
lastID = -1
lastBlockID = -1


def getLastID():
	global lastID
	if (lastID == -1):
		lastID = Client.objects.all().aggregate(Max('uid')).get("uid__max")
	lastID = lastID + 1
	return lastID

def getLastSessionID():
	global lastSessionID
	if (lastSessionID == -1):
		lastSessionID = Session.objects.all().aggregate(Max('sessionid')).get("sessionid__max")
	lastSessionID = lastSessionID + 1
	return lastSessionID

def getLastBlockID():
	global lastBlockID
	if (lastBlockID == -1):
		lastBlockID = Block.objects.all().aggregate(Max('blockid')).get("blockid__max")
	lastBlockID = lastBlockID + 1
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


################################  Block Info Pages #############################################

@login_required
@user_passes_test(is_manager)
def blockInfo(request):
	context = RequestContext(request)
	context_dict={}
	return render_to_response('manager/blockInfo.html', context_dict, context)
################################################################################################
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



###################### Add block id query in context detail########################
@login_required
@user_passes_test(is_manager)
def managerBlocks(request):
	context = RequestContext(request)
	blockInfo = Block.objects.all()
	#venueInfo = SubvenueUsedforSession.objects.filter(session_sessionid__in=sessionInfo.values_list('sessionid'))
	#info = sessionInfo | venueInfo
	context_dict={'blocks':blockInfo}
	return render_to_response('manager/blocks.html', context_dict, context)
###################################################################################


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
	return render_to_response('success.html', context_dict, context)


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

@login_required
@user_passes_test(is_parent)
def childProfile(request, id):
	context = RequestContext(request)
	context_dict = {}
	parentid = request.user.id
	child = Client.objects.get(uid=id)
	if request.method == 'POST':
		form = EditPersonalDetailsForm(request.POST)
		# If the request was not a POST, display the form to enter details.
	form = EditPersonalDetailsForm()
	context_dict['form'] = form
	context_dict['child'] = child
	return render_to_response('parent/childProfile.html', context_dict, context)


@login_required
@user_passes_test(is_parent)
def childProfile(request, id):
	context = RequestContext(request)
	context_dict = {}
	parentid = request.user.id
	child = Client.objects.get(uid=id)

	if request.method == 'POST':
		form = EditPersonalDetailsForm(request.POST)
		# Have we been provided with a valid form?
		if form.is_valid():
			info=form.save(commit=False)
			child.telephone = info.telephone
			child.email = info.email
			child.save()
			# Redirect on success
			return redirect('/success.html')
		else:
			# The supplied form contained errors - just print them to the terminal.
			print form.errors
	else:
		# If the request was not a POST, display the form to enter details.
		form = EditPersonalDetailsForm()
		context_dict['form'] = form
		context_dict['child'] = child
<<<<<<< HEAD
		return render_to_response('parent/childProfile.html', context_dict, context)

=======
		return render_to_response('parent/editChildProfile.html', context_dict, context)

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
 		print form
 		#If the request was not a POST, display the form to enter details.
 	else:
 		form = EditPersonalDetailsForm()
 		context_dict['form'] = form
		context_dict['sessions'] = sessions
 		context_dict['child'] = child
 	return render_to_response('parent/childProfile.html', context_dict, context)

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
def addChild(request):
	if request.method == "POST":
		global lastID

		# THIS NEED TO BE CHANGED TO AUTOINCREMENT IN THE DATABASE!
		if (lastID == -1):
			lastID = Client.objects.all().aggregate(Max('uid')).get("uid__max")

		lastID = lastID + 1

		try:
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
		except:
			return redirect('/fail.html')
	return redirect('/success.html')

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

@login_required
@user_passes_test(is_manager)
def sessionInfo(request, sessionID):
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


@login_required
@user_passes_test(is_manager)
def addSession(request):
	context = RequestContext(request)
	context_dict={}

	# A HTTP POST?
	if request.method == 'POST':
		form = SessionForm1(request.POST)
		# Have we been provided with a valid form?
		if form.is_valid():
			session=form.save(commit=False)
			session.sessionid = getLastSessionID()
			print session.begintime

			# Now save to the DB block.save()
			# Redirect on success
			return redirect('/success.html')
		else:
			# The supplied form contained errors - just print them to the terminal.
			#print form.begintime
			print form.errors
	else:
		# If the request was not a POST, display the form to enter details.
		form = SessionForm1()
	return render_to_response('manager/addSession.html', {'form': form}, context)

	# if request.method == "POST":
	# 	global lastSessionID

	# 	# THIS NEED TO BE CHANGED TO AUTOINCREMENT IN THE DATABASE!
	# 	if (lastSessionID == -1):
	# 		lastSessionID = Session.objects.all().aggregate(Max('sessionid')).get("sessionid__max")

	# 	lastSessionID = lastSessionID + 1
	# 	try:

	# 		f_sessionid = lastSessionID
	# 		f_duration = request.POST.get("duration", "")
	# 		f_begintime = request.POST.get("begintime", "")
	# 		f_endtime = request.POST.get("endtime", "")
	# 		block_blockid = int(request.POST.get("block_blockid", ""))
	# 		f_block_blockid = Block.objects.get(blockid=block_blockid)
	# 		f_capacity = request.POST.get("capacity", "")
	# 		f_agegroup = request.POST.get("agegroup", "")
	# 		f_skillgroup = request.POST.get("skillgroup", "")
	# 		f_isfull = request.POST.get("isfull", "")
	# 		# VALIDATION HERE!!!

	# 		p = Session.objects.get_or_create(sessionid=f_sessionid, duration=f_duration, begintime=f_begintime, endtime=f_endtime, block_blockid=f_block_blockid, capacity=f_capacity, agegroup=f_agegroup, skillgroup=f_skillgroup, isfull=f_isfull )
	# 	#return redirect('/bookingsystem/manager/confirmed.html')
	# 	except:
	# 		return redirect('/fail.html')
	# 	return redirect('/success.html')
	# else:
	# 	return render_to_response('manager/addSession.html', context_dict, context)

@login_required
@user_passes_test(is_manager)
def addBlock(request):
	context = RequestContext(request)
	# A HTTP POST?
	if request.method == 'POST':
		form = BlockForm(request.POST)
		# Have we been provided with a valid form?
		if form.is_valid():
			block=form.save(commit=False)
			block.blockid = getLastBlockID()
			# Now save to the DB block.save()
			print block.begindate
			# Redirect on success
			return redirect('/success.html')
		else:
			# The supplied form contained errors - just print them to the terminal.
			print form.errors
	else:
		# If the request was not a POST, display the form to enter details.
		form = BlockForm()
	return render_to_response('manager/addBlock.html', {'form': form}, context)









