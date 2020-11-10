#week 5 - Web Services and XML
#Chapter 13 Assignment

# Extracting Data from XML

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and 
# extract the comment counts from the XML data, compute the sum of the numbers in the file.

#We provide two files for this assignment. One is a sample file where we give you the sum for your 
# testing and the other is the actual data you need to process for the assignment.

#    Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#    Actual data: http://py4e-data.dr-chuck.net/comments_938718.xml (Sum ends with 38)

#You do not need to save these files to your folder since your program will read the data directly 
# from the URL. Note: Each student will have a distinct data url for the assignment - so only 
# use your own data url for analysis.

#Data Format and Approach

#The data consists of a number of names and comment counts in XML as follows:

"""
<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
#url = "http://py4e-data.dr-chuck.net/comments_42.xml"
#url = "http://py4e-data.dr-chuck.net/comments_938718.xml"
if len(url) < 1: quit()
    
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())

tree = ET.fromstring(data)

lst = tree.findall('comments/comment')
#print("list:", lst)

counter = 0
for item in lst:
    #print("count: ", item.find("count").text)
    counter = counter + int(item.find("count").text)

print('Count:', len(lst))
print("Sum:", counter)