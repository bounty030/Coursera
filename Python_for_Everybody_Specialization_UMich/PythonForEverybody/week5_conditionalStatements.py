#3.1 Conditional Statements

#if statements has a condition, if it is true, the indented next 
# lines will be executed, if it is false the next indented 
# lines will be skipped. Indenting by 4 spaces, indenting matters!
# make sure to turn tabs into spaces, otherwise python will complain!!! 


#comparison operators:
# < less than
# <= less than or equal to
# == equal to
# >= greater than or equal to
# > greater than
# != not equal
"""
x = 1
if x>2:
    print("Bigger than 2")
else:
    print("Not bigger than 2")
"""

#nested decisions
"""
y=50
if y>1:
    print("larger than 1")
    if y<100:
        print("lesser than 100")
print("done")
"""


#3.2 More Conditional Statements

#multi-way
#only one of the statements will be true and run
"""
z=5
if z<2:
    print("small")
elif z<10:
    print("Medium")
else:
    print("LARGE")
print("All done")
"""

#try and except structure
#this is a way to eliminate a traceback error

num = input("Enter a number: ") 
try:
    intnum = int(num)
    print("Your number: ", intnum)
except:
    print("Please input a number")