from django.conf.urls import url

from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout

from . import forms
from . import views

urlpatterns = [
    url(r'^question/(?P<q_no>[-\w]+)', views.HomeView.as_view(), name='question'),
    url(r'^login/', login, {'template_name': 'login.html','authentication_form': forms.LoginForm}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/exit'}, name='logout'),
]
