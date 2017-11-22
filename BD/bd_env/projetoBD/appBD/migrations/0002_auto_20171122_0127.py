# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 03:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appBD', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('cliente_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appBD.Cliente')),
                ('cpf', models.CharField(max_length=10)),
                ('rg', models.CharField(max_length=7)),
                ('dataNascimento', models.DateField()),
                ('sexo', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'pessoaFisica',
            },
            bases=('appBD.cliente',),
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('cliente_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appBD.Cliente')),
                ('cnpj', models.CharField(max_length=17)),
                ('razaoSocial', models.CharField(max_length=30)),
                ('nomeFantasia', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'pessoaJuridica',
            },
            bases=('appBD.cliente',),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(default='F', max_length=1),
            preserve_default=False,
        ),
    ]
