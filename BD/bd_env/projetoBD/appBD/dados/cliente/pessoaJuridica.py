from django.db import models
from .cliente import Cliente

class PessoaJuridica(Cliente):
	cnpj = models.CharField(max_length=17)
	razaoSocial = models.CharField(max_length=30)
	nomeFantasia = models.CharField(max_length=20)

	class Meta:
		db_table = "pessoaJuridica"