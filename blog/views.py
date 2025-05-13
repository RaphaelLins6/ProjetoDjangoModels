from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Produto, Categoria, ItemPedido, Pedido, Pagamento, Cliente
from django.contrib import messages
from .forms import PagamentoForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def listar_produtos(request):
    produtos = Produto.objects.all() 
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def produtos_por_categoria(request):
    categorias = Categoria.objects.prefetch_related('produtos').all()
    return render(request, 'produtos_por_categoria', {'categorias': categorias})
    
def categoria_listar(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria_listar.html', {'categorias': categorias})


def adicionar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    cliente = Cliente.objects.first()
    pedido, criado = Pedido.objects.get_or_create(cliente=cliente, status='aberto', finalizado=False)
    item_existente = ItemPedido.objects.filter(pedido=pedido, produto=produto).first()
    if item_existente:
        item_existente.quantidade += 1
        item_existente.save()
        messages.success(request, f'Quantidade atualizada para "{produto.nome}".')
    else:
        ItemPedido.objects.create(pedido=pedido, produto=produto, quantidade=1)
        messages.success(request, f'"{produto.nome}" foi adicionado ao carrinho.')

    return redirect('listar_produtos')

def carrinho_view(request):
    cliente = Cliente.objects.first()
    pedido = Pedido.objects.filter(cliente=cliente, status='aberto', finalizado=False).first()
    itens = pedido.itempedido_set.all() if pedido else []

    return render(request, 'carrinho.html', {'pedido': pedido, 'itens': itens})

def pagamento_view(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, status='aberto')
    total = sum(item.produto.preco * item.quantidade for item in pedido.itempedido_set.all())

    if request.method == 'POST':
        form = PagamentoForm(request.POST, request.FILES)
        if form.is_valid():
            pagamento = form.save(commit=False)
            pagamento.pedido = pedido
            pagamento.valor = total
            pagamento.status = 'aprovado'
            pedido.finalizado = True
            pedido.status = 'confirmado'
            pedido.save()
            pagamento.save()
            messages.success(request, 'Pagamento registrado!')
            return redirect('carrinho')
    else:
        form = PagamentoForm()

    return render(request, 'pagamento.html', {
        'pedido': pedido,
        'total': total,
        'form': form,
    })

def pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos.html', {'pedidos': pedidos})
