
from django.contrib import admin
from django.urls import path,re_path,include
from student import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'^$', views.home, name="home"),
    # re_path(r'^upload/$', views.upload, name="upload"),
    re_path(r'^accounts/',include('accounts.urls')),
    re_path(r'^',include('student.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
