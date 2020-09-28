from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import Loginform
from django.contrib.auth.models import User


def SignUp(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password =raw_password)
            login(request,user)
            return redirect('trainer')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def LoginView(request):

    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.POST['username'])
            login(request,user)
            return redirect('trainer')
    else:
        form = Loginform()

    return render(request,'login.html',{'form':form})
