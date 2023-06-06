from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from general_pages.decorators import is_profile

@is_profile
def index(request):
    return render(request, 'general_pages/index.html')

@is_profile
def contact(request):
    return render(request, 'general_pages/contact.html')

@is_profile
def about(request):
    return render(request, 'general_pages/about.html')
