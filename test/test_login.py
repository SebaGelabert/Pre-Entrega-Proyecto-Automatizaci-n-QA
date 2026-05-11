import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_login_validation(login_in_driver): 
    try:
        driver = login_in_driver 

        assert "/inventory.html" in driver.current_url, (
            "No ha redirigido a la página solicitada"
        )        

    except AssertionError as e:
        print(f"Error en la validación del login: {e}")

    finally:
        time.sleep(2)    
