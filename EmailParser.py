import sys
import imaplib
import email
import datetime
import EmailCredentials as ec

IMAP_HOST = 'imap.gmail.com'

def getLogin():
    userName = raw_input("Email address: ")
    password = raw_input()
    return 0

imap = imaplib.IMAP4_SSL(IMAP_HOST)
imap.login(ec.USER,ec.PWD)

status, data = imap.select('INBOX')

print data