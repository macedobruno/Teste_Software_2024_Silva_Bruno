import numpy as np

class Calculadora:
    
    def soma(self, a, b):
        return a + b

    def subtrai(self, a, b):
        return a - b

    def multiplica(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b

    def soma_vetores(self, v1, v2):
        return np.add(v1, v2)
    
    def produto_matriz(self, m1, m2):
        return np.dot(m1, m2)