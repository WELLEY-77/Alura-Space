from django.db import models

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
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'Fotografia [{self.nome}]'