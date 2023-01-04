from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("categories/", views.EmployeeView.as_view()),
    path("categories/<int:pk>/", views.EmployeeDetailView.as_view()),
]
