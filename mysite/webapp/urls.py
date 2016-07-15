from django.conf.urls import url
from . import views # relative import from current package, locally

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^projects/$', views.projects, name='projects'),
]
