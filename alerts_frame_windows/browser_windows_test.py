from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")

wait = WebDriverWait(driver, 15)

# New tab link
new_tab = wait.until(EC.element_to_be_clickable((By.ID, "tabButton")))
new_tab.click()

time.sleep(2)

driver.switch_to.window(driver.window_handles[1])
print("Titulo de la nueva pestaña:", driver.title)

driver.switch_to.window(driver.window_handles[0])

# New window
new_window = wait.until(EC.element_to_be_clickable((By.ID, "windowButton")))
new_window.click()

time.sleep(2)

driver.switch_to.window(driver.window_handles[2])
print("Titulo de la nueva pestaña:", driver.title)

driver.switch_to.window(driver.window_handles[0])

# NOTA: El boton "New Window Message" (messageWindowButton) causa un crash
# de la sesion de ChromeDriver al intentar leer el titulo/contenido de la
# ventana que abre. Se investigo: no es un alert, no es timing, no es un
# indice incorrecto de window_handles. Posible causante: un dialogo nativo
# del SO o comportamiento no estandar de esa ventana especifica.
# Pendiente de revisar en otro momento.


time.sleep(5)
driver.quit()