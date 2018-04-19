from django.shortcuts import render


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.core import serializers
from django.forms.models import model_to_dict
from django.shortcuts import render_to_response
from django.template import RequestContext


from django.views import View
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import resolve
from django.contrib.auth import logout

from .models import *

from .forms import *

from django.contrib.auth.hashers import make_password, check_password
import random
import urllib.parse as ap
import urllib.request
from django.core.mail import send_mail, EmailMessage
from django.db.models import Avg


def page_not_found_view(request):
	template_name = '404.html'
	context = {}
	return render(request, template_name, context)

def internal_server_error_view(request):
	error_url = request.get_full_path()
	template_name = '500.html'
	context = {"error_url": error_url}
	return render(request, template_name, context)

class HomeView(TemplateView):
	'''
	Generates OTP, checks if user exists and has an email address.
	'''
	template_name = 'question.html'
	max_questions = 20
	time_interval = 1

	def _fetch_question_no(self):
		current_user = self.request.user
		question_no = current_user.answered + 1
		return int(question_no)


	def get_context_data(self,q_no, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		form = AnswerForm()
		game_time = GameTime.objects.filter(user__username = self.request.user.username).first()
		end = game_time.end_time
		question = Question.objects.filter(question_no=q_no).first()
		print(question.no_of_images)
		image_no = question.no_of_images
		context['form'] = form
		context['q_no'] = q_no
		context['images'] = image_no
		context['end'] = end
		return context

	def get(self, request, q_no, **kwargs):
		context = self.get_context_data(q_no,**kwargs)
		print(q_no)
		user = self.request.user
		check_point = self._fetch_question_no()
		print(check_point)
		if int(check_point) != int(q_no):
			return redirect('/admin')
		else:
			if q_no == 1:
				time = GameTime.objects.filter(user = user).update(start_time=datetime.now()+timedelta(hours=5,minutes=30), end_time = (datetime.now()+timedelta(hours=5,minutes=30)) + timedelta(hours = time_interval))
				print('here')
			next_question = self._fetch_question_no()

			if next_question == (self.max_questions):
				return redirect('/finish')
		return render(request, self.template_name)

	def post(self, request, *args, **kwargs):
		user_answer = form.answer.data
		ans = Questions.query.objects.filter(q_no=q_no).all()
		answer_from_user = UserAnswers(q_no,session['uid'],user_answer)
		db.session.add(answer_from_user)
		db.session.commit()
		correct_answers = []
		for a in ans:
			correct_answers.append(a.answer)
		if user_answer.lower() in [c.lower() for c in correct_answers]:
			user = self.request.user
			points = user.answered
			points +=1 
			User.objects.filter(username = user.username).update(answered = points, last_answered_time=datetime.now()+timedelta(hours=5,minutes=30))
			next_question = fetch_question_no()
			if next_question == (self.max_questions):
				return redirect('/finish')
			next_question +=1
			return redirect('/question/'+str(next_question))
		else:
			flash("Wrong Answer")
			return render_template('question.html',form=form,q_no=q_no,images=int(images),end=end)

		return render(request, self.template_name)



