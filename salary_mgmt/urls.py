from django.urls import path, include
from . import views
from rest_framework import routers

# router = routers.DefaultRouter
# router.register(r'users/', EmployeeSalaryViewSet)

# urlpatterns = router.urls
urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('', views.user_index, name='user_index'),
    path('users/', views.get_user, name='user_index'),   
    path('<int:pk>/', views.user_detail, name='user_detail'),
    path('users/upload', views.upload_csv, name='user_index'),
]
