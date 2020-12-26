from django.urls import path

from produtos import views

app_name = 'produtos'
urlpatterns = [
    path('', views.ProdutoViewSet.as_view({'get': 'list'}), name='lista'),


]
