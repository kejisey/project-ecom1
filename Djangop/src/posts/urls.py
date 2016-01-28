from django.conf.urls import url
from django.contrib import admin
from django.utils.text import slugify

from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    wedliny_list,
    garmazeria_list,
    art_spozywcze_list,
    napoje_list,
	)

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^wedliny/$', wedliny_list),
    url(r'^garmazeria/$', garmazeria_list),
    url(r'^art_spozywcze_list/$', art_spozywcze_list),
    url(r'^napoje_list/$', napoje_list),
    url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    

]