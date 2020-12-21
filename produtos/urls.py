from django.urls import path

from produtos import views

app_name = 'produtos'
urlpatterns = [
    path('', views.ProdutoViewSet.as_view(), name='lista'),
    path('detalhes/<int:pk>/', views.ProdutoDetail.as_view(), name='detalhes-produtos'),
    path('excluir/<int:pk>/', views.ProdutoExcluir.as_view(), name='excluir'),

]
