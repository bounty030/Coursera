#--------------Expressions Part 1
#constants: 1, 2, 3 ...
#reserved words: cannot be used for functions, variables, classes etc.
#reserved words examples: break, if, False, True, None, as, except, else ...

#variable: named place in the memory where you can store data

#find a place in the memory, label it "x" and put 12.2 in it
x=12.2

#override the previous value with the label "x" with 100
x=100

#variables are case sensitive: spam, Spam, SPAM are different variables

#mnemonic variables: variables with describing or sensible names
hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)

#assignment: x=1 does not mean "equal" it is just assigning 
# a value i.e. 1 to the label in the memory 


#--------------Expressions Part 2
#Sequence of evaluation: 
#1. Paranthesis (Klammern)
#2. Power (Exponent)
#3. Multiplication 
#4. Addition
#5. Left to Right

#function type(variable) gives you the type of a variable

#differnece between floating points and integers: 
# floating points have more range but less precision

#function input() waits for the user input which is called a prompt
# and returns the user input as a string 


#--------------Expressions Part 3
#converting user input example

#convert elevator floors
eu_floor = input("Europe floor? ")
us_floor = int(eu_floor) + 1
print(us_floor)