from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class HomeView(View):
    def get(self,request):
        return render(request,'app/index-3.html')


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



