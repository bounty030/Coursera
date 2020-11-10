#week 6 - chapter 10 - tuples

#A tuple1 is a sequence of values much like a list. 
# The values stored in a tuple can be any type, and they are indexed by 
# integers.

"""
t = ("a", "b", "c")
print(t[1])

#o create a tuple with a single element, you have to include 
# the final comma:
t1 = ("a",)
print(type(t1))

#without the comma at the end it is a string
t2=("a")
print(type(t2))

#you cannot modify one of the elements of a tuple
#but you can replace a tuple with another
t3 = t + t1
print(t3)
"""


#tuple assignment
"""
m = ["have", "fun"]
x, y = m
print(x)
print(y)
"""

#or:
"""
x = m[0]
y = m[1]
print(x)
print(y)
"""

#other example:
"""
addr="monty@python.org"
uname, domain = addr.split("@")
print(uname)
print(domain)
"""


#sorting dictionaries with tuples
#dictionaries are unsorted but a list is sortable
#the dictionary is turned into a list with tuples and the tuples are sorted
"""
d={'a':10,'b':1, "y": 5, 'c':22, "z":0, "d":1}
t=list(d.items())
print("Unsorted; ", t)
t.sort()
print("Sorted: ", t)
"""


#looking for the most common words and ordering them
"""
import string

path = "/home/tbfk/Documents/VSC/Coursera/PythonDataStructures/"
fhand=open(path + 'romeo-full.txt')
counts=dict()

for line in fhand:
    line = line.translate(str.maketrans('','', string.punctuation))
    line = line.lower()
    words = line.split()

    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
        
    # Sort the dictionary by value
    lst=list()
    for key, val in list(counts.items()):
        lst.append((val, key))

    lst.sort(reverse=True)

#print(lst[:10])
for key, val in lst[:10]:
    print(key, val)
"""

#using tuples as keys in dictionaries, [last_name, first_name] is a tuple
#the () around a tuple are not necessary
"""
telephone_directory[last_name, first_name] = number
"""

"""
directory = dict()
directory["cheese", "gerd"] = "015776452312"
#print(directory)
print(directory["cheese", "gerd"])
#print(dir(directory))
"""

#when to use tuples?

#1. In some contexts, like areturnstatement, it is syntactically simpler 
# to createa tuple than a list. In other contexts, you might prefer a list.

#2. If you want to use a sequence as a dictionary key, you have to use an 
# immutable type like a tuple or string.

#3. If you are passing a sequence as an argument to a function, using 
# tuples reduces the potential for unexpected behavior due to aliasing.

#Because tuples are immutable, they don’t provide methods like
# "sort" and "reverse",which modify existing lists.