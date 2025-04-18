# Generated by Django 5.2 on 2025-04-09 01:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('ativa', models.BooleanField(default=True)),
                ('criada_em', models.DateTimeField(auto_now_add=True)),
                ('atualizada_em', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estoque', models.IntegerField()),
                ('disponivel', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='blog.categoria')),
            ],
            options={
                'verbose_name': 'Produto',
                'ordering': ['nome'],
            },
        ),
    ]
