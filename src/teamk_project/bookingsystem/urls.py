from django.conf.urls import patterns, url
from bookingsystem import views



urlpatterns = patterns('',
	url(r'^index/$', views.index, name='index'),
	url(r'^coach/$', views.coachIndex, name='coachIndex'),
	url(r'^coach/index', views.coachIndex, name='coachIndex'),
	url(r'^coach/sessions', views.sessions, name='sessions'),
	url(r'^coach/attendance/(?P<id>\d+)?', views.attendance, name='attendance'),
    url(r'^coach/printAttendance/(?P<id>\d+)?', views.printAttendance, name='printAttendance'),
	url(r'^coach/attended/(?P<id>\d+)/(?P<sid>\d+)?', views.attended, name='attended'),
	url(r'^coach/submitAttendance', views.submitAttendance, name='submitAttendance'),
    url(r'^coach/editProfile', views.editProfile, name='editProfile'),
    url(r'^coach/printScheduleCoach', views.printScheduleCoach, name='printScheduleCoach'),
	url(r'^manager/markPaid', views.markPaid, name="processPayment"),
	url(r'^manager/$', views.managerIndex, name='index'),
	url(r'^manager/applicationApproved/$', views.applicationApproved, name='applicationApproved'),
	url(r'^manager/applicationDeclined/$', views.applicationDeclined, name='applicationDeclined'),
	url(r'^manager/applicationAllApproved/$', views.applicationAllApproved, name='applicationAllApproved'),
	url(r'^manager/applicationAllDeclined/$', views.applicationAllDeclined, name='applicationAllDeclined'),
	url(r'^manager/applicationDeleted/$', views.removeSelection, name='removeSelection'),
	url(r'^manager/index', views.managerIndex, name='index'),
	url(r'^manager/loggedin', views.loggedin, name='loggedin'),
	url(r'^manager/bookings', views.managerBookings, name='managerBookings'),
	url(r'^manager/confirmbooking', views.confirmbooking, name='confirmbooking'),
	url(r'^manager/coaches', views.coaches, name='coaches'),
	url(r'^manager/coachProfile/(?P<id>\d+)?', views.coachProfile, name='coachProfile'),
    url(r'^manager/managers', views.managers, name='managers'),
    url(r'^manager/managerProfile/(?P<id>\d+)?', views.managerProfile, name='managerProfile'),
	url(r'^manager/members', views.members, name='members'),
	url(r'^manager/sessions', views.managerSessions, name='managerSessions'),
	url(r'^manager/blocks', views.managerBlocks, name='managerBlocks'),
	url(r'^manager/blockInfo/(?P<bid>\d+)?', views.blockInfo, name='blockInfo'),
	url(r'^manager/audit', views.audit, name='audit'),
	url(r'^manager/addSession', views.addSession, name='addSession'),
	url(r'^manager/removeSession/(?P<sid>\d+)?', views.removeSession, name='removeSession'),
	url(r'^manager/confirmRemoveSession/(?P<sid>\d+)?', views.confirmRemoveSession, name='confirmRemoveSessionx'),
	url(r'^manager/addBlock', views.addBlock, name='addBlock'),
	url(r'^manager/removeBlock/(?P<bid>\d+)?', views.removeBlock, name='removeBlock'),
	url(r'^manager/confirmRemoveBlock/(?P<bid>\d+)?', views.confirmRemoveBlock, name='confirmRemoveBlock'),
	url(r'^manager/editProfile', views.editProfile, name='editProfile'),
	url(r'^parent/$', views.parentIndex, name='parentIndex'),
	url(r'^parent/index', views.parentIndex, name='parentIndex'),
	url(r'^parent/paypalConfirm', views.paypalConfirm, name='paypalConfirm'),
	url(r'^parent/bookSessions(\d{1,5})/(\d{1,5})', views.bookSessions1, name='bookSessions1'),
	url(r'^parent/bookSessions', views.bookSessions, name='bookSessions'),
	url(r'^parent/bookSeason(\d{1,5})/(\d{1,5})', views.bookSeason1, name='bookSeason1'),
	url(r'^parent/bookSeason', views.bookSeason, name='bookSeason'),
	url(r'^parent/bookings', views.parentBookings, name='parentBookings'),
	url(r'^parent/userBookings(\d{1,5})', views.userBookings, name='userBookings2'),
	url(r'^parent/userBookings', views.userBookings, name='userBookings'),
	url(r'^parent/confirmBookings/(?P<uID>\d+)?', views.confirmBookings, name='confirmBookings'),
	url(r'^parent/confirmBookings', views.confirmBookings, name='confirmBookings'),
	url(r'^parent/childrenList', views.childrenList, name='childrenList'),
	url(r'^parent/childProfile/(?P<id>\d+)?', views.childProfile, name='childProfile'),
	url(r'^parent/removeChild/(?P<uid>\d+)?', views.removeChild, name='removeChild'),
	url(r'^parent/confirmRemoveChild/(?P<uid>\d+)?', views.confirmRemoveChild, name='confirmRemoveChild'),
	url(r'^parent/addNewChild', views.addNewChild, name='addNewChild'),
	url(r'^parent/payments', views.payments, name='payments'),
	url(r'^parent/childSessions', views.childSessions, name='childSessions'),
	url(r'^manager/sessionInfo(\d{1,5})', views.sessionInfo, name='sessionInfo'),
	url(r'^manager/addCoachToSession', views.addCoachToSession, name='addCoachToSession'),
    url(r'^parent/editProfile', views.editProfile, name='editProfile'),
    url(r'^parent/printSchedule/(?P<uid>\d+)?', views.printSchedule, name='printSchedule'),
  url(r'^manager/removeCoachFromSession/(?P<id>\d+)/(?P<sid>\d+)?', views.removeCoachFromSession, name='removeCoachFromSession'),
  url(r'^manager/addChildToSession', views.addChildToSession, name='addChildToSession'),
  url(r'^manager/removeChildFromSession/(?P<id>\d+)/(?P<sid>\d+)?', views.removeChildFromSession, name='removeChildFromSession'),
  url(r'^manager/addNewCoach', views.addNewCoach, name='addNewCoach'),
  url(r'^manager/removeCoach/(?P<id>\d+)?', views.removeCoach, name='removeCoach'),
  url(r'^manager/confirmRemoveCoach/(?P<id>\d+)?', views.confirmRemoveCoach, name='confirmRemoveCoach'),
  url(r'^manager/addNewManager', views.addNewManager, name='addNewManager'),
  url(r'^manager/removeManager/(?P<id>\d+)?', views.removeManager, name='removeManager'),
  url(r'^manager/confirmRemoveManager/(?P<id>\d+)?', views.confirmRemoveManager, name='confirmRemoveManager'),
  url(r'^manager/managerChildProfile/(?P<id>\d+)?', views.managerChildProfile, name='managerChildProfile'),
  url(r'^manager/setDefaultCoaches',views.setDefaultCoaches, name='managerSetDefaultCoaches')
	#url(r'^manager/applicationApproved/$', views.applicationApproved, name='applicationApproved'),


	)
