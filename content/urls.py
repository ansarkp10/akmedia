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

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('menu/', views.menu, name='menu'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
