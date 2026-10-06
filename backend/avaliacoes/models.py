from django.db import models
from alunos.models import Aluno
from disciplinas.models import Disciplina

# Create your models here.
class Avaliacao(models.Model):

    STATUS_CHOICES = [
        ('PENDENTE', 'PENDENTE'),
        ('RESPONDIDA', 'RESPONDIDA'),
    ]

    nota = models.IntegerField(null=True, blank=True)
    comentario = models.TextField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDENTE'
    )

    data_criacao = models.DateTimeField(auto_now_add=True)

    # Um aluno pode fazer várias avaliacoes
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE
    )

    # Uma disciplina pode ter várias avaliacoes, mas uma avaliacao pertence a uma disciplina.
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.aluno} - {self.disciplina}'
    
    