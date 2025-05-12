# 📝 Projeto Django - Modelos de Dados

Bem-vindo ao repositório do **Projeto Django Models**! Este projeto foi desenvolvido para demonstrar a criação e utilização de **modelos no Django**, que são a base para a manipulação de dados em aplicações web. Aqui você encontrará a estrutura do projeto, explicações sobre os arquivos e como começar a utilizá-lo. 🚀

---

## 🖥️ Tecnologias Utilizadas

<p align="center"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/2048px-Python.svg.png" alt="Python" width="60" height="50"/> &nbsp;&nbsp; 
<img src="https://images.icon-icons.com/2415/PNG/512/django_original_logo_icon_146559.png" alt="Django" width="60" height="50"/> &nbsp;&nbsp;
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/2560px-SQLite370.svg.png" alt="SQLite" width="100" height="50"/> &nbsp;&nbsp;
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
Os templates são definidos no diretório templates e são usados para renderizar o conteúdo HTML dinâmico no Django. Aqui está um exemplo de template para listar produtos por categoria:
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

📌 Criar views para exibir os dados no frontend.

---

## 👥 Autores

**Turma de ciência da computação - UDF**
- [@RaphaelLins6](https://www.github.com/RaphaelLins6) - Raphael Lins (RGM:27797660)
- [@jotape99](https://www.github.com/jotape99) - João Pedro (RGM:28167333)
- [@joaogkt](https://www.github.com/joaogkt) - João Gabriel (RGM:28017188)

## 📜 Licença

Este projeto é livre para uso e modificação. Contribuições são bem-vindas! 😊

---