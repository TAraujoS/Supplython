from django.urls import path

from . import views

urlpatterns = [
    path("departments/", views.DepartmentView.as_view()),
    path("departments/<int:pk>/", views.DepartmentDetailView.as_view()),
]
