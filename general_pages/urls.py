from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('chat/<str:chat_box_name>/', views.chat_box, name='chat'),
]