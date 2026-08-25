from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver = webdriver.Chrome()
driver.get("https://demoqa.com/upload-download")

wait = WebDriverWait(driver, 15)

# 1. Subir archivo
ruta_completa = os.path.abspath("elements/archivo_prueba.txt")
input_upload = driver.find_element(By.ID, "uploadFile")
input_upload.send_keys(ruta_completa)

# Verificar que se subio correctamente
mensaje = wait.until(EC.presence_of_element_located((By.ID, "uploadedFilePath"))).text
print("Archivo subido:", mensaje)

# 2. Descargar archivo (solo hacer click, la descarga la maneja el navegador)
boton_descarga = driver.find_element(By.ID, "downloadButton")
boton_descarga.click()

time.sleep(3)
driver.quit()