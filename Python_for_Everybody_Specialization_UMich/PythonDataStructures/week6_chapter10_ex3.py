#week 6 - chapter 10 - tuples

#Exercise 3: Write a program that reads a file and prints the letters in 
# decreasing order of frequency. Your program should convert all the input 
# to lower case and only count the letters a-z. Your program should not 
# count spaces, digits, punctuation, or anything other than the letters a-z.  
# Find text samples from several different languages and see how letter 
# frequency varies between languages. Compare your results with the tables 
# at https://wikipedia.org/wiki/Letter_frequencies.

import string
path = "/home/tbfk/Documents/VSC/Coursera/PythonDataStructures/"
fname = path + "mbox-short.txt"
fhandle = open(fname)

count = dict()

for line in fhandle:
    line = line.lower()
    line = line.rstrip()
    line = line.translate(str.maketrans('','', ".,:-/_()+|0123456789\t\n?[];@#'<>=~&%\" "))
    #print(line)

    for word in line:
        
        #print(word)
        count[word] = count.get(word, 0) + 1

count_list = list(count.items())
count_list.sort(reverse=False)

for key, val in count_list[:]:
    print(key, val)