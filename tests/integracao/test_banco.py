# tests/integracao/test_banco.py

def test_salvar_pedido():
    resultado = salvar_pedido_no_banco(pedido)
    assert resultado == True  # Verifica se o pedido foi salvo no banco
