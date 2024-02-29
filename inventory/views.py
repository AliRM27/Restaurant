from django.shortcuts import render

def index(request):
    return render(request, 'inventory/base.html')

def next(request):
    return render(request, 'inventory/next.html')

def login(request):
    return render(request, 'inventory/login_page.html')

def sign_up(request):
    return render(request, 'inventory/sign_up_page.html')