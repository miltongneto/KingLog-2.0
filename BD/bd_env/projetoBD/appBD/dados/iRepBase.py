from abc import ABC, abstractmethod
class IRepBase(ABC):

	@abstractmethod
	def inserir(self, entidade):
		pass

	@abstractmethod
	def atualizar(self, entidade):
		pass

	@abstractmethod
	def deletar(self, entidade):
		pass
