"""Generates a file for taking cclub minutes"""
import requests
import datetime
import os
import os.path

# The following block of code will obtain the current day, month, year, and time from the `datetime` library. It will also properly format the day to be postfixed with a "th", "st", "nd", or "rd".
TODAY = datetime.datetime.now()
MONTH_NAME = TODAY.strftime("%B")
MONTH = TODAY.month
if MONTH < 10:
    FILE_MONTH = "0{}".format(MONTH)
else:
    FILE_MONTH = "{}".format(MONTH)
DAY = TODAY.day
if DAY < 10:
    FILE_DAY = "0{}".format(DAY)
else:
    FILE_DAY = DAY
if 4 <= DAY <= 20 or 24 <= DAY <= 30:
    FORMAL_DAY = "{}th".format(DAY)
else:
    FORMAL_DAY = "{}{}".format(DAY, ["st", "nd", "rd"][DAY % 10 - 1])
YEAR = TODAY.year
HOUR = TODAY.strftime("%I")
MINUTE = TODAY.strftime("%M")
AMPM = TODAY.strftime("%p")
DAY_NAME = TODAY.strftime("%A")
# The following `try` will obtain the number of people present in the office along with their name if it has been registered with fish. It is always good to count the number of people, since not everyone is connected to the router. If there is not a connection to the router, an "x" will be given in place of the number of people.
try:
    REQUEST = requests.get("http://141.218.118.171:5001/json")
    PEOPLE = len(REQUEST.json()['registered'])+REQUEST.json()['others']
    PEOPLE_LIST = ", including: "  + ", ".join(REQUEST.json()['registered'])
except requests.exceptions.ConnectionError:   
    PEOPLE = "x"
    PEOPLE_LIST = ""

# This line properly formats the day for the file name.
FILENAME = "{}{}{}.md".format(YEAR, FILE_MONTH, FILE_DAY)

# This block generates the first couple of line, and puts some useful information such as the day, the people at the meeting, and the time. The data is then written to the notes file.
LINE1 = "# {} {}, {} Meeting Minutes".format(MONTH_NAME, FORMAL_DAY, YEAR)
LINE2 = "> Notes taken by Taylor in vim" # This line can be edited in order to fit the notes taker.
LINE3 = "> {} people in attendance{}".format(PEOPLE, PEOPLE_LIST)
LINE4 = "> {}:{} {}, On a {}, 2225 Kohrman Hall".format(HOUR.lstrip('0'), MINUTE, AMPM, DAY_NAME)
LINE5 = "### Topic"

def filecheck():
    """Checks if the file can be created and if it will overwrite an existing file."""
    if os.path.isfile(FILENAME) == True:
        print( "In this directory there is already a file for today's minutes. Proceed? (y, n, or o")
        print( "WARNING: THIS WILL DELETE THE CURRENT FILE")
        user_input = raw_input("> ")
        if user_input == "y":
            user_file = open(FILENAME, 'w+')
            user_file.write("{}\n{}\n\n{}\n\n{}\n\n{}\n".format(LINE1, LINE2, LINE3, LINE4, LINE5))
            user_file.close()
            """
            This line can be edited to open the editor of the user's choice. In order to open with the desired editor, just replace `emacsclient -nc` with a command to open your editor.
            """
            os.system("vim $argv {}".format(FILENAME))
        elif user_input == "n":
            quit()
        elif user_input == "o":
            os.system("vim -nc $argv {}".format(FILENAME)) # See above if you would like to change the text editor.
        elif user_input != "n" or user_input != "y" or user_input != "o":
            print ("Invalid input.")
            filecheck()
    elif os.path.isfile(FILENAME) == False:
        user_file = open(FILENAME, 'w+')
        user_file.write("{}\n{}\n\n{}\n\n{}\n\n{}\n".format(LINE1, LINE2, LINE3, LINE4, LINE5))
        user_file.close()
        os.system("vim $argv {}".format(FILENAME)) # See above if you would like to change the text editor.

filecheck()
