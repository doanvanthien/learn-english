

from django.conf.urls import url

from . import views

# url(r'^(?P<part>[a-zA-Z]{1,})$', views.index, name='part'),
urlpatterns = [
	url(r'^$', views.index),
	url(r'get_word/$', views.get_word),
	url(r'exercise/$', views.exercises), # 
	url(r'update/$', views.update_modules), # update module
]