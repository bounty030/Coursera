#Week 6 - Functions and Building Functions: 

#a function is like store and reuse, write a pattern once
# and reuse it, DRY - Don't Repeat Yourself

#def: start the definition of a function
#a function takes some input and produces an output
#invoking a function: e.g. number=int("42")
#def testfun(var) - var is called an argument of the function testfun

#functions which do not return values are called fruitful functions
#functions which do not return values are called non-fruitful functions

#Exercise 1 from book
"""
import random

for i in range(10):
    x = random.random()
    print(x)
"""


#Exercise 2 and 3 from book
"""
def print_lyrics():
    print("I'm a lumberjack. and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()
"""

#Exercise 7 from book: Rewrite the grade program from the previous chapter 
# using a function called computegrade that takes a score as its 
# parameter and returns a grade as a string.

score = input("Enter Score: ")

try:
    score = float(score)
except:
    score = -1

def computegrade(score):
    
    if (score >= 0.0) and (score <= 1.0):
        if score >= 0.9:
            grade = "A"
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        elif score < 0.6:
            print("F")
    
    else:
        print("Error, Score must be between 0.0 and 1.0")
        grade = "Bad score"

    return grade

grade = computegrade(score)
print(grade)