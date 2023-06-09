from PyQt5.QtWidgets import QWidget, QMessageBox
from UI.Ui_Lesson import Ui_Lesson
import Words as wrd


class Lesson(QWidget, Ui_Lesson):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Методы________________________________
        self.__fill_content(text)
        # ________________________________

    def __fill_content(self, text):
        if text == 1:
            QMessageBox.about(self, wrd.for_all_occasions['oops'], wrd.for_all_occasions['oops'])
            return
        self.lessons_text_browser.setText(text)
