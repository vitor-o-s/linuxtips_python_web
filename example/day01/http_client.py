import socket # Abre porta para internet

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9000))

command = "GET http://localhost/index.html HTTP/1.0\r\n\r\n".encode()
client.send(command)

while True:
    data = client.recv(512) # bytes
    if len(data) < 1:
        break
    print(data.decode(), end='')

client.close()