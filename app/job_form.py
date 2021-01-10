from django import forms
from .models import *


class JobCreationForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'name': 'title'}),
        required=True, max_length=100)
    locations = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location', 'name': 'location'}),
        required=True, max_length=100)
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'name': 'description'}),
        required=True, max_length=100)
    requirements = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Requirements', 'name': 'requirements'}),
        required=True, max_length=100)
    salary = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Salary', 'name': 'salary'}),
        required=True, max_length=100)
    experience = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Experience', 'name': 'experience'}),
        required=True, max_length=100)
    expire_date = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Expire Date', 'name': 'expire_date'}),
        required=True, max_length=100)

    class Meta:
        model = JobPost
        fields = "__all__"
