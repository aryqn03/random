
import config as config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
import time

browser = webdriver.Chrome()
browser.get('https://robinhood.com/login')

wait = WebDriverWait(browser, 10)

username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
password = wait.until(EC.presence_of_element_located((By.NAME, "password")))

username.send_keys(config.rbh_user)
password.send_keys(config.rbh_pass)


button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.web-app-emotion-cache-316ztu')))
button.click()

time.sleep(10)

browser.find_element(By.XPATH, "/html/body/div/div/div[1]/button").click()

input()