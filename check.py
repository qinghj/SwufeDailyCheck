from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time
import os

option = ChromeOptions()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')
option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_experimental_option('useAutomationExtension',False)
driver = webdriver.Chrome(options=option)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
    {'source':'Object.defineProperty(navigator,"webdriver",{get:(=>undefine}'})

name = os.environ['___NAME']
password = os.environ['___PWD']

driver.get("http://swufeapp.iswufe.info/jinzhi/index.php")

driver.find_element("xpath",'//*[@id="username"]').send_keys(name)
driver.find_element("xpath",'//*[@id="password"]').send_keys(password)
driver.find_element("xpath",'//*[@id="casLoginForm"]/p[4]/button').click()
driver.find_element("xpath",'//*[@id="middle-grid"]/div[1]/div').click()
time.sleep(1)
driver.find_element("xpath",'//*[@id="yirisanbao"]/div[13]').click()
time.sleep(1)
driver.find_element("xpath",'//*[@id="yirisanbao"]/button').click()
time.sleep(1)

driver.close()