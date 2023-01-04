from django.urls import path
from .views import ContractView, ContractDetailView

urlpatterns = [
    path("contract/", ContractView.as_view()),
    path("contract/<int:pk>/", ContractDetailView.as_view()),
]
