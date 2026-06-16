from page.login_page import LoginPage
from utils.logger import logger

# login con datos reales

def test_login_ok(driver):
    logger.info("Iniciando Driver Test login ok")
    login_page = LoginPage(driver)

    logger.info("Ingresando Datos")
    login_page.login("standard_user","secret_sauce")

    logger.info("Iniciando sesion")

    assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"
    
    if "/inventory.html" in driver.current_url:
        logger.info("Sesion iniciada correctamente")
    else:
        logger.error("Error al iniciar sesion")

# login con datos falsos    

def test_login_invalid_password(driver):
    login_page = LoginPage(driver)

    login_page.login("standard_user","123456")

    error = login_page.get_error_password_message()

    assert "Epic sadface: Username and password doesn't match in this service" in error
   
