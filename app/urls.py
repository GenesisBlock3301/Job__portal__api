from django.urls import path,include
from . import views
from . import job_view

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('resume/',views.ResumeView.as_view(),name='resume'),
    path('add-skill/',views.AddSkillView.as_view(),name='add-skill'),
    path('add-experience/',views.AddExperinceView.as_view(),name='add-experience'),
    path('add-project/',views.AddProjectView.as_view(),name='add-project'),
    path('add-education/',views.AddEducationView.as_view(),name='add-education'),
    path('add-certificate/',views.AddCertificateView.as_view(),name='add-certificate'),
]+[
    path('job-detail/',job_view.JobDetailView.as_view(),name='job-view'),
]
