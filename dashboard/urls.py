from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('dashboard.views',
    # Example:
    (r'^$', 'startups'),
    (r'^startups/$', 'startups'),
    (r'^startups/(?P<startup_id>\d+)/$', 'startup_detail'),
    (r'^startups/(?P<startup_id>\d+)/reviews/new/$', 'new_review'),
    (r'^startups/(?P<startup_id>\d+)/reviews/(?P<review_id>\d+)/', 'review_detail'),
    (r'^people/$', 'people'),
    (r'^people/(?P<person_id>\d+)/$', 'person_detail'),
    (r'^json/startups/$', 'json_startups'),
    
)

