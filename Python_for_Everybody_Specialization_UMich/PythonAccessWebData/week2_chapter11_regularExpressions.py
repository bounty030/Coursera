#week 2 - chapter 11 - Regular Expressions

#regular expressions are kind of an "old school" language
# and compact

"""
Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end
"""

#greedy means: match the largest possible string

#regular expressions library
import re

path = "/home/tbfk/Documents/VSC/Coursera/PythonDataStructures/"

fname = "mbox-short.txt"

fhandle = open(path + fname)

for line in fhandle:
    line = line.rstrip()

    #print every line that starts with "From"
    #the ^ indicates beginning of a line
    #if re.search("^From", line):

    #line that starts with "X" and is followed by any character
    # "." one or multiply times "*"
    #if re.search("^X.*", line):

    #line that starts with "X" followed by "-" and 
    #non-whitespaces characters "\S" for multiple times "+" 
    #if re.search("^X-\S+:", line):
    
    #gives back a list of all lines that have multiple numbers
    #between 0 and 9 in it
    #if re.findall("[0-9]+", line):

    #non-greedy matching: match the shortest string
    #if re.findall("^F.+?",line):


    #look for e-mail adresses
    #if re.findall("^From (\S+@\S+) ", line):

    #look for confidence value, floating point number
    #if re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line):

    #if you want to look for special characters such as a $
    #(there is none in the file mbox-short.txt)
    #if re.findall("\$[0-9.]+",line):
        #print(line)

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)
print(y)