from django.shortcuts import render, redirect
from .models import Produto, Categoria


# Create your views here.

def listar_produtos(request):
    categorias = Categoria.objects.prefetch_related('produtos').all()  # Certifique-se de usar o related_name correto
    return render(request, 'blog/listar_produtos.html', {'categorias': categorias})

def produtos_por_categoria(request):
    categorias = Categoria.objects.prefetch_related('produtos').all()
    return render(request, 'catalogo/lista_por_categoria.html', {'categorias': categorias})

