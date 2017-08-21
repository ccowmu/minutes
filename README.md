# CCOWMU Minutes #

Stores all the cclub minutes in markdown for easy viewing.

### Goals ###
* Simplicity
* Automation
* Minimal user interaction

### Requirements ###
* Python 2.7.6 or greater
* sendmail
* Cron jobs:
```
30 23 * * * cd /path/to/local/repo && git pull -q origin master
40 23 * * * cd /path/to/local/repo && ./mailer.py
50 23 * * * cp -n /path/to/local/repo/*.md /var/www/website/minutes/path/
```

### Instructions ###

#### Browser ####

* Click the create new file icon to the right of the repo name on this page
* Name as a markdown file with todays date in format YYYYMMDD.md
* Record meeting minutes with markdown syntax and click save
  * Refer to the markdown syntax cheat sheet below for formatting help
  * I also highly suggest running the minutes through the online syntax checker below if you are unfamiliar with markdown
  * Use the preview pane if you use the github web interface (if writing minutes via that)

#### Vim ####

With some configuration, Vim can check for spelling and grammar mistakes,
and make viewing the rendered markdown simpler.

Edit your `~/.vimrc` file, and add the following lines:
```viml
" Markdown
syntax on
au BufRead,BufNewFile *.md setl filetype=markdown spell
au FileType markdown noremap <buffer> <Leader>r :!grip -b "%"<cr>
```

The first two lines will ensure syntax highlighting and spell checking is
enabled for `.md` files.

The third line relies on a program called `grip` to render the markdown and
display it in your browser. To install `grip` (assuming you have python
already) run:
```
pip install grip
```

Now, while editing the markdown file, simply use the normal-mode command `\r`.
A browser tab should open with the rendered markdown. When you are finished
previewing, close the tab, return to vim, and close `grip` by pressing `ctrl-c`
and enter.

### Explanation ###

The cron jobs will pull the human readable minutes from this repo, email the
human readable markdown language to users, and upload the minutes to the
website where the markdown is translated and displayed as html.

### Reference ###
* [Markdown Syntax Cheatsheet](http://scottboms.com/downloads/documentation/markdown_cheatsheet.pdf)
* [Online Markdown Syntax Checker](http://www.markdownviewer.com/)
* [Github flavored markdown](https://help.github.com/articles/github-flavored-markdown)
* [cclub minutes repo wiki](https://github.com/ccowmu/minutes/wiki/publisher)
* [grip markdown previewer](https://github.com/joeyespo/grip)
