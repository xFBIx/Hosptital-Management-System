from django.shortcuts import render

def about(request):
    return render(request, 'general_pages/about.html')