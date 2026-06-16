Feature: Inicio de sesion
    Background:
        Given el usuario esta en la pagina de Login

    Scenario: Login exitoso
        When ingresa el usuario 'standard_user' y la contraseña 'secret_sauce'
        And hace click en el boton Login
        Then deberia ingresar al inventario

    Scenario: Login invalido con contraseña incorrecta
        When ingresa el usuario 'standard_user' y la contraseña '12345'
        And hace click en el boton Login
        Then deberia ver el mensaje de error 'Epic sadface: Username and password not match in this service'

    Scenario Outline: Login invalido con difeentes usuarios
        When ingresa el usuario '<usuario>' y la contraseña '<password>'
        And hace click en el boton Login
        Then deberia ver el mensaje de error '<mensaje>'

        Examples:
            |usuario|password|mensaje|
            |standard_user|12345|Epic sadface: Username and password not match in this service
            |standart_user|secret_sauce|Epic sadface: Username and password not match in this service
            | VACIO | secret_sauce | Epic sadface: Username is required |
            | standard_user | VACIO | Epic sadface: Password is required |