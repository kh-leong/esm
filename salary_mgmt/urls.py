from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.user_index, name='user_index'),
    path('users/', views.get_user, name='user_index'),   
    path('<int:pk>/', views.user_detail, name='user_detail'),
]