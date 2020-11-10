#week 3 - chapter 12 - network and sockets

#an Internet socket or network socket is an endpoint of a 
#bidirectional inter-process communication flow across an
#Internet Protocol-based computer betwork, such as the internet


#TCPIP are ports from servers that connect to different
#applications such as e-mail server, web server, mail box ...

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#to make a connection we need:
# host: data.pr4e.org; port: 80
mysock.connect(("data.pr4e.org", 80))

#HTTP - Hypertext Transfer Protocol
#is a set of rules to allow browsers to retrieve web
#documents from servers over the internet

#URL - uniform resource locator

#a GET command issues a Request to a Web Server which
#sends a Response back

#The response will contain header data and
#the content of the file

#make a request
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
#send request
mysock.send(cmd)

while True:
    data = mysock.recv(512) # receive up to 512 characters
    if (len(data) < 1): #if you get no data -> end of file
        break
    print(data.decode()) #if we get data -> decode it
mysock.close()