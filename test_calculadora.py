import sys
import pytest
import numpy as np
try:
    import pandas as pd
except ImportError:
    pass
from calculadora import Calculadora

class TestCalculadora:
    
    @pytest.fixture
    def calc(self):
        return Calculadora()

    def test_soma(self, calc):
        assert calc.soma(1, 2) == 3
        assert calc.soma(-1, 1) == 0
        assert calc.soma(-1, -1) == -2

    def test_subtrai(self, calc):
        assert calc.subtrai(2, 1) == 1
        assert calc.subtrai(1, 1) == 0
        assert calc.subtrai(-1, -1) == 0

    def test_multiplica(self, calc):
        assert calc.multiplica(2, 3) == 6
        assert calc.multiplica(-1, 1) == -1
        assert calc.multiplica(-1, -1) == 1

    def test_divide(self, calc):
        assert calc.divide(6, 3) == 2
        assert calc.divide(-1, 1) == -1
        assert calc.divide(-1, -1) == 1
        with pytest.raises(ValueError):
            calc.divide(1, 0)

    @pytest.mark.skip(reason="Método ainda não implementado")
    def test_raiz(self, calc):
        numero = 4
        esperado = np.sqrt(numero)
        resultado = calc.raiz_quadrada(numero)
        assert np.isclose(resultado, esperado)
        
        numero = 9
        esperado = np.sqrt(numero)
        resultado = calc.raiz_quadrada(numero)
        assert np.isclose(resultado, esperado)
        
        numero = 49
        esperado = np.sqrt(numero)
        resultado = calc.raiz_quadrada(numero)
        assert np.isclose(resultado, esperado)
        
    @pytest.mark.skipif('numpy' not in sys.modules, reason="Biblioteca numpy é necessária para o teste.")
    def test_soma_vetores(self, calc):
        vetor1 = np.array([1, 2, 3])
        vetor2 = np.array([4, 5, 6])
        resultado = calc.soma_vetores(vetor1, vetor2)
        esperado = np.add(vetor1, vetor2)
        assert all([r1 == r2 for r1, r2 in zip(resultado, esperado)])
        
        vetor1 = np.array([8, 5, 0])
        vetor2 = np.array([2, 2, 9])
        resultado = calc.soma_vetores(vetor1, vetor2)
        esperado = np.add(vetor1, vetor2)
        assert all([r1 == r2 for r1, r2 in zip(resultado, esperado)])
        
        vetor1 = np.array([3.1, 0.24, 1.1])
        vetor2 = np.array([2.9, 5.3, 9.22])
        resultado = calc.soma_vetores(vetor1, vetor2)
        esperado = np.add(vetor1, vetor2)
        assert all([r1 == r2 for r1, r2 in zip(resultado, esperado)])
    
    @pytest.mark.skipif('pandas' not in sys.modules, reason="Biblioteca pandas não é necessária, mas isso é um teste")
    def test_produto_matriz(self, calc):
        matriz1 = np.array([[1, 2], [3, 4]])
        matriz2 = np.array([[5, 6], [7, 8]])
        resultado = calc.produto_matriz(matriz1, matriz2)
        esperado = np.array([[19, 22], [43, 50]])
        assert all([m1 == m2 for m1, m2 in zip(resultado, esperado)])
        
        # Caso 1: Produto de uma matriz com uma matriz identidade
        matriz = np.array([[1, 2], [3, 4]])
        identidade = np.eye(2)
        resultado = calc.produto_matriz(matriz, identidade)
        esperado = matriz
        assert all([m1 == m2 for m1, m2 in zip(resultado, esperado)])

        # Caso 2: Produto de uma matriz com uma matriz de zeros
        zeros = np.zeros((2, 2))
        resultado = calc.produto_matriz(matriz, zeros)
        esperado = zeros
        assert all([m1 == m2 for m1, m2 in zip(resultado, esperado)])

        # Caso 3: Produto de duas matrizes não quadradas
        matriz1 = np.array([[1, 2, 3], [4, 5, 6]])
        matriz2 = np.array([[7, 8], [9, 10], [11, 12]])
        resultado = calc.produto_matriz(matriz1, matriz2)
        esperado = np.array([[58, 64], [139, 154]])
        assert all([m1 == m2 for m1, m2 in zip(resultado, esperado)])