from django.shortcuts import render, redirect
from allauth.account.views import LoginView
from django.contrib.auth.models import Group, User
from django.contrib import messages
from .forms import profileform
from .models import Profile, Appointment
from django.contrib.auth.decorators import login_required
from general_pages.decorators import is_profile, profile, allowed_users

class loginview(LoginView):
    def form_valid(self, form):
        username = form.cleaned_data.get('login')
        user = User.objects.filter(username = username).first()
        group = str(Group.objects.filter(user = user).first())
        if (group == 'Staff'):
            messages.warning(self.request, f'If you are a staff member, please log in at the staff login page.')
            return redirect('account_login')
        return super().form_valid(form)

@login_required(login_url='account_login')
@profile    
def make_profile(request):
    if request.method == 'POST':
        form = profileform(request.POST)
        if form.is_valid():
            gender = form.cleaned_data.get('gender')
            history_of_illness = form.cleaned_data.get('history_of_illness')
            record_of_prescriptions = form.cleaned_data.get('record_of_prescriptions')
            request.user.groups.add(Group.objects.get(name='Patient'))
            Profile.objects.create(user = request.user, gender = gender, history_of_illness = history_of_illness, record_of_prescriptions = record_of_prescriptions)
            return redirect('homepage')
    context ={}
    context['form']= profileform()
    return render(request, 'patients/make-profile.html', context)

@login_required(login_url='account_login')
@is_profile
@allowed_users(allowed_roles='Patient')
def appointment(request):
    if request.method == 'POST':
        appointment = request.POST.get('appointment')
        doctor = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        health_issue = request.POST.get('health_issue')
        if (appointment == 'Regular'):
            bill = 1500
        elif (appointment == 'Nurse'):
            bill = 500
        elif (appointment == 'Emergency'):
            bill = 2000
        Appointment.objects.create(patient = request.user, doctor = doctor, service = appointment, health_issue = health_issue, date = date, time = time, bill = bill)
        messages.success(request, f'Appointment made successfully!')
        return redirect('homepage')
    else:
        return render(request, 'patients/appointment.html')

@login_required(login_url='account_login')
@is_profile
@allowed_users(allowed_roles='Patient')    
def profile(request):
    return render(request, 'patients/profile.html')

@login_required(login_url='account_login')
@is_profile
@allowed_users(allowed_roles='Patient')
def account(request):
    context = {'appointments': Appointment.objects.all().filter(patient = request.user)}
    return render(request, 'patients/account.html', context)

@login_required(login_url='account_login')
@is_profile
@allowed_users(allowed_roles='Patient')
def paybill(request, pk):
    appointment = Appointment.objects.get(id = pk)
    appointment.bill_paid = True
    appointment.save()
    return redirect('account')