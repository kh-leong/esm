from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.user_index, name='user_index'),
    path('users/', views.get_user, name='user_index'),   
    path('users/upload', views.upload_csv, name='user_index'),
]
