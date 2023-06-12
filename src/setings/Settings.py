from PyQt5.QtWidgets import QWidget
from UI.Ui_Settings import Ui_Settings


class Settings(QWidget, Ui_Settings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
