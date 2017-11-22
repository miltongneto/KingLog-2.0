from django.db import models
from .cliente import Cliente

class PessoaFisica(Cliente):
	cpf = models.CharField(max_length=10)
	rg = models.CharField(max_length=7)
	dataNascimento = models.DateField()
	sexo = models.CharField(max_length=1)

	class Meta:
   		db_table = "pessoaFisica"
