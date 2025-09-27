import pytest

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b

# -------------------
# Testes Unitários
# -------------------

def test_soma():
    assert soma(2, 3) == 5

def test_subtrai():
    assert subtrai(5, 2) == 3

def test_multiplica():
    assert multiplica(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divide(10, 0)