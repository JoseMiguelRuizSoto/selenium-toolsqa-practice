from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/buttons")

wait = WebDriverWait(driver, 15)

# Doble click
btn_double = wait.until(EC.element_to_be_clickable((By.ID, "doubleClickBtn")))
driver.execute_script("arguments[0].scrollIntoView(true);", btn_double)
time.sleep(1)
ActionChains(driver).double_click(btn_double).perform()
print(driver.find_element(By.ID, "doubleClickMessage").text) 

# Click derecho
btn_derecho = wait.until(EC.element_to_be_clickable((By.ID, "rightClickBtn")))
driver.execute_script("arguments[0].scrollIntoView(true);", btn_derecho)
time.sleep(1)
ActionChains(driver).context_click(btn_derecho).perform()
print(driver.find_element(By.ID, "rightClickMessage").text)

# Click me
btn_simple = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click Me']")))
driver.execute_script("arguments[0].scrollIntoView(true);", btn_simple)
time.sleep(1)
btn_simple.click()
print(driver.find_element(By.ID, "dynamicClickMessage").text)


time.sleep(5)

#parrafos = driver.find_elements(By.TAG_NAME, "p")
#print(f"Cantidad de <p> encontrados: {len(parrafos)}")
#for i, p in enumerate(parrafos):
    #print(f"[{i}] texto='{p.text}' visible={p.is_displayed()} id={p.get_attribute('id')}")

driver.quit()