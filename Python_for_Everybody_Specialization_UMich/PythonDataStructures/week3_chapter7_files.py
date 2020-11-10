#week 3 / chapter 7 - Files

#defining a file with path
path = "/home/tbfk/Documents/VSC/Coursera/PythonDataStructures/"
filename = path + "mbox.txt"
fhand = open(filename)

#opening a file: handle = open(filename, mode)
#handle is a connection to a file

#newline is a character "\n" and counts as one character
#a blank/empty line is also just one "\n"
"""
test="X\nY"
print(len(test))
"""

#file handle as a sequence
"""
xfile = open("filename")
for cheese in xfile:
    print(cheese)
"""

#for reads linewise, example for counting lines
"""
counter = 0
xfile = open(filename)
for line in xfile:
    counter = counter + 1

print(counter) 
"""

#reading the whole file as a single line with newline \n
#using read()
"""
fhand = open(filename)
inp = fhand.read()
print(len(inp))
print(inp[:20])
"""

#searching through a file
"""
for line in fhand:
    if line.startswith("Lorem"):
        print(line)
"""

#each line has a newline at the end, to get rid of it
# print(line.rstrip())


#searching for lines by skipping some with which start with a certain string
"""
for line in fhand:
    if not line.startswith("Lorem"):
        print(line.rstrip())
"""     

#searching for line with string in it
"""
for line in fhand:
    if "Lorem" in line:
        print(line.rstrip())
"""

#handling bad file names
"""
fname = input("Enter the file name: ")
try:
    fhand = open(fname)

except:
    print("File cannot be opened:", fname)
    quit()
"""


# 7.1 Write a program that prompts for a file name, then opens that file 
# and reads through the file, and print the contents of the file in 
# upper case. Use the file words.txt to produce the output below.

#You can download the sample data at http://www.py4e.com/code3/words.txt

# Use words.txt as the file name
#fname = input("Enter file name: ")
"""
fh = open(path + "words.txt")

for line in fh:
    uppercase = line.upper()
    print(uppercase.rstrip())
"""


# 7.2 Write a program that prompts for a file name, then opens that 
# file and reads through the file, looking for lines of the form:

#X-DSPAM-Confidence:    0.8475

#Count these lines and extract the floating point values from each of the 
# lines and compute the average of those values and produce an output as 
# shown below. Do not use the sum() function or a variable named sum in 
# your solution.

#You can download the sample data at 
# http://www.py4e.com/code3/mbox-short.txt when you are testing below 
# enter mbox-short.txt as the file name.
"""
fh = open(path + "mbox-short.txt")

counter = 0
value = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        col = line.find("0")
        length = len(line)
        content = line[col:length]

        counter = counter + 1
        value = value + float(content)

#print("Counter: ",counter)
#print("Sum: ", value)
print("Average spam confidence:", value/counter)
"""

#writing to files
"""
fout = open("test.txt","w")
print(fout)
line1 = "This is a test line\n"
line2 = "Second test \t line"
fout.write(line1)
fout.write(line2)
fout.close()
fin = open("test.txt")
for line in fin:
    #repr(): prints tabs and newlines as strings for debugging
    print(repr(line))

fin.close()
"""

#book chapter 7 - Exercise 3: Sometimes when programmers get bored or want to have abit of fun, they add a harmless
# Easter  Egg to their program. Modify the program that prompts the user for the file name so that it prints a funny message 
# when the user types in the exact file name “na na booboo”.  The program should behave normally for all other files which 
# exist and don’t exist. Here is a sample execution of the program: 
# python egg.py 
# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt
# python egg.py
# Enter the file name: missing.tyxt 
# File cannot be opened: missing.tyx
# python egg.py 
# Enter the file name: na na boo boo
# NA NA BOO BOO TO YOU - You have been punk'd!
# We are not encouraging you to put Easter Eggs in your programs; thisis just an exercise.

fname = input("Enter the file name: ")
#Easter egg
if fname == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()
try:
    fin = open(fname)
except:
    print("File cannot be opened: ", fname)
    exit()

counter = 0
for line in fin:
    counter = counter + 1

print("There were %d subject lines in %s" %(counter, fname))
fin.close()

