from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', views.profile, name='profile'),
    # [\w.@+-]+은 django에 내장된 username 패턴과 일치
]