import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from time import sleep


class Window(QWidget):
    def __init__(self):
        super().__init__()#调用父构造函数初始化
        self.setWindow()#设置窗口
        self.setButton()  # 设置按钮
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.move)
        self.timer.start()
        self.show()

    def setWindow(self):
        #self.setWindowOpacity(0.1)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        screen = QDesktopWidget().screenGeometry()
        self.setGeometry(300, 300, screen.width(), screen.height())  # 设置窗口位置XY及大小XY

    def setButton(self):
        QToolTip.setFont(QFont('SansSerif', 10))#设置提示框字体与字号
        buttonRestart = QPushButton('Reset', self)#创建重新开始按钮
        buttonRestart.resize(100, 30)
        buttonRestart.move(150, 450)
        buttonRestart.setToolTip('Click here to restart')

    def move(self):
        while True:
            print('.')
            sleep(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())