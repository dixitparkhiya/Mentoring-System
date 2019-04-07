
from django.contrib import admin
from django.urls import path,re_path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name = 'student'

urlpatterns = [

    re_path(r'^upload/$', views.upload, name="upload"),
    re_path(r'^$',views.home, name="home"),
]

