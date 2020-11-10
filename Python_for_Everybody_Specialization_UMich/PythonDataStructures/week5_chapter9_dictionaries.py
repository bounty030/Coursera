#week 5 - chapter 9 - dictionaries

#another collection, more than one value

#a list is a very linear collection of values that stay in order

#dictionary is a "bag" of values, each with its own label (key)
#like a mini database
#dictionaries have no order but always a key to find a value
"""
purse = dict()
purse["money"]=12
purse["candy"]=3
purse["tissues"]=75
print(purse)
print(purse["money"])

purse["candy"] = purse["candy"] + 2
print(purse)
"""


#defining an empty dictionary
"""
ooo={}
jjj={"chuck":1, "fred": 42, "jan":100}
print(ooo)
print(jjj)
"""


#Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. 
# Then you can use the "in" operator as a fast way to check whether a string is in the dictionary.
"""
path = "/home/tbfk/Documents/VSC/Coursera/PythonDataStructures/"
filename = path + "words.txt"
fhand = open(filename)
word_dict = dict()
for line in fhand:
    line = line.rstrip()
    pieces = line.split()
    for word in pieces:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            continue

print(word_dict)
"""


#counting with dictionaries / creating a histogram
"""
counts=dict()
names=["csev", "cwen", "csev", "zqian", "cwen"]
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name]=counts[name]+1
print(counts)
"""


#the above code can be shortened using the get(x,y) function, 
#x: key of dictionary
#y: default value if the key is not yet in the dictionary
"""
counts=dict()
names=["csev", "cwen", "csev", "zqian", "cwen"]
for name in names:
    counts[name] = counts.get(name,0) + 1

print(counts)
"""


#to check if a key is in a dict use "in"
"""
jjj={"chuck":1, "fred": 42, "jan":100}
check = "fred" in jjj
print(check)
"""


#to check if a value is in a dict use the method "values" which takes the values of a dict and makes a list out of it
"""
jjj={"chuck":1, "fred": 42, "jan":100}
vals = list(jjj.values())
check = 100 in vals
print(check)
"""


#dictionaries and files
#counting pattern
"""
counts = dict()
print("Enter a line of text: ")
line = input("")

words = line.split()

print("Words:", words)
print("Counting...")
for word in words:
    counts[word] = counts.get(word, 0) +1
print("Counts", counts)
"""


#Exercise 2: Write a program that categorizes each mail message by which 
# day of the week the commit was done. To do this look for lines that start 
# with “From”, then look for the third word and keep a running count of 
# each of the days of the week. At the end of the program print out the 
# contents of your dictionary (order does not matter).
"""
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
"""
path = "/home/tbfk/Documents/VSC/Coursera/PythonDataStructures/"
mail = dict()
fname = path + "mbox-short.txt" #input("Enter a file name: ")

try:
    fhandle = open(fname)
except:
    print("File %s cannot be found" %fname)
    exit()

for line in fhandle:
    line = line.rstrip()
    print(line)
    if not line.startswith("From "):
        continue
    else:
        words = line.split()
        print(words)
        day = words[2]
        mail[day] = mail.get(day,0) + 1

print(mail)

