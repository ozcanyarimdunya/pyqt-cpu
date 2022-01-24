import psutil
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMenu, QSystemTrayIcon

__version__ = "0.2.1"


class TaskCpu(QThread):
    on_cpu_changed = pyqtSignal(int)

    def run(self):
        while True:
            value = psutil.cpu_percent(interval=1)
            self.on_cpu_changed.emit(int(value))  # noqa


class WindowCpu(QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        self.menu = QMenu()
        self.usage = QAction()
        self.usage.setText("Initialised")
        self.menu.addAction(self.usage)
        self.version = QAction("Notifier ({})".format(__version__))
        self.version.setDisabled(True)
        self.menu.addAction(self.version)
        self.menu.addSeparator()
        self.menu.addAction("Quit", lambda: exit(0))
        self.setContextMenu(self.menu)
        self.setIcon(QIcon("icons/0.svg"))
        self.show()
        self.task = TaskCpu()
        self.task.start()
        self.task.on_cpu_changed.connect(lambda value: self.set_icon(value))  # noqa

    def set_icon(self, value):
        """
        initial  == 0 white
        [0-25)   == 1 blue
        [25-50)  == 2 green
        [50-75)  == 3 yellow
        [75-100) == 4 orange
        [100-)   == 5 red

        :param value:
        :return:
        """
        if 0 <= value < 25:
            icon = 1
        elif 25 <= value < 50:
            icon = 2
        elif 50 <= value < 75:
            icon = 3
        elif 75 <= value < 100:
            icon = 4
        else:
            icon = 5
        self.usage.setText("Usage % {}".format(value))
        self.setIcon(QIcon("icons/{}.svg".format(icon)))


if __name__ == "__main__":
    app = QApplication([])
    cpu = WindowCpu()
    app.exec()
