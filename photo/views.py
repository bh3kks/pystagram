# coding: utf-8
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Photo
from photo.forms import PhotoEditForm
from django.conf import settings

# view.py : 특정 url에 접근하면 화면에 표시할 내용 호출 


def single_photo(request, photo_id):

	# photo_id와 같은 객체를 photo에 저장
	# 객체가 없을 시 404 error
	photo = get_object_or_404(Photo, pk=photo_id)


	response_text = '<p>{photo_id}번 사진을 출력합니다.</p>'
	response_text += '<p>{photo_url}</p>'
	response_text += '<p><img src="{photo_url}" /></p>'

	return HttpResponse(response_text.format(
			photo_id=photo_id,
			photo_url=photo.image_file.url
		)
	)

@login_required
# login이 필요하다는 문구 출력
def new_photo(request):
	
	# is_authenticated : 로그인 여부를 ture/false로 반환
	if not request.user.is_authenticated():
		return redirect(settings.LOGIN_URL)

	# get의 경우 그대로 사용
	if request.method == "GET":
		edit_form = PhotoEditForm()

	# post의 경우 post로 전달한 객체가 request.POST에, 파일은 request.FILES에 담겨있다
	elif request.method == "POST":
		edit_form = PhotoEditForm(request.POST, request.FILES)

		# is_valid : 폼에 전달된 모든 데이터가 유효하면 True
		if edit_form.is_valid():
			new_photo = edit_form.save(commit=False)
			# commit=False : 인스턴스 객체만 반영하고 DB에 실제로 반영하지 않음
			new_photo.user = request.user
			# 해당 객체에 user할당 (request에는 기본적으로 user도 같이 넘어옴)
			new_photo.save()
			# PhotoEditForm을 저장하지만 Photo를 기반으로 하므로 Photo 객체가 저장

			return redirect(new_photo.get_absolute_url())
			# redirect는 해당 url로 이동

	return render(request,  'new_photo.html', {'form': edit_form,})
	# PhotoEditForm이 담긴 edit_form 객체를 전달

