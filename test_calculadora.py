import pytest
import numpy as np
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