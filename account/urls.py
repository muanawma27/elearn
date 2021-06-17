from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',loggingout,name='logout'),
    path('dashboard/',dashboard,name='dashboard'),
    path('profile/',profile,name='profile'),


    path('updateprofessions/',updateprofessions,name="update_professions"),
    path('updatehobbies/',updatehobbies,name="updatehobbies"),
    path('updateinterests/',updateinterests,name="updateinterests"),




]