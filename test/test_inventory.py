import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture 
def driver_logged(login_in_driver):
    driver = login_in_driver
    return driver


def test_inventory_title(driver_logged):
    titulo = driver_logged.title
    assert titulo == "Swag Labs", "Error al ingresar a la pagina"
    print("PAGINA CORRECTA")
    time.sleep(2)


def test_productos_visibles(driver_logged):
    productos = driver_logged.find_elements(By.CLASS_NAME, "inventory_item") 
    assert len(productos) > 0, "No se encontraron productos en el inventario"
    print("PRODUCTOS VISIBLES")
    time.sleep(2)


def test_ui_elements(driver_logged):      
    menu = driver_logged.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed(), "El menú hamburguesa no está visible"
    filtro = driver_logged.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro.is_displayed(), "El filtro no está visible"
    print("ELEMENTOS VISIBLES")
    time.sleep(2)