from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .job_form import *
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
import datetime


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
            # print(">>>>>>>>>>>>>>>>>>>>>>>>", categoryInstance, ">>>>>>>>>>>>>>>>>>>", companyOwner)
            if request.user.is_owner or request.user.is_superuser:
                job = JobPost.objects.create(posted_by=request.user, job_category=categoryInstance, title=title,
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
        jobs = JobPost.objects.all()
        page = request.GET.get('page', 1)
        pagination = Paginator(jobs, per_page=10)
        try:
            all_jobs = pagination.page(page)
        except PageNotAnInteger:
            all_jobs = pagination.page(1)
        except EmptyPage:
            all_jobs = Paginator.page(pagination.num_pages)
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>",pagination.num_pages,">>>>>>>>>>>>",jobs_pag.paginator.page_range)
        job_types = ['Part Time', 'Full Time', 'Other']
        categories = Category.objects.all()
        return render(request, 'app/job/browse-job.html',
                      {'job_posts': all_jobs, 'job_types': job_types, 'categories': categories})


class JobDetailView(View):
    def get(self, request, pk):
        job = get_object_or_404(JobPost, pk=pk)
        return render(request, 'app/job/job-detail.html', {"job": job})


class SearchJobView(View):
    def post(self, request):
        keyword = request.POST.get('keyword', '')
        location = request.POST.get('location', '')
        # print('>>>>>>>>>>>>>>>>>>',location,keyword)
        qs = JobPost.objects.filter(title__icontains=keyword, locations__icontains=location) | JobPost.objects.filter(
            posted_by__name__icontains=keyword, locations__icontains=location)
        return JsonResponse({'search_items': list(qs.values()), 'status': 'ok'})


class CategoryDetailsView(View):
    def get(self, request, id):
        cat = Category.objects.get(id=id)
        categories_item = cat.job_cats.all()
        page = request.GET.get('page', 1)
        pagination = Paginator(categories_item, per_page=10)
        try:
            # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>catagory>>>>>>>>>>>>>>>>>>>>>>", page, pagination.num_pages)
            all_jobs = pagination.page(page)
        except PageNotAnInteger:
            all_jobs = pagination.page(1)
        except EmptyPage:
            all_jobs = Paginator.page(pagination.num_pages)
        return render(request, 'app/job/category-detail.html', {'all_jobs': all_jobs, "cat_name": cat.name})
