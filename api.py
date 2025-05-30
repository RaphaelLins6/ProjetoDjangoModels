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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/produtos")
def listar_produtos():
    produtos = Produto.objects.all()
    return [{"id": p.id, "nome": p.nome, "preco": float(p.preco), "tem_estoque": p.estoque > 0} for p in produtos]

class ProdutoSchema(BaseModel):
    nome: str
    descricao: str = ""
    preco: float
    estoque: int
    categoria: int

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

@app.get("/api/categorias")
def listar_categorias():
    categorias = Categoria.objects.all()
    return [{"id": c.id, "nome": c.nome, "descricao": c.descricao} for c in categorias]

class CategoriaSchema(BaseModel):
    nome: str
    descricao: str = ""

@app.post("/api/categorias")
def criar_categoria(categoria: CategoriaSchema):
    nova_categoria = Categoria.objects.create(
        nome=categoria.nome,
        descricao=categoria.descricao
    )
    return {"id": nova_categoria.id, "nome": nova_categoria.nome, "descricao": nova_categoria.descricao}

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

@app.get("/api/pedidos")
def listar_pedidos():
    pedidos = Pedido.objects.all()
    return [{"id": p.id, "cliente": p.cliente.nome if p.cliente else None, "data": p.data_pedido} for p in pedidos]

@app.get("/api/itens_pedido")
def listar_itens_pedido():
    itens = ItemPedido.objects.all()
    return [{"id": i.id, "produto": i.produto.nome, "quantidade": i.quantidade, "pedido": i.pedido.id} for i in itens]

@app.get("/api/pagamentos")
def listar_pagamentos():
    pagamentos = Pagamento.objects.all()
    return [{"id": p.id, "pedido": p.pedido.id, "valor": float(p.valor), "status": p.status} for p in pagamentos]