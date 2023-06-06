from django.shortcuts import render, redirect
from general_pages.decorators import unauthenticated_user
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import views as auth_views
from django.shortcuts import resolve_url
from django.contrib.auth.decorators import login_required
from general_pages.decorators import allowed_users
from patients.models import Profile, Appointment
from django.contrib.auth.models import User

# def about(request):
#     return render(request, 'general_pages/about.html')

class LoginView(auth_views.LoginView):
    next_page = None

    def form_valid(self, form):
        user = form.get_user()
        group = str(Group.objects.filter(user = user).first())
        if not (group == 'Staff'):
            messages.warning(self.request, f'You are not a staff member.')
            return redirect('login-staff')
        messages.success(self.request, f'Successfully signed in as {user}.')
        return super().form_valid(form)
    
    def get_success_url(self):
        return self.get_redirect_url() or self.get_default_redirect_url()
    
    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        return resolve_url(self.next_page or 'homepage')

@unauthenticated_user
def register_staff(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(Group.objects.get(name='Staff'))
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}! You can now log in')
            return redirect('login-staff')
    else:
        form = UserRegisterForm()
    return render(request, 'staff/register-staff.html', {'form': form})

@login_required(login_url='login-staff')
@allowed_users(allowed_roles='Staff')
def patients(request):
    context = { 'patients': Profile.objects.all() }
    return render(request, 'staff/patients.html', context)

@login_required(login_url='login-staff')
@allowed_users(allowed_roles='Staff')
def patient_detail(request, pk):
    context = { 'user': User.objects.get(id=pk), 'appointments': Appointment.objects.all().filter(patient = pk)}
    return render(request, 'staff/patient-detail.html', context)
