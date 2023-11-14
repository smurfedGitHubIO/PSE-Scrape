from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

# lst = ["Tick", "Tick Data Structure", "Trade Cancellation",]

driver.get("https://www.sgx.com/research-education/derivatives")
# button = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[4]/article/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download/widget-reports-derivatives-tick-and-trade-cancellation/div/sgx-input-select[1]/label/span[2]")
button = driver.find_element(By.CSS_SELECTOR, 'input[type="text"][class="sgx-input-control sgx-input-select-filter"][name="type"]')
# button = driver.find_element(By.NAME, 'type')
# button.send_keys("Tick Data Structure")

# button = WebDriverWait(driver, 10).until(
    # EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"][class="sgx-input-control sgx-input-select-filter"][name="type"]'))
# )
# button = driver.find_element(By.CSS_SELECTOR, 'span.sgx-icon--before.sgx-select-picker-label')
# driver.execute_script("arguments[0].value = 'Tick Data Structure';", button)
button.click()
button.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
button.send_keys(Keys.ENTER)
time.sleep(1)
button2 = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[4]/article/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download/widget-reports-derivatives-tick-and-trade-cancellation/div/button")
button2.click()

# dropdown1 = driver.find_element(By.CLASS_NAME, "sgx-input-select-filter-wrapper")
# print(dropdown1.get_attribute('value'))

# driver.quit()
