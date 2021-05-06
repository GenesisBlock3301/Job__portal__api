from django.urls import path, include
from . import views

urlpatterns = [
    path('users/',views.UsersView.as_view()),
    path('seeker-register/',views.SeekerSignupView.as_view()),
    path('owner-register/',views.OwnerSignupView.as_view()),
    path('login/',views.LoginView.as_view()),
]
