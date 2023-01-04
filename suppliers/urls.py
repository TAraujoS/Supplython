from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("suppliers/", views.SupplierView.as_view()),
    path("suppliers/<int:pk>/", views.SupplierDetailView.as_view())
]