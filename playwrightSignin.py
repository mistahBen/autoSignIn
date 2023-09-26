## A script to quickly run known usernames and passwords through initial sign up through Google/Microsoft Azure

from os.path import exists
import os
import time
import csv
import logging
from playwright.sync_api import sync_playwright
from lib import Config

google_url = Config.urls['google_auth']
domain = Config.user_domain

playwright = sync_playwright().start()
# Use playwright.chromium, playwright.firefox or playwright.webkit
# Pass headless=False to launch() to see the browser UI
browser = playwright.firfox.launch(headless=False)
page = browser.new_page()
page.goto(google_url)


## logging

logging.basicConfig(filename="auto-login.txt", filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)


# find and use CSV
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
options.add_argument("--width=1024")
options.add_argument("--height=768")



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
        nCounter=+1
        return nCounter
    except:
        print("TOS page not found")
    time.sleep(2)

  
def microsoft(user, password):
    write(user + "@district65.net",into='sign in')
    press(RETURN)
    time.sleep(2)
    write(password)
    press(RETURN)
    time.sleep(1)
    checkGpage(user)
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
                counter=+1
                print(f'Last student submitted: {studID} out of {counter} and {nCounter} new logins in this session.')
                kill_browser()
                
if __name__ == '__main__':
    main()
