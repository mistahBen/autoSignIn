"""
A short script to run to get through all of the various alerts and security prompts to use the webdriver.
"""
from os.path import exists
import os
from selenium.webdriver import FirefoxOptions
from helium import *
from time import sleep

print("Initiating webdriver and checking for 'allstudents.csv' file... Once the browser launches, it will close automatically after 10 seconds.")


__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))
LIST = os.path.join(__location__, "allstudents.csv")
if exists(LIST) is False: 
    print("CAUTION: 'allstudents.csv' file not found. Be sure to create one or put it in this directory before running signin.py.\n")
    
driver = get_driver()
options = FirefoxOptions()
options.add_argument("-private")
options.add_argument("--width=800")
options.add_argument("--height=600")

start_firefox('bing.com', options=options)
sleep(10)
kill_browser()