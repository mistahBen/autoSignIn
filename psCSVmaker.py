# Powerschool spreadsheet retriever

"""
A script to make getting student data from powerschool a little easier without requiring direct API calls.

"""
import time
from os.path import exists
import os
import csv
from datetime import datetime
from tkinter.ttk import Combobox
from selenium.webdriver import FirefoxOptions
from helium import *
import getpass
import keyring
from passlib.hash import bcrypt
import keyring.util.platform_ as keyring_platform

hasher = bcrypt.using(rounds=13)
NAMESPACE = "Powerschool"
    
class ENV:

    ps_site = 'district65.powerschool.com/admin'
    domain = '@district65.net'
    user = getpass.getuser()
    account = user+domain
    
class Security:
    
    ENTRY = getpass.getuser()
    def set_password():
        hasher = bcrypt.using(rounds=13)
        AUTH = getpass.getpass()
        keyring.set_password(NAMESPACE, Security.ENTRY, AUTH)
        h = hasher.hash(AUTH)
        print(h)
        print(f"Password for username {cred.username} in namespace {NAMESPACE} created.")

    cred = keyring.get_credential(NAMESPACE, ENTRY)

    
cred = Security.cred

if not (cred):
    Security.set_password()
    
print(keyring_platform.config_root()) # confirms keyring configured


__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))
LIST = os.path.join(__location__, "allstudents.csv")



## Helium webdriver options

driver = get_driver()
options = FirefoxOptions()
options.add_argument("-private")
options.add_argument("--width=800") # resolution set only to reduce crowding
options.add_argument("--height=600")


def google(user):
    write(user + "@district65.net")
    press(RETURN)
    if Text("locked").exists:
        logging.ERROR(f'user {user} reported as locked')
    if Text("Couldn't find").exists:
        logging.ERROR(f'user {user} NOT FOUND in Google')
    time.sleep(3)


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
        
def get_date():
    now = datetime.now()
    entry_date = now.strftime(r"%m/%d/%Y")
    return entry_date    
class ps:
    field_names = [Last_Name, First_Name, Student_Number, 
                   Lunch_ID, Grade_Level, SchoolID]
    
    def search(sLevel=0, eLevel=9, entry_date=get_date()):
        # grade levels should be between 0:8. date is m/d/yy format
        # sample: `Grade_level>-1;Grade_level<9;Enroll_status=0;entrydate>2/15/22`
        search_string = f'Grade_level>={sLevel};Grade_level=<{eLevel};Enroll_status=0;entrydate>{entry_date}'
        return search_string

    def get_report():
        quick_export_url = 'https://district65.powerschool.com/admin/importexport/exportstudents.html?dothisfor=selected'
        go_to(quick_export_url)
        for name in ps.field_names:
            write(f'{name}\n', into="tt")
        try:
            select(Combobox('fielddelim'),'comma')
        except:
            print('unable to select comma')
        try:
            select(Combobox('recddelim'),'CRLF')
        except:
            print('unable to select CRLF')
        click('Submit')
    
def main():
    user = Security.ENTRY
    Security.set_password()
    
    import pdb
    start_firefox(ENV.ps_site,options=options)
    go_to(ENV.ps_site)
    google(ENV.user)
    microsoft(ENV.user, cred)
    write(ps.search())
    click('search')
    write(ps.get_report())
    
                
if __name__ == '__main__':
    main()
