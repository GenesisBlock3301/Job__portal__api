from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


class HomeView(View):
    def get(self,request):
        recentJob = JobPost.objects.all().order_by('created_at')
        categories = Category.objects.all()
        page = request.GET.get('page', 1)
        pagination = Paginator(recentJob, per_page=10)
        try:
            all_jobs = pagination.page(page)
        except PageNotAnInteger:
            all_jobs = pagination.page(1)
        except EmptyPage:
            all_jobs = Paginator.page(pagination.num_pages)
        return render(request,'app/index-3.html',{'recentJob':all_jobs,'categories':categories})


class ResumeView(View):
    def get(self,request):
        return render(request,'app/resume/submit-resume.html')


class AddSkillView(View):
    def get(self,request):
        return render(request,'app/resume/add-skill.html')


class AddExperinceView(View):
    def get(self,request):
        return render(request,'app/resume/add-experience.html')


class AddProjectView(View):
    def get(self,request):
        return render(request,'app/resume/add-project.html')


class AddEducationView(View):
    def get(self,request):
        return render(request,'app/resume/add-education.html')


class AddCertificateView(View):
    def get(self,request):
        return render(request,'app/resume/add-certificates.html')



