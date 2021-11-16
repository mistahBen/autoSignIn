readme/setup info

Purpose is to be able to get new student accounts fully authenticated and active with their Google services. While older students should be able to do this easily on their own. We find that doing this for Kindergarteners removes an annoying barrier to using platforms like Clever.

Run scripts in python3 (not python)

Setup:
1. in terminal type:
python3 -m pip install selenium==4.0.0

this should install selenium for your version of python3


2. Next run "firstrun.py" script so you can jump through the MacOS access permissions for the Chrome webdriver.
When run successfully a new Chrome session will start and enter text in the username window.

csv should be in userID,Lunch_PIN format with no header row.
You can get lists of those by exporting from powerschool.
    Get a list of students (grade level building searches work best), then click "quick export" and choose "Student_Number" and "Lunch_ID"

    Set the delimiter to comma, click "submit" to get the .txt file. then rename to "students.csv"

    Put the csv file into the directory where this script is run.


    a quick way to do this (if you're in the directory of the student export folder):
    $: mv $HOME/Downloads/student.export.text /directory/of/signin/students.csv

Known issues:
I have tried to make this script run as quickly as possible, but sometimes a page will take a second or 2 longer to load which will trip up the script and cause it to stop/crash.
The script prints out the last student ID entered in the "last.txt" file in the directory. Find that student and then delete any students before that one. Save the csv and run the script again.
