# coding: utf-8

from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

def main_view(request):
	# 메인 화면 출력
	return render(request, 'main_view.html')


def signin(request):

	if request.method == "GET":
		userform = UserCreationForm()

	elif request.method == "POST":
		userform = UserCreationForm(request.POST)

		if userform.is_valid():
			userform.save()

			return HttpResponse('COMPLETE SIGN IN')

	return render(request, "signin.html", {"userform": userform,})


def login_view(request):
	# 로그인 화면 출력
	return render(request, 'login.html')

def login_check(request):
	# 아이디, 비밀번호 체크 뷰
	if 'email' in request.POST:
		if len(request.POST['email']) == 0:
			return HttpResponse('글자를 입력하세요.')
		else:
			cur_email = request.POST['email']
	else: 
		return HttpResponse('False in ID')

	if 'password' in request.POST:
		if len(request.POST['password']) == 0:
			return HttpResponse('글자를 입력하세요.')
		else:
			cur_password = request.POST['password']
	else: 
		return HttpResponse('False in password')

	user = authenticate(username=cur_email, password=cur_password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect('/user/%s/' %cur_email)
		else:
			return HttpResponse('ACCOUNT DISABLED')
	else:
		return HttpResponse('INCORRECT PASSWORD.')


def timeline(request, username):

	User = get_user_model()
	# get_user_model : settings의 이용자 모델을 가져옴

	user = get_object_or_404(User, username=username)
	photos = user.photo_set.order_by('-created_at', '-pk')
	# 이용자모델 중 username이 같은 객체를 저장

	return render(request, 'timeline.html', 
		{
			'current_user': user,
			'photos': photos,
		}
	)

def profile(request, username):

	User = get_user_model()
	user = get_object_or_404(User, username=username)

	return HttpResponse('%s Profile' % user)