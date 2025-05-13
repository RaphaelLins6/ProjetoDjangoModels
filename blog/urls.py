from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path("", views.home, name="home"),
    path('produtos/categorias/', views.produtos_por_categoria, name='produtos_por_categoria'),
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('produtos/categorias/', views.produtos_por_categoria, name='produtos_por_categoria'),
    path('carrinho/adicionar/<int:produto_id>/', views.adicionar_produto, name='adicionar_produto'),
    path('carrinho/', views.carrinho_view, name='carrinho'),
    path('pagamento/<int:pedido_id>/', views.pagamento_view, name='pagamento_view'),
    path("pedidos/", views.pedidos, name="pedidos"),
    path('produtos/criar/', views.criar_produto, name='criar_produto'),
    path('clientes/criar/', views.criar_cliente, name='criar_cliente'),
]
