from django.conf.urls import url

from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.views import login, logout

from . import forms
from . import views

urlpatterns = [
    url(r'^/$', RedirectView.as_view(url='/login')),
    url(r'^question/(?P<q_no>[-\w]+)', views.HomeView.as_view(), name='question'),
    url(r'^login/', login, {'template_name': 'login.html','authentication_form': forms.LoginForm}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/exit'}, name='logout'),
    url(r'^start/', views.start_view, name='start'),
    url(r'^caught/', TemplateView.as_view(template_name='caught.html')),
    url(r'^finish/', views.finish_view, name='finish'),
    url(r'^rules/', TemplateView.as_view(template_name='rules.html'), name='rules'),
]
