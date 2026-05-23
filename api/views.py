from django.shortcuts import render

# Create your views here.
from api.models import Empresa
from rest_framework import viewsets
from api.serializers import EmpresaSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer