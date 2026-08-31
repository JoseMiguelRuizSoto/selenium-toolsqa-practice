from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/auto-complete")

wait = WebDriverWait(driver, 15)

# Multiple color
multiple_input = driver.find_element(By.ID, "autoCompleteMultipleInput")
for color in ["Blue", "Green", "Yellow"]:
    multiple_input.send_keys(color)
    multiple_input.send_keys(Keys.ENTER)
    time.sleep(0.5)

# Verificar que los colores se agregaron como tags
tags = driver.find_elements(By.CSS_SELECTOR, "[class*='multi-value__label']")
print(f"Colores agregados (multiple): {len(tags)}")
for tag in tags:
    print(" -", tag.text)

# Single color
single_input = driver.find_element(By.ID, "autoCompleteSingleInput")
single_input.send_keys("Red")
single_input.send_keys(Keys.ENTER)

time.sleep(1)

# Verificar el color unico seleccionado
valor_single = driver.find_element(By.ID, "autoCompleteSingleContainer").text
print("Color unico seleccionado:", valor_single)

time.sleep(3)
driver.quit()