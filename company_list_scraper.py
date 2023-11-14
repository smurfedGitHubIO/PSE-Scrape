import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
url = "https://edge.pse.com.ph/otherReports/form.do"

driver = webdriver.Chrome()
driver.get(url)

time.sleep(2)
agreeButton= driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/a")
agreeButton.click()
time.sleep(2)
typeMe = driver.find_element(By.ID, "tmplNm")
typeMe.send_keys("information statement")
time.sleep(2)
button = driver.find_element(By.ID, "btnSearch")
button.click()
## next step
## click all the links on the current page
# for i in range(50):
#findtable = driver.find_element(By.XPATH, f"/html/body/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/a")
#findtable.click()

## next next step
## get access to the next button something idk
