"""
Student batch sign-in

Requires Google Chrome driver, selenium, and a list of student IDs and passwords.

*** PHOTO SENSITIVITY CAUTION ***
Some of the page actions occur very rapidly which creates some brief flickering. If this is an issue, you can adjust the wait times and sleep times in this script for longer intervals. You can also do other tasks or have other windows over the browser window.

To get selenium, run the following:
python3 -m pip install selenium==

Refer to the readme for further details.
<<<<<<< HEAD

test change
=======
"""
import os
import csv
import re
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


# set Chromedriver in local directory
directory = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))
s = Service(os.path.join(directory, 'chromedriver'))
driver = webdriver.Chrome(service=s)

executor_url = driver.command_executor._url
session_id = driver.session_id

print(executor_url, session_id)

SITE = "https://accounts.google.com/"
driver.get(SITE)


domain = "@district65.net"  # edit this for your specific needs

# open student csv
__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))
LIST = os.path.join(__location__, "students.csv")
with open(LIST, newline='') as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        # more humanlike interaction with random wait times for each login
        rand = random.randint(3, 10)
        studID, PIN = (row[0], row[1])
        emailaddr = {studID, domain}
        user = str(''.join(emailaddr))
        driver.implicitly_wait(4)

        # fill in username and hit the next button
        # this checks if at the 'choose a user' option
        if bool(re.search('signinchooser', driver.current_url)):
            driver.find_element_by_xpath(
                "//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[2]/div/div/div[2]").click()
            driver.implicitly_wait(1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[type='email']")))
        username = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        username.send_keys(user)
        driver.implicitly_wait(rand)
        username.send_keys(Keys.RETURN)
        time.sleep(2)
        # Microsoft page
        username2 = driver.find_element(By.NAME, 'loginfmt')
        # Microsoft sign in page
        username2.send_keys(user)
        username2.send_keys(Keys.RETURN)
        time.sleep(2)
        userpass = driver.find_element(By.NAME, 'passwd')
        userpass.send_keys(PIN)
        driver.find_element(By.NAME, 'passwd').send_keys(Keys.RETURN)
        # declin microsoft 'remember sign-in'
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "idBtn_Back")))
        cancelbutton = driver.find_element(By.ID, "idBtn_Back")
        cancelbutton.click()

        time.sleep(rand)
        verify = driver.find_element(By.TAG_NAME, 'h1').get_attribute('span')
        span = driver.find_element(
            By.XPATH, "//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div")
        if bool(span):
            # if presented with "confirm it's you" message, click yes
            driver.find_element(
                By.XPATH, "//*[@id='view_container']/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()

        time.sleep(3)
        urlcheck = driver.current_url
        if bool(re.search('gaplustos', urlcheck)):
            # print("speedbump detected") #debugging
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'button')))
            accept = driver.find_element(By.TAG_NAME, 'button')
            accept.click()
            driver.implicitly_wait(4)
            time.sleep(rand)
        msg = "Last student submitted: "
        laststudent = {msg, studID}
        # report last student successfully logged in to stdout
        print(str(''.join(laststudent)))
        time.sleep(3)

        # logout of account
        accounticon = driver.find_element(
            By.XPATH, "//*[@id='gb']/div[2]/div[3]/div[1]/div[2]/div/a")
        accounticon.click()
        driver.implicitly_wait(4)
        logout = driver.find_element(By.XPATH, "//*[@id='gb_71']")
        logout.click()
        driver.implicitly_wait(rand)
        # clear history so we can log in again
        driver.get("chrome://settings/clearBrowserData")
        driver.implicitly_wait(4)
        clearcache = driver.find_element(
            By.TAG_NAME, 'body').send_keys(Keys.TAB * 7, Keys.RETURN)
        driver.implicitly_wait(4)
        driver.get(SITE)

driver.close()
