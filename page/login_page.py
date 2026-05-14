from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        #selectores
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login_button")
        self.get_error_password = (By.CSS_SELECTOR, "[data-test = 'error']")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def ingresar_usuario(self, usuario):
        self.driver.find_element(*self.username_input).send_keys(usuario)        

    def ingresar_password(self, password):    
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def loguin(self, usuario, passwoed):
        self.open()
        self.ingresar_usuario()
        self.ingresar_password()
        self.click_login()    

    def get_error_password_message(self):
        return self.driver.find_element(*self.error_password).text
