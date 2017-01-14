#!python3
# twilio_example.py - Program that tests SMS functionality in Python using Twilio module
#

from twilio.rest import TwilioRestClient
accountSID = 'AC92f6ed5882d5f9a622b3891c61beb04c'
authToken = '992861d7bb1346acf7d65fdce12892c0'
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+18192011324'
myCellphone = input('enter the phone number you\'d like to send a text message: \n')
messagebody = input('please enter the message you want to send: \n')
message = twilioCli.messages.create(body=messagebody, from_=myTwilioNumber, to=myCellphone)

