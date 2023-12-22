from django.shortcuts import render

# Create your views here.

def app(request):
    return render(request,'user/app.html',)

def dashboard(request):
    return render(request,'user/dashboard.html',)

def profile(request):
    return render(request,'user/profile.html',)

def login(request):
    return render(request,'user/login.html',)

def sign_up(request):
    return render(request,'user/sign_up.html',)

def about(request):
    return render(request,'user/about.html',)

def contact(request):
    return render(request,'user/contact.html',)

def chatbot(request):
    return render(request,'user/chatbot.html',)

def track(request):
    return render(request,'user/track.html',)