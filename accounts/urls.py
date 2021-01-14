from django.urls import path,include
from . import views


urlpatterns = [
    path('profile/',views.ProfileView.as_view(),name="profile"),
]+[
    path('login/',views.LoginView.as_view(),name='login-user'),
    path('seeker-signup/',views.SeekerSignUpView.as_view(),name='seeker-user'),
    path('owner-signup/',views.OwnerSignUpView.as_view(),name='owner-user'),
    path('user-logout/',views.dj_logout,name='user-logout'),
]
