from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome
