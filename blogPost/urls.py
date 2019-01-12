from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
app_name='blogApp'
urlpatterns=[
	url(r'login/$',
		auth_views.LoginView.as_view(template_name='blogPost/login.html'),
		name='login'),
	url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),
	url(r'signup/$',views.SignUp.as_view(),name='signup'),	
	url(r'create/$',views.CreateBlog.as_view(),name='create'),
	url(r'^(?P<pk>[-\w]+)/$',views.ViewBlog.as_view()),
]