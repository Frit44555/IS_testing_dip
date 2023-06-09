from PyQt5.QtWidgets import QWidget
from psycopg2 import Error

from UI.form_for_admin.dialog_admin.Ui_CreateTestingFinish import Ui_CreateTestingFinish


class CreateTestingFinish(QWidget, Ui_CreateTestingFinish):
    def __init__(self, data_base, questions, root, type_testing, quantity_of_questions, time_to_complete, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        self.__root = root
        self.__questions = questions
        self.__type_testing = type_testing
        self.__quantity_of_questions = quantity_of_questions
        self.__time_to_complete = time_to_complete
        # ________________________________

        # Методы________________________________
        self.__fill_combobox_exists_tags()
        self.__set_action()
        # ________________________________

        # Опции________________________________
        self.create_push_button.setEnabled(False)
        # ________________________________

    def __set_action(self):
        """
        Устанавливает действия кнопкам
        """
        self.create_push_button.clicked.connect(self.__crate_testing)
        self.name_line_edit.textChanged.connect(self.__enable_button)

    def __enable_button(self):
        """
        Включение кнопки
        """
        self.create_push_button.setEnabled(True)

    def __fill_combobox_exists_tags(self):
        """
        Метод заполняет combobox всех тегов
        """
        self.all_tags_combo_box.clear()
        try:
            # Получение тегов доступных группе и всех тегов
            self.__all_tag = self.__db.get_tags()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        # в случае если список будет пустым, то вернётся код 1, и смысла продолжать заполнение нет
        if self.__all_tag == 1:
            return

        for row in self.__all_tag:
            self.all_tags_combo_box.addItem(row[1])

    def __crate_testing(self):
        """
        Метод завершающий создание тестирование
        """
        name = self.name_line_edit.text()
        tag_id = self.all_tags_combo_box.currentIndex()
        try:
            # массив ID вопросов, ID тег, название, тип теста, количество заданий,
            self.__db.create_test(self.__questions, self.__all_tag[tag_id][0], name, self.__type_testing,
                                  self.__quantity_of_questions, self.__time_to_complete)
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        try:
            self.__db.connection.commit()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        self.__root._close_creator()
        self.close()
