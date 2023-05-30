from PyQt5.QtWidgets import QWidget
from psycopg2 import Error
from UI.Ui_ResultUser import Ui_ResultUser


class ResultUser(QWidget, Ui_ResultUser):
    def __init__(self, data, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__data = data
        self.__db = data_base
        # ________________________________

        # Функции________________________________
        self.__set_action()
        self.__fill_result_list()
        # ________________________________

    def __set_action(self):
        self.show_result_push_button.clicked.connect(self.__draw_statistics)

    def __fill_result_list(self):
        """
        Заполняет список пройденных тестов.
        :return None
        """
        try:
            for row in self.__data:
                elem_lest = ''
                test = self.__db.get_name_time_type_note_on_test(row[2])
                if test == 1:
                    continue

                elem_lest += 'Номер: ' + str(row[0]) + ' | '
                elem_lest += 'Название теста: ' + test[0] + ' | '
                elem_lest += 'Время выполнения: ' + str(row[5] - row[4])[:-7] + ' | '

                self.result_list_widget.addItem(elem_lest)

        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

    def __draw_statistics(self):
        """
        Показывает статистику результата
        :return None
        """
        try:
            # Item выбранного элемента
            index = self.result_list_widget.selectedIndexes()[0]
            # Строка выбранного элемента
            st = index.data()
            print(len(st[6:st.find('|')].strip()))
        except BaseException as error:
            # Вызвать QMessageBox
            print(error)
