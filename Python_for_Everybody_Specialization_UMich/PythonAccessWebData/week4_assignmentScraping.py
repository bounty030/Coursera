#week 4 - Assignment
#Scraping Numbers from HTML using BeautifulSoup


#The program will use urllib to read the HTML from the data files 
# below, and parse the data, extracting numbers and compute the 
# sum of the numbers in the file.

#We provide two files for this assignment. One is a sample file 
# where we give you the sum for your testing and the other is the 
# actual data you need to process for the assignment.

 #   Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
 #   Actual data: http://py4e-data.dr-chuck.net/comments_938716.html (Sum ends with 10)


#-----------Parsing Web Pages
#scraping: when a program or scripts pretends to be a browser and
#retrieves web pages, extracts information
#search engines scrape web pages


#Beautiful Soup is a library for scraping HTML pages
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = "http://py4e-data.dr-chuck.net/comments_938716.html"
url = input("Enter - ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#Retrieve all of the anchor tags and look for an anchor tag
#that contains "href"
tags = soup("span")
#print(tags)

count = 0
sum_ = 0
for tag in tags:
    # Look at the parts of a tag
    #print ('TAG:',tag)
    #print ('URL:',tag.get('href', None))
    #print ('Contents:',tag.contents[0])
    #print ('Attrs:',tag.attrs)
    count = count + 1
    sum_ = sum_ + int(tag.contents[0])

print("Count ", count)
print("Sum ", sum_)