from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("employees/", views.EmployeeView.as_view()),
    path("employees/<int:pk>/", views.EmployeeDetailView.as_view()),
    path("employees/login/", jwt_views.TokenObtainPairView.as_view()),
]
