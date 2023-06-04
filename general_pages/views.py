from django.shortcuts import render

def index(request):
    return render(request, 'general_pages/index.html')
