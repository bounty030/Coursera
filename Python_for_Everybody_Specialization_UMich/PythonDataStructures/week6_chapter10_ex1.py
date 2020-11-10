#week 6 - chapter 10 - tuples

#Exercise 1: Revise a previous program as follows: Read and parse 
# the “From” lines and pull out the addresses from the line. 
# Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most 
# commits by creating a list of (count, email) tuples from the dictionary. 
# Then sort the list in reverse order and print out the person who has 
# the most commits.

"""
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""

path = "/home/tbfk/Documents/VSC/Coursera/PythonDataStructures/"
fname = path + "mbox-short.txt"
fhandle = open(fname)

count = dict()

for line in fhandle:
    line.rstrip()
    if not line.startswith("From "):
        continue
    else:
        words = line.split()
        #print(words)
        address = words[1]
        #print(address)
        count[address] = count.get(address, 0) + 1

count_list = list()
for key, val in list(count.items()):
    count_list.append((val, key))

count_list.sort(reverse=True)

for key, val in count_list[:1]:
    print(val, key)
    
