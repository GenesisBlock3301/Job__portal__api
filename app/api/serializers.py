from rest_framework import serializers
from app.models import *
from django.core.mail import send_mail
from portal.settings import EMAIL_HOST_USER


class JobPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = "__all__"

    # def create(self, validated_data):
    #     photo = validated_data['photo']
    #     posted_by = validated_data['posted_by']
    #     job_category = validated_data['job_category']
    #     job_type = validated_data['job_type']
    #     title = validated_data['title']
    #     locations = validated_data['locations']
    #     requirements = validated_data['requirements']
    #     description = validated_data['description']
    #     salary = validated_data['salary']
    #     experience = validated_data['experience']
    #     created_at = validated_data['created_at']
    #     expire_date = validated_data['expire_date']
    #     categoryIntance =
    #     return JobPost.objects.create()


class ContactSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField(max_length=3000)

    def save(self):
        name = self.validated_data['name']
        email = self.validated_data['email']
        message = self.validated_data['message']
        subject = "Have some query"
        message = name + "\n" + message + "\n" + email
        send_mail(subject=subject, message=message, from_email=email,recipient_list=[EMAIL_HOST_USER],fail_silently=False)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

