from django.conf.urls import patterns, url
from bookingsystem import views

urlpatterns = patterns('',
    url(r'^index/$', views.index, name='index'),
	url(r'^coach/$', views.coachIndex, name='coachIndex'),
	url(r'^coach/index', views.coachIndex, name='coachIndex'),
	url(r'^coach/sessions', views.sessions, name='sessions'),
	url(r'^coach/attendance', views.attendance, name='attendance'),
	url(r'^coach/editProfile', views.coachEditProfile, name='coachEditProfile'),
	url(r'^manager/$', views.managerIndex, name='index'),
	url(r'^manager/applicationApproved/$', views.applicationApproved, name='applicationApproved'),
	url(r'^manager/index', views.managerIndex, name='index'),
    url(r'^manager/loggedin', views.loggedin, name='loggedin'),
	url(r'^manager/bookings', views.managerBookings, name='managerBookings'),
	url(r'^manager/confirmbooking', views.confirmbooking, name='confirmbooking'),
	url(r'^manager/coaches', views.coaches, name='coaches'),
	url(r'^manager/coachProfile', views.coachProfile, name='coachProfile'),
    url(r'^manager/members', views.members, name='members'),
    url(r'^manager/sessions', views.managerSessions, name='managerSessions'),
	url(r'^manager/audit', views.audit, name='audit'),
	url(r'^parent/$', views.parentIndex, name='parentIndex'),
	url(r'^parent/index', views.parentIndex, name='parentIndex'),
	url(r'^parent/bookSessions(\d{2})', views.bookSessions2, name='bookSessions1'),
	url(r'^parent/bookSessions(\d{1})', views.bookSessions1, name='bookSessions'),
	url(r'^parent/bookSessions', views.bookSessions, name='bookSessions'),
	url(r'^parent/bookings', views.parentBookings, name='parentBookings'),
	url(r'^parent/childrenList', views.childrenList, name='childrenList'),
	url(r'^parent/childProfile(\d{1})', views.childProfile1, name='childProfile1'),
	url(r'^parent/childProfile(\d{2})', views.childProfile2, name='childProfile2'),
	url(r'^parent/childProfile', views.childProfile, name='childProfile'), ##########  Remove that later
	url(r'^parent/addNewChild', views.addNewChild, name='addNewChild'),
	url(r'^parent/payments', views.payments, name='payments'),
	url(r'^parent/editProfile', views.parentEditProfile, name='parentEditProfile'),
	#url(r'^manager/applicationApproved/$', views.applicationApproved, name='applicationApproved'),
	url(r'^parent/childSessions', views.childSessions, name='childSessions'),

	)
	
