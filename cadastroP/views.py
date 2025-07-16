# cadastroP/views.py

from django.shortcuts import render, redirect
from .models import Produto
from django.contrib import messages

def cadastrar_produto(request):
    # ... (código existente para cadastrar_produto)
    if request.method == 'POST':
        # ... (lógica de POST)
        return redirect('cadastrar_produto')
    else:
        return render(request, 'cadastroP/cadastro.html') # Caminho correto para cadastro.html

def listar_produtos(request):
    """
    View para exibir uma lista de todos os produtos cadastrados.
    """
    produtos = Produto.objects.all().order_by('nome')
    # CORREÇÃO AQUI: Certifique-se de que o caminho do template está correto
    return render(request, 'cadastroP/lista.html', {'produtos': produtos}) # <--- Deve ser 'cadastroP/lista.html'
