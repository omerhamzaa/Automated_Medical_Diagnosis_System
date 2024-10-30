from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from diagnosis_app.models import Diagnosis


def get_diagnoses(request):
    diagnoses = Diagnosis.objects.all()
    data = [{
        "id": diagnosis.id,
        "diagnosis_name": diagnosis.diagnosis_name,
        "description": diagnosis.description,
        "diagnosis_at": diagnosis.diagnosis_at,
        "patients_id": diagnosis.Patients_id.id,
    } for diagnosis in diagnoses]
    return Response(data)


def create_diagnosis(request):
    diagnosis = Diagnosis.objects.create(**request.data)
    return Response({
        "id": diagnosis.id,
        "diagnosis_name": diagnosis.diagnosis_name,
        "description": diagnosis.description,
        "diagnosis_at": diagnosis.diagnosis_at,
        "patients_id": diagnosis.Patients_id.id,
    }, status=status.HTTP_201_CREATED)


def update_diagnosis(request, pk):
    diagnosis = get_object_or_404(Diagnosis, pk=pk)
    for attr, value in request.data.items():
        setattr(diagnosis, attr, value)
    diagnosis.save()
    return Response({
        "id": diagnosis.id,
        "diagnosis_name": diagnosis.diagnosis_name,
        "description": diagnosis.description,
        "diagnosis_at": diagnosis.diagnosis_at,
        "patients_id": diagnosis.Patients_id.id,
    })


def delete_diagnosis(request, pk):
    diagnosis = get_object_or_404(Diagnosis, pk=pk)
    diagnosis.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)