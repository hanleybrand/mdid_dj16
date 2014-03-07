from django.conf.urls import *
from views import set_marker


urlpatterns = patterns('',
    url(r'^audiotextsync/(?P<id>[\d]+)/(?P<name>[-\w]+)/setmarker/$', set_marker, name='audiotextsync-setmarker'),
)
