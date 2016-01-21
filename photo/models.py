# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

# Create your models here.
# models.py : 모델은 데이터를 구성하는 항목 자체(field)와 데이터를 다루는 행위(behavior)를 포함

class Photo(models.Model):
	# Model의 속성은 field로 나타냄 -> Django가 제공하는 자료형
	# 각 field는 field option이 존재
	# 개별 사진을 구분하는 id - 자동 생성

	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	# settings에 존재하는 이용자 모델이위치한 경로 문자열

	image_file = models.ImageField(upload_to='original/%Y/%m/%d')
	# 원본 사진 파일 - ImageField 사용
	# 사진은 해당 위치로 전송, %Y/%m/%d로 년/월/일에 맞는 폴더에 저장

	filtered_image_file = models.ImageField(upload_to='filtered/%Y/%m/%d')
	# 필터 적용된 사진 파일 - ImageField 사용

	description = models.TextField(max_length=300, blank=True)

	# 사진에 대한 설명

	created_at = models.DateTimeField(auto_now_add=True)
	# 생성일시

	def delete(self, *args, **kwargs):
		# 해당 클래스를 지우고 연결된 데이터도 지우는 delete 함수
		self.image_file.delete()
		self.filtered_image_file.delete()
		super(Photo, self).delete(*args, **kwargs)
		# 삭제할 인자를 알지 못하는 경우에 args, kwargs로 넘겨받은 인자를 삭제

	def get_absolute_url(self):
		return reverse_lazy('view_single_photo', kwargs={'photo_id': self.id})
		# 현재 사진의 photo_id를 self.id로 전달하여 URL을 가져옴



