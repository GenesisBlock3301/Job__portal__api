from django.urls import path,include
from . import views


urlpatterns = [
    path('profile/',views.ProfileView.as_view(),name="profile"),
    path('candidates/',views.AllUserProfile.as_view(),name='candidates'),
    path('candidate-detail/<int:id>/',views.UserProfileDetail.as_view(),name='candidate-detail')
]+[
    path('user-login/',views.LoginView.as_view(),name='login-user'),
    path('seeker-signup/',views.SeekerSignUpView.as_view(),name='seeker-user'),
    path('owner-signup/',views.OwnerSignUpView.as_view(),name='owner-user'),
    path('user-logout/',views.user_logout,name='user-logout'),
    path('search-candidate/',views.searchCandidate,name='search-candidate'),
]+[
    path('<path>/',views.download,name='file')
]
