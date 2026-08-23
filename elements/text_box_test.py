from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Abre el navegador Chrome
driver = webdriver.Chrome()

# Navega a la pagina de practica
driver.get("https://demoqa.com/text-box")

# Llena cada campo del formulario
driver.find_element(By.ID, "userName").send_keys("Jose Ruiz")
driver.find_element(By.ID, "userEmail").send_keys("ruiz.josemiguel@gmail.com")
driver.find_element(By.ID, "currentAddress").send_keys("Santiago, Chile")
driver.find_element(By.ID, "permanentAddress").send_keys("Santiago, Chile")

# Hace click en el boton Submit
submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
submit_button.click()

# Espera unos segundos para que puedas ver el resultado antes de que se cierre
resultado = driver.find_element(By.ID, "output").text
print(resultado)
time.sleep(5)

# Cierra el navegador
driver.quit()