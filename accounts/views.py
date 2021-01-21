from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from .forms import *
from django.contrib.auth import login, authenticate, logout as dj_logout
from .models import *
from app.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse, Http404
import os
from django.conf import settings


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
        return render(request, 'register/user-login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
        return render(request, 'register/user-login.html',
                      {'form': form, 'status': "Your password or username is incorrect"})


def user_logout(request):
    dj_logout(request)
    return redirect('login-user')


class ProfileView(View):
    def get(self, request):
        user = request.user
        print(">>>>>>>>>>>>>>>>>>>>User", user)
        if user.is_authenticated:
            try:
                profile = Profile.objects.get(user=user)
            except Profile.DoesNotExist:
                # path = settings.MEDIA_ROOT+'/media/Capture.PNG'
                profile = Profile.objects.create(user=user, pro_photo='', resume='', first_name='', last_name='',
                                                 degree_name='',
                                                 graduate_year='', father_name='', mother_name='',
                                                 gender='', religion='', marital_status='', nationality='',
                                                 phone_number='', date_of_birth='', address='', job_name='',
                                                 keywords='', salary_range='', job_type='')
                profile.save()

            form = UserProfileForm(initial={
                'pro_photo': profile.pro_photo,
                'resume': profile.resume,
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'degree_name': profile.degree_name,
                'graduate_year': profile.graduate_year,
                'father_name': profile.father_name,
                'mother_name': profile.mother_name,
                'gender': profile.gender,
                'religion': profile.religion,
                'marital_status': profile.marital_status,
                'nationality': profile.nationality,
                'phone_number': profile.phone_number,
                'date_of_birth': profile.date_of_birth,
                'address': profile.address,
                'job_name': profile.job_name,
                'keywords': profile.keywords,
                'salary_range': profile.salary_range,
                'job_type': profile.job_type

            })
            return render(request, 'profile/user-profile.html', {'profile': profile, 'form': form})
        else:
            return redirect('login-user')

    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", form)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            profile.pro_photo = request.FILES['pro_photo']
            profile.resume = request.FILES['resume']
            profile.first_name = request.POST['first_name']
            profile.last_name = request.POST['last_name']
            profile.father_name = request.POST['father_name']
            profile.mother_name = request.POST['mother_name']
            profile.degree_name = request.POST['degree_name']
            profile.graduate_year = request.POST['graduate_year']
            profile.gender = request.POST['gender']
            profile.religion = request.POST['religion']
            profile.marital_status = request.POST['marital_status']
            profile.nationality = request.POST['nationality']
            profile.phone_number = request.POST['phone_number']
            profile.date_of_birth = request.POST['date_of_birth']
            profile.address = request.POST['address']
            profile.job_name = request.POST['job_name']
            profile.keywords = request.POST['keywords']
            profile.salary_range = request.POST['salary_range']
            profile.job_type = request.POST['job_type']
            profile.save()
            return redirect('profile')
        else:
            return HttpResponse("Error")


class AllUserProfile(View):

    def get(self, request):
        candidates = Profile.objects.filter(user__is_seeker=True)
        job_types = ['Part Time', 'Full Time', 'Other']
        categories = Category.objects.all()
        page = request.GET.get('page', 1)
        pagination = Paginator(candidates, per_page=10)
        try:
            candidates = pagination.page(page)
        except PageNotAnInteger:
            candidates = pagination.page(1)
        except EmptyPage:
            candidates = Paginator.page(pagination.num_pages)
        return render(request, 'profile/browse-candidates.html',
                      {'candidates': candidates, 'job_types': job_types, 'categories': categories})


def searchCandidate(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", keyword, "<<<<<<")
        search_items = Profile.objects.filter(job_name__icontains=keyword) | Profile.objects.filter(
            job_type__icontains=keyword) | Profile.objects.filter(keywords__icontains=keyword)
        return JsonResponse({'search_cand': list(search_items.values()), 'status': "OK"})


class UserProfileDetail(View):
    def get(self, request, id):
        candidate = Profile.objects.get(pk=id)
        return render(request, 'profile/userprofile-to-other.html', {'candidate': candidate})


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


class AllOwnerProfile(View):
    def get(self, request):
        companies = Profile.objects.filter(user__is_owner=True)
        job_types = ['Part Time', 'Full Time', 'Other']
        categories = Category.objects.all()
        page = request.GET.get('page', 1)
        pagination = Paginator(companies, per_page=10)
        try:
            companies = pagination.page(page)
        except PageNotAnInteger:
            companies = pagination.page(1)
        except EmptyPage:
            companies = Paginator.page(pagination.num_pages)
        return render(request, 'profile/browse-company.html',
                      {'companies': companies, 'job_types': job_types, 'categories': categories})


def searchCompany(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", keyword, "<<<<<<")
        search_items = Profile.objects.filter(job_name__icontains=keyword) | Profile.objects.filter(
            job_type__icontains=keyword) | Profile.objects.filter(keywords__icontains=keyword)
        return JsonResponse({'search_cand': list(search_items.values()), 'status': "OK"})


class CompanyDetail(View):
    def get(self, request, id):
        candidate = Profile.objects.get(pk=id)
        return render(request, 'profile/userprofile-to-other.html', {'candidate': candidate})
