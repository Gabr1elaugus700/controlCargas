from django.urls import path
from .views import OrdemServicoView, OrdemServicoListView, OrdemServicoDetailView

app_name = 'controle'


urlpatterns = [
    
    path('ordem-servico/', OrdemServicoView.as_view(), name='ordem_servico_create'),

    # Endpoint para listar todas as ordens de serviço
    path('ordem-servico/lista/', OrdemServicoListView.as_view(), name='ordem_servico_list'),

    # Endpoint para visualizar os detalhes de uma ordem de serviço específica
    path('ordem-servico/<int:pk>/', OrdemServicoDetailView.as_view(), name='ordem_servico_detail'),
]