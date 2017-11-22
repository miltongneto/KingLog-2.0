from django.shortcuts import render
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.response import Response
from app.dados.cliente import Cliente
from app.dados.pessoaFisica import PessoaFisica
from app.dados.serializer import ClienteSerializer, PessoaFisicaSerializer, PessoaJuridicaSerializer
from .comunicacaoBD import ComunicacaoBD
import requests

class ClienteService(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]

    @list_route(methods=['post'])
    def cadastrar(self, request):
        print("Enviando para o bd...")
        # serializer = ClienteSerializer(cliente, context={'request': request})
        print(ComunicacaoBD.cadastrarCliente)
        response = requests.post(ComunicacaoBD.cadastrarCliente, json=request.data)   
        print(response)

        return Response(None)