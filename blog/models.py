from django.db import models
from django.contrib.auth.models import User

# Crie seus models aqui

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

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True)
    endereco = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Cliente'

    def __str__(self):
        return self.nome
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    produtos = models.ManyToManyField(Produto, through='ItemPedido')
    criado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[

        ('aberto', 'Em aberto'), ('rascunho', "Rascunho"), ('confirmado', "Confirmado"), ('cancelado', "Cancelado"), ('pago', "Pago"), ('enviado', "Enviado")
    ])
    finalizado = models.BooleanField(default=False)

    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'Pedido'

    def __str__(self):
        return f'Pedido #{self.id} - {self.cliente.nome}'
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantidade}x {self.produto.nome}'
    
class Pagamento(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='pagamentos')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField(auto_now_add=True)
    metodo = models.CharField(max_length=50, choices=[
        ('credito', 'Cartão de Crédito'),
        ('boleto', 'Boleto Bancário'),
        ('pix', 'PIX'),
    ])
    status = models.CharField(max_length=20, choices=[
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('recusado', 'Recusado'),
    ])
    comprovante = models.ImageField(upload_to='comprovantes/', null=True, blank=True)

    class Meta:
        ordering = ['-data_pagamento']
        verbose_name = 'Pagamento'

    def __str__(self):
        return f'Pagamento #{self.id} - Pedido #{self.pedido.id}'

    @property
    def valor_formatado(self):
        return f'R$ {self.valor:.2f}'.replace('.', ',')

    @property
    def foi_pago(self):
        return self.status == 'aprovado'