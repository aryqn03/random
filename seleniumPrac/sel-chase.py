import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config as config

browser = webdriver.Chrome()
browser.get("https://secure.chase.com")

wait = WebDriverWait(browser, 20)

time.sleep(10)

username = wait.until(EC.presence_of_element_located((By.ID, "userId-text-input-field")))

username.send_keys(config.bank_user)

# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.jpui.input.logon-xs-toggle.clientSideError"))).send_keys("aryanj03")

# might get chase account locked for trying to breach sensitive info

input()