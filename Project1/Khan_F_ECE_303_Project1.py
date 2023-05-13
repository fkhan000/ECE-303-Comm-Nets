#Fakharyar Khan
#February 3rd, 2022
#Communication Networks
#Professor Keene

                              #### Project #1: Web Server ####
#import socket module

from socket import *

import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket



#we use the bind function to specify that our server
#will communicate through port 80. The "" parameter indicates
#that we want our server to be accessible to anyone that has the address

serverSocket.bind(("", 80))

#we can use the listen function to specify how long we want our queue to be
#for connection requests to the server. Since this server is barely going to be used
#I set the queue length to be 1

serverSocket.listen(1)



while True:

  #Establish the connection

  print('Ready to serve...')

  #the .accept method will wait for a connection request from a client
  #once this occurs, the method will get a socket used to communicate
  #with the client and a tuple which holds the address of the client

  connectionSocket, addr = serverSocket.accept() 

  try:
    #the .recv method receives the HTTP request message from the client
    #it takes in the buffer size which represents the maximum number of bytes
    #the message can be
    message =   connectionSocket.recv(1024)
    filename = message.split()[1]                 
    
    #we get the filename from the message and we then open it and store its contents
    #in outputdata. If the file doesn't exist on the server, we raise an exception
    #and give a 404 error

    f = open(filename[1:])                    
    outputdata = f.read()

    #Send one HTTP header line into socket

    #here we send out the status line
    #and since we got to this point, we have the file and so we
    #can give the 200 OK status code
    connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
    
    #Send the content of the requested file to the client
    
    #now we send the contents of the file
    #we take each character in the file, encode it
    #and then send it to the client
    for i in range(0, len(outputdata)):           
      connectionSocket.send(outputdata[i].encode())

    connectionSocket.send("\r\n".encode())
    connectionSocket.close()
  
  except IOError:

    #Send response message for file not found

    #send out status line
    connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())

    #and body
    connectionSocket.send("Uh-oh looks like the file you requested isn't in our server...".encode())


    #Close client socket
    
    connectionSocket.close()

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data
