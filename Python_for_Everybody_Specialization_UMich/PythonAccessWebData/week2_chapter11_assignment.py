#week 2 - chapter 11 - assignment

# Finding Numbers in a Haystack
#In this assignment you will read through and parse a file 
# with text and numbers. You will extract all the numbers 
# in the file and compute the sum of the numbers. 


#Data Files
#We provide two files for this assignment. One is a sample 
# file where we give you the sum for your testing and the 
# other is the actual data you need to process for the 
# assignment.

#Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt 
# (There are 90 values with a sum=445833)
#Actual data: http://py4e-data.dr-chuck.net/regex_sum_938714.txt 
# (There are 70 values and the sum ends with 194)

#Handling The Data
#The basic outline of this problem is to read the file, look 
# for integers using the re.findall(), looking for a regular 
# expression of '[0-9]+' and then converting the extracted 
# strings to integers and summing up the integers. 

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

path = "/home/tbfk/Documents/VSC/Coursera/PythonAccessWebData/"

fname = "regex_sum_938714.txt"

fhandle = open(path + fname)

counter = 0
numlist=list()

for line in fhandle:
    line = line.rstrip()

    if re.findall("[0-9]+",line):
        #create a list of tuples (strings) with only numbers
        numbers_str = re.findall("[0-9]+",line)
        #convert into list of tuples (integers)
        numbers_int = list(map(int, numbers_str))

        counter = counter + len(numbers_int)
        #take sum of tuples (get rid of tuples)
        numlist.append(sum(list(numbers_int)))

#print(numlist)
print("Values: ", counter)
print("Sum: ", sum(list(numlist)))