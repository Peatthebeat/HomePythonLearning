#! python3
# password_walk.py - A program that walks all drives and extracts plain text passwords out of the files
#
#
import os
import re
import string
from ctypes import windll
import shutil
import zipfile
import logging
from time import gmtime,strftime

print(strftime("%Y-%m-%d_%H-%M-%S", gmtime()))

logging.basicConfig(filename='c:\\temp\\passfile\\log.txt', level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.info('start of program')
# logfileinput = open('c:\\temp\\passfile\\test.txt')
# Example of a subprocess output that could be added to the log file
for lines in (open('c:\\temp\\passfile\\test.txt')):
    logging.warning(lines.rstrip())


# List available drives from my computer
def get_drives():
    print('Listing available drives on this system...')
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    logging.info('Got following drive from get_drives:')
    logging.info(drives)
    return drives
availdrives = (get_drives())


# drive walk for txt files
def txtfilescan(drive):
    print('Now scanning drive ' + drive + ':\\ and subdirectories for text files...')
    txtfiles = open('c:\\temp\\passfile\\textfilesindrive' + drive +'.txt', 'w')
    for folderName, subfolders, filenames in os.walk(drive + ':\\'):
        for subfolder in subfolders:
            for filename in filenames:
                if filename.endswith('txt'):        # TODO other filetypes as well (doc, docx, xls, xlsx, pdf etc.)
                    fullfilename = (folderName + '\\' + filename)
                    if os.path.getsize(fullfilename) <= 10000:
                        txtfiles.write(folderName + '\\' + filename + '\n')
    txtfiles.close()

pattern = {'pass', 'password', 'p/w', 'mot de passe', 'mdp', 'contrasena', 'pw'}
# TODO search text files for 'pattern'
# TODO list text files lines that contains 'pattern'
# TODO upgrade list re.match with pattern (now hard coded but needs an input)
# C drive textfile pattern scanning


def passfilescan(drive):
    print('Scanning file list in c:\\temp\\passfile\\textfilesindrive' + drive + '.txt for password strings...')
    textfile = open('c:\\temp\\textfilesindrive' + drive + '.txt', 'r')
    textfile = [i.replace('\n', '') for i in textfile]   # remove the new line caracter from list
    passfile = open('c:\\temp\\passfile\\' + drive + '\\passfilelist' + drive + '.txt', 'w')
    for lines in textfile:
        if lines != ('c:\\Temp\\passfile\\' + drive + '\\passfilelist' + drive + '.txt'):
            try:
                txttosearch = open(lines, 'r')
                for txttodisplay in txttosearch:
                    if re.match('(.*)(P|p)(A|a)(S|s)(S|s)(.*)', txttodisplay) or \
                            re.match('(.*)(P|p)(A|a)(S|s)(S|s)(W|w)(O|o)(R|r)(D|d)(.*)', txttodisplay) or \
                            re.match('(.*)(M|m)(O|o)(T|t) (D|d)(E|e) (P|p)(A|a)(S|s)(S|s)(E|e)(.*)', txttodisplay) or\
                            re.match('(.*)(M|m)(D|d)(P|p)', txttodisplay):
                        passfile.write(lines + '\n' + txttodisplay)
                        #print(lines + '\n' + txttodisplay)
                txttosearch.close()
            except UnicodeDecodeError:      # I think this is for accent in french that generates an error
                continue
def copypassfiles(drive):       # creates tree from drive that contains the text files
    workingdir = ('c:\\temp\\passfile\\' + drive)
    passfile = open(workingdir + '\\passfilelist' + drive + '.txt', 'r')
    passfile = [i.replace('\n', '') for i in passfile]  # remove the new line caracter from list
    if not os.path.exists(workingdir):
        os.mkdir(workingdir)
        os.chdir(workingdir)
    else:
        os.chdir(workingdir)
    for files in passfile:
        if re.match((r'[A-Za-z].\\(.*)'), files):
            dirtocopy = (workingdir + os.path.dirname(files[2:]))
            if not os.path.exists(dirtocopy):
                print(dirtocopy)
                os.makedirs(dirtocopy)
                os.chdir(dirtocopy)
                shutil.copy(files, '.')
                os.chdir(workingdir)
            else:
                print(dirtocopy)
                os.chdir(dirtocopy)
                shutil.copy(files, '.')
                os.chdir('c:\\temp\\passfile')
# TODO zip text files in archive current directory
def zippassfile(drive):
    workingdir = ('c:\\temp\\passfile\\' + drive)
    os.chdir(workingdir)
    passfile = open('c:\\temp\\passfilelist' + drive + '.txt', 'r')
    passfile = [i.replace('\n', '') for i in passfile]  # remove the new line caracter from list
    filezip = zipfile.ZipFile('.\\zipfile' + drive + '.zip', 'w')
    for files in passfile:
        if re.match((r'[A-Za-z].\\(.*)'), files):
            filezip.write(files, compress_type=zipfile.ZIP_DEFLATED)
    filezip.close()
# TODO scan for USB removable stick and move zip file in it
# Main block
for drive in availdrives:
    txtfilescan(drive)
    passfilescan(drive)
    copypassfiles(drive)
    zippassfile(drive)
