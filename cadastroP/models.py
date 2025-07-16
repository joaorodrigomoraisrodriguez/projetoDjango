# cadastroP/models.py

from django.db import models

class Produto(models.Model):
    """
    Modelo para representar um produto no sistema.
    Contém campos para nome, preço e descrição do produto.
    """
    nome = models.CharField(max_length=200, verbose_name="Nome do Produto")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    # CORREÇÃO AQUI: Use TextField para descrições e permita que seja opcional
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome'] # Ordena os produtos por nome por padrão

    def __str__(self):
        """
        Retorna uma representação em string do objeto Produto.
        Útil para o painel administrativo e depuração.
        """
        return self.nome
