#! python3
# shutil_example.py - Examples of shutil lib file manipulations

import shutil
import os
os.chdir('c:\\temp')

# Creating a directory
if not os.path.exists('c:\\temp\\crepes') and not os.path.isdir('c:\\temp\\crepes'):
    os.mkdir('c:\\temp\\crepes')
os.chdir('c:\\temp\\crepes')
# Copying a file
if not os.path.exists('.\\test.txt') and not os.path.isfile('.\\test.txt'):
    shutil.copy('..\\test.txt', '.\\')
print(os.listdir('c:\\temp\\crepes'))

# Copying a folder and its subdirectory
if not os.path.exists('d:\\backup\\Tools_backup'):
    shutil.copytree('c:\\Tools', 'd:\\backup\\Tools_backup')

# Moving a file (can rename as well, use same code)
if os.path.exists('c:\\temp\\test.txt'):
    if os.path.exists('c:\\temp\\crepes'):
        shutil.move('c:\\temp\\test.txt', 'c:\\temp\\crepes\\test_new.txt')

# Listing a directory tree
for folderName, subfolders, filenames in os.walk('c:\\temp\\crepes'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('Subfolder of ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('File inside ' + folderName + ': ' + filename)

# Zip file manipulation possible also
