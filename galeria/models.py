from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Fotografia(models.Model):

    OPCOES_CATEGORIAS = [
        ('ESTRELA', 'Estrela'),
        ('PLANETA', 'Planeta'),
        ('GALÁXIA', 'Galáxia'),
        ('NEBULOSA', 'Nebulosa'),
    ]

    nome = models.CharField(max_length=50, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, default='',choices=OPCOES_CATEGORIAS )
    descricao = models.TextField(null=False, blank=False)
    publicada = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/',blank=True)
    data_fotografia = models.DateTimeField(blank=False, default=datetime.now)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )


    def __str__(self):
        return self.nome