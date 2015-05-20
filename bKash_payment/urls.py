from rest_framework.urlpatterns import format_suffix_patterns

__author__ = 'milu'

from django.conf.urls import patterns
from apps.users.decorator import login_required_custom as auth
from django.conf.urls import patterns,url,include
from views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url (
           regex = '^$',
           view =  auth(home),
           name = 'bKash-home'
    ),
)

urlpatterns = format_suffix_patterns(urlpatterns)