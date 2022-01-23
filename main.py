from imap_tools import MailBox, AND
from playsound import playsound
from config import *
from datetime import date

def ring ( ):
	while True:
		playsound ( SOUND, block = True )

# login to mail inbox
mailbox = MailBox ( HOST )
mailbox . login ( EMAIL, PASSWORD, "INBOX" )

while ( True ):
	# get mails date with subject 
	mails = [ msg . date for msg in mailbox . fetch ( AND ( subject = SUBJECT, from_=FROM ) ) ]
	
	# have mail 
	if len ( mails ) == 0:
		continue
	for i in mails:
		print ( i )

	# check if it is new mail
	if mails [ 0 ] . strftime ( "%Y-%m-%d" ) . startswith ( date . today ( ) . strftime ( "%Y-%m-%d" ) ):
		ring ( )

mailbox.logout()

