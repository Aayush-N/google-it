from django.db import models
from django.contrib.auth.models import AbstractUser, User


class User(AbstractUser):
	"""
	Description: Holds details about the user
	"""
	phone = models.CharField("Phone", max_length=15, null=True, blank=True)
	college = models.CharField("College Name", max_length=50, null=True, blank=True)
	answered = models.IntegerField(default=0)
	last_answered_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.username

class Question(models.Model):
	"""
	Description: Contains the questions
	"""
	description = models.CharField("Question description", max_length=100)
	question_no = models.IntegerField(default=1)
	no_of_images = models.IntegerField(default=1)
	image = models.ManyToManyField('ImageModel')
	answer = models.CharField("Answer to the question", max_length=50)

	def __str__(self):
		return self.description
 

class UserAnswers(models.Model):
	"""
	Description: Store users answers
	"""
	question = models.ForeignKey('question')
	user = models.ForeignKey('user')
	answer = models.CharField("Answer given to the question", max_length=50)

	def __str__(self):
		return self.user.username


class GameTime(models.Model):
	"""
	Description: Game Time Elapsed
	"""
	user = models.ForeignKey('user')
	start_time =  models.DateTimeField(auto_now=True)
	end_time =  models.DateTimeField()
	
	def __str__(self):
		return self.user.username

class ImageModel(models.Model):
	document = models.FileField(upload_to='images/', default='..img/default.jpg')
	question_no = models.IntegerField(default=1)

	def __str__(self):
		return str('Question ' + str(self.question_no))