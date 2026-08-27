from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/links")

wait = WebDriverWait(driver, 15)

# 1. Click en "Home" (abre pestaña nueva)
home_link = wait.until(EC.element_to_be_clickable((By.ID, "simpleLink")))
home_link.click()

time.sleep(2)  # espera a que la nueva pestaña termine de abrir

# Cambiar el foco a la pestaña nueva
driver.switch_to.window(driver.window_handles[1])
print("Titulo de la nueva pestaña:", driver.title)

# Cerrar la pestaña nueva y volver a la original
driver.close()
driver.switch_to.window(driver.window_handles[0])

# 2. Click en un link tipo API 
created_link = wait.until(EC.element_to_be_clickable((By.ID, "created")))
created_link.click()
wait.until(EC.text_to_be_present_in_element((By.ID, "linkResponse"), "201"))
mensaje = driver.find_element(By.ID, "linkResponse").text
print(mensaje)

time.sleep(1)

# 3. Click en link "Bad Request" (400)
bad_request_link = wait.until(EC.element_to_be_clickable((By.ID, "bad-request")))
bad_request_link.click()
wait.until(EC.text_to_be_present_in_element((By.ID, "linkResponse"), "400"))
mensaje = driver.find_element(By.ID, "linkResponse").text
print(mensaje)

time.sleep(1)

# 4. Click en link "Unauthorized" (401)
unauthorized_link = wait.until(EC.element_to_be_clickable((By.ID, "unauthorized")))
unauthorized_link.click()
wait.until(EC.text_to_be_present_in_element((By.ID, "linkResponse"), "401"))
mensaje = driver.find_element(By.ID, "linkResponse").text
print(mensaje)


time.sleep(5)
driver.quit()