from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from app import views

urlpatterns = [
	path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.single, name='single'),
    path('profile/', views.profile, name='profile'),
    path('deactivate/', views.delprofile, name='delaccount'),
    path('signup/', views.Signup, name='signup'),
    path('matches/', views.matches, name='matches'),
    path('teams/', views.teams, name='teams'),
    path('teams/<slug:slug>/', views.country, name='single_country'),
    path('contact/', views.contact, name='contact'),
    
    # path('profile/<int:pk>/', views.profile, name='profile'),
    # path('blog/single/', views.single, name='single'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)