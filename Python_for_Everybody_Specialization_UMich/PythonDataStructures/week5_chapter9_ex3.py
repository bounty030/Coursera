#Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count 
# how many messages have come from each email address, and print the dictionary. 
"""
# Enter file name: mbox-short.txt 
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,'zqian@umich.edu': 4, 
# 'stephen.marquard@uct.ac.za': 2,'ray@media.berkeley.edu': 1}
"""

path = "/home/tbfk/Documents/VSC/Coursera/PythonDataStructures/"
count = dict()
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
        mailadress = words[1]
        count[mailadress] = count.get(mailadress,0) + 1

print(count)

