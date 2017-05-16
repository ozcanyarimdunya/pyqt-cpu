"""
    This app created by @ozcaan11
    Özcan Yarımdünya / semiworld.org
"""

import sys

import psutil as psutil
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, qApp, QApplication

import resources


class CPU(QObject):
    def __init__(self):
        super().__init__()

        self.icon = QSystemTrayIcon()
        self.icon.setIcon(QIcon(':0/number_0.png'))

        self.menu = QMenu()
        self.menu.addAction('Quit', qApp.quit)
        self.icon.setContextMenu(self.menu)

        self.thread = ThreadClass()
        self.thread.start()
        self.thread.cpu_signal.connect(self.update_cpu)

        self.icon.show()

    def update_cpu(self, val):
        self.icon.setIcon(QIcon(':{}/number_{}.png'.format(str(val), str(val))))


class ThreadClass(QThread):
    cpu_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()

    def run(self):
        while 1:
            val = psutil.cpu_percent(interval=1)
            self.cpu_signal.emit(int(val))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CPU()
    sys.exit(app.exec_())
