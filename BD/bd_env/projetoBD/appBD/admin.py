from django.contrib import admin
from .dados.cliente.cliente import Cliente
from .dados.cliente.pessoaFisica import PessoaFisica

# Register your models here.

admin.site.register(Cliente)
admin.site.register(PessoaFisica)
