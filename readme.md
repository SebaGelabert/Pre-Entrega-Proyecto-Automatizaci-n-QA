# Proyecto de Automatizacion QA - Sebastián Gelabert.

## Descripción:
Proyecto de automatización de pruebas funcionales sobre el sitio SauceDemo (https://www.saucedemo.com/), 
desarrollado como parte de la cursada de QA Automation.

## Objetivo del proyecto:
El objetivo es validar los flujos principales de la aplicación mediante tests automatizados con las herramientas antes mencionadas, simulando el comportamiento de un usuario real en el navegador ingresando a dicho sitio.

## Tecnologías usadas:
-Python
-Selenium WebDriver
-Pytest
-Requests
-Pytest HTML
-Logging
-JSON
-CSV
-Git
-GitHub

## Patrón utilizado:
Se implementó el patrón Page Object Model (POM) para separar la lógica de interacción con las páginas de los casos de prueba, esto permite un mejor mantenimiento y reutilización del código.

## Instalación

-Clonar el repositorio:

`git clone https://github.com/SebaGelabert/Pre-Entrega-Proyecto-Automatizaci-n-QA.git`

## Instalación Dependencias:

`pip install -r requirements.txt`

## Funcionamiento de las pruebas:

### Test Login (`test_login.py`)
- Valida el loggin delusuario con email y password y que al ingresar, el usuario sea redirigido correctamente a la página de inventario (`/inventory.html`).

### Test Inventario (`test_inventory.py`)
- Abre el navegador, hace el login y se ubica en el inventario de productos. 
- Verifica que el título de la página sea "Swag Labs".
- Comprueba que los productos sean visibles en el inventario.
- Valida que los elementos de UI estén presentes: menú hamburguesa y filtro de productos.

### Test Login CSV (`test_login_csv.py`)
- Lee el archivo CSV e intenta haceer el login. Se verifica si el usuario es o no válido.
- La idea es probar múltiples combinaciones de usuario y contraseña leyendo los datos desde un archivo CSV.

### Test Carrito (`test_cart.py`)
- Agrega el primer producto disponible al carrito.
- Verifica que el contador del carrito se actualice correctamente.
- Navega al carrito y confirma que el producto agregado coincida con el seleccionado.

### Test Carrito JSON (`test_cart_json.py`)
- Esta prueba lee el JSON, agrega productos al carrito, luego va al carrito, obtiene y compara nombre y precio de productos.

### Test API (`test_api.py`)
- Esta prueba realiza un Login válido, Login sin Password y Login sin email.
- También Crea, Obtiene y Elimina usuario.
- Todo con Error Code.

### Logging
Se generan automáticamente archivos de log en la carpeta "logs/...", registrando:
-Inicio de las pruebas.
-Acciones realizadas.
-Eventos importantes.
-Errores encontrados durante la ejecución.

### Capturas automáticas
En caso de fallo de una prueba UI, se genera automáticamente una captura de pantalla del navegador en carpeta "screenshots/...".
Las imágenes son incorporadas al reporte HTML para facilitar el análisis de errores.

### Reportes HTML
Los reportes HTML se generan automáticamente en archivo "report.html", incluyendo:
-Tests ejecutados.
-Tests aprobados y fallidos.
-Tiempo de ejecución.
-Detalle de errores.
-Capturas de pantalla en caso de fallo.

## Ejecución de los tests

### Correr todos los tests:

py -m pytest test/ -s

### Correr un test específico:

py -m pytest test/test_login.py -s
py -m pytest test/test_inventory.py -s
py -m pytest test/test_cart.py -s
py -m pytest -v -s test/test_cart_json.py
py -m pytest -v -s test/test_api.py
py -m pytest -v test/test_login_csv.py
py -m behave 

Los reportes HTML se generan automáticamente en `report.html` al finalizar cada ejecución.