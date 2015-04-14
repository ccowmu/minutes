#!/usr/bin/python

'''
Computer Club of WMU Markdown Publishing System
by cpg

This is a module that can be used to process any computer club documentation 
from markdown to one of the following formats:
- HTML with simple, built-in CSS
- Plain HTML
- PDF
- PNG? This would be for a flat, poster-style graphic
'''

import mistune
import pdfkit
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def from_file(filename):
    ''' Gets the text from a file. If the file isn't found, return an empty 
        string. '''

    # Start with a default empty output string.
    source = ""
    
    # Try to read the file.
    try:
        with open(filename, 'r') as source_file:
            source = source_file.read()
    except:
        # Continue to use the empty string.
        print "%s not found." % filename

    return source

def to_file(source, filename):
    ''' Writes given text to a file. '''
    try:
        with open(filename, 'w') as destination_file:
            destination_file.write(source)
    except:
        print "Could not write to %s." % filename

def md_to_html(source_md):
    ''' Basic function for getting the HTML source for a string. '''
    return mistune.markdown(source_md)

def md_to_html_document(source_md, source_css=None):
    ''' Turns Markdown syntax and CSS into an HTML document. This is useful 
        for sending emails. '''
    return '<!DOCTYPE html>\n<html>%s<body>%s</body></html>' % (md_to_html(source_md), get_html_head(source_css=source_css))

def css_to_html_tag(source_css):
    ''' Gets an HTML tag for inline CSS formatting from some basic CSS. '''
    return '<style type="text/css">%s</style>' % source_css

def html_to_pdf_file(source_html, output_pdf_filename, source_css_filename=None):
    ''' Writes HTML/CSS to a PDF file. 
        Uses one CSS file for simplicity. This is passed on as a single item 
        list. 
        The path given for the PDF is returned. '''
    if source_css_filename is not None:
        pdfkit.from_string(source_html, output_pdf_filename, 
            css=source_css_filename)
    else:
        pdfkit.from_string(source_html, output_pdf_filename)

    return output_pdf_filename 

def md_to_html_email(source_md, source_css=""):
    ''' Puts HTML (assuming with inline CSS if necessary) into an email 
        message object. You will need to add subject, sender, and recipient 
        information to the email object before sending with smtplib. '''

    # Create multipart/alternative message.
    message = MIMEMultipart('alternative')
    
    # Create the parts of the email.
    email_part_plain = MIMEText(source_md, 'plain')
    email_part_html = MIMEText(md_to_html_document(source_md, source_css), 'html')

    # Attach the parts. The last one will be preferred.
    message.attach(email_part_plain)
    message.attach(email_part_html)

    # Return a flattened email message string for use with smtplib.
    return message

def pdf_file_to_pdf_attachment(source_pdf_filename):
    ''' Takes a path to a PDF file and creates an attachment for an email
        message. '''

    # Open the PDF in binary mode.
    with open(source_pdf_filename, 'rb') as pdf_file:
        # Create a PDF message.
        pdf_attachment = MIMEBase('application', 'pdf')
        pdf_attachment.set_payload(pdf_file.read())
        encoders.encode_base64(pdf_attachment)
        pdf_attachment.add_header('Content-Disposition', 'attachment',
            filename=os.path.basename(source_pdf_filename))
        # Return the attachment for an email message possibly generated from
            # md_to_html_email.
        return email_message

def get_html_head(title="", source_css=None):
    ''' Create an HTML head given some parameters. '''
    # Return a head tag. If there is CSS, make a style tag.
    return '<head>\n<title>%s</title>\n%s</head>' % (title, css_to_html_tag(source_css) if source_css is not None else "")
