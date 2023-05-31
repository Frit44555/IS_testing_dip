from PyQt5.QtWidgets import QWidget
from UI.ui_quest.Ui_StatusAnswer import Ui_Form


class StatusAnswerWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def answered(self):
        self.widget.setStyleSheet('background-color: #fff013; border-radius: 14px;')

    def unanswered(self):
        self.widget.setStyleSheet('background-color: rgb(255, 0, 0); border-radius: 14px;')
