from socket import *


class MySocket:

    def __init__(self, username):
        self.host = '127.0.0.1'
        self.port = 50520
        self.bufferSize = 1024
        self.ADDR = (self.host, self.port)
        self.username = username
        self.connector = socket()

    def get(self):
        self.connector.connect(self.ADDR)
        username = self.username + '\n'
        self.connector.send(username.encode('utf8'))
        data = self.connector.recv(self.bufferSize)
        data = data.decode('gb2312')
        self.connector.close()
        return data


if __name__ == '__main__':
    client = MySocket('tu_4s2q3o3p4928')
    print(client.get())