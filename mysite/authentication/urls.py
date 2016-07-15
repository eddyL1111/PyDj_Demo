from django.conf.urls import url
from . import views 

urlpatterns = [
	url(r'^login/$', views.LoginForm.as_view(), name='login'),
	url(r'^signup/$', views.SignupForm.as_view(), name='signup'),
	url(r'^$', views.index, name='index'),
	url(r'^logout/$', views.LogoutView, name='logout'),
]