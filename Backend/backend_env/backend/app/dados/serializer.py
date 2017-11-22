from app.dados.cliente import Cliente
from app.dados.pessoaFisica import PessoaFisica
from app.dados.pessoaJuridica import PessoaJuridica
from rest_framework import serializers

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PessoaFisicaSerializer(ClienteSerializer):
    class Meta:
        model = PessoaFisica
        fields = '__all__'

class PessoaJuridicaSerializer(ClienteSerializer):
    class Meta:
        model = PessoaJuridica
        fields = '__all__'