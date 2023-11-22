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

## /html/body/div[2]/div[2]/p[2]/select/ <- select last option
for handle in driver.window_handles:
    print(handle)
    driver.switch_to.window(handle)
time.sleep(2)
findCount = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/p[2]/label")
attachmentCount = findCount.text
counter = int(attachmentCount[attachmentCount.find('(')+1:-1])
# pyautogui.press(['alt', 'tab'])
# time.sleep(15)
for i in range(counter):
    time.sleep(2)
    select = driver.find_element(By.ID, "file_list")
    select.click()
    for i in range(int(findCount.text[-2])):
        select.send_keys(Keys.DOWN)
        time.sleep(2)
    select.click()
    time.sleep(2)
    # time.sleep(2)
    downloadButton = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/p[2]/a")
    downloadButton.click()
    time.sleep(20)
    downloadButton.send_keys(Keys.ESCAPE)
    time.sleep(1)
    for i in range(9):
        time.sleep(1)
        downloadButton.send_keys(Keys.TAB)
## /html/body/div[2]/div[2]/p[2]/a <- download button
# driver.quit()
## next next step
## get access to the next button something idk
## tomorrow na to