#week 4 - chapter 12 
#---------------Unicode Characters and Strings

#ASCII - American Standard Code for Information Interchange

#each character is represented by a number between 0 and 256
#stored in 8 bits of memory

#1 byte = 8 bits

#The ord() function tells us the numeric value of a ASCII char
"""
print(ord("H"))
print(ord("\n"))
"""

#japanese and american/european computers could not talk
#to each other because of different codes for representing
#characters
#-> unicode was developed to exchange data

#Different unicode character sets
#UTF-16: fixed length - two bytes
#UTF-32: fixed length - four bytes
#UTF-8:  variable length - 1-4 bytes

#UTF-8 is the most used because it overlaps with ASCII


"""
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#to make a connection we need:
# host: data.pr4e.org; port: 80
mysock.connect(("data.pr4e.org", 80))


#Encoding: when sending data to an external resource like a 
# network socket we send bytes, which mean we need to encode 
# Python 3 strings into bytes
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

#Decoding: when reading data from an external resource, we receive
#bytes and first must decode them to a string

while True:
    data = mysock.recv(512) #in bytes
    if (len (data)) < 1:
        break
    #on default decode() assumes UTF-8/ASCII

    mystring = data.decode() #in unicode
    print(mystring)

mysock.close()
"""

#--------------Retrieving Web Pages
"""
#Making the above code shorter by using the urllib library
#urllib makes the socket interaction similar to files
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
#this for loop skips the header
for line in fhand:
    print(line.decode().strip())
"""


#-----------Parsing Web Pages
#scraping: when a program or scripts pretends to be a browser and
#retrieves web pages, extracts information
#search engines scrape web pages


#Beautiful Soup is a library for scraping HTML pages
import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup

url = "http://www.dr-chuck.com/page1.htm"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

#Retrieve all of the anchor tags and look for an anchor tag
#that contains "href"
tags = soup("a")
print(tags)
"""
for tag in tags:
    print(tag.get("href", None))
"""