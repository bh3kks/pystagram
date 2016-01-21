# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Photo

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
