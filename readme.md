# Google auto-signin with Helium

### Use case:
We have a lot of young students, and many platforms (particularly Clever) may present glitches or errors when trying to use those platforms to access various apps or services if the account has not completed a first sign-in. This Python script takes a list of usernames and passwords and can rapidly go through the tedious user sign-in process. This script is written to move through a Google/Azure user sign-in process, but could easily be altered to access other sites for signing in.

## setup info
requires the helium python package as well as the geckodriver for Firefox (as well as firefox itself). Firefox is the preferred browser because it does not have the more stringent user profile requirements of other browsers and is also widely available across operating systems.

It is strongly recommended to run "firstrun.py" script so you can jump through the MacOS access permissions for the Gecko webdriver for Firefox.

___

When the script runs, a new browser session will start and sign in over and over, iterating over a csv file the user needs to set up before running the program.
