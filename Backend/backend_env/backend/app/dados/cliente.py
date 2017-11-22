from django.db import models

class Cliente (models.Model):
	nome = models.CharField(max_length=100)
	email = models.CharField(max_length=50)
	telefone = models.CharField(max_length=13)
	tipo = models.CharField(max_length=1)

	class Meta:
   		db_table = "cliente"

