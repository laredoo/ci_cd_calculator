class Calculadora:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def adicionar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero não é permitida."
        return a / b