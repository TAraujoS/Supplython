from django.urls import path
from . import views

urlpatterns = [
    path("invoices/", views.InvoiceView.as_view()),
    path("invoices/<int:pk>/", views.InvoiceDetailView.as_view()),
]
