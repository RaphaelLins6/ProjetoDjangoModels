from django.shortcuts import render
from .models import Produto

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'blog/listar_produtos.html', {'produtos': produtos})

# Create your views here.
