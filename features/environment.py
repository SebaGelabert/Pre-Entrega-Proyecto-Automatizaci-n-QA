from selenium import webdriver

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome() #abro anvegador
    context.driver.maximize_window() #pantalla grande

def after_scenario(context, scenario):
    context.driver.quit() #cierro navegador    