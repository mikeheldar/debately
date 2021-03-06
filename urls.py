import os

from django.conf.urls.defaults import *

urlpatterns = patterns('debately.views',
    (r'^debates/challenge/(\d+)', 'challenge_debate'),
    (r'^debates/create/$', 'create_debate'),
    (r'^debates/(\d+)$', 'debate'),
    (r'^entries/(\d+)/comment/', 'create_comment'),
    (r'^messages$', 'usermessages'),                       
    (r'^users/(.*)', 'userpage'),
    (r'^$', 'index'),
)
