from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

lst = ["Tick", "Tick Data Structure", "Trade Cancellation", "Trade Cancellation Data Structure"]

driver.get("https://www.sgx.com/research-education/derivatives")
# for i in range(4):
button = driver.find_element(By.NAME, 'date')
driver.execute_script(f"arguments[0].value = '01 Nov 2023';", button)
button2 = driver.find_element(By.XPATH, "./html/body/div[1]/main/div[4]/article/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download/widget-reports-derivatives-tick-and-trade-cancellation/div/button")
button2.click()

# dropdown1 = driver.find_element(By.CLASS_NAME, "sgx-input-select-filter-wrapper")
# print(dropdown1.get_attribute('value'))

driver.quit()
