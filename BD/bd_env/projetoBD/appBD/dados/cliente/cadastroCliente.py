from appBD.dados.repAbstractFactory import RepAbstractFactory

class CadastroCliente(object):
	
	iRepCliente = None

	def __init__(self):
		self.iRepCliente = RepAbstractFactory.obterFactory("BD").criarRepCliente()

	def inserir(self, cliente):		
		self.iRepCliente.inserir(cliente)
