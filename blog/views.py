from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Produto, Categoria, ItemPedido, Pedido, Pagamento, Cliente
from django.contrib import messages
from .forms import PagamentoForm
from .forms import ProdutoForm
from .forms import ClienteForm
from .forms import CategoriaForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def listar_produtos(request):
    produtos = Produto.objects.all() 
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'editar_produto.html', {'form': form, 'produto': produto})

def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')
    return render(request, 'deletar_produto.html', {'produto': produto})

def produtos_por_categoria(request):
    categorias = Categoria.objects.prefetch_related('produtos').all()
    return render(request, 'produtos_por_categoria', {'categorias': categorias})

def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'criar_categoria.html', {'form': form})

def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'editar_categoria.html', {'form': form, 'categoria': categoria})

def deletar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')
    return render(request, 'deletar_categoria.html', {'categoria': categoria})

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('listar_produtos')  
    else:
        form = ProdutoForm()
    
    return render(request, 'criar_produto.html', {'form': form})

def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('criar_cliente')  
    else:
        form = ClienteForm()
    
    return render(request, 'criar_cliente.html', {'form': form})

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
