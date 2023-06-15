from django.urls import path
from .views import LoginView
from general_pages.decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from staff import views as staff_views

urlpatterns = [
    path('register-staff/', staff_views.register_staff, name='register-staff'),
    path('login-staff/', unauthenticated_user(LoginView.as_view(template_name='staff/login-staff.html')), name='login-staff'),
    path('logout-staff/', auth_views.LogoutView.as_view(template_name='staff/logout-staff.html'), name='logout-staff'),
    path('patients/', staff_views.patients, name='patients'),
    path('patient/<int:pk>/', staff_views.patient_detail, name='patient-detail'),
    path('profile-table/', login_required(login_url='login-staff')(allowed_users(allowed_roles='Staff')(staff_views.PersonListView.as_view())), name='profile-table'),
]