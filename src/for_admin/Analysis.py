from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.Ui_Analysis import Ui_Analysis
from psycopg2 import Error


class Analysis(QWidget, Ui_Analysis):
    def __init__(self, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        # ________________________________

        # Функции________________________________
        self.__fill_list_users()
        # ________________________________

    def __set_action(self):
        """
        Устанавливает действия кнопкам
        """
        pass

    def __fill_list_users(self):
        """
        Заполняет список пользователей
        """
        try:
            self.__results_all = self.__db.get_results_all()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        if self.__results_all == 1:
            return

        self.result_user_list_widget.clear()
        for row in self.__results_all:
            # ID результата, ID пользователя, ID теста, массив ответов, время начала, время конца, коммент админа,
            # коммент пользователя, статус проверки
            elem_lest = ''
            elem_lest += 'Номер: ' + str(row[0]) + ' | '
            elem_lest += 'ID пользователя: ' + str(row[1]) + ' | '
            elem_lest += 'Тест: ' + str(row[2]) + ' | '
            elem_lest += 'Начал: ' + str(row[4])[:-7] + ' | '
            elem_lest += 'Закончил: ' + str(row[5])[:-7] + ' | '

            self.result_user_list_widget.addItem(elem_lest)

    def __fill_list_test(self):
        """
        Заполняет список статистики тестов
        """
        pass
