#Week 1 / Chapter 6 - Strings



# get a single character in a string using an index 
# specified in square brackets 
"""
fruit = "banana"
first_char = fruit[0]
print(first_char)
"""

#strings have a length
"""
length_string = len(fruit)
print("Length of string:",length_string)
"""

#looping through strings
"""
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
"""

#another example of looping through strings is with the "for" statement:
"""
for  letter in fruit:
    print(letter)
"""

#counting a specific letter with a loop
"""
count = 0
fruit = "banana"
for letter in fruit:
    if letter == "a":
        count = count + 1

print(count)
"""

#slicing strings
"""
s = "Monty Python"
print(s[0:5])
print(s[0:100])
print(s[:2])
print(s[2:])
"""

#concatenate strings
"""
a = "Hello "
b = a + "There"
print(b)
"""

#the "in" keyword can be used to check to see if one string is "in" another
"""
fruit = "banana"
if "n" in fruit:
    print("Found it!")
"""

#string comparison with ==, <, > ...
"""
a = "string1"
b = "string2"

if a == b:
    print("Same strings")
else:
    print("Different strings")
"""


#String Library: Python has a number of string methods which
# are in the string library
#difference between a function and a method: 
#method is part of a class and is invoked by appending the method name
#to a variable e.g. greet.lower()
"""
greet = "Hello Tim"
print(greet.lower())
"""


#"dir" to show methods of a class
"""
test_string = "hello"
print(type(test_string))
print(dir(test_string))
"""


#searching a string with find()
"""
test_string = "hello"
pos = test_string.find("l")
print(pos)
"""

#invoking multiple methods
"""
line= "Have a nice day"
print(line.lower().startswith("h"))
"""

#book chapter 6 - exercise 1
#Write a while loop that starts at the last character in the string and 
# works its way backwards to the first character in the string, printing 
# each letter on a separate line, except backwards.
"""
fruit = "banana"
index = len(fruit)

while index > 0:
    letter = fruit[index-1]
    index = index -1
    print(letter)
   
"""

#book chapter 6 - exercise 3
#encapsulate this code in a function named count, 
# and generalize it so that it accepts the string and the letter as 
# arguments
"""
def counter(match, word):
    count = 0
    for letter in word:
        if letter == match:
            count = count + 1
    print (count)
   
counter("m", "momlsdfsfam")
"""


#book chapter 6 - exercise 4
#There is a string method calledcountthat is similar to the functionin 
# the previous exercise. Read the documentation of this method 
# at:https://docs.python.org/library/stdtypes.html#string-methodsWrite an 
# invocation that counts the number of times the letter a occurs 
# in “banana”.
"""
fruit="banana"
print(fruit.count("a",0,20))
"""

#format operator: for constructing strings and replacing parts of the strings
# %d: integer
# %g: floating point
# %s: string
"""
print("In %d years I have spotted %g %s." %(3, 0.1, "camels"))
"""

#book chapter 6 - exercise 5
#Take the following Python code that stores a 
# string: text = "X-DSPAM-Confidence:    0.8475"
# Use find and string slicing to extract the portion of the string after 
# the colon character and then use the float function to convert 
# the extracted string into a floating point number.

"""
text = "X-DSPAM-Confidence:    0.8475"

length = len(text)
number = float(text[text.find("0") : len(text)])
print(number)
"""


#book chapter 6 - exercise 6
#Exercise 6:   Read the documentation of the string methods at
# https://docs.python.org/library/stdtypes.html#string-methods
# You might want to experiment with some of them to make sure you understand 
# how they work. strip and replace are particularly useful.
# The documentation uses a syntax that might be confusing. 
# For example, in find(sub[, start[, end]]), the brackets indicate optional 
# arguments. So sub is required, but start is optional, and if you 
# include start, then end is optional

#strips spaces at front and end of string if argument left empty strip()
#rstrip() and lstrip() removes whitespaces only from right and left
"""
test_string = "    sdgfgdasff   sejig    sdn   "

print(test_string.strip())
print(test_string.lstrip())
print(test_string.rstrip())
"""


#string.replace("a", "b") replaces "a" with "b" of the string
"""
a = "abcde"
b = a.replace("a", "z")
print(b)
"""


