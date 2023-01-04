from django.urls import path

from . import views

urlpatterns = [
  path("supplier/departament/", views.DepartamentView.as_view()),
  path("supplier/departament/<int:pk>/", views.DepartamentDetailView.as_view()),
]