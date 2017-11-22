from .iRepBase import IRepBase

class RepBaseBD(IRepBase):

	def inserir(self, entidade):
		print("RepBase, Inserir")
		entidade.save()

	def atualizar(self, entidade):
		pass

	def deletar(self, entidade):
		print("RepBase, Deletar")
		pass