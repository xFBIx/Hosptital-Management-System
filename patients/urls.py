from django.urls import path, include
from . import views as patient_views
from .views import loginview

urlpatterns = [
    path('make-profile/', patient_views.make_profile, name='make-profile'),
    path('accounts/login/', loginview.as_view(), name='account_login'),
    path('accounts/', include('allauth.urls')),
    path('appointment/', patient_views.appointment, name='appointment'),
    path('profile/', patient_views.profile, name='profile'),
    path('profile/update/', patient_views.profile_update, name='profile-update'),
    path('account/', patient_views.account, name='account'),
    path('paybill/<int:pk>', patient_views.paybill, name='paybill'),
]