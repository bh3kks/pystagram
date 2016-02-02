from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from profiles.urls import urlpatterns as profile_urls

urlpatterns = [

	url(r'^main/$', 'profiles.views.main_view', name='main_view'),
	# 메인 화면 url

	url(r'^signin/$', 'profiles.views.signin', name='singin'),
	# 회원가입 화면 rul

	url(r'^login/check/$', 'profiles.views.login_check', name='login_check'),
	# login 체크 화면 url

    url(r'^accounts/logout/', 'django.contrib.auth.views.logout', name='logout'),
    # logout 화면 url - 장고에 내장된 logout 함수 사용

	url(r'^photo/(?P<photo_id>\d+)/$', 'photo.views.single_photo', name='view_single_photo'),
	# 하나의 사진 출력 url
	# url(regex(정규표현식) , view(화면 표시할 함수), name)

	url(r'^photo/upload/(?P<user_id>\d+)/$', 'photo.views.new_photo', name='new_photo'),
	# 사진 업로드 url

    url(r'^admin/', include(admin.site.urls)),
    # admin url

    url(r'^user/', include(profile_urls, namespace='profiles'),),
    # user로 시작하는 url의 경우 profile_urls객체를 매핑, 이름공간을 profiles로 지정
]

# media url 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
