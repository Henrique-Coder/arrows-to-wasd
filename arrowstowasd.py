from dependencies import imgs
from PyQt5 import QtCore, QtGui, QtWidgets
from ahk import AHK
from webbrowser import open as webopen
from ahk.directives import NoTrayIcon
from os.path import dirname
from psutil import process_iter
import keyboard
from sys import exit, argv


def close_ahk_process():
    for proc in process_iter():
        if proc.name() == 'AutoHotkey.exe':
            proc.terminate()
close_ahk_process()

class Ui_wtoa_menu(object):
    def setupUi(self, wtoa_menu):
        wtoa_menu.setObjectName('wtoa_menu')
        wtoa_menu.resize(300, 250)
        font = QtGui.QFont()
        font.setFamily('MS Shell Dlg 2')
        wtoa_menu.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(':/images/images/icon.ico'), QtGui.QIcon.Active, QtGui.QIcon.On)
        wtoa_menu.setWindowIcon(icon)
        wtoa_menu.setStyleSheet('background-color: rgb(50, 50, 60); border-style: outset; border-width: 0px; border-radius: 12px;')
        self.centralwidget = QtWidgets.QWidget(wtoa_menu)
        self.centralwidget.setObjectName('centralwidget')
        self.btn_enableahk = QtWidgets.QPushButton(self.centralwidget)
        self.btn_enableahk.setGeometry(QtCore.QRect(90, 160, 131, 31))
        self.btn_enableahk.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_enableahk.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_enableahk.setAutoFillBackground(False)
        self.btn_enableahk.setStyleSheet('background-color: rgba(0, 204, 102, 220); border-color: rgba(0, 204, 102, 220); color: white; font: bold 12px; border-style: outset; border-width: 1px; border-radius: 5px;')
        self.btn_enableahk.setObjectName('btn_enableahk')
        self.txt_enable_disable = QtWidgets.QLabel(self.centralwidget)
        self.txt_enable_disable.setGeometry(QtCore.QRect(10, 130, 281, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.txt_enable_disable.setFont(font)
        self.txt_enable_disable.setStyleSheet('')
        self.txt_enable_disable.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_enable_disable.setObjectName('txt_enable_disable')
        self.btn_disableahk = QtWidgets.QPushButton(self.centralwidget)
        self.btn_disableahk.setGeometry(QtCore.QRect(90, 160, 131, 31))
        self.btn_disableahk.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_disableahk.setStyleSheet('background-color: rgba(231, 67, 74, 220); border-color: rgba(231, 67, 74, 220); color: white; font: bold 12px; border-style: outset; border-width: 1px; border-radius: 5px;')
        self.btn_disableahk.setObjectName('btn_disableahk')
        self.coder_github = QtWidgets.QPushButton(self.centralwidget)
        self.coder_github.setGeometry(QtCore.QRect(10, 210, 281, 23))
        self.coder_github.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.coder_github.setFocusPolicy(QtCore.Qt.NoFocus)
        self.coder_github.setStyleSheet('background-color: rgba(255, 255, 255, 0); color: rgb(102, 102, 255); font: bold 10px;')
        self.coder_github.setObjectName('coder_github')
        self.W_NoColor = QtWidgets.QLabel(self.centralwidget)
        self.W_NoColor.setGeometry(QtCore.QRect(220, 50, 31, 31))
        self.W_NoColor.setStyleSheet('image: url(:/images/images/W_NoColor.png);')
        self.W_NoColor.setText('')
        self.W_NoColor.setObjectName('W_NoColor')
        self.S_NoColor = QtWidgets.QLabel(self.centralwidget)
        self.S_NoColor.setGeometry(QtCore.QRect(220, 80, 31, 31))
        self.S_NoColor.setStyleSheet('image: url(:/images/images/S_NoColor.png);')
        self.S_NoColor.setText('')
        self.S_NoColor.setObjectName('S_NoColor')
        self.D_NoColor = QtWidgets.QLabel(self.centralwidget)
        self.D_NoColor.setGeometry(QtCore.QRect(250, 80, 31, 31))
        self.D_NoColor.setStyleSheet('image: url(:/images/images/D_NoColor.png);')
        self.D_NoColor.setText('')
        self.D_NoColor.setObjectName('D_NoColor')
        self.A_NoColor = QtWidgets.QLabel(self.centralwidget)
        self.A_NoColor.setGeometry(QtCore.QRect(190, 80, 31, 31))
        self.A_NoColor.setStyleSheet('image: url(:/images/images/A_NoColor.png);')
        self.A_NoColor.setText('')
        self.A_NoColor.setObjectName('A_NoColor')
        self.GlobalArrow = QtWidgets.QLabel(self.centralwidget)
        self.GlobalArrow.setGeometry(QtCore.QRect(140, 60, 21, 31))
        self.GlobalArrow.setStyleSheet('image: url(:/images/images/GlobalArrow.png);')
        self.GlobalArrow.setText('')
        self.GlobalArrow.setObjectName('GlobalArrow')
        self.LeftArrow_NoColor = QtWidgets.QLabel(self.centralwidget)
        self.LeftArrow_NoColor.setGeometry(QtCore.QRect(20, 80, 31, 31))
        self.LeftArrow_NoColor.setStyleSheet('image: url(:/images/images/LeftArrow_NoColor.png);')
        self.LeftArrow_NoColor.setText('')
        self.LeftArrow_NoColor.setObjectName('LeftArrow_NoColor')
        self.DownArrow_NoColor = QtWidgets.QLabel(self.centralwidget)
        self.DownArrow_NoColor.setGeometry(QtCore.QRect(50, 80, 31, 31))
        self.DownArrow_NoColor.setStyleSheet('image: url(:/images/images/DownArrow_NoColor.png);')
        self.DownArrow_NoColor.setText('')
        self.DownArrow_NoColor.setObjectName('DownArrow_NoColor')
        self.UpArrow_NoColor = QtWidgets.QLabel(self.centralwidget)
        self.UpArrow_NoColor.setGeometry(QtCore.QRect(50, 50, 31, 31))
        self.UpArrow_NoColor.setStyleSheet('image: url(:/images/images/UpArrow_NoColor.png);')
        self.UpArrow_NoColor.setText('')
        self.UpArrow_NoColor.setObjectName('UpArrow_NoColor')
        self.RightArrow_NoColor = QtWidgets.QLabel(self.centralwidget)
        self.RightArrow_NoColor.setGeometry(QtCore.QRect(80, 80, 31, 31))
        self.RightArrow_NoColor.setStyleSheet('image: url(:/images/images/RightArrow_NoColor.png);')
        self.RightArrow_NoColor.setText('')
        self.RightArrow_NoColor.setObjectName('RightArrow_NoColor')
        self.titlebar_close = QtWidgets.QPushButton(self.centralwidget)
        self.titlebar_close.setGeometry(QtCore.QRect(110, 0, 81, 41))
        self.titlebar_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.titlebar_close.setFocusPolicy(QtCore.Qt.NoFocus)
        self.titlebar_close.setAutoFillBackground(False)
        self.titlebar_close.setStyleSheet('image: url(:/images/images/titlebar_close_white.png); background-color: rgba(255, 255, 255, 0); border-color: rgba(255, 255, 255, 0); border-style: outset; border-width: 10px;')
        self.titlebar_close.setText('')
        self.titlebar_close.setObjectName('titlebar_close')
        self.txt_enable_disable.raise_()
        self.coder_github.raise_()
        self.btn_disableahk.raise_()
        self.btn_enableahk.raise_()
        self.LeftArrow_NoColor.raise_()
        self.D_NoColor.raise_()
        self.GlobalArrow.raise_()
        self.S_NoColor.raise_()
        self.UpArrow_NoColor.raise_()
        self.W_NoColor.raise_()
        self.A_NoColor.raise_()
        self.DownArrow_NoColor.raise_()
        self.RightArrow_NoColor.raise_()
        self.titlebar_close.raise_()
        wtoa_menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(wtoa_menu)
        QtCore.QMetaObject.connectSlotsByName(wtoa_menu)

    def retranslateUi(self, wtoa_menu):
        _translate = QtCore.QCoreApplication.translate
        wtoa_menu.setWindowTitle(_translate('wtoa_menu', 'WASD.TO.ARROWS'))
        self.btn_enableahk.setText(_translate('wtoa_menu', 'ENABLE'))
        self.txt_enable_disable.setText(_translate('wtoa_menu', '<html><head/><body><p align=\'center\'><span style=\' font-size:9pt; color:#ffffff;\'>Tap the button below to </span><span style=\' font-size:9pt; text-decoration: underline; color:#38ffc4;\'>enable</span><span style=\' font-size:9pt; color:#ffffff;\'> the script</span></p></body></html>'))
        self.btn_disableahk.setText(_translate('wtoa_menu', 'DISABLE'))
        self.coder_github.setText(_translate('wtoa_menu', ' Coder: https://github.com/Henrique-Coder'))

        # Set fixed window size
        wtoa_menu.setFixedSize(300, 250)

        # Hide disableahk button
        self.btn_disableahk.hide()

        # Hide the original title bar
        wtoa_menu.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        wtoa_menu.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        def moveWindow(e):
            if e.buttons() == QtCore.Qt.LeftButton:
                wtoa_menu.move(wtoa_menu.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()
        def mousePressEvent(e):
            self.clickPosition = e.globalPos()
        self.centralwidget.mouseMoveEvent = moveWindow
        self.centralwidget.mousePressEvent = mousePressEvent

        def coder_github():
            webopen('https://github.com/Henrique-Coder')
        def hover_animation(self):
            self.btn_enableahk.setStyleSheet('''
                QPushButton {
                    background-color: rgba(0, 204, 102, 220); border-color: rgba(0, 204, 102, 220); color: white; font: bold 12px; border-style: outset; border-width: 1px; border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: rgba(0, 204, 102, 220); color: white; font: bold 12px; border-style: outset; border-width: 0px; border-radius: 5px;
                }''')
            self.btn_disableahk.setStyleSheet('''
                QPushButton {
                    background-color: rgba(231, 67, 74, 220); border-color: rgba(231, 67, 74, 220); color: white; font: bold 12px; border-style: outset; border-width: 1px; border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: rgba(231, 67, 74, 220); color: white; font: bold 12px; border-style: outset; border-width: 0px; border-radius: 5px;
                }''')
            self.titlebar_close.setStyleSheet('''
                QPushButton {
                    image: url(:/images/images/titlebar_close_white.png); background-color: rgba(255, 255, 255, 0); border-color: rgba(255, 255, 255, 0); border-style: outset; border-width: 10px;
                }
                QPushButton:hover {
                    image: url(:/images/images/titlebar_close_red.png); background-color: rgba(255, 255, 255, 0); border-color: rgba(255, 255, 255, 0); border-style: outset; border-width: 10px;
                }''')

        def stopandexit():
            for p in running_scripts:
                p.terminate()
            running_scripts.clear()
            exit()
        def enable():
            script = open(exe_dir + r'\wasdtoarrows.ahk', 'r').read()
            p = ahk.run_script(script, blocking=False)
            running_scripts.append(p)
            self.btn_enableahk.hide()

            self.btn_disableahk.show()
            self.txt_enable_disable.setText(_translate('wtoa_menu', '<html><head/><body><p align=\'center\'><span style=\' font-size:9pt; color:#ffffff;\'>Tap the button below to </span><span style=\' font-size:9pt; text-decoration: underline; color:#ff6668;\'>disable</span><span style=\' font-size:9pt; color:#ffffff;\'> the script</span></p></body></html>'))
        def disable():
            for p in running_scripts:
                p.terminate()
            running_scripts.clear()
            self.btn_disableahk.hide()

            self.btn_enableahk.show()
            self.txt_enable_disable.setText(_translate('wtoa_menu', '<html><head/><body><p align=\'center\'><span style=\' font-size:9pt; color:#ffffff;\'>Tap the button below to </span><span style=\' font-size:9pt; text-decoration: underline; color:#38ffc4;\'>enable</span><span style=\' font-size:9pt; color:#ffffff;\'> the script</span></p></body></html>'))

        hover_animation(self)

        self.coder_github.clicked.connect(coder_github)
        self.btn_enableahk.clicked.connect(enable)
        self.btn_disableahk.clicked.connect(disable)
        self.titlebar_close.clicked.connect(stopandexit)


if __name__ == '__main__':
    ahk = AHK(directives=[NoTrayIcon])
    running_scripts = list()
    exe_dir = dirname(__file__)
    app = QtWidgets.QApplication(argv)
    wtoa_menu = QtWidgets.QMainWindow()
    ui = Ui_wtoa_menu()
    ui.setupUi(wtoa_menu)
    wtoa_menu.show()
    exit(app.exec_())
