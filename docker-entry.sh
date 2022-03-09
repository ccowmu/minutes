#!/bin/bash

read -p 'Relative path to markdown file: ' path

python3 mailer.py $path