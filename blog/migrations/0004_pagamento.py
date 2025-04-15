# Generated by Django 5.2 on 2025-04-15 19:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_cliente_itempedido_pedido_itempedido_pedido_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_pagamento', models.DateField(auto_now_add=True)),
                ('metodo', models.CharField(choices=[('credito', 'Cartão de Crédito'), ('boleto', 'Boleto Bancário'), ('pix', 'PIX')], max_length=50)),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('aprovado', 'Aprovado'), ('recusado', 'Recusado')], max_length=20)),
                ('comprovante', models.ImageField(blank=True, null=True, upload_to='comprovantes/')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagamentos', to='blog.pedido')),
            ],
            options={
                'verbose_name': 'Pagamento',
                'ordering': ['-data_pagamento'],
            },
        ),
    ]
