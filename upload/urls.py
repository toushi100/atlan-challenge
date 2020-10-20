from django.urls import path
from . import views


urlpatterns =[
    path('', views.show),
    path('pause/', views.pause_upload, name='pause_upload'),
    path('stop/', views.stop, name='stop'),
    path('resume/', views.resume, name='resume')


]

