from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import *
from django.contrib.auth import login, authenticate, logout as dj_logout


class ProfileView(View):
    def get(self, request):
        return render(request, 'profile/user-profile.html')


class SeekerSignUpView(View):
    def get(self, request):
        form = SeekerSignUpForm
        return render(request, 'register/seeker_signup.html', {'form': form})

    def post(self, request):
        form = SeekerSignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login-user')
        return render(request, 'register/seeker_signup.html', {'form': form,
                                                      'status': "Password not match or Password must be consist of number and character and lenght greater than 8"})


class OwnerSignUpView(View):
    def get(self, request):
        form = OwnerSignUpForm
        return render(request, 'register/owner_signup.html', {'form': form})

    def post(self, request):
        form = OwnerSignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login-user')
        return render(request, 'register/owner_signup.html', {'form': form,
                                                      'status': "Password not match or Password must be consist of number and character and lenght greater than 8"})


class LoginView(View):
    def get(self, request):
        form = LoginForm
        return render(request, 'register/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username =None,email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
        return render(request, 'auth/login.html', {'form': form, 'status': "Your password or username is incorrect"})


def user_logout(request):
    dj_logout(request)
    return redirect('home')
