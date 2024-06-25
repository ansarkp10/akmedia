from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('content/<int:pk>/', views.content_detail, name='content_detail'),    
    path('content/create/', views.content_create, name='content_create'),
    path('content/<int:pk>/update/', views.content_update, name='content_update'),
    path('content/<int:pk>/delete/', views.content_delete, name='content_delete'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('menu/', views.menu, name='menu'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
