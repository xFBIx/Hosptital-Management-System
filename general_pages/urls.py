from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]