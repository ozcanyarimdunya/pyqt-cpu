"""
    This app created by @ozcanyarimdunya
    Özcan Yarımdünya / semiworld.org
    
    :required library => psutils, PyQt5
"""

import sys

import psutil
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, qApp, QApplication, QWidget, QAction, QDesktopWidget

from cpu_notifier.about import Ui_FormAbout
from cpu_notifier.resources import res_number
from cpu_notifier.resources import res_icon

res_number.qInitResources()
res_icon.qInitResources()


class ThreadCPU(QThread):
    onCpuChanged = pyqtSignal(int)

    def run(self):
        while 1:
            val = psutil.cpu_percent(interval=1)
            self.onCpuChanged.emit(int(val))


class About(Ui_FormAbout, QWidget):
    def __init__(self, flags=None, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)
        self.setupUi(self)
        self.center()
        self.btnClose.clicked.connect(lambda: self.hide())

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        event.ignore()
        self.hide()


class CPU(QObject):
    iconic = False

    def __init__(self):
        super().__init__()

        self.icon = QSystemTrayIcon()

        # menu
        self.menu = QMenu()

        self.number_or_icon = QAction('Show as icon')
        self.number_or_icon.triggered.connect(lambda: self.change_pointer())
        self.menu.addAction(self.number_or_icon)

        self.menu.addAction('About', lambda: self.show_about())
        self.menu.addAction('Quit', lambda: self.quit_program())
        self.icon.setContextMenu(self.menu)

        # thread
        self.thread = ThreadCPU()
        self.thread.start()
        self.thread.onCpuChanged.connect(lambda val: self.update_icon(val))

        # about
        self.about = About()

        # configure
        self.update_icon(0)
        self.icon.show()

    def update_icon(self, val):
        if self.iconic:
            if 20 > val >= 0:
                self.icon.setIcon(QIcon(':0_20/0_20.png'))
            elif 40 > val >= 20:
                self.icon.setIcon(QIcon(':20_40/20_40.png'))
            elif 60 > val >= 40:
                self.icon.setIcon(QIcon(':40_60/40_60.png'))
            elif 80 > val >= 60:
                self.icon.setIcon(QIcon(':60_80/60_80.png'))
            else:  # 100 > val >= 80:
                self.icon.setIcon(QIcon(':80_100/80_100.png'))
        else:
            self.icon.setIcon(QIcon(':{}/number_{}.png'.format(str(val), str(val))))

    def change_pointer(self):
        self.iconic = not self.iconic
        if self.iconic:
            self.number_or_icon.setText("Show as number")
        else:
            self.number_or_icon.setText("Show as icon")

    def show_about(self):
        self.about.show()

    @staticmethod
    def quit_program():
        qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cpu = CPU()
    sys.exit(app.exec_())
