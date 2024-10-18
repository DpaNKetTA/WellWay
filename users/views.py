from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

# Create your views here.
from users.forms import UserRegistrationForm, UserLoginForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('MainPage'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/prost.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/prost0.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('MainPage'))