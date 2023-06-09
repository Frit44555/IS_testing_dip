from PyQt5.QtWidgets import QWidget, QMessageBox
from psycopg2 import Error
import src.Words as wrd
from UI.form_for_admin.Ui_CreateLesson import Ui_CreateLesson


class CreateLesson(QWidget, Ui_CreateLesson):
    def __init__(self, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        # ________________________________

        # Методы________________________________
        self.__set_action()
        # ________________________________

        # Опции________________________________
        self.create_push_button.setEnabled(False)
        self.close_push_button.setEnabled(False)
        # ________________________________

    def __set_action(self):
        self.text_edit.textChanged.connect(self.__enable_buttons)
        self.close_push_button.clicked.connect(self.__close)
        self.create_push_button.clicked.connect(self.__create)

    def __enable_buttons(self):
        self.create_push_button.setEnabled(True)
        self.close_push_button.setEnabled(True)

    def __close(self):
        self.create_push_button.setEnabled(False)
        self.close_push_button.setEnabled(False)
        self.text_edit.clear()
        self.name_line_edit.clear()

    def __create(self):
        name = self.name_line_edit.text().strip()
        text = self.text_edit.toPlainText()
        if not name:
            QMessageBox.about(self, wrd.create_lesson['error_create_not_name_title'],
                              wrd.create_lesson['error_create_not_name_text'])
            return

        try:
            self.__db.create_lesson(name, text)
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        self.__db.connection.commit()
        self.__close()

