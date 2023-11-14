import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyautogui

url = "https://edge.pse.com.ph/otherReports/form.do"

driver = webdriver.Chrome()
driver.get(url)

time.sleep(2)
agreeButton= driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/a")
agreeButton.click()
time.sleep(2)
typeMe = driver.find_element(By.ID, "tmplNm")
typeMe.send_keys("information statement")
# waitt = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "btnSearch"))).click()
time.sleep(2)
button = driver.find_element(By.ID, "btnSearch")
button.click()
## next step
## click all the links on the current page
# for i in range(50):
time.sleep(2)
findtable = driver.find_element(By.XPATH, f"/html/body/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/a")
findtable.click()

time.sleep(2)
#findCount = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/p[2]/label")
#print(findCount.text)
## /html/body/div[2]/div[2]/p[2]/select/ <- select last option

pyautogui.press(['alt', 'tab'])
pyautogui.press(['tab', 'down', 'tab', 'enter'])

# time.sleep(2)
# downloadButton = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/p[2]/a")
# downloadButton.click()
## /html/body/div[2]/div[2]/p[2]/a <- download button

## next next step
## get access to the next button something idk
