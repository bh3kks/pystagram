from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', views.timeline, name='timeline'),
    # [\w.@+-]+은 django에 내장된 username 패턴과 일치

    url(r'^(?P<username>[\w.@+-]+)/profile/$', views.profile, name='profile'),
    # 해당 유저의 프로필 출력

    url(r'^(?P<username>[\w.@+-]+)/profile/edit/$', views.profile_edit, name='profile_edit'),
   	# 프로필을 수정하는 화면
]