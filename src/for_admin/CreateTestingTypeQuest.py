from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.Ui_CreateTestingTypeQuest import Ui_CreateTestingTypeQuest


class CreateTestingTypeQuest(QWidget, Ui_CreateTestingTypeQuest):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
