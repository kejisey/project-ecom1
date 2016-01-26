from django.conf.urls import url
from django.contrib import admin
from django.utils.text import slugify

from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    items1,
	)

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^items1/$', items1),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    

]