#! python3
# filewrite.py - This program is an example of file read/write operation in Python

import os
import time

currentdir = os.getcwd()
pathexample = ('c:\\windows\\notepad.exe')


print('Current working directory')
currentdir = os.getcwd()
print(currentdir)
print('Changing directory...')
os.chdir('c:\\windows')
print('New Current working directory')
currentdir = os.getcwd()
print(currentdir)
print('Path handling...')
print(pathexample)
print('Directory name for current path (' + pathexample + ') is ' + os.path.dirname(pathexample))
print('Filename for current path (' + pathexample + ') is ' + os.path.basename(pathexample))
print('Splitting path into list tuple')                                     # there are 2 ways of doing this
pathparsed = (os.path.dirname(pathexample), os.path.basename(pathexample))  # first way
print(pathparsed)
pathparsed1 = os.path.split(pathexample)                                    # second way
print(pathparsed1)
print('Get size of file')
print(os.path.getsize(pathexample))
print('Check if file exists')
print(os.path.exists(pathexample))
print('List directory contents')
print(os.listdir(os.path.dirname(pathexample)))

directory = ('c:\\temp')
directoryfiles = os.listdir('c:\\temp')
totalSize = 0
for i in range(0, len(directoryfiles)):
    totalSize = (totalSize + os.path.getsize(os.path.join(directory, directoryfiles[i])))
print(str(totalSize) + ' bytes')
fileopen2 = open('c:\\temp\\test667.txt', 'a')
fileopen2.write(str(totalSize) + ' bytes\n')
totalSize = (totalSize / 1024)
print(str(float("{0:.2f}".format(totalSize))) + ' Kilobytes')
fileopen2.write((str(float("{0:.2f}".format(totalSize))) + ' Kilobytes\n'))
totalSize = (totalSize / 1024)
print(str(float("{0:.2f}".format(totalSize))) + ' Megabytes')
fileopen2.write((str(float("{0:.2f}".format(totalSize))) + ' Megabytes\n'))
totalSize = (totalSize / 1024)
print(str(float("{0:.2f}".format(totalSize))) + ' Gigabytes')
fileopen2.write((str(float("{0:.2f}".format(totalSize))) + ' Gigabytes\n'))
fileopen = open('c:\\temp\\test666.txt', 'w')
fileopen.write('This is a test')
fileopen.close()
fileopen = open('c:\\temp\\test666.txt', 'a')
fileopen.write('\n')
fileopen.close()
fileopen = open('c:\\temp\\test666.txt')
content = fileopen.read()
fileopen.close()
print(content)
