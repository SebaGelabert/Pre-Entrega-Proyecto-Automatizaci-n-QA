from page.login_page import LoginPage

def test_login_ok(driver):
    login_page = LoginPage(driver)

    login_page.loguin("standard_user", "secret_sauce")

    assert"/inventory.html" in driver.current_url, "No se redirigió al inventario"

def test_login_invalid_password(driver):
    login_page = LoginPage(driver)

    login_page.loguin("standard_user", "123456")

    error = login_page.get_error_password()

    assert"Epic sadface: You can only access '/cart.html' when you are logged in." in error



