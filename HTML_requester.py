import socket
website = input("Enter a web address and press Enter: ")
print("\nYour website content is:\n")
serverName = website
serverPort = 80
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % website
clientSocket.send(message.encode())
modifiedMessage, serverAddress = clientSocket.recvfrom(4096)
print(modifiedMessage.decode())
clientSocket.close()