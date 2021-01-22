from rest_framework.views import APIView
from rest_framework import status
from app.models import *
from .serializers import *
from rest_framework.response import Response
from django.core.mail import send_mail


class HomeView(APIView):
    def get(self, request):
        job_posts = JobPost.objects.all()
        serializer = JobPostSerializers(job_posts, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ContactView(APIView):
    def post(self, request):
        serializer = ContactSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # print(">>>>>>>>>>>>>>>data", serializer.data.get('address'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_501_NOT_IMPLEMENTED)


class CreateJobView(APIView):
    def get(self, request):
        # categories = Category.objects.all()
        jobs = JobPost.objects.all()
        serializer = JobPostSerializers(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer = JobPostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            photo = serializer.data['photo']
            title = serializer.data['title']
            job_category = serializer.data['job_category']
            job_type = serializer.data['job_type']
            locations = serializer.data['locations']
            requirements = serializer.data['requirements']
            description = serializer.data['description']
            salary = serializer.data['salary']
            experience = serializer.data['experience']
            expire_date = serializer.data['expire_date']
            category = Category.objects.get(id=job_category)
            if request.user.is_owner or request.user.is_superuser:
                job = JobPost.objects.create(posted_by=request.user, photo=photo, job_category=category, title=title,
                                             job_type=job_type, locations=locations, requirements=requirements,
                                             description=description, salary=salary, experience=experience,
                                             expire_date=expire_date)
                job.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
