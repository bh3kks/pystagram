# coding: utf-8
from django.db import models

# Create your models here.
# models.py : 모델은 데이터를 구성하는 항목 자체(field)와 데이터를 다루는 행위(behavior)를 포함

class Photo(models.Model):
	# Model의 속성은 field로 나타냄 -> Django가 제공하는 자료형
	# 각 field는 field option이 존재
	# 개별 사진을 구분하는 id - 자동 생성
	
	image_file = models.ImageField()
	# 원본 사진 파일
	filtered_image_file = models.ImageField()
	# 필터 적용된 사진 파일
	description = models.TextField(max_length=300)
	# 사진에 대한 설명
	created_at = models.DateTimeField(auto_now_add=True)
	# 생성일시

