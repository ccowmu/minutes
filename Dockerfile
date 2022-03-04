FROM python:3.8

ADD . .

RUN pip install mistune pdfkit
