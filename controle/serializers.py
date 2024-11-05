# serializers.py
from rest_framework import serializers
from .models import OrdemServico

class OrdemServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdemServico
        fields = ['id', 'titulo', 'descricao', 'data_recebida', 'status']
