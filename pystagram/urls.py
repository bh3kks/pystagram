from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

	url(r'^photo/(?P<photo_id>\d+)/$', 'photo.views.single_photo', name='view_single_photo'),
	# 하나의 사진 출력 url
	# url(regex(정규표현식) , view(화면 표시할 함수), name)

	url(r'^photo/upload/$', 'photo.views.new_photo', name='new_photo'),
	# 사진 업로드 url

	url(r'^accounts/login/', 'django.contrib.auth.views.login', name='login',
		kwargs={'template_name': 'login.html'}),
	# login 화면 url - 장고에 내장된 login 함수 사용
	# kwargs는 해당 login함수에 추가로 인자 전달 : key가 'template_name'이고 값이 'login.html'
	# login함수에 template_name이 전달되면 login.html을 로그인 화면 출력으로 사용

    url(r'^accounts/logout/', 'django.contrib.auth.views.logout', name='logout'),
    # logout 화면 url - 장고에 내장된 logout 함수 사용

    url(r'^admin/', include(admin.site.urls)),
    # admin url
)

# media url 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
