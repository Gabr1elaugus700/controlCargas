from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import OrdemServico
from .serializers import OrdemServicoSerializer

# View para criar uma nova ordem de serviço
class OrdemServicoView(APIView):
    def post(self, request):
        serializer = OrdemServicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View para listar todas as ordens de serviço
class OrdemServicoListView(generics.ListAPIView):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer

# View para detalhes de uma ordem de serviço específica
class OrdemServicoDetailView(generics.RetrieveAPIView):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer