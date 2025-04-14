from django.contrib import admin
from .models import Categoria, Produto, Cliente, Pedido, ItemPedido

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(ItemPedido)