from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import *

admin.site.site_header = 'GoogleIt Admin Interface'

@admin.register(User)
class UserAdmin(DjangoUserAdmin):

	fieldsets = (
		(None, {'fields': ('username', 'email', 'password')}),
		(('Personal info'), {'fields': ('first_name', 'last_name', 'phone')}),
		# (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
		# 							   'groups', 'user_permissions')}),
		(('Academic Details'), {'fields': ('college',)}),
		# (('Important dates'), {'fields': ('last_login', 'date_joined')}),
		(('Completion'), {'fields': ('answered',)})
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2'),
		}),
	)

	list_display = ('username', 'first_name', 'phone', 'college', 'answered', 'last_answered_time')
	search_fields = ('first_name', 'college', 'username', 'phone')
	ordering = ('username',)

@admin.register(GameTime)
class GameTimeAdmin(admin.ModelAdmin):
	list_display = ('user_function','start_time','end_time')
	search_fields = ('user_function',)

	def user_function(self, instance):
		return instance.username

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('description','question_no')
	search_fields = ('description', 'question_no')

@admin.register(UserAnswers)
class UserAnswersAdmin(admin.ModelAdmin):
	list_display = ('question_function','user_function','answer')
	search_fields = ('question_function', 'user_function')

	def question_function(self, instance):
		return instance.question_no

	def user_function(self, instance):
		return instance.username

