from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import re


class SeekerSignUpForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email ID'}),
                            required=True, max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                                required=True, max_length=30)
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}), required=True,
        max_length=30)
    is_seeker = forms.CharField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2','is_seeker']

    def clean_email(self):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        email = self.cleaned_data['email']
        r = User.objects.filter(email=email)
        if r.count() or (email and not re.search(regex, email)):
            raise ValidationError("Your email used or incorrect.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password2 and password1 and password2 != password1:
            raise ValidationError("Password doesn't match.")
        return password2


class OwnerSignUpForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email ID'}),
                            required=True, max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                                required=True, max_length=30)
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}), required=True,
        max_length=30)
    is_owner = forms.CharField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2','is_owner']

    def clean_email(self):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        email = self.cleaned_data['email']
        r = User.objects.filter(email=email)
        if r.count() or (email and not re.search(regex, email)):
            raise ValidationError("Your email used or incorrect.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password2 and password1 and password2 != password1:
            raise ValidationError("Password doesn't match.")
        return password2


class LoginForm(forms.Form):
    email = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                               required=True, max_length=30)
    password = forms.CharField(label="",
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               required=True, max_length=30)
