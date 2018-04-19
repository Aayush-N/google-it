from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import *
from django.forms import ModelForm

class LoginForm(AuthenticationForm):
	'''
	Form for taking Username and password
	'''
	username = forms.CharField(label="usn", max_length=30,
							   widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'id': 'username','placeholder': 'Enter Username'}))
	password = forms.CharField(label="Password", max_length=30,
							   widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'id': 'password', 'placeholder': 'Enter Password'}))

class AnswerForm(forms.ModelForm):
	class Meta:
		model = UserAnswers
		fields = ['answer',]
