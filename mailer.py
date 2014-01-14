#!/usr/bin/python

'''
CCOWMU Minute Mailer
This simple script is to mail the minutes after each meeting.
Please set the following:
  Minutes path
  Minutes file naming convention
Please set this script to run in cron
  -Recommended: daily at 11pm
'''

import time
import os
import smtplib

timestamp = time.strftime('%Y%m%d', time.localtime())
datestamp = time.strftime('%a, %b %d', time.localtime())

# Mail all on system
#with os.popen('cat /etc/passwd | grep -e "/home" | grep -v "/bin/false" | grep -Eo "[^,]+?@[^:]+"') as f:
#  emails = f.readlines()
#with open("../do_not_contact.txt", 'w') as f:
#  dnc = f.readlines()
#emails = [email for email in emails if email not in dnc]

# Mail specified
with open("../mailing_list.txt", 'r') as f:
  emails = f.readlines()

try:
  with open("%s.md" % str(timestamp), 'r') as f:
    minutes = f.read()
except:
  # No minutes today
  exit()

message = 'Subject: %s\n\n%s' % ("Minutes for %s" % str(datestamp), minutes)

try:
  smtpObj = smtplib.SMTP('localhost')
  smtpObj.sendmail("minutes@ccowmu.org", emails, message)
except:
  #print("Error: unable to send email")
  pass
