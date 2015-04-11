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

import os
import re
import smtplib
import sys
import time


if len(sys.argv) > 1:
    try:
        folder, now = re.match(r'^(\w+)\/(\d{8})\.md$', sys.argv[1]).groups()
        folders = [folder]
        now = time.strptime(now, '%Y%m%d')
    except:
        print("Example usage: 'python mailer.py <folder>/<YYYYMMDD>.md'")
        exit()
else:
    folders = [name for name in os.listdir('.') if os.path.isdir(os.path.join('.', name))]
    now = time.localtime()

try:
    with open("mailing_list.txt", 'r') as f:
        emails = f.read().splitlines()
except:
    print("Error: could not find mailing list")

timestamp = time.strftime('%Y%m%d', now)
datestamp = time.strftime('%a, %b %d', now)
smtpObj = smtplib.SMTP('localhost')

for folder in folders:
    try:
        with open("%s/%s.md" % (folder, timestamp), 'r') as f:
            minutes = f.read()
    except:
        if len(sys.argv) > 1:
            print("Error: %s/%s.md not found" % (folder, timestamp))
        continue  # No minutes today

    title = "%s minutes" % folder.capitalize() if folder != 'minutes' else "Minutes"
    message = 'Subject: %s\n\n%s' % ("%s for %s" % (title, datestamp), minutes)

    try:
        smtpObj.sendmail("minutes@yakko.cs.wmich.edu", emails, message)
        if len(sys.argv) > 1:
            print("%s/%s.md mailed!" % (folder, timestamp))
    except:
        print("Error: unable to send email")
