from PySide6.QtCore import QObject, Signal


class Controller(QObject):
    finished = Signal()
    progress = Signal(int)

    def __init__(self):
        super().__init__()

    def run(self):
        from time import sleep
        for i in range(10):
            sleep(1)
            self.progress.emit((i + 1) * 10)
        self.finished.emit()
