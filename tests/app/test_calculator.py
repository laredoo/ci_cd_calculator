from tests.factory.calculator import create_fake_calculator
import pytest

def test_adicionar():
    calc = create_fake_calculator(3)
    assert calc.adicionar(5, 3) == 8
    assert calc.adicionar(-1, 1) == 0
    assert calc.adicionar(-1, -1) == -2

def test_subtrair():
    calc = create_fake_calculator(3)
    assert calc.subtrair(5, 3) == 2
    assert calc.subtrair(-1, 1) == -2
    assert calc.subtrair(-1, -1) == 0

def test_multiplicar():
    calc = create_fake_calculator(3)
    assert calc.multiplicar(5, 3) == 15
    assert calc.multiplicar(-1, 1) == -1
    assert calc.multiplicar(-1, -1) == 1

def test_dividir():
    calc = create_fake_calculator(3)
    assert calc.dividir(6, 3) == 2
    assert calc.dividir(-1, 1) == -1
    assert calc.dividir(-1, -1) == 1
    assert calc.dividir(5, 0) == "Erro: Divisão por zero não é permitida."

def test_dividir_zero():
    calc = create_fake_calculator(3)
    assert calc.dividir(0, 5) == 0

def test_operacoes_mistas():
    calc = create_fake_calculator(3)
    assert calc.adicionar(1, calc.subtrair(5, 3)) == 3
    assert calc.multiplicar(calc.dividir(10, 2), 3) == 15
    assert calc.adicionar(calc.multiplicar(2, 3), calc.subtrair(5, 3)) == 8
