from django.db import models

class OrdemServico(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_recebida = models.DateTimeField()
    status = models.CharField(
        max_length=50,
        choices=[
            ('pendente', 'Pendente'),
            ('em andamento', 'Em Andamento'),
            ('concluida', 'Concluída'),
        ],
        default='pendente'
    )

    def __str__(self):
        return f"{self.titulo} - {self.status}"