from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class JobDetailView(View):
    def get(self,request):
        return render(request,'app/job/user-profile.html')


class BrowseJob(View):
    def get(self,request):
        return render(request,'app/job/browse-job.html')
