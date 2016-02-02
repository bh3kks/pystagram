# coding: utf-8

from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from .models import UserProfile
from profiles.profile_forms import ProfileEditForm
from django.contrib.auth.decorators import login_required

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

		else:
			return HttpResponse('Existing ID or Password Error!')

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
	num_of_photos = photos.count()
	# 이용자모델 중 username이 같은 객체를 저장
	try:
		user_profile = get_object_or_404(UserProfile, user=user) 
	except:
		user_profile = 0

	return render(request, 'timeline.html', 
		{
			'current_user': user,
			'photos': photos,
			'current_user_profile': user_profile,
			'num_of_photos':num_of_photos,
		}
	)

def profile(request, username):

	User = get_user_model()
	user = get_object_or_404(User, username=username)

	try:
		user_profile = get_object_or_404(UserProfile, user=user) 
	except:
		return redirect('/user/%s/profile/edit/' % user)

	return render(request, 'profile.html', 
		{
			'current_user': user,
			'current_user_profile': user_profile,
		}
	)

@login_required
def profile_edit(request, username):

	if not request.user.is_authenticated():
		return redirect(settings.LOGIN_URL)

	User = get_user_model()
	user = get_object_or_404(User, username=username)

	first_edit = ''

	try:
		user_profile = get_object_or_404(UserProfile, user=user)
	except:
		first_edit = 'You Should Upload Your Profile!'

	if request.user != user:
		return HttpResponse('Not Your Profile')

	if request.method == "GET":
		edit_form = ProfileEditForm()

	# post의 경우 post로 전달한 객체가 request.POST에, 파일은 request.FILES에 담겨있다
	elif request.method == "POST":
		edit_form = ProfileEditForm(request.POST, request.FILES)

		# is_valid : 폼에 전달된 모든 데이터가 유효하면 True
		if edit_form.is_valid():
			new_profile = edit_form.save(commit=False)
			# commit=False : 인스턴스 객체만 반영하고 DB에 실제로 반영하지 않음

			new_profile.user = user
			# 해당 객체에 user할당 (request에는 기본적으로 user도 같이 넘어옴)
			new_profile.save()
			# PhotoEditForm을 저장하지만 Photo를 기반으로 하므로 Photo 객체가 저장
			if first_edit=='':
				user_profile.delete()

			return redirect('/user/%s/profile/' % user)
			# redirect는 해당 url로 이동

	return render(request, 'profile_edit.html', 
		{
			'form': edit_form,
			'current_user': user,
			'first_edit':first_edit,
		}
	)