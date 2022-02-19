import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QThread

from Controller import Controller
from View import View


class App(QApplication):
    def __init__(self):
        super().__init__()
        self.controller = Controller()
        self.main_view = View(self.controller, 'loadingbar.ui')

        # Multi-threading
        self.controller_thread = QThread()
        self.controller.moveToThread(self.controller_thread)
        # self.controller_thread.started.connect(self.controller.run)
        self.controller.finished.connect(self.controller_thread.quit)
        self.controller.finished.connect(self.controller.deleteLater)
        self.controller_thread.finished.connect(
            self.controller_thread.deleteLater)
        self.controller.progress.connect(self.main_view.set_loading_bar_pct)
        self.controller_thread.start()

        # Loop GUI
        self.main_view.ui.show()


if __name__ == "__main__":
    app = App()
    sys.exit(app.exec())
