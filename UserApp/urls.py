from django.urls import path

from .views import *


urlpatterns = [
    path('', loginUser, name='LOGIN'),
    path('logout/', logoutUser, name='LOGOUT'),
    path('register/', registerUser, name='REGISTER'),
    path('profile/', userProfile, name='PROFILE'),
    path('forgetpassword/', forgetPassword, name='FORGET'),
    path('reset/<uidb64>/<token>/', resetLink, name='RESET'),
    path('confirm/', confirmResetting, name='CONFIRM'),
]
