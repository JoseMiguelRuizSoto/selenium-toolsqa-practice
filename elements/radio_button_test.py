from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/radio-button")

wait = WebDriverWait(driver, 15)

# Click en el radio button "Yes"
yes_radio = wait.until(EC.element_to_be_clickable((By.ID, "yesRadio")))
yes_radio.click()

# Verificar el resultado (aparece un mensaje "You have selected Yes")
resultado = driver.find_element(By.CLASS_NAME, "text-success").text
print(resultado)

time.sleep(3)

# Click en el radio button "Impressive"
impressive_radio = wait.until(EC.element_to_be_clickable((By.ID, "impressiveRadio")))
impressive_radio.click()

resultado2 = driver.find_element(By.CLASS_NAME, "text-success").text
print(resultado2)

time.sleep(3)
driver.quit()