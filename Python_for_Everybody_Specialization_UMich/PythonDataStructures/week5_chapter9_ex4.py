#Exercise 4: Add code to the above program to figure out who has the most 
# messages in the file. After all the data has been read and the dictionary 
# has been created, look through the dictionary using a maximum loop 
# (see Chapter 5: Maximum and minimum loops) to find who has the most 
# messages and print how many messages the person has.

"""
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195
"""


path = "/home/tbfk/Documents/VSC/Coursera/PythonDataStructures/"
count = dict()
fname = path + "mbox.txt" #input("Enter a file name: ")
max_count = None
person = None

try:
    fhandle = open(fname)
except:
    print("File %s cannot be found" %fname)
    exit()

for line in fhandle:
    line = line.rstrip()
    #print(line)
    if not line.startswith("From "):
        continue
    else:
        words = line.split()
        #print(words)
        mailadress = words[1]
        count[mailadress] = count.get(mailadress,0) + 1

for key, val in count.items():
    if (max_count is None) or val > max_count:
        max_count = val
        person = key 

print(person, max_count)

