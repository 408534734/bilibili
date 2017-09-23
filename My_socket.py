from socket import *

class My_socket:
    host = '127.0.0.1'
    port = 50520
    bufferSize = 1024
    ADDR = (host, port)

    def __init__(self, username):
        self.client = socket()
        self.client.connect(self.ADDR)
        username = username + '\n'
        self.client.send(username.encode('utf8'))
        data = self.client.recv(self.bufferSize)
        data = data.decode('gb2312')
        print(data)
        self.client.close()

if __name__ == '__main__':
    client = My_socket('tu_4s2q3o3p4928')