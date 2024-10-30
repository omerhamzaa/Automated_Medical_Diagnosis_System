from django.shortcuts import render
from rest_framework.views import APIView

from src.diagnosis_view import get_diagnoses, create_diagnosis, update_diagnosis, delete_diagnosis


class DiagnosisView(APIView):
    def get(self, request):
        return get_diagnoses(request)

    def post(self, request):
        return create_diagnosis(request)

    def put(self, request, pk):
        return update_diagnosis(request, pk)

    def delete(self, request, pk):
        return delete_diagnosis(request, pk)
