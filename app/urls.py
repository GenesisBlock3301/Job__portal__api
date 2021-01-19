from django.urls import path,include
from . import views
from . import job_view

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('basic-info/',views.ResumeView.as_view(),name='resume'),
    path('add-skill/',views.AddSkillView.as_view(),name='add-skill'),
    path('add-experience/',views.AddExperinceView.as_view(),name='add-experience'),
    path('add-project/',views.AddProjectView.as_view(),name='add-project'),
    path('add-education/',views.AddEducationView.as_view(),name='add-education'),
    path('add-certificate/',views.AddCertificateView.as_view(),name='add-certificate'),
]+[
    path('browse-job/<int:pk>/',job_view.JobDetailView.as_view(),name='job-detail'),
    path('browse-job/',job_view.BrowseJob.as_view(),name='browse-job'),
    path('create-job/',job_view.CreateJob.as_view(),name='create-job'),
    path('search-job/',job_view.SearchJobView.as_view(),name='search-job'),
]+[
    path('category-detail/<int:id>/',job_view.CategoryDetailsView.as_view(),name='category-details')
]
