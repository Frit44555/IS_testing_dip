from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.Ui_CreateLesson import Ui_CreateLesson


class CreateLesson(QWidget, Ui_CreateLesson):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
