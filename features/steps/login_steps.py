# pasos para el Feature de inicio de sesión
from page.login_page import LoginPage
from behave import given, when, then

# instrucción para ejecutar el navegador
@given("el usuario esta en la pagina de Login")
def step_usuario_en_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

# instrucción para ingresar las credenciales
@when("ingresa el usuario '{usuario}' y la contraseña '{password}'")
def step_ingresar_credenciales(context, usuario, password):
    if usuario == "VACIO":
        usuario = ""

    if password == "VACIO":
        password = ""    

    context.login_page.enter_username(usuario)
    context.login_page.enter_password(password)

# instrucción para hacer clic en el botón de inicio de sesión
@when("hace clic en el botón de inicio de sesión")
def step_click_login(context):
    context.login_page.click_login()    

# instrucción para validar el inicio de sesión exitoso    
@then("el usuario debería ingresara la página de productos")
def step_validar_login_exitoso(context):
    assert "/inventory.html" in context.driver.current_url, "no direcciono a la página de productos" # validación

# when para escenario de login con datos inválidos
@when("deberia mostrar el mensaje de error '{message}'")
def step_validar_mensaje_error(context, message):
    error = context.login_page.get_error_password_message()
    assert message in error, f"El mensaje de error esperado '{message}' no se encontro en el mensaje actual '{error}'"