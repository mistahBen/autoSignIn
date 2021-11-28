import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
PATH = os.path.join(__location__, 'chromedriver')

driver = webdriver.Chrome(PATH)
driver.implicitly_wait(0.5)
SITE = "https://accounts.google.com"
driver.get(SITE)
driver.implicitly_wait(4)
textcheck = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
textcheck.send_keys("Input test. This window will close in 7 seconds.")
driver.implicitly_wait(7)
driver.close()
