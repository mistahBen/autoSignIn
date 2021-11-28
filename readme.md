# Google auto-signin

## setup info

Make sure you are running this in python3 and have selenium version 4.0.0 library. You will also need a csv of the userIDs and passwords you wish to use. You may append your list to the template csv (just rename it to students.csv).

    Edit the domain to the appropriate one for your accounts. (i.e. "school.edu")

It is strongly recommended to run "firstrun.py" script so you can jump through the MacOS access permissions for the Chrome webdriver. This has not been tested on Windows.

___
Purpose is to be able to get new student accounts fully authenticated and active with their Google services. While older students should be able to do this easily on their own, we find that doing this for elementary students removes an annoying barrier to using platforms like Clever.

When the script runs, a new Chrome session will start and enter text in the username window. Once it gets to the end of the list the chrome window closes

___
Known issues:
Given the unpredictability of network speeds, sometimes the script runs before a page has time to fully load the elements it is looking for which will cause it to crash.
The program outputs the last student succesfully signed-in to stdout so you can delete the completed entries and then run the script again.
