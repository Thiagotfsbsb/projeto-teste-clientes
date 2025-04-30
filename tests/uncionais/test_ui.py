# tests/funcionais/test_ui.py

from selenium import webdriver

def test_realizar_pedido():
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000")
    
    driver.find_element_by_id("adicionar_item").click()
    driver.find_element_by_id("finalizar_pedido").click()
    
    assert "Pedido Confirmado" in driver.page_source
    driver.quit()
