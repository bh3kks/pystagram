from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', views.timeline, name='timeline'),
    # [\w.@+-]+은 django에 내장된 username 패턴과 일치

    url(r'^(?P<username>[\w.@+-]+)/profile/$', views.profile, name='profile'),
    # 해당 유저의 프로필 출력
    # User 모델을 새롭게 정의하여
    # 프로필 사진, 개인 설명, 팔로워 등의 정보 만들 것
]