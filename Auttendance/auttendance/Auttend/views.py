from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Auttend/index.html')

def records(request):
    return render(request, 'Auttend/records.html')

def about(request):
    return render(request, 'Auttend/about.html')