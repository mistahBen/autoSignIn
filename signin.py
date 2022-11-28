import time
# import getopt
# import sys
# import re
from os.path import exists
import os
import csv
from selenium.webdriver import FirefoxOptions
from helium import *
<<<<<<< Updated upstream
from selenium.common.exceptions import NoSuchElementException as exElem
from env import SITE, domain
=======
# from selenium.common.exceptions import NoSuchElementException as exElem
from lib import config, elements
import logging

### Logging settings

def log_level(level="INFO"):
    level = getattr(logging, level.upper())
    if not isinstance(level, int):
        raise ValueError('Invalid log level: %s' % level)
    return level

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', 
                    filename='batch_signin.log', encoding='utf-8', filemode='w', level=log_level())
>>>>>>> Stashed changes

"""
Student batch sign-in

Requires:
Helium Python library (and Selenium), Firefox.
Make sure that Geckodriver (Firefox webdriver) has been exempted from apple quarantine with the following terminal command:

xattr -d com.apple.quarantine {path/to/driver}/geckodriver

Refer to the readme for further details.

"""


__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))
LIST = os.path.join(__location__, "allstudents.csv")
if exists(LIST) is False:  # allow manual input
    logging.warning("student list not found.")
    print("students.csv file not found. You may manually input a student username and password or quit this script(ctrl+D), add a students.csv file and run it again.\n")
    s = input("Student Number: ")
    p = input("Password: ")
    with open(LIST, 'w') as f:
        f.write("Student_Number,Lunch_ID\n"+s+","+p)
        logging.info('list %s created.', LIST)


## Helium webdriver options
DRIVER = get_driver()
options = FirefoxOptions()
options.add_argument("-private")
options.add_argument("--width=800") # resolution set only to reduce crowding
options.add_argument("--height=600")

def google(user):
    go_to('accounts.google.com')
    write(user + "@district65.net")
    press(RETURN)
    if Text("locked").exists:
        logging.ERROR(f'user {user} reported as locked')
    if Text("Couldn't find").exists:
        logging.ERROR(f'user {user} NOT FOUND in Google')
    time.sleep(3)
    
    
def checkGpage(user):
    try:
        click('I understand')
        logging.info(f"{user} accepted TOS")
    except:
        print("TOS page not found")

<<<<<<< Updated upstream
=======
def acc_exc(user):
    try:
        Text("locked").exists
        logging.ERROR(f'user {user} reported as locked')
    except:
        pass
    try:
        Text("Couldn't find").exists
        logging.ERROR(f'user {user} NOT FOUND in Google')
    except:
        pass
    
>>>>>>> Stashed changes
def microsoft(user, password):
    write(user + "@district65.net",into='sign in')
    press(RETURN)
    time.sleep(2)
    write(password)
    press(RETURN)
    time.sleep(1)
<<<<<<< Updated upstream
    checkGpage(user)
    if Text("Stay signed in").exists():
        click("No")

## counters
counter=0
nCounter=0

=======
    try: 
        Text("Stay signed in").exists()
        click("No")
        logging.info('%s signed in', user)
    except:
        pass
>>>>>>> Stashed changes

def main():
    
    with open(LIST, newline='') as f:
        reader = csv.reader(f)
        next(reader, None)
        for item, row in enumerate(reader,start=1):
            studID, pin = (row[2], row[3])
            if pin is str("0"):
                print(studID+" has no corresponding Lunch ID. Skipping...")
                kill_browser()
            else:
                start_firefox(options=options)
                logging.info(DRIVER)
                google(studID)
                # acc_exc(studID)
                microsoft(studID, pin)
                checkGpage(studID)
                success_count = item
                print(f'Last student submitted: {studID}. {success_count} total entries in this session.')
                logging.info('%s students completed', success_count)
                kill_browser()
                
if __name__ == '__main__':
    main()
