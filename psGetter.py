#Powerschool getter#
import os
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

if not cred:
    Security.set_password()
    
print(keyring_platform.config_root())


# DRIVER = get_driver()
# options = FirefoxOptions()
# options.add_argument("-private")
# options.add_argument("--width=800") # resolution set only to reduce crowding
# options.add_argument("--height=600")

# def go2Powerschool():
#     go_to(ps_site)
    
    
# def main():
#     start_firefox(options=options)
#     go2Powerschool()
    
# if __name__ = "__main__":
#     main()