from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateStudentAPIView.as_view(), name='get_post_students'),
    path('<int:pk>/', views.RetrieveUpdateDestroyStudentAPIView.as_view(), name='get_delete_update_students'),
]