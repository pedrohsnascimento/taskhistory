from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('aberto', 'Em Aberto'),
    ('aguardando', 'Aguardando'),
    ('andamento', 'Em Andamento'),
    ('sem_resolucao', 'Sem Resolução'),
    ('resolvido', 'Resolvido'),
)

class Task(models.Model):
    data = models.DateField()
    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=2000)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberto')
    usuario_afetado = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas_afetadas')
    usuario_acao = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas_executadas')

    def __str__(self):
        return self.nome
