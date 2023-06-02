from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.Ui_CheckResultTestingQuest import Ui_CheckResultTestingQuest


class CheckResultTestingQuest(QWidget, Ui_CheckResultTestingQuest):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
