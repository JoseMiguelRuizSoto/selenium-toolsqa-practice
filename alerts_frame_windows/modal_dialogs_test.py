from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/modal-dialogs")

wait = WebDriverWait(driver, 15)

# Small modal
small = driver.find_element(By.ID, "showSmallModal")
small.click()
print("Contenido del Small modal:", driver.find_element(By.CLASS_NAME, "modal-body").text)
close_small = driver.find_element(By.ID, "closeSmallModal").click()

# Large modal
large = driver.find_element(By.ID, "showLargeModal")
large.click()
print("Contenido del Small modal:", driver.find_element(By.CLASS_NAME, "modal-body").text)
close_large = driver.find_element(By.ID, "closeLargeModal").click()

time.sleep(3)
driver.quit()