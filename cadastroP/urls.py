# cadastroP/urls.py

from django.urls import path
from . import views # Importa as views do seu próprio app

urlpatterns = [
    path('cadastro/', views.cadastrar_produto, name='cadastrar_produto'),
    path('lista/', views.listar_produtos, name='listar_produtos'),
    # Remova a linha abaixo se ela estiver presente:
    # path('', include('cadastro_produtos_projeto.urls')), # <--- ESTA LINHA DEVE SER REMOVIDA!
]
