from django.conf.urls import patterns, url
from manager import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
    url(r'^loggedin', views.loggedin, name='loggedin'),
	url(r'^index', views.index, name='index'),
	url(r'^bookings', views.bookings, name='bookings'),
	url(r'^coaches', views.coaches, name='coaches'),
    url(r'^members', views.members, name='members')
)
	# url(r'^coaches', views.coaches, name='coaches'),
	# url(r'^coachProfile', views.coachProfile, name='coachProfile'),
	# url(r'^members', views.members, name='members'),
	# url(r'^confirmbooking', views.confirmbooking, name='confirmbooking'),
	# url(r'^audit', views.audit, name='audit'))
