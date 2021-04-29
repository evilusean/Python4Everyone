import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n".encode()
mysock.send(cmd)
#makes the connection to webserver and port 80
#cmd = get sends to the server

while True:
    data =mysock.recv(512)
    if (len(data) <1):
        break
    print(data.decode())

#receives file 512 characters at a time
mysock.close
#closes connection