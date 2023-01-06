from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

urlpatterns = [
    path("employees/", views.EmployeeView.as_view()),
    path("employees/<int:pk>/", views.EmployeeDetailView.as_view()),
    path("employees/login/", jwt_views.TokenObtainPairView.as_view()),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
]
