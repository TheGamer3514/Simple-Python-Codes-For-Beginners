"""
fileread.py
This script opens a file and prints its contents to the console.
"""

f = open('other/file.txt', 'r') # must have a file named file.txt
file_contents = f.read()
print (file_contents)
f.close()
