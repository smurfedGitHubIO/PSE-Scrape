from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.sgx.com/research-education/derivatives")
button = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[4]/article/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download/widget-reports-derivatives-tick-and-trade-cancellation/div/button")
button.click()

#driver.quit()
