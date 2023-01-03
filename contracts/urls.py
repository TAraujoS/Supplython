from django.urls import path
from .views import ContractView, ContractDetailView

urlpatterns = [
    path("contract/", ContractView.as_view()),
    path("contract/<contract_id>/", ContractDetailView.as_view()),
]
