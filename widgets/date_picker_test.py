from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/date-picker")

wait = WebDriverWait(driver, 15)

# Select date
driver.find_element(By.ID, "datePickerMonthYearInput").click()

month_select = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "react-datepicker__month-select")))
Select(month_select).select_by_visible_text("May")
Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")).select_by_visible_text("1999")
driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day.react-datepicker__day--010").click()

# Verificar el valor que quedo en el input
fecha_seleccionada = driver.find_element(By.ID, "datePickerMonthYearInput").get_attribute("value")
print("Fecha seleccionada:", fecha_seleccionada)

time.sleep(1)

# Select date & time
fecha_input = driver.find_element(By.ID, "dateAndTimePickerInput")
fecha_input.click()
fecha_input.send_keys(Keys.CONTROL, "a")
fecha_input.send_keys("May 10, 1999 10:15 AM")
fecha_input.send_keys(Keys.ENTER)

time.sleep(1)

fecha_hora_seleccionada = driver.find_element(By.ID, "dateAndTimePickerInput").get_attribute("value")
print("Fecha y hora seleccionada:", fecha_hora_seleccionada)

time.sleep(3)
driver.quit()