'''
Created on Jan 20, 2016

@author: nick
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import sys

#def sendEmail(to, gmail_user, gmail_pwd):
def sendEmail(to, url, content_change, server_is_down):
    gmail_user = "hongshanzhang012@gmail.com"
    gmail_pwd = 'gFromtj012'

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Activity detected in " + url
    msg['From'] = gmail_user
    msg['To'] = to

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\n \n Activity detected in the url: " + url + "\n"
    
    txt=""
    if content_change == True:
        txt=txt+"The content of the url you are monitoring has changed.\n"
        
    if server_is_down == True:
        txt=txt+"Warning! The server is down right now. \n"
        
    
    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi!<br>
           How are you?<br>
           Activity detected in the url you are monitoring: <br>
    """
    html=html+txt+"<br>"
    
    html=html+"<br> <a href="+url+">"+url+"</a>"
    html = html+"""\
         </p>
         </br>
         <p>Hongshan zhang</p>
      </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    smtpserver.sendmail(gmail_user, to, msg.as_string())
    smtpserver.close()

if __name__ == "__main__":
    sendEmail(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]) 
    