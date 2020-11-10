#Week 7 - Loops and Iteration: 

#loops have iteration variables that change each time through a loop

#infinite loop (while) -> iteration variable does not change each time

#the break statement ends the current loop and jumps to the code lines
# following the loop
# Example for break:
"""
n = 0

while n == 0:
    break

print("done")
"""

#the continue statement ends the current iteration and jumps
# to the top of the loop and starts the next iteration
"""
while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done")
"""

#Definite Loops (for)
#E.g. iterate through a list, a file etc
"""
for i in range(5,1,-1):
    print(i)
print("Blastoff!")
"""

#Another example
"""
friends = ["Georg", "Ede", "Nils"]

for friend in friends:
    print("Hello", friend)

print("Greeted all friends")
"""

#None type is the absence of a value.
#"is" and "is not" is stronger than "==" and should only be used for
# "None" or boolean types


#book chapter 5 exercise 1
#  Write a program which repeatedly reads numbers until the user 
# enters “done”. Once “done” is entered, print out the total, 
# count, and average of the numbers. If the user enters anything 
# other than a number, detect their mistake using try and except and 
# print an error message and skip to the next number.

total = 0
count = 0
num_list = []

while True:
    num = input("Enter number: ")
    if num == "done":
        break
    else:
        try:
            num = float(num)
            num_list.append(num)
        except:
            print("Not a number")

print("Finished the number list")

for number in num_list:
    count = count + 1
    total = total + number

average = total / count
print("Total:", total, "Count:", count, "Average:", average)
