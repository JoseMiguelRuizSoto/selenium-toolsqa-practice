from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/nestedframes")

wait = WebDriverWait(driver, 15)

# Entrar al frame padre
driver.switch_to.frame("frame1")
print("Contenido del frame padre:", driver.find_element(By.TAG_NAME, "body").text)

# Entrar al frame hijo (sin id/name, usamos indice 0)
driver.switch_to.frame(0)
print("Contenido del frame hijo:", driver.find_element(By.TAG_NAME, "body").text)

# Un solo comando vuelve directo a la pagina principal, sin importar la profundidad
driver.switch_to.default_content()

time.sleep(3)
driver.quit()