from django.urls import path
from .views import DiagnosisView

urlpatterns = [
    path('diagnoses/', DiagnosisView.as_view(), name='diagnosis-list'),
    path('diagnoses/<int:pk>/', DiagnosisView.as_view(), name='diagnosis-detail'),
]