from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Abre el navegador Chrome
driver = webdriver.Chrome()

# Navega a la pagina de practica
driver.get("https://demoqa.com/checkbox")

# Espera a que el arbol este listo y haz click en el checkbox de "Home"
wait = WebDriverWait(driver, 15)
home_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Select Home']")))
home_checkbox.click()

# Verificar el resultado
resultado = driver.find_element(By.ID, "result").text
print(resultado)
time.sleep(5)

# Cierra el navegador
driver.quit()