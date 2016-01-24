# coding: utf-8

from __future__ import unicode_literals
from django import forms
from profiles.models import UserProfile


class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ('user', )
