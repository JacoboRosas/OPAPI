from django.urls import path #We import the path function
from . import views # We also import the views module for the app

#Here we will have the different paths for our webpage
urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('test/', views.test, name='test'),  # About page
]

