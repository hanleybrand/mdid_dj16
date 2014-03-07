#TODO - when app is running and all changes are committed: remove old comments and reformat for PEP8
from django.conf.urls import patterns, url, include
from django.contrib.contenttypes.models import ContentType
# from django.views.generic.simple import direct_to_template
from django.views.generic import TemplateView

#  from django.views.generic.create_update import create_object, delete_object, update_object is gone --
# django.views.generic.create_update.create_object replaced by
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib.comments.models import Comment
from django.contrib.flatpages.models import FlatPage
from django.utils.functional import lazy
from django.conf import settings
from views import *

reverse_lazy = lazy(reverse, str)

urlpatterns = patterns('',
    url(r'^css/(?P<stylesheet>[-\w]+)/$', css, name='ui-css'),
    url(r'^api/select-record/', select_record, name='ui-api-select-record'),
    url(r'^tag/(?P<type>\d+)/(?P<id>\d+)/', add_tags, name='ui-add-tags'),
    url(r'^tag/remove/(?P<type>\d+)/(?P<id>\d+)/', remove_tag, name='ui-remove-tag'),
    url(r'^manage/$', manage, name='ui-management'),
    url(r'^options/$', options, name='ui-options'),
    url(r'^clear-selected/$', clear_selected_records, name='ui-clear-selected'),
    url(r'^delete-selected/$', delete_selected_records, name='ui-delete-selected'),
    # direct_to_template replaced in dj1.5
    # url(r'^report-problem/$', direct_to_template, {'template': 'ui_report_problem.html'}, name='ui-report-problem'),
    url(r'^report-problem/$', TemplateView.as_view(template_name='ui_report_problem.html'), name='ui-report-problem'),
    url(r'^announcement/new/$', CreateView, {
        'model': Comment,
        'template_name': 'ui_announcements_form.html',
        'extra_context': {
            'flatpage_content_type': ContentType.objects.get_for_model(FlatPage).id,
            'site': settings.SITE_ID,
        },
        'post_save_redirect': reverse_lazy('main'),
        'login_required': True,
        }, name='ui-announcement-new'),
    url(r'^announcement/(?P<object_id>\d+)/edit/$', UpdateView, {
        'model': Comment,
        'template_name': 'ui_announcements_form.html',
        'extra_context': {
            'flatpage_content_type': ContentType.objects.get_for_model(FlatPage).id,
            'site': settings.SITE_ID,
        },
        'post_save_redirect': reverse_lazy('main'),
        'login_required': True,
        }, name='ui-announcement-edit'),
    url(r'^announcement/(?P<object_id>\d+)/delete/$', DeleteView, {
        'model': Comment,
        'template_name': 'ui_announcements_delete.html',
        'post_delete_redirect': reverse_lazy('main'),
        'login_required': True,
        }, name='ui-announcement-delete'),
)
