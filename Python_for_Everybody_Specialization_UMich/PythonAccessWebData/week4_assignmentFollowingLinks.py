#week 4 - Assignment
#Following Links in Python


# In this assignment you will write a Python program that expands on 
# http://www.py4e.com/code3/urllinks.py. The program will use urllib 
# to read the HTML from the data files below, extract the href= vaues 
# from the anchor tags, scan for a tag that is in a particular 
# position relative to the first name in the list, follow that link 
# and repeat the process a number of times and report the last name 
# you find.

#We provide two files for this assignment. One is a sample file where 
# we give you the name for your testing and the other is the actual 
# data you need to process for the assignment

"""
    Sample problem: Start at 
    http://py4e-data.dr-chuck.net/known_by_Fikret.html

    Find the link at position 3 (the first name is 1). 
    Follow that link. 
    Repeat this process 4 times. 
    The answer is the last name that you retrieve.
    Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
    Last name in sequence: Anayah
    
    Actual problem: Start at: 
    http://py4e-data.dr-chuck.net/known_by_Raman.html
    Find the link at position 18 (the first name is 1). 
    Follow that link. 
    Repeat this process 7 times. 
    The answer is the last name that you retrieve.
    Hint: The first character of the name of the last page that 
    you will load is: K
"""

"""
Sample execution

Here is a sample execution of a solution:

$ python3 solution.py
Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Enter count: 4
Enter position: 3
Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html


"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#url = "http://py4e-data.dr-chuck.net/known_by_Raman.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#count variables
count = int(input("Enter count: "))
position = int(input("Enter position: "))

def scrape_url(url, pos):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    position = 0
    tags = soup('a')

    for tag in tags:
        position = position + 1
        if position == pos:
            new_url = tag.get('href', None)
        else: continue

    return new_url

#count = 7
#position = 18

count_var = 0

print(url)
while count_var < count:
    new_url = scrape_url(url, position)
    print(new_url)
    url = new_url
    count_var += 1

