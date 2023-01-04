from django.urls import path

from . import views

urlpatterns = [
  path("departament/", views.DepartamentView.as_view()),
  path("departament/<int:pk>/", views.DepartamentDetailView.as_view()),
]