from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/broken")

wait = WebDriverWait(driver, 15)

# Verificar la imagen
imagen = wait.until(EC.presence_of_element_located((By.XPATH, "//img")))
ancho_natural = driver.execute_script("return arguments[0].naturalWidth", imagen)

if ancho_natural == 0:
    print("La imagen esta ROTA (no cargo)")
else:
    print("La imagen carga correctamente")

# Verificar el link
link_roto = driver.find_element(By.XPATH, "//a[text()='Click Here for Broken Link']")
href = link_roto.get_attribute("href")
print("URL del link:", href)

time.sleep(3)
driver.quit()