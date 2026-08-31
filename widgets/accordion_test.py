from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/accordian")

wait = WebDriverWait(driver, 15)

secciones = [
    "What is Lorem Ipsum?",
    "Where does it come from?",
    "Why do we use it?"
]

for titulo in secciones:
    boton = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[text()='{titulo}']")))

    # Solo hacer click si NO esta ya expandida (evita colapsar la primera por error)
    if boton.get_attribute("aria-expanded") == "false":
        driver.execute_script("arguments[0].scrollIntoView(true);", boton)
        driver.execute_script("arguments[0].click();", boton)
        time.sleep(1)

    contenido = driver.find_element(By.XPATH, f"//button[text()='{titulo}']/ancestor::div[@class='accordion-item']//div[@class='accordion-body']").text
    print(f"--- {titulo} ---")
    print(contenido[:100] + "...")

time.sleep(3)
driver.quit()