#Exercise 5:  This program records the domain name (instead of the address) 
# where the message was sent from instead of who the mail came from (i.e., the whole email address). 
# At the end of the program, print out the contents of your dictionary.
"""
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
"""

path = "/home/tbfk/Documents/VSC/Coursera/PythonDataStructures/"
count = dict()
fname = path + "mbox-short.txt" #input("Enter a file name: ")
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
        domain = mailadress[mailadress.find("@")+1:]
        #print(domain)
        count[domain] = count.get(domain,0) + 1

print(count)

