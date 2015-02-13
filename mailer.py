#!/usr/bin/python

'''
CCOWMU Minute Mailer
This simple script is to mail the minutes after each meeting.
Please set the following:
    Minutes path
    Minutes file naming convention
Please set this script to run once daily in cron
    -Recommended: 11pm
'''

import time
import re
import smtplib
import sys


when = time.localtime()

if len(sys.argv) == 2:
    if re.match(r'^\d{8}$', sys.argv[1]):
        when = time.strptime(sys.argv[1], '%Y%m%d')
    else:
        print("Input Error: use 'python mailer.py YYYYMMDD' for a specific date")

timestamp = time.strftime('%Y%m%d', when)
datestamp = time.strftime('%a, %b %d', when)

with open("mailing_list.txt", 'r') as f:
    emails = f.read().splitlines()

try:
    with open("minutes/%s.md" % str(timestamp), 'r') as f:
        minutes = f.read()
except:
    if len(sys.argv) == 2:
        print("Error: %s.md not found" % str(timestamp))
    exit()

message = 'Subject: %s\n\n%s' % ("Minutes for %s" % str(datestamp), minutes)

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail("minutes@yakko.cs.wmich.edu", emails, message)
    if len(sys.argv) == 2:
        print("Minutes mailed!")
except:
    if len(sys.argv) == 2:
        print("Error: unable to send email")
