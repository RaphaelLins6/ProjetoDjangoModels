# 📝 Projeto Django - E-commerce 

Bem-vindo ao repositório do **Projeto Django**! Este projeto foi desenvolvido para demonstrar a criação e utilização de **modelos, templates, views e APIs no Django**, que são a base para a criação de aplicações web. Aqui você encontrará a estrutura do projeto, explicações sobre os arquivos e como começar a utilizá-lo. 🚀

---

## 🖥️ Tecnologias Utilizadas

<p align="center"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/2048px-Python.svg.png" alt="Python" width="60" height="50"/> &nbsp;&nbsp; 
<img src="https://images.icon-icons.com/2415/PNG/512/django_original_logo_icon_146559.png" alt="Django" width="60" height="50"/> &nbsp;&nbsp;
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/2048px-Visual_Studio_Code_1.35_icon.svg.png" alt="Visual Studio Code" width="60" height="50"/> &nbsp;&nbsp;

---

## 🛠️ Modelos (Models)

Os **modelos** são definidos no arquivo `blog/models.py`. Eles representam as tabelas do banco de dados e permitem manipular os dados de forma programática. Aqui está um exemplo de modelo para uma categoria de produto:

```python
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ativa = models.BooleanField(default=True)
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Categoria'

    @property
    def nome_maiusculo(self):
        return self.nome.upper()

    @property
    def resumo_descricao(self):
        return self.descricao[:50] + '...'

    def __str__(self):
        return self.nome
```

---

## 🎨 Templates
Os **templates** são definidos no diretório templates e são usados para renderizar o conteúdo HTML dinâmico no Django. Aqui está um exemplo de template para listar produtos por categoria:
```
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Produtos por Categoria</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
        }
        .categoria {
            margin: 20px auto;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 8px;
            max-width: 800px;
            background-color: #fff;
        }
        .produto {
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <h1>Produtos por Categoria</h1>
    {% for categoria in categorias %}
        <div class="categoria">
            <h2>{{ categoria.nome }}</h2>
            <p>{{ categoria.descricao }}</p>
            <ul>
                {% for produto in categoria.produtos.all %}
                    <li class="produto">{{ produto.nome }} - R$ {{ produto.preco }}</li>
                {% endfor %}
            </ul>
        </div>
    {% endfor %}
</body>
</html>
```
---

## 🎭 Views

As **views** são responsáveis por processar as requisições HTTP e retornar respostas, como páginas HTML ou dados em formato JSON. Elas conectam os modelos aos templates, permitindo a exibição de dados dinâmicos no navegador.

No arquivo `blog/views.py`, você pode definir uma view para listar produtos por categoria. Aqui está um exemplo:

```python
from django.shortcuts import render
from .models import Categoria

def listar_produtos(request):
    categorias = Categoria.objects.prefetch_related('produtos').all()  # Carrega categorias e seus produtos
    return render(request, 'blog/listar_produtos.html', {'categorias': categorias})
```

---

## ⚡ APIs

### Integração com FastAPI

Além das views tradicionais do Django, este projeto também expõe uma **API moderna utilizando FastAPI**. Com ela, é possível consumir e manipular os dados de categorias e produtos de forma rápida e eficiente, facilitando a integração com frontends em JavaScript, aplicações móveis ou outros sistemas.

### Como executar a API FastAPI

1. Certifique-se de que as dependências estão instaladas (veja `requirements.txt`).
2. No terminal, ative o ambiente virtual e execute:
   ```
   uvicorn api:app --reload --port 8001
   ```
3. Acesse a documentação interativa da API em:  
   [http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs)

Com a FastAPI, seu projeto Django ganha uma camada de API RESTful moderna, pronta para integração com qualquer frontend!

---

## 🗃️ Como criar e aplicar migrações

Após definir ou alterar os modelos, você deve criar e aplicar migrações para atualizar o banco de dados:

Criar as migrações:
`python manage.py makemigrations`

Aplicar as migrações:
` python manage.py migrate`

---

## 🚀 Como Executar o Projeto
Siga os passos abaixo para executar o projeto localmente:

Certifique-se de ter o Python e o Django instalados.

Clone este repositório:
`git clone https://github.com/RaphaelLins6/ProjetoDjangoModels.git`

Navegue até o diretório do projeto:
`cd ProjetoDjangoModels`

Ative o ambiente virtual:

No Windows:
`venv\Scripts\activate`

No Linux/Mac:
`source venv/bin/activate`

Inicie o servidor de desenvolvimento:
`python manage.py runserver`

Acesse o projeto no navegador em: http://127.0.0.1:8000.

---

## 🌟 Funcionalidades Planejadas

📌 Adicionar modelos para categorias, produtos, clientes, pedidos e itens dos pedidos.

📌 Desenvolver templates dinâmicos para renderizar informações de forma interativa e estilizada.

📌 Criar views para exibir os dados no frontend.

📌 Implementar uma API para expor os dados do projeto, permitindo integração com outras aplicações ou serviços.

---

## 🎬 Demonstração

### Tela Inicial

> Vídeo da aplicação!

https://github.com/user-attachments/assets/ad3cd00b-17cc-4fca-b576-384aa0e8ed40

> Vídeo da API!

https://github.com/user-attachments/assets/fa529b68-302d-49f7-b783-f93898eaa731

---

## 👥 Autores

**Turma de ciência da computação - UDF**
- [@RaphaelLins6](https://www.github.com/RaphaelLins6) - Raphael Lins (RGM:27797660)
- [@jotape99](https://www.github.com/jotape99) - João Pedro (RGM:28167333)
- [@joaogkt](https://www.github.com/joaogkt) - João Gabriel (RGM:28017188)

## 📜 Licença

Este projeto é livre para uso e modificação. Contribuições são bem-vindas! 😊

---

> Projeto acadêmico desenvolvido para a disciplina de Aplicações para Internet – 8º Semestre.
