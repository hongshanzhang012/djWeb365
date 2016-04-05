import urllib2
from os.path import exists
import pySendEmail
import re
import os
import psycopg2
#note that we have to import the Psycopg2 extras library!
import psycopg2.extras
import sys
import md5
import datetime

#run hourly from crontab
#crontab -e
#29 * * * * python /var/www/djWeb365/src/pyUrlCrawler.py

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def pyUrlCrawler():
    conn_string = "host='127.0.0.1' dbname='urlcrawler' user='postgres_nick' password='postgres_nick'"
    conn = psycopg2.connect(conn_string)

    # By specifying a name for the cursor, psycopg2 creates a server-side cursor
    cur1 = conn.cursor('cursor_unique', cursor_factory=psycopg2.extras.DictCursor)
    cur2 = conn.cursor()
    #"Register" to support table name in upper case
    cur1.execute('SELECT * FROM register_register') #appname is appended to tablename automatically
    
    while True:
        rows = cur1.fetchmany(2000)
    
        if not rows:
            break
    
        for row in rows:
            email=row[1]
            url=row[2]
            content_change=row[3]
            server_is_down=row[4]
            
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            newPage = response.read()
        
            #compare old_page and new_page
            lines=newPage.count('\n')
            if lines<=0: # server is down
                if server_is_down== True:
                    pySendEmail.sendEmail(email, url, False, True )
            elif content_change==True: #see if there is content_change
                m = md5.new()
                m.update(newPage)
                md5_new=m.hexdigest()
                
                #search table register_urlcontent
                cur2.execute('SELECT * FROM register_urlcontent WHERE url=%s', [url])
                data=cur2.fetchone()
                if not data: #new url, insert it into table rulcontent
                    cur3=conn.cursor()
                    cur3.execute("""INSERT INTO register_urlcontent VALUES (%s,%s,%s)""",[url, md5_new,datetime.datetime.now()])
                    cur3.close()
                elif data[2]!=md5_new: #content changed, should be data[1]
                    cur3=conn.cursor()
                    cur3.execute ("""
                       UPDATE register_urlcontent
                       SET md5=%s, modified=%s
                       WHERE url=%s
                        """, [md5_new, datetime.datetime.now(), url])
                    cur3.close()
                    pySendEmail.sendEmail(email, url, True, False )    
    cur1.close()
    cur2.close()
    try:
       conn.commit()
    except:
       conn.rollback()

    conn.close()
    return
    
if __name__ == "__main__":
    pyUrlCrawler()
    