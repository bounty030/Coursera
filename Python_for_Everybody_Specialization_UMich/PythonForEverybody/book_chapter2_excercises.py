#---------2.15  Exercises
# Exercise 2: Write a program that usesinputto prompt a user for 
# theirname and then welcomes them

"""
name=input("Enter your name: ")
print("Hello",name)
"""


#Exercise 3: Write a program to prompt the user for hours and 
# rate perhour to compute gross pay.

"""
hours=input("Enter Hours: ")
rate=input("Enter Rate: ")
pay=float(hours) * float(rate)
print("Pay:",pay)
"""

#Exercise 4: Assume that we execute the following assignment state-ments

#width = 17
#height = 12.0

#For each of the following expressions, write the value of the 
# expression and thetype (of the value of the expression).

#1.width//2
# 2.width/2.0
# 3.height/3
# 4.1 + 2 * 5


#Exercise 5: Write a program which prompts the user for a 
# Celsius tem-perature, convert the temperature to Fahrenheit, 
# and print out theconverted temperature

celsius = input("Enter a temperature in Celsius: ")
fahrenheit = (float(celsius) * (9/5)) + 32
print("Temperature in Fahrenheit:",fahrenheit)