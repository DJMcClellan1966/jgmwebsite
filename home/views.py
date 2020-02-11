from django.shortcuts import render

def home(request):
    return render(request, 'jobs/home.html')

def terms(request):
    return render(request, 'jobs/terms.html')

def privacy(request):
    return render(request, 'jobs/privacy.html')
