from abc import ABC, abstractmethod
from .cliente.repClienteBD import RepClienteBD

class RepAbstractFactory(ABC):

	def obterFactory(configuracaoRep):
		if configuracaoRep == "BD":
			return RepBDFactory()

	@abstractmethod
	def criarRepCliente(self):
		pass

class RepBDFactory(RepAbstractFactory):

	def criarRepCliente(self):
		return RepClienteBD()