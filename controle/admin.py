from django.contrib import admin
from .models import OrdemServico

class OrdemServicoAdmin(admin.ModelAdmin):
    # Campos exibidos na listagem
    list_display = ('titulo', 'data_recebida', 'status')
    
    # Campos que podem ser clicados para acessar o detalhe
    list_display_links = ('titulo',)
    
    # Filtros laterais
    list_filter = ('status', 'data_recebida')
    
    # Campos de busca
    search_fields = ('titulo', 'descricao')
    
    # Ordenação padrão (da mais recente para a mais antiga)
    ordering = ('-data_recebida',)

admin.site.register(OrdemServico, OrdemServicoAdmin)
# Register your models here.
