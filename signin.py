import time
import re
from os.path import exists
import os
import csv
from selenium.webdriver import FirefoxOptions
from helium import *
from selenium.common.exceptions import NoSuchElementException as exElem
from lib import config, elements

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
    print("students.csv file not found. You may manually input a student username and password or quit this script(ctrl+D), add a students.csv file and run it again.\n")
    s = input("Student Number: ")
    p = input("Password: ")
    with open(LIST, 'w') as f:
        f.write("Student_Number,Lunch_ID\n"+s+","+p)


## Helium webdriver options
driver = get_driver()
options = FirefoxOptions()
options.add_argument("-private")
options.add_argument("--width=800") # resolution set only to reduce crowding
options.add_argument("--height=600")



def google(user):
    go_to('accounts.google.com')
    write(user + "@district65.net")
    press(RETURN)
    
    time.sleep(3)
    
    
def checkGpage(user):
    try:
        click('I understand')
        logging.info(f"{user} accepted TOS")
        nCounter=+1
        return nCounter
    except:
        print("TOS page not found")
    time.sleep(2)

def acc_exc(user):
    if Text("locked").exists:
        logging.ERROR(f'user {user} reported as locked')
    if Text("Couldn't find").exists:
        logging.ERROR(f'user {user} NOT FOUND in Google')
        
def microsoft(user, password):
    write(user + "@district65.net",into='sign in')
    press(RETURN)
    time.sleep(2)
    write(password)
    press(RETURN)
    time.sleep(1)
    if Text("Stay signed in").exists():
        click("No")

## counters
counter=0
nCounter=0
## 


def main():
    
    with open(LIST, newline='') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            start_firefox(options=options)
            driver
            studID, pin = (row[2], row[3])
            # studID, PIN = (row[0], row[1])
            if pin is str("0"):
                print(studID+" has no corresponding Lunch ID. Skipping...")
                kill_browser()
                pass
            else:
                google(studID)
                acc_exc(studID)
                microsoft(studID, pin)
                # pdb.set_trace()
                checkGpage(studID)
                counter=+1
                print(f'Last student submitted: {studID} out of {counter} and {nCounter} new logins in this session.')
                kill_browser()
                
if __name__ == '__main__':
    main()
