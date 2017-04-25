# CCOWMU Minutes #

Stores all the cclub minutes in markdown for easy viewing.

### Goals ###
* Simplicity
* Automation
* Minimal user interaction

### Requirements ###
* Python 2.7.6 or greater
* sendmail
* Cron jobs
 * 30 23 \* \* \* cd /path/to/local/repo && git pull -q origin master
 * 40 23 \* \* \* cd /path/to/local/repo && ./mailer.py
 * 50 23 \* \* \* cp -n /path/to/local/repo/*.md /var/www/website/minutes/path/

### Instructions ###
* Click the create new file icon to the right of the repo name on this page
* Name as a markdown file with todays date in format YYYYMMDD.md
* Record meeting minutes with markdown syntax and click save
  * Refer to the markdown syntax cheat sheet below for formatting help
  * I also highly suggest running the minutes through the online syntax checker below if you are unfamiliar with markdown
  * Use the preview pane if you use the github web interface (if writing minutes via that)

The cron jobs will then pull the human readable minutes from this repo, email the human readable markdown language to users, and upload the minutes to the website where the markdown is translated and displayed as html.

### Reference ###
* [Markdown Syntax Cheatsheet](http://scottboms.com/downloads/documentation/markdown_cheatsheet.pdf)
* [Online Markdown Syntax Checker](http://www.markdownviewer.com/)
* [Github flavored markdown](https://help.github.com/articles/github-flavored-markdown)
* [cclub minutes repo wiki](https://github.com/ccowmu/minutes/wiki/publisher)
