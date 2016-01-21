# coding: utf-8

from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model


def profile(request, username):

	User = get_user_model()
	# get_user_model : settings의 이용자 모델을 가져옴

	user = get_object_or_404(User, username=username)
	# 이용자모델 중 username이 같은 객체를 저장

	return render(request, 'profile.html', {'current_user': user,})
