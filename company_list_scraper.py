import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
url = "https://edge.pse.com.ph/otherReports/form.do"

driver = webdriver.Chrome()
driver.get(url)
typeMe = driver.find_element(By.ID, "tmplNm")
typeMe.send_keys("information statement")
button = driver.find_element(By.ID, "btnSearch")
button.click()
