from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path("", views.home, name="home"),
    path('contas/', include('contas.urls')),  
    path('register/', include('django.contrib.auth.urls')),
    path('produtos/criar/', views.criar_produto, name='criar_produto'),
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('produtos/editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('produtos/deletar/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),
    path('categorias/', views.produtos_por_categoria, name='produtos_por_categoria'),
    path('categorias/criar/', views.criar_categoria, name='criar_categoria'),
    path('categorias/editar/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/deletar/<int:categoria_id>/', views.deletar_categoria, name='deletar_categoria'),
    path('carrinho/adicionar/<int:produto_id>/', views.adicionar_produto, name='adicionar_produto'),
    path('carrinho/', views.carrinho_view, name='carrinho'),
    path('pagamento/<int:pedido_id>/', views.pagamento_view, name='pagamento_view'),
    path("pedidos/", views.pedidos, name="pedidos"),
    path('clientes/criar/', views.criar_cliente, name='criar_cliente'),
]
