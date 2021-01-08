from django.shortcuts import render
from django.views.generic import View


class ProfileView(View):
    def get(self,request):
        return render(request,'profile/user-profile.html')


class SignUpView(View):
    def get(self,request):
        return render(request,'register/signup.html')


class LoginView(View):
    def get(self,request):
        return render(request,'register/login.html')
