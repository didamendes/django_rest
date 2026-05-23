from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from api.models import Empresa
from rest_framework import viewsets, status
from api.serializers import EmpresaSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['nome', 'telefone']
    search_fields = ['nome', 'telefone']
    ordering_fields = ['id', 'nome', 'telefone']
    ordering = ['id']

@api_view(['POST'])
def soma_view(request, numero1, numero2):
    total = numero1 + numero2
    return Response({"resultado": total}, status=status.HTTP_200_OK)


@api_view(['POST'])
def soma_formato2(request):
    numero1 = request.data.get('numero1')
    numero2 = request.data.get('numero2')

    if numero1 is None or numero2 is None:
        return Response(
            {"erro": "Os campos 'numero1' e 'numero2' são obrigatórios."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        total = int(numero1) + int(numero2)
    except (TypeError, ValueError):
        return Response(
            {"erro": "Os campos 'numero1' e 'numero2' devem ser números inteiros."},
            status=status.HTTP_400_BAD_REQUEST
        )

    return Response({"resultado": total}, status=status.HTTP_200_OK)


class SomaFormato2View(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["numero1", "numero2"],
            properties={
                "numero1": openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="Primeiro número inteiro"
                ),
                "numero2": openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="Segundo número inteiro"
                ),
            },
        ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "resultado": openapi.Schema(type=openapi.TYPE_INTEGER)
                }
            ),
            400: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "erro": openapi.Schema(type=openapi.TYPE_STRING)
                }
            ),
        },
    )
    def post(self, request):
        numero1 = request.data.get('numero1')
        numero2 = request.data.get('numero2')

        if numero1 is None or numero2 is None:
            return Response(
                {"erro": "Os campos 'numero1' e 'numero2' são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            total = int(numero1) + int(numero2)
        except (TypeError, ValueError):
            return Response(
                {"erro": "Os campos 'numero1' e 'numero2' devem ser números inteiros."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response({"resultado": total}, status=status.HTTP_200_OK)