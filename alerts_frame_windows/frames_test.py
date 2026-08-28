from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://demoqa.com/frames")
wait = WebDriverWait(driver, 15)

# Iframe 1 - espera a que este disponible y cambia automaticamente
wait.until(EC.frame_to_be_available_and_switch_to_it("frame1"))
print("Iframe 1:", driver.find_element(By.TAG_NAME, "body").text)
driver.switch_to.default_content()

# Iframe 2
wait.until(EC.frame_to_be_available_and_switch_to_it("frame2"))
resultado2 = wait.until(EC.presence_of_element_located((By.ID, "sampleHeading"))).text
print("Iframe 2:", resultado2)
driver.switch_to.default_content()

time.sleep(3)
driver.quit()