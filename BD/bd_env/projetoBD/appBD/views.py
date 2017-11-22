from django.shortcuts import render
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from appBD.dados.cliente.cliente import Cliente
from appBD.dados.cliente.pessoaFisica import PessoaFisica
from appBD.dados.cliente.cadastroCliente import CadastroCliente
from appBD.dados.cliente.serializer import ClienteSerializer, PessoaFisicaSerializer, PessoaJuridicaSerializer

class ClienteCadastroViewSet(viewsets.ModelViewSet):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	permission_classes = [AllowAny]

	@list_route(methods=['post'])
	def cadastrarCliente(self, request):
		print("cadastrando...")

		serializer = None
		if request.data['tipo'] == 'F':
			serializer = PessoaFisicaSerializer(data=request.data, context={'request': request})
		else:
			serializer = PessoaJuridicaSerializer(data=request.data, context={'request': request})
		
		if serializer.is_valid():
			cadastroCliente = CadastroCliente()
			cadastroCliente.inserir(serializer)
			
		return Response(None)