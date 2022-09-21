import time
import re
from os.path import exists
import os
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from lib import config, elements

import pdb

"""
Student batch sign-in

Requires Google Chrome driver, selenium, and a list of student IDs and passwords.

*** PHOTO SENSITIVITY CAUTION ***
Some of the page actions occur very rapidly which creates some brief flickering. If this is an issue, you can adjust the wait times and sleep times in this script for longer intervals. You can also do other tasks or have other windows over the browser window.

To get selenium, run the following:
python3 -m pip install selenium

Refer to the readme for further details.

"""

__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))
LIST = os.path.join(__location__, "students.csv")
if exists(LIST) is False:  # allow manual input
    print("students.csv file not found. You may manually input a student username and password or quit this script(ctrl+D), add a students.csv file and run it again.\n")
    s = input("Student Number: ")
    p = input("Password: ")
    with open(LIST, 'w') as f:
        f.write("Student_Number,Lunch_ID\n"+s+","+p)


def driver_info():
    directory = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    s = Service(f"{directory}/chromedriver103") # 103 for chromium, 105 for current chrome install
    chromeOptions = Options()
    chromeOptions.add_argument("--allow-profiles-outside-user-dir")
    chromeOptions.binary_location=f"{directory}/Chromium.app/Contents/MacOS/Chromium"
    # chromeOptions.add_argument("--user-data-dir=/Users/alexanderb/Documents/GitHub/studentquicklookup/chromeProfile")
    chromeOptions.add_argument("--incognito")

    driver = webdriver.Chrome(service=s, options=chromeOptions)
    return driver


def sign_in(studID, PIN, driver):
    user = str('@'.join([studID, config.domain]))
    driver.implicitly_wait(4)

    if re.search('signinchooser', driver.current_url):
        driver.find_element_by_xpath(elements.g_email).click()
        driver.implicitly_wait(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[type='email']")))
    username = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
    username.send_keys(user)
    driver.implicitly_wait(4)
    username.send_keys(Keys.RETURN)
    time.sleep(2)
    # Microsoft page
    username2 = driver.find_element(By.NAME, 'loginfmt')
    # Microsoft sign in page
    username2.send_keys(user)
    username2.send_keys(Keys.RETURN)
    # if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
    #                                                                   "//*[@id='passwordError']"))):
    #     print("student "+user + " not able to sign in. proceeding")
    #     driver.close()
    #     pass
    time.sleep(2)
    userpass = driver.find_element(By.NAME, 'passwd')
    userpass.send_keys(PIN)
    driver.find_element(By.NAME, 'passwd').send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "idBtn_Back")))
    # decline microsoft 'remember sign-in'
    cancelbutton = driver.find_element(By.ID, "idBtn_Back")
    cancelbutton.click()
    time.sleep(2)
    
    # """begin Debug"""
    # pdb.set_trace()
   
#    #  verify = driver.find_element(By.TAG_NAME, 'h1').get_attribute('span')
#     if driver.find_element(By.XPATH, elements.g_confirm):
#         # if presented with "confirm it's you" message, click yes
#         driver.find_element(By.XPATH, elements.g_confirm_button).click()

    time.sleep(3)
    urlcheck = driver.current_url
    if re.search('gaplustos', urlcheck):
        WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.ID, 'confirm')))
        accept = driver.find_element(By.ID, 'confirm')
        accept.click()
    
    msg = "Last student submitted: "
    # report last student successfully logged in to stdout
    print(str(''.join([msg, studID])))
    time.sleep(2)

    # log out of account, clear cache
    driver.get("https://accounts.google.com/logout")
    driver.implicitly_wait(4)
    driver.get("chrome://settings/clearBrowserData")
    driver.implicitly_wait(4)
    driver.find_element(By.TAG_NAME, 'body').send_keys(
        Keys.TAB * 7, Keys.RETURN)
    driver.implicitly_wait(4)
    driver.get(config.SITE)


def main():

    driver = driver_info()
    executor_url = driver.command_executor._url
    session_id = driver.session_id
    print(executor_url, session_id)
    driver.get(config.SITE)

    with open(LIST, newline='') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            studID, PIN = (row[0], row[1])
            if PIN is str("0"):
                print(studID+" has no corresponding Lunch ID. Skipping...")
                pass
            else:
                sign_in(studID, PIN, driver)

        driver.close()


if __name__ == '__main__':
    main()
