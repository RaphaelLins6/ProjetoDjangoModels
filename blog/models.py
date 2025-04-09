from django.db import models

# Create your models here.

from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ativa = models.BooleanField(default=True)
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Categoria'

    @property
    def nome_maiusculo(self):
        return self.nome.upper()

    @property
    def resumo_descricao(self):
        return self.descricao[:50] + '...'

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')  # Aqui está o related_name

    class Meta:
        ordering = ['nome']
        verbose_name = 'Produto'

    @property
    def preco_formatado(self):
        return f'R$ {self.preco:.2f}'.replace('.', ',')

    @property
    def tem_estoque(self):
        return self.estoque > 0

    def __str__(self):
        return self.nome
