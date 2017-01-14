#! python3
# pw.py - An insecure password locker program

import sys
import pyperclip

PASSWORDS ={'email': 'thisismyemailpass',
            'blog': 'thisismyblogpass',
            'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]       # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to your clipboard')
else:
    print('There is no account ' + account)
