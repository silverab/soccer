from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from team import views

urlpatterns = [
	path('team/', views.teamhome, name='teamhome'),
	
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)