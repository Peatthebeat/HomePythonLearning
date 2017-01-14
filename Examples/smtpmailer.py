#!#python3
# smtpmailer.py - Program that tests SMTP functionality in Python
#

import smtplib

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpObj.ehlo()
smtpObj.login('pierrelucmorais@gmail.com', 'bjdqnbbrnkefvvpw')
smtpObj.sendmail('pierrelucmorais@gmail.com', 'vanessa.legault.beauregard@gmail.com', 'Subject: So Long\nDear Vanessa,\
 so long and thanks for all the fish.\nSincerely, \nPete\nXXOO')
smtpObj.quit()
