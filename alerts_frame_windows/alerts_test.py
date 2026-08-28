from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")

wait = WebDriverWait(driver, 15)

# 1. Alert simple
driver.find_element(By.ID, "alertButton").click()
alerta = wait.until(EC.alert_is_present())
print("Alert simple - texto:", alerta.text)
alerta.accept()

# 2. Alert con timer 
driver.find_element(By.ID, "timerAlertButton").click()
alerta = wait.until(EC.alert_is_present())
print("Alert con timer - texto:", alerta.text)
alerta.accept()

# 3. Confirm alert 
driver.find_element(By.ID, "confirmButton").click()
alerta = wait.until(EC.alert_is_present())
print("Confirm alert - texto:", alerta.text)
alerta.accept()  # equivalente a click en "OK"
resultado_confirm = driver.find_element(By.ID, "confirmResult").text
print("Resultado del confirm:", resultado_confirm)

# 4. Prompt alert 
driver.find_element(By.ID, "promtButton").click()
alerta = wait.until(EC.alert_is_present())
print("Prompt alert - texto:", alerta.text)
alerta.send_keys("Jose Ruiz")
alerta.accept()
resultado_prompt = driver.find_element(By.ID, "promptResult").text
print("Resultado del prompt:", resultado_prompt)

time.sleep(3)
driver.quit()