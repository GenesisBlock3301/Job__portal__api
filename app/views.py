from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from portal.settings import EMAIL_HOST_USER


class HomeView(View):
    def get(self, request):
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
        return render(request, 'app/index-3.html', {'recentJob': all_jobs, 'categories': categories})


class ResumeView(View):
    def get(self, request):
        return render(request, 'app/resume/add-basic-info.html')


class AddSkillView(View):
    def get(self, request):
        return render(request, 'app/resume/add-skill.html')


class AddExperinceView(View):
    def get(self, request):
        return render(request, 'app/resume/add-experience.html')


class AddProjectView(View):
    def get(self, request):
        return render(request, 'app/resume/add-project.html')


class AddEducationView(View):
    def get(self, request):
        return render(request, 'app/resume/add-education.html')


class AddCertificateView(View):
    def get(self, request):
        return render(request, 'app/resume/add-certificates.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'app/site/contact.html')

    def post(self, request):
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        subject = "Have some query"
        message = name + "\n" + message+"\n"+email

        # print('>>>>>>>>>>>>>>>>',name,">>>>>>>>>>>>",message,'>>>>>>>>>>>',email)
        send_mail(subject=subject, message=message, from_email=email,recipient_list=[EMAIL_HOST_USER], fail_silently=False)

        return redirect('contact')


class AboutView(View):
    def get(self, request):
        return render(request, 'app/site/about-us.html')
