from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


from backend import views


urlpatterns = [
    url(r'^expos/$', views.check, name='check'),
    url(r'^pic/$', views.return_picture, name='return_picture'),
    url(r'^pic/(?P<pk>\d+)/$', views.return_picture, name='return_picture'),
    url(r'^expo/$', views.return_expo, name='return_expo'),
    url(r'^expo/(?P<num>\d+)/$', views.return_expo, name='return_expo')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
