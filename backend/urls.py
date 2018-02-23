from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


from backend import views


urlpatterns = [
    url(r'^test/$', views.check, name='check'),
    url(r'^pic/$', views.return_picture, name='return_picture')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
