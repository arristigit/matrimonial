from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('register', register_user, name='register'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('inputdetails', inputdetails, name='inputdetails'),
    # path('image', image, name='image'),
    path('editProfile/<int:id>', editProfile, name='editProfile'),
    path('profile/<int:id>', profile, name='profile'),
]