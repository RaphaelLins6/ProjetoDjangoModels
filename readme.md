# 📝 Projeto Django - Modelos de Dados

Bem-vindo ao repositório do **Projeto Django Models**! Este projeto foi desenvolvido para demonstrar a criação e utilização de **modelos no Django**, que são a base para a manipulação de dados em aplicações web. Aqui você encontrará a estrutura do projeto, explicações sobre os arquivos e como começar a utilizá-lo. 🚀

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

📌 Adicionar modelos para categorias, produtos, clientes, pedidos e itens dos pedidos.

📌 Criar views para exibir os dados no frontend.

---

## 🖥️ Tecnologias Utilizadas

*Django:* Framework web para desenvolvimento rápido e seguro.

*SQLite:* Banco de dados leve e integrado.

---

## 📜 Licença

Este projeto é livre para uso e modificação. Contribuições são bem-vindas! 😊

---

## 👥 Autores

**Turma de ciência da computação - UDF**
- [@RaphaelLins6](https://www.github.com/RaphaelLins6) - Raphael Lins (RGM:27797660)
- [@jotape99](https://www.github.com/jotape99) - João Pedro (RGM:28167333)
- [@joaogkt](https://www.github.com/joaogkt) - João Gabriel (RGM:28017188)
