from django.conf.urls import patterns, url
from manager import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^index', views.index, name='index'),
	url(r'^bookings', views.bookings, name='bookings'),
<<<<<<< HEAD
	url(r'^coaches', views.coaches, name='coaches')
)
=======
	url(r'^coaches', views.coaches, name='coaches'),
	url(r'^coachProfile', views.coachProfile, name='coachProfile'),
	url(r'^members', views.members, name='members'),
	url(r'^confirmbooking', views.confirmbooking, name='confirmbooking'),
	url(r'^audit', views.audit, name='audit'))
>>>>>>> 44dba765de46bf369610a1855c4353354151bda0
