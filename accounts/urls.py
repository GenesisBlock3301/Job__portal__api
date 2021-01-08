from django.urls import path,include
from . import views


urlpatterns = [
    path('profile/',views.ProfileView.as_view(),name="profile"),
]+[
    path('login/',views.LoginView.as_view(),name='login'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
]
