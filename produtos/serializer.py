from rest_framework import serializers

from produtos.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id', 'nome', 'descricao', 'valor')

    # def create(self, validated_data):
    #     try:
    #         produto = Produto.objects.create(
    #             nome=validated_data['nome'],
    #             descricao=validated_data['descricao'],
    #             valor=validated_data['valor'],
    #         )
    #         return produto
    #     except Exception as e:
    #         raise e
