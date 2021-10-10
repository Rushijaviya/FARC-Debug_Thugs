from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('credit', views.frauddetection, name='frauddetection'),
    path('companies', views.companies, name='companies'),
    path('blogg', views.blogg, name='blogg'),
    path('post', views.post, name='post'),
    path('post2', views.post2, name='post2'),
    path('post3', views.post3, name='post3'),
    path('post4', views.post4, name='post4'),
]
