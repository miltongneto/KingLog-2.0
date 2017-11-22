from django.db import models

class Endereco(models.Model):
	CEP = models.CharField(max_length=8)
	rua = models.CharField(max_length=20)
	numero = models.CharField(max_length=5)
	complemento = models.CharField(max_length=10)
	bairro = models.CharField(max_length=15)
	estado = models.CharField(max_length=15)
	pais = models.CharField(max_length=15)

	class Meta:
		db_table = "endereco"