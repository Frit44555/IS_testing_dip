from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.Ui_CheckResultTesting import Ui_CheckResultTesting
from src.for_admin.CheckResultTestingQuest import CheckResultTestingQuest


class CheckResultTesting(QWidget, Ui_CheckResultTesting):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Опции________________________________
        self.complete_button.setEnabled(False)
        self.stop_button.setEnabled(False)
        # ________________________________
