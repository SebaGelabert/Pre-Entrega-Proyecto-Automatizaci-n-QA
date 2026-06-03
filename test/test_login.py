from page.login_page import LoginPage

# login con datos reales

def test_login_ok(driver):
    login_page = LoginPage(driver)

    login_page.login("standard_user","secret_sauce")

    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"

# login con datos falsos    

def test_login_invalid_password(driver):
    login_page = LoginPage(driver)

    login_page.login("XXXXXXXX","123456")

    error = login_page.get_error_password_message()

   # assert "Epic sadface: Username and password doesn't match in this service" in error
    assert error == "hola"
