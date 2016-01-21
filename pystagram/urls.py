from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

	url(r'^photo/(?P<photo_id>\d+)/$', 'photo.views.single_photo', name='view_single_photo'),
	# 하나의 사진 출력 url
	# url(regex(정규표현식) , view(화면 표시할 함수), name)
	url(r'^photo/upload/$', 'photo.views.new_photo', name='new_photo'),
	

    url(r'^admin/', include(admin.site.urls)),
    # admin url
)

# media url 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
