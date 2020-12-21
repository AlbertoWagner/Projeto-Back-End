from rest_framework import generics, status
from rest_framework.response import Response

from produtos.models import Produto
from produtos.serializer import ProdutoSerializer


class ProdutoViewSet(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ProdutoExcluir(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
