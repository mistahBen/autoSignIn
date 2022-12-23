import time
# import getopt
# import sys
# import re
import argparse
from os.path import exists
import os
import csv
from selenium.webdriver import FirefoxOptions
from helium import *
from selenium.common.exceptions import NoSuchElementException as exElem
from env import SITE, domain
import logging


"""
Student batch sign-in

Requires:
Helium Python library (and Selenium), Firefox.
Make sure that Geckodriver (Firefox webdriver) has been exempted from apple quarantine with the following terminal command:

xattr -d com.apple.quarantine {path/to/driver}/geckodriver

Refer to the readme for further details.

"""
# default student_csv_name = "students.csv"
student_csv_name = "students.csv"

__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))
LIST =  os.path.join(__location__, student_csv_name )

# def_LIST = os.path.join(__location__, student_csv_name )

# arguments= argparse.ArgumentParser('')

# arguments.add_argument('-f', '--file', dest=LIST, default=def_LIST)


# if exists(LIST) is False:  # allow manual input
#     logging.warning("student list not found.")
#     print("students.csv file not found. You may manually input a student username and password or quit this script(ctrl+D), add a students.csv file and run it again.\n")
#     s = input("Student Number: ")
#     p = input("Password: ")
#     with open(LIST, 'w') as f:
#         f.write("Student_Number,Lunch_ID\n"+s+","+p)
#         logging.info('list %s created.', LIST)


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
    try:
        Text("locked").exists
        logging.ERROR(f'user {str(user)} reported as locked')
    except:
        pass
    try:
        Text("Couldn't find").exists
        logging.ERROR(f'user {str(user)} NOT FOUND in Google')
    except:
        pass
    time.sleep(3)
    
    
def checkGpage(user):
    try:
        click('I understand')
        logging.info(f"{user} accepted TOS")
    except:
        print("TOS page not found")

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


def main():
    
    with open(LIST, newline='') as f:
        reader = csv.reader(f)
        next(reader, None)
        for item, row in enumerate(reader,start=1):
            studID, pin = (row[0], row[1])
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
