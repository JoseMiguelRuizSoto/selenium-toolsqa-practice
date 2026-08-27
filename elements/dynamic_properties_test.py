from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")

wait = WebDriverWait(driver, 15)

# Botón Visible - verificar que NO existe al cargar la pagina
elementos_visible = driver.find_elements(By.ID, "visibleAfter")
print("Boton Visible existe al cargar la pagina:", len(elementos_visible) > 0)

# Botón Enable
boton_enable = driver.find_element(By.ID, "enableAfter")
print("Enable habilitado al cargar la pagina:", boton_enable.is_enabled())

enable = wait.until(EC.element_to_be_clickable((By.ID, "enableAfter")))
print("Enable habilitado despues de esperar:", enable.is_enabled())
enable.click()

# Botón Color
boton_color = driver.find_element(By.ID, "colorChange")
color_antes = boton_color.value_of_css_property("background-color")
print("Color antes:", color_antes)

time.sleep(6)

color_despues = boton_color.value_of_css_property("background-color")
print("Color despues:", color_despues)

# Botón Visible - verificar despues de esperar que aparezca
visible = wait.until(EC.visibility_of_element_located((By.ID, "visibleAfter")))
print("Boton Visible es visible despues de esperar:", visible.is_displayed())

time.sleep(3)
driver.quit()