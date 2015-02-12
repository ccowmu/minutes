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
import smtplib

timestamp = time.strftime('%Y%m%d', time.localtime())
datestamp = time.strftime('%a, %b %d', time.localtime())

with open("mailing_list.txt", 'r') as f:
    emails = f.read().splitlines()

try:
    with open("minutes/%s.md" % str(timestamp), 'r') as f:
        minutes = f.read()
except:
    # No minutes today
    exit()

message = 'Subject: %s\n\n%s' % ("Minutes for %s" % str(datestamp), minutes)

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail("minutes@yakko.cs.wmich.edu", emails, message)
except:
    #print("Error: unable to send email")
    pass
