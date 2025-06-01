from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_blog.settings')
import django
django.setup()
from blog.models import Produto, Categoria, ItemPedido, Pedido, Pagamento, Cliente
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class ProdutoSchema(BaseModel):
    nome: str
    descricao: str = ""
    preco: float
    estoque: int
    categoria: int

class CategoriaSchema(BaseModel):
    nome: str
    descricao: str = ""

class ClienteSchema(BaseModel):
    nome: str
    email: str
    telefone: str = ""
    endereco: str = ""

class PagamentoSchema(BaseModel):
    pedido: int
    valor: float
    status: str = "pendente"

class ItemPedidoSchema(BaseModel):
    produto: int
    quantidade: int
    pedido: int

class PedidoSchema(BaseModel):
    cliente: int
    status: str = "aberto"
    finalizado: bool = False
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000"],  
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/produtos")
def listar_produtos():
    produtos = Produto.objects.all()
    return [{"id": p.id, "nome": p.nome, "preco": float(p.preco), "tem_estoque": p.estoque > 0} for p in produtos]



@app.get("/api/produtos/{produto_id}")
def get_produto(produto_id: int):
    try:
        p = Produto.objects.get(id=produto_id)
        return {
            "id": p.id,
            "nome": p.nome,
            "descricao": p.descricao,
            "preco": float(p.preco),
            "estoque": p.estoque
        }
    except Produto.DoesNotExist:
        return {}, 404
    
@app.post("/api/produtos")
def criar_produto(produto: ProdutoSchema):
    categoria = Categoria.objects.get(id=produto.categoria)
    novo_produto = Produto.objects.create(
        nome=produto.nome,
        descricao=produto.descricao,
        preco=produto.preco,
        estoque=produto.estoque,
        categoria=categoria
    )
    return {
        "id": novo_produto.id,
        "nome": novo_produto.nome,
        "descricao": novo_produto.descricao,
        "preco": float(novo_produto.preco),
        "estoque": novo_produto.estoque,
        "categoria": novo_produto.categoria.id
    }

@app.put("/api/produtos/{produto_id}")
def atualizar_produto(produto_id: int, produto: ProdutoSchema):
    prod = Produto.objects.get(id=produto_id)
    prod.nome = produto.nome
    prod.descricao = produto.descricao
    prod.preco = produto.preco
    prod.estoque = produto.estoque
    prod.save()
    return {
        "id": prod.id,
        "nome": prod.nome,
        "descricao": prod.descricao,
        "preco": float(prod.preco),
        "estoque": prod.estoque
    }

@app.delete("/api/produtos/{produto_id}")
def deletar_produto(produto_id: int):
    prod = Produto.objects.get(id=produto_id)
    prod.delete()
    return {"ok": True}

@app.get("/api/categorias_com_produtos")
def categorias_com_produtos():
    categorias = Categoria.objects.all()
    return [
        {
            "id": c.id,
            "nome": c.nome,
            "descricao": c.descricao,
            "produtos": [
                {
                    "id": p.id,
                    "nome": p.nome,
                    "preco": float(p.preco),
                    "tem_estoque": p.estoque > 0
                }
                for p in c.produtos.all()
            ]
        }
        for c in categorias
    ]


@app.get("/api/categorias/{categoria_id}")
def get_categoria(categoria_id: int):
    try:
        c = Categoria.objects.get(id=categoria_id)
        return {
            "id": c.id,
            "nome": c.nome,
            "descricao": c.descricao
        }
    except Categoria.DoesNotExist:
        return {}, 404
    
@app.post("/api/categorias")
def criar_categoria(categoria: CategoriaSchema):
    nova_categoria = Categoria.objects.create(
        nome=categoria.nome,
        descricao=categoria.descricao
    )
    return {
        "id": nova_categoria.id,
        "nome": nova_categoria.nome,
        "descricao": nova_categoria.descricao
    }

@app.put("/api/categorias/{categoria_id}")
def atualizar_categoria(categoria_id: int, categoria: CategoriaSchema):
    cat = Categoria.objects.get(id=categoria_id)
    cat.nome = categoria.nome
    cat.descricao = categoria.descricao
    cat.save()
    return {"id": cat.id, "nome": cat.nome, "descricao": cat.descricao}

@app.delete("/api/categorias/{categoria_id}")
def deletar_categoria(categoria_id: int):
    cat = Categoria.objects.get(id=categoria_id)
    cat.delete()
    return {"ok": True}

@app.get("/api/clientes")
def listar_clientes():
    clientes = Cliente.objects.all()
    return [{"id": c.id, "nome": c.nome, "email": c.email} for c in clientes]




@app.post("/api/clientes")
def criar_categoria(clientes: ClienteSchema):
    novo_cliente = Cliente.objects.create(
        nome=clientes.nome,
        email=clientes.email,
        telefone=clientes.telefone,
        endereco=clientes.endereco

    )
    return {
        "id": novo_cliente.id,
        "nome": novo_cliente.nome,
        "email": novo_cliente.email,
        "telefone": novo_cliente.telefone,
        "endereco": novo_cliente.endereco
    }

@app.get("/api/clientes/{cliente_id}")
def get_cliente(cliente_id: int):
    try:
        c = Cliente.objects.get(id=cliente_id)
        return {
            "id": c.id,
            "nome": c.nome,
            "email": c.email,
            "telefone": c.telefone,
            "endereco": c.endereco
        }
    except Cliente.DoesNotExist:
        return {}, 404
@app.put("/api/clientes/{cliente_id}")
def atualizar_cliente(cliente_id: int, cliente: ClienteSchema):
    cli = Cliente.objects.get(id=cliente_id)
    cli.nome = cliente.nome
    cli.email = cliente.email
    cli.telefone = cliente.telefone
    cli.endereco = cliente.endereco
    cli.save()
    return {
        "id": cli.id,
        "nome": cli.nome,
        "email": cli.email,
        "telefone": cli.telefone,
        "endereco": cli.endereco
    }
@app.delete("/api/clientes/{cliente_id}")
def deletar_cliente(cliente_id: int):
    cli = Cliente.objects.get(id=cliente_id)
    cli.delete()
    return {"ok": True}



@app.get("/api/pedidos")
def listar_pedidos():
    pedidos = Pedido.objects.all()
    return [{"id": p.id, "cliente": p.cliente.nome if p.cliente else None, "data": p.data_pedido} for p in pedidos]

@app.get("/api/pedidos/{pedido_id}")
def get_pedido(pedido_id: int):
    try:
        p = Pedido.objects.get(id=pedido_id)
        return {
            "id": p.id,
            "cliente": p.cliente.nome if p.cliente else None,
            "data": p.data_pedido,
            "status": p.status,
            "finalizado": p.finalizado
        }
    except Pedido.DoesNotExist:
        return {}, 404

@app.post("/api/pedidos")
def criar_pedido(pedido: PedidoSchema):
    cliente = Cliente.objects.get(id=pedido.cliente)
    novo_pedido = Pedido.objects.create(
        cliente=cliente,
        status=pedido.status,
        finalizado=pedido.finalizado
    )
    return {
        "id": novo_pedido.id,
        "cliente": novo_pedido.cliente.nome if novo_pedido.cliente else None,
        "data": novo_pedido.data_pedido,
        "status": novo_pedido.status,
        "finalizado": novo_pedido.finalizado
    }
@app.put("/api/pedidos/{pedido_id}")
def atualizar_pedido(pedido_id: int, pedido: PedidoSchema):
    ped = Pedido.objects.get(id=pedido_id)
    ped.cliente = Cliente.objects.get(id=pedido.cliente)
    ped.status = pedido.status
    ped.finalizado = pedido.finalizado
    ped.save()
    return {
        "id": ped.id,
        "cliente": ped.cliente.nome if ped.cliente else None,
        "data": ped.data_pedido,
        "status": ped.status,
        "finalizado": ped.finalizado
    }
@app.delete("/api/pedidos/{pedido_id}")
def deletar_pedido(pedido_id: int):
    ped = Pedido.objects.get(id=pedido_id)
    ped.delete()
    return {"ok": True}



@app.get("/api/itens_pedido")
def listar_itens_pedido():
    itens = ItemPedido.objects.all()
    return [{"id": i.id, "produto": i.produto.nome, "quantidade": i.quantidade, "pedido": i.pedido.id} for i in itens]

def get_item_pedido(item_id: int):
    try:
        i = ItemPedido.objects.get(id=item_id)
        return {
            "id": i.id,
            "produto": i.produto.nome,
            "quantidade": i.quantidade,
            "pedido": i.pedido.id
        }
    except ItemPedido.DoesNotExist:
        return {}, 404
@app.post("/api/itens_pedido")
def criar_item_pedido(item: ItemPedidoSchema):
    produto = Produto.objects.get(id=item.produto)
    pedido = Pedido.objects.get(id=item.pedido)
    novo_item = ItemPedido.objects.create(
        produto=produto,
        quantidade=item.quantidade,
        pedido=pedido
    )
    return {
        "id": novo_item.id,
        "produto": novo_item.produto.nome,
        "quantidade": novo_item.quantidade,
        "pedido": novo_item.pedido.id
    }
@app.put("/api/itens_pedido/{item_id}")
def atualizar_item_pedido(item_id: int, item: ItemPedidoSchema):
    it = ItemPedido.objects.get(id=item_id)
    it.produto = Produto.objects.get(id=item.produto)
    it.quantidade = item.quantidade
    it.pedido = Pedido.objects.get(id=item.pedido)
    it.save()
    return {
        "id": it.id,
        "produto": it.produto.nome,
        "quantidade": it.quantidade,
        "pedido": it.pedido.id
    }
@app.delete("/api/itens_pedido/{item_id}")
def deletar_item_pedido(item_id: int):
    it = ItemPedido.objects.get(id=item_id)
    it.delete()
    return {"ok": True}


@app.get("/api/pagamentos")
def listar_pagamentos():
    pagamentos = Pagamento.objects.all()
    return [{"id": p.id, "pedido": p.pedido.id, "valor": float(p.valor), "status": p.status} for p in pagamentos]



@app.get("/api/pagamentos/{pagamento_id}")
def get_pagamento(pagamento_id: int):
    try:
        p = Pagamento.objects.get(id=pagamento_id)
        return {
            "id": p.id,
            "pedido": p.pedido.id,
            "valor": float(p.valor),
            "status": p.status
        }
    except Pagamento.DoesNotExist:
        return {}, 404
    
@app.post("/api/pagamentos")
def criar_pagamento(pagamento: PagamentoSchema):
    pedido = Pedido.objects.get(id=pagamento.pedido)
    novo_pagamento = Pagamento.objects.create(
        pedido=pedido,
        valor=pagamento.valor,
        status=pagamento.status
    )
    return {
        "id": novo_pagamento.id,
        "pedido": novo_pagamento.pedido.id,
        "valor": float(novo_pagamento.valor),
        "status": novo_pagamento.status
    }

@app.put("/api/pagamentos/{pagamento_id}")
def atualizar_pagamento(pagamento_id: int, pagamento: PagamentoSchema):
    pag = Pagamento.objects.get(id=pagamento_id)
    pag.pedido = Pedido.objects.get(id=pagamento.pedido)
    pag.valor = pagamento.valor
    pag.status = pagamento.status
    pag.save()
    return {
        "id": pag.id,
        "pedido": pag.pedido.id,
        "valor": float(pag.valor),
        "status": pag.status
    }

@app.delete("/api/pagamentos/{pagamento_id}")
def deletar_pagamento(pagamento_id: int):
    pag = Pagamento.objects.get(id=pagamento_id)
    pag.delete()
    return {"ok": True}