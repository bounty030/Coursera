#week 4 chapter 8 - Lists

#data structures - a particular way of organizing data in a computer

#list is a sequence of values, the values can be any type (strings, integer, floats ...)
#values in list are called elements or sometimes items

#create list by enclosing elements with square brackets: [0,3,2,500,"hello"]
#a list in another list is called nested: [0, "slsd", [0,2]]
#create empty list: []

"""
cheeses = ["Gouda", "Cheddar", "Edam"]
numbers = [2, 17]
empty = []
print(cheeses, numbers, empty)
print(cheeses[2])
"""

#unlike strings, lists are mutable (changeable) because the order of items in a list can be changed or reassigned
"""
numbers=[0,1,2]
print(numbers)
numbers[1] = 3
print(numbers)
"""

#a list is a relationship between indices and elements which is called "mapping"
#if an index has a negative value it counts backwards from the end of the list
"""
numbers=[0,1,2]
print(numbers)
numbers[-1] = 3
print(numbers)
"""

#"in" operator also works on lists
"""
cheeses = ["Gouda", "Cheddar", "Edam"]
check = "Gouda" in cheeses
print(check)
"""

#traversing a list
"""
cheeses = ["Gouda", "Cheddar", "Edam"]
for cheese in cheeses:
    print(cheese)
"""

#for updating the elements the indices needed, this is often done with 
# "range" and "len"; range(4) gives the list [0,1,2,3]
"""
numbers=[0,1,2]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)
"""

#a nested list still counts as a single list

#list operations
#+ : concatenates lists
#* : repeats a list a given number of times
#the slice operator ":" also works on lists
"""
t=["a", "b", "c", "d", "e", "f", "g", "h"]
print(t[1:3])
print(t[3:])
print(t[:])
"""

#a slice operator on the left side can update multiple elements
"""
t=["a", "b", "c", "d", "e", "f", "g", "h"]
t[1:3] = ["x","y"]
print(t)
"""

#"extends" appends on list to another
"""
t1=["a", "b"]
t2=["c", "d"]
t1.extend(t2) #only t1 is extended
print("t1: ", t1)
print("t2: ", t2)
"""

#sorting the elements from low to high .sort()
"""
t=["y", "q", "a", "h", "z", "b"]
t.sort()
print(t)
"""


#deleting list elements
"""
t=["y", "q", "a", "h", "z", "b"]
x = t.pop(1) #pop has a return value
print(t)
print(x)
"""

#if the deleted value is not needed use "del" as it returns None
"""
t=["y", "q", "a", "h", "z", "b"]
del t[1] #remove single element
del t[1:3] #remove multiple elements
print(t)
"""

#remove an element using the elements name instead of its index
"""
t=["y", "q", "a", "h", "z", "b"]
t.remove("y")
print(t)
"""


#building a list from scratch
"""
stuff=list()
stuff.append("book")
stuff.append(99)
print(stuff)
"""


#-----------strings and lists
#split a string
"""
abc="with three words"
stuff = abc.split()
print(stuff)
for word in stuff:
    print(word)
"""

#convert string to list with list()
"""
string="spam"
t=list(string)
print(t)
"""

#when you do not use a delimiter for split() it just looks for spaces
#give a delimiter as argument such as ";"
"""
line="first;second;third"
thing=line.split(";")
print(thing)
"""

#book chapter 8 - exercise 1
#Exercise 1: Write a function called "chop" that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called "middle" that takes a list and returns a new list 
# that contains all but the first and last elements.
"""
t=[1,2,3]

def chop(t):
    del t[0]
    last = len(t) - 1
    del t[last]
    return None

def middle(t):
    last = len(t) - 1
    return t[1:last]

#chop(t)
x=middle(t)
print(x)
"""

#book chapter 8 - exercise 6
#Exercise 6: Rewrite the program that prompts the user for a list of
# numbers and prints out the maximum and minimum of the numbers at the end 
# when the user enters “done”. Write the program to store the numbers the 
# user enters in a list and use the max() and min() functions to compute 
# the maximum and minimum numbers after the loop completes.

# Enter a number: 6
# Enter a number: 2
# Enter a number: 9
# Enter a number: 3
# Enter a number: 5
# Enter a number: done
# Maximum: 9.0
# Minimum: 2.0

lst = list()
while True:
    number = input("Enter a number: ")
    try:
        num = float(number)
        lst.append(num)
    except:
        if number == "done":
            break
        else:
            print("%s is not a number" %number)
    
print("Maximum: ", max(lst))
print("Minimum: ", min(lst))

