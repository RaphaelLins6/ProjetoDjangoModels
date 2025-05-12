from django.shortcuts import render, redirect
from .models import Produto, Categoria


# Create your views here.

def listar_produtos(request):
    produtos = Produto.objects.all()  # Busca todos os produtos no banco de dados
    return render(request, 'blog/listar_produtos.html', {'produtos': produtos})

def produtos_por_categoria(request):
    categorias = Categoria.objects.prefetch_related('produtos').all()
    return render(request, 'blog/produtos_por_categoria', {'categorias': categorias})

