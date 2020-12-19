from rest_framework import generics
from produtos.models import Produto
from produtos.serializer import ProdutoSerializer


class ProdutoViewSet(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

