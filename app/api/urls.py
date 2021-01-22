from django.urls import path
from .views import *

urlpatterns = [
    path('home/',HomeView.as_view()),
    path('contact/',ContactView.as_view()),
    path('create-job/',CreateJobView.as_view()),
]
