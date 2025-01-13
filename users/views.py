from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        'title':'Home - Autorization'
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title':'Home - registration'
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        'title':'Home - Profile'
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    ...
