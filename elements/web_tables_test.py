from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/webtables")

wait = WebDriverWait(driver, 15)

# Verificacion rapida: confirmar que el boton "Add" existe antes de seguir
add_buttons = driver.find_elements(By.ID, "addNewRecordButton")
print(f"Botones 'Add' encontrados: {len(add_buttons)}")

# Click en "Add" para abrir el formulario
add_button = wait.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton")))
add_button.click()

# Llenar el formulario del modal
wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys("Jose")
driver.find_element(By.ID, "lastName").send_keys("Ruiz")
driver.find_element(By.ID, "userEmail").send_keys("ruiz.josemiguel@gmail.com")
driver.find_element(By.ID, "age").send_keys("25")
driver.find_element(By.ID, "salary").send_keys("1500000")
driver.find_element(By.ID, "department").send_keys("QA Automation")

# Enviar el formulario
driver.find_element(By.ID, "submit").click()

time.sleep(3)

#with open("debug_webtables.html", "w", encoding="utf-8") as f:
    #f.write(driver.page_source)
# Verificar que el nuevo registro aparecio en la tabla
tabla = driver.find_element(By.TAG_NAME, "tbody").text
print(tabla)

time.sleep(5)
driver.quit()