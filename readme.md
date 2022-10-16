# Google auto-signin

## setup info
requires the helium python package as well as the geckodriver for Firefox (as well as firefox itself).

It is strongly recommended to run "firstrun.py" script so you can jump through the MacOS access permissions for the Gecko webdriver for Firefox. This script recommends using Firefox as Chrome has complicating 'profile' requirements.

___
Purpose is to be able to get new student accounts fully authenticated and active with their Google services. While older students should be able to do this easily on their own, we find that doing this for elementary students removes an annoying barrier to using platforms like Clever.

When the script runs, a new browser session will start and sign in over and over, iterating over a csv file the user needs to set up before running the program.
