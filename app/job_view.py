from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .job_form import *
from .models import *


class CreateJob(View):
    form_class = JobCreationForm

    def get(self, request):
        category = Category.objects.all()
        job_type = ['Part Time', 'Full Time', 'Other']
        return render(request, 'app/job/create-job.html',
                      {'form': self.form_class, 'categories': category, 'job_type': job_type})

    def post(self, request):
        user = request.user
        if user.is_authenticated and user.is_owner:
            title = request.POST.get('title', '')
            job_category = request.POST.get('job_cat', '')
            job_type = request.POST.get('job_type', '')
            location = request.POST.get('location', '')
            requirements = request.POST.get('requirements', '')
            description = request.POST.get('description', '')
            salary = request.POST.get('salary', '')
            experience = request.POST.get('experience', '')
            created_at = datetime.datetime.now()
            expire_date = request.POST.get('expire_date', '')
            categoryInstance = Category.objects.get(name=job_category)
            companyOwner = CompanyOwner.objects.get(user=user)
            # print(">>>>>>>>>>>>>>>>>>>>>>>>", categoryInstance, ">>>>>>>>>>>>>>>>>>>", companyOwner)
            job = JobPost.objects.create(posted_by=companyOwner, job_category=categoryInstance, title=title,
                                         job_type=job_type,
                                         locations=location, requirements=requirements, description=description,
                                         salary=salary,
                                         experience=experience, created_at=created_at, expire_date=expire_date)
            job.save()
        category = Category.objects.all()
        job_type = ['Part Time', 'Full Time', 'Other']
        return render(request, 'app/job/create-job.html',
                      {'form': self.form_class, 'categories': category, 'job_type': job_type})


class BrowseJob(View):

    def get(self, request):
        all_jobs = JobPost.objects.all()
        return render(request, 'app/job/browse-job.html', {'job_posts': all_jobs})


class JobDetailView(View):
    def get(self, request, pk):
        job = get_object_or_404(JobPost, pk=pk)
        return render(request, 'app/job/job-detail.html', {"job": job})
