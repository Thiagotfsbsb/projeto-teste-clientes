# tests/unitarios/test_calculo.py

def test_calcular_total():
    resultado = calcular_total(10, 2)  # Preço 10, quantidade 2
    assert resultado == 20  # Esperado que o total seja 20
