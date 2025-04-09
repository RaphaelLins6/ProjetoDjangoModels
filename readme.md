# 📝 Projeto Django - Modelos de Dados

Bem-vindo ao repositório do **Projeto Django Models**! Este projeto foi desenvolvido para demonstrar a criação e utilização de **modelos no Django**, que são a base para a manipulação de dados em aplicações web. Aqui você encontrará a estrutura do projeto, explicações sobre os arquivos e como começar a utilizá-lo. 🚀

---

## 🛠️ Modelos (Models)

Os **modelos** são definidos no arquivo `blog/models.py`. Eles representam as tabelas do banco de dados e permitem manipular os dados de forma programática. Aqui está um exemplo de modelo para um post de blog:

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Título do post
    content = models.TextField()             # Conteúdo do post
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação
    updated_at = models.DateTimeField(auto_now=True)      # Data de última atualização

    def __str__(self):
        return self.title
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
`git clone <URL_DO_REPOSITORIO>`

Navegue até o diretório do projeto:
`cd ProjetoDjangoModels`

Inicie o servidor de desenvolvimento:
`python manage.py runserver`

Acesse o projeto no navegador em: http://127.0.0.1:8000.

---

## 🌟 Funcionalidades Planejadas

📌 Adicionar modelos para categorias e comentários.

📌 Criar views para exibir os dados no frontend.

📌 Melhorar o design do painel administrativo.

---

## 🖥️ Tecnologias Utilizadas

*Django:* Framework web para desenvolvimento rápido e seguro.

*SQLite:* Banco de dados leve e integrado.

---

## 📜 Licença

Este projeto é livre para uso e modificação. Contribuições são bem-vindas! 😊