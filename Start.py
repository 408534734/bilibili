import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QDesktopWidget, QPushButton
from Windows import *
from MySocket import *


class Start(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindow()
        self.initUI()
        self.show()

    def setWindow(self):
        self.resize(400, 120)#设置窗口大小
        self.setCenter()#设置窗口居中(自定义函数)
        self.setWindowTitle('弹幕互动系统')#设置窗口标题

    def setCenter(self):#直接复制的，不知道什么原理，反正能居中6
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        serverAddress = QLabel('服务器地址 : ')
        username = QLabel('用  户  名 : ')
        empty = QLabel(' ')
        self.serverAddressEdit = QLineEdit()
        self.usernameEdit = QLineEdit()
        buttonStart = QPushButton('连接', self)
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(serverAddress, 1, 0)
        grid.addWidget(self.serverAddressEdit, 1, 1)
        grid.addWidget(username, 2, 0)
        grid.addWidget(self.usernameEdit, 2, 1)
        grid.addWidget(empty, 3, 0)
        self.setLayout(grid)
        buttonStart.resize(80, 30)
        buttonStart.clicked.connect(self.connectServer)
        buttonStart.move(160, 80)

    def connectServer(self):
        serverAddress = self.serverAddressEdit.text()
        username = self.usernameEdit.text()
        socket = MySocket(serverAddress, username)
        main = Window(socket)
        main.show()
        #self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    start_window = Start()
    sys.exit(app.exec_())
