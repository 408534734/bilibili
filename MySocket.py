from socket import *


class MySocket:

    def __init__(self, host, username):
        self.host = host
        self.port = 50520
        self.bufferSize = 1024
        self.ADDR = (self.host, self.port)
        self.username = username
        self.connector = socket()

    def get(self):
        try:
            self.connector.connect(self.ADDR)
            username = self.username + '\n'
            self.connector.send(username.encode('utf8'))
            data = self.connector.recv(self.bufferSize)
            data = data.decode('gb2312')
            self.connector.close()
            return data
        except TimeoutError:
            return '连接超时！'
        except ConnectionRefusedError:
            return '连接错误！'
        else:
            return 'UnknowError'


if __name__ == '__main__':
    socket = MySocket('127.0.0.1', 'tu_4s2q3o3p4928')
    #print(client.get)
