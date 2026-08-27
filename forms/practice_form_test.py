from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

wait = WebDriverWait(driver, 15)

# --- Campos de texto simples
driver.find_element(By.ID, "firstName").send_keys("Jose")
driver.find_element(By.ID, "lastName").send_keys("Ruiz")
driver.find_element(By.ID, "userEmail").send_keys("ruiz.josemiguel@gmail.com")

# --- Radio button de genero 
genero_male = driver.find_element(By.XPATH, "//label[text()='Male']")
driver.execute_script("arguments[0].click();", genero_male)

# --- Telefono ---
driver.find_element(By.ID, "userNumber").send_keys("9123456789")

# --- Fecha de nacimiento 
driver.find_element(By.ID, "dateOfBirthInput").click()
Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")).select_by_visible_text("May")
Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")).select_by_visible_text("1999")
driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--015:not(.react-datepicker__day--outside-month)").click()

# --- Subjects 
subjects_input = driver.find_element(By.ID, "subjectsInput")
subjects_input.send_keys("Maths")
subjects_input.send_keys(Keys.ENTER)

# --- Hobbies
hobby_reading = driver.find_element(By.XPATH, "//label[text()='Reading']")
driver.execute_script("arguments[0].click();", hobby_reading)

# --- Upload de fotos
ruta_foto = os.path.abspath("elements/archivo_prueba.txt")
driver.find_element(By.ID, "uploadPicture").send_keys(ruta_foto)

# --- Direccion ---
driver.find_element(By.ID, "currentAddress").send_keys("Santiago, Chile")

# Estado y Ciudad
state_dropdown = driver.find_element(By.ID, "state")
driver.execute_script("arguments[0].scrollIntoView(true);", state_dropdown)
time.sleep(1)
state_dropdown.click()

time.sleep(1)  

opciones = driver.find_elements(By.CSS_SELECTOR, "div[id^='react-select']")
for op in opciones:
    print("Opcion encontrada:", op.text)

driver.find_element(By.XPATH, "//div[text()='NCR']").click()

city_dropdown = driver.find_element(By.ID, "city")
driver.execute_script("arguments[0].scrollIntoView(true);", city_dropdown)
time.sleep(1)
city_dropdown.click()  # click normal, igual que hicimos con state
time.sleep(1)
driver.find_element(By.XPATH, "//div[text()='Delhi']").click()

# --- Enviar formulario ---
driver.find_element(By.ID, "submit").click()
driver.save_screenshot("debug_submit.png")

# --- Verificar que aparecio el modal de confirmacion ---
modal_titulo = wait.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))).text
print("Modal de confirmacion:", modal_titulo)

time.sleep(5)
driver.quit()