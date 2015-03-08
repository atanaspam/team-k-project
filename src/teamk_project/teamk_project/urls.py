from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.contrib.auth.views import password_reset
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/password/reset/done/'}, name="password_reset"),
    url(r'^password/reset/done/$','django.contrib.auth.views.password_reset_done'),
    url(r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/password/done/'}),
    url(r'^password/done/$', 'django.contrib.auth.views.password_reset_complete'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bookingsystem/', include('bookingsystem.urls')),
    url(r'^$', 'teamk_project.views.index', name='index'),
    url(r'^login/', 'teamk_project.views.login', name='login'),
    url(r'^register', 'teamk_project.views.register', name='register'),
    url(r'^logout/', 'teamk_project.views.logout', name='logout'),
    url(r'^invalid', 'teamk_project.views.invalid', name='invalid'),
    url(r'^fail', 'teamk_project.views.fail', name='fail'),
    url(r'^success', 'teamk_project.views.success', name='success'),
    url(r'^successEmb', 'teamk_project.views.successEmb', name='successEmb'),
    url(r'^editProfile', 'teamk_project.views.editProfile', name='editProfile'),
    url(r'^about','teamk_project.views.about', name='about'),
    url(r'^ageGroups','teamk_project.views.ageGroups', name='ageGroups'),
    url(r'^contact','teamk_project.views.contact', name='contact'),
    url(r'^events','teamk_project.views.events', name='events'),
    url(r'^news','teamk_project.views.news', name='news'),

)