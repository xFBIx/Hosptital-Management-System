from django.shortcuts import render, redirect
from general_pages.decorators import is_profile, chat_access
from django.contrib.auth.models import User

@is_profile
def index(request):
    return render(request, 'general_pages/index.html')

@is_profile
def contact(request):
    return render(request, 'general_pages/contact.html')

@is_profile
def about(request):
    return render(request, 'general_pages/about.html')

@is_profile
@chat_access
def chat_box(request, chat_box_name):
    user = User.objects.filter(username = chat_box_name).first()
    if request.user.groups.all()[0].name == 'Patient' and chat_box_name == request.user.username:
        return render(request, 'general_pages/chat.html', {
            'chat_box_name': request.user.username,
        })
    elif request.user.groups.all()[0].name == 'Staff' and user in User.objects.all():  
        return render(request, 'general_pages/chat.html', {
            'chat_box_name': chat_box_name
        })
    else:
        return redirect('homepage')