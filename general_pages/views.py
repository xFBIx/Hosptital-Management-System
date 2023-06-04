from django.shortcuts import render

def index(request):
    return render(request, 'general_pages/index.html')

def contact(request):
    return render(request, 'general_pages/contact.html')

def about(request):
    return render(request, 'general_pages/about.html')
