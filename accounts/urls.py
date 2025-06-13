from django.urls import path , include
from django.contrib.auth.views import LoginView
from . import forms , views


urlpatterns = [
    path('login/',LoginView.as_view(authentication_form =forms.UserLoginForm),name='login'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('profile/',views.edit_profile,name='profile'),
    path('', include('django.contrib.auth.urls')),
]
