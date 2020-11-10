#Week 7 - Assignment 5.2

#5.2 Write a program that repeatedly prompts a user for integer 
# numbers until the user enters 'done'. Once 'done' is entered, 
# print out the largest and smallest of the numbers. If the user 
# enters anything other than a valid number catch it with a 
# try/except and put out an appropriate message and ignore the 
# number. Enter 7, 2, bob, 10, and 4 and match the output below. 

#None type is the absence of a value.
#"is" and "is not" is stronger than "==" and should only be used for
# "None" or boolean types

largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    else:
        try:
            num_int = int(num)
            if (smallest is None) or (num_int < smallest):
                smallest = num_int
            elif (largest is None) or (num_int > largest):
                largest = num_int
        except:
            print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)


