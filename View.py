import sys

from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow


class View(QMainWindow):
    def __init__(self, main_controller, ui_file_name):
        super().__init__()
        self.controller = main_controller
        self.ui = self._setup_ui(ui_file_name)
        self.ui.pushButton.clicked.connect(self.controller.run)

    @staticmethod
    def _setup_ui(ui_file_name):
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
            sys.exit(-1)
        loader = QUiLoader()
        ui_file.close()
        ui = loader.load(ui_file)
        return ui

    def set_loading_bar_pct(self, pct):
        self.ui.progressBar.setProperty('value', pct)
