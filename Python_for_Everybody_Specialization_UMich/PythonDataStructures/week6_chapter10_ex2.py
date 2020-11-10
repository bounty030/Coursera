#week 6 - chapter 10 - tuples

#Exercise 2: This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the “From” line
# by finding the time string and then splitting that string into parts 
# using the colon character. Once you have accumulated the counts for each
# hour, print out the counts, one per line, sorted by hour as shown below.

"""
 python timeofday.py
 Enter a file name: mbox-short.txt
 04 3
 06 1
 07 1
 09 2
 10 3
 11 6
 14 1
 15 2
 16 4
 17 2
 18 1
 19 1
"""

path = "/home/tbfk/Documents/VSC/Coursera/PythonDataStructures/"
fname = path + "mbox-short.txt"
fhandle = open(fname)

count = dict()

for line in fhandle:
    line.rstrip()
    if not line.startswith("From "):
        continue
    else:
        words = line.split()
        #print(words)
        time = words[5]
        time_split = time.split(":")
        hour = time_split[0]
        #print(hour)
        count[hour] = count.get(hour, 0) + 1

count_list = list(count.items())
count_list.sort(reverse=False)

for key, val in count_list[:]:
    print(key, val)
    
