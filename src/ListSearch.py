from UI.Ui_ListSearch import Ui_ListSearch
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QSpacerItem, QSizePolicy
from PyQt5.QtCore import pyqtSlot
from psycopg2 import Error

# My widgets
from ResultUser import ResultUser


class ListSearch(QWidget, Ui_ListSearch):
    def __init__(self, main_window, data_base, group_user, user_id, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__main_window = main_window
        self.__db = data_base
        self.__group_user = group_user
        self.__user_id = user_id
        self.__assigned_tests = None
        self.__working_data_on_tests = None
        self.__working_data_on_lessons = None
        self.__test_id = None
        self.__appointment_test_id = None
        self.__lesson_id = None
        self.result_user = None
        # ________________________________

        # Функции________________________________
        self.__fill_tables()
        self.__set_action()
        self.__fill_appointment_test_list()
        # ________________________________

        # Опции________________________________
        self.test_table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lessons_table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # ________________________________

        # Объекты________________________________
        self.result_user = ResultUser(parent=self, data=self.__db.get_results_user(user_id), data_base=self.__db)
        self.result_grid.addWidget(self.result_user)
        # spacerItem7 = QSpacerItem(20, 383, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # self.verticalLayout_3.addItem(spacerItem7)
        # ________________________________

    def __set_action(self):
        """
        Устанавливает действия кнопкам
        :return None
        """
        self.start_lesson_push_button.clicked.connect(self.__open_lesson)
        self.start_test_push_button.clicked.connect(lambda: self.__open_testing(1))
        self.start_appointment_test_push_button.clicked.connect(lambda: self.__open_testing(2))
        self.test_table_widget.doubleClicked.connect(self.__get_test_id)
        self.lessons_table_widget.doubleClicked.connect(self.__get_lesson_id)
        self.refresh_result_push_button.clicked.connect(self.__refresh_result)
        self.appointment_test_list_widget.doubleClicked.connect(self.__get_appointment_test)

    def __fill_tables(self):
        """
        Заполнение таблиц 'Тесты' и 'Уроки'.
        :return None
        """
        # Получение рабочих данных по таблицам 'тесты' и 'уроки'
        try:
            self.__working_data_on_tests = self.__db.working_data_on_tests(self.__group_user)
            self.__working_data_on_lessons = self.__db.working_data_on_lessons(self.__group_user)
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)
        # заполнение таблицы 'тесты'
        if self.__working_data_on_tests != 1:
            numcols = 4
            numrows = len(self.__working_data_on_tests)
            self.test_table_widget.setRowCount(numrows)
            for row in range(numrows):
                for column in range(numcols):
                    self.test_table_widget.setItem(row, column,
                                                   QTableWidgetItem(str(self.__working_data_on_tests[row][column + 3])))
        else:
            return
        # заполнение таблицы 'уроки'
        if self.__working_data_on_lessons != 1:
            numcols = 1
            numrows = len(self.__working_data_on_lessons)
            self.lessons_table_widget.setRowCount(numrows)
            for row in range(numrows):
                for column in range(numcols):
                    self.lessons_table_widget.setItem(row, column,
                                                      QTableWidgetItem(
                                                          str(self.__working_data_on_lessons[row][column + 1]
                                                              )
                                                      ))
        else:
            return

    def __get_test_id(self):
        """
        Получение индекса выделенной строки, получение ID теста, установка названия выбранного теста.
        :return None
        """
        row_id = self.test_table_widget.currentIndex().row()
        test_name = self.test_table_widget.item(row_id, 0).text()
        # Данные выбранного теста, [(ID, тип)]
        self.__test_id = [i[::4] for i in self.__working_data_on_tests if test_name in i]
        self.chose_test.setText(test_name)

    def __get_lesson_id(self):
        """
        Получение индекса выделенной строки, получение ID учебного материала, установка названия выбранного материала.
        :return None
        """
        row_id = self.test_table_widget.currentIndex().row()
        lesson_name = self.test_table_widget.item(row_id, 0).text()
        self.__lesson_id = [i[0] for i in self.__working_data_on_lessons if lesson_name in i]
        self.chose_lesson.setText(lesson_name)

    def __get_appointment_test(self):
        """
        Получение индекса выбранного назначенного теста, и установка названия теста в лейбл.
        :return None
        """
        # Item выбранного элемента
        index = self.appointment_test_list_widget.selectedIndexes()[0]
        # Строка выбранного элемента
        st = index.data()
        test_name = st[15:st.find('|')].strip()
        self.chose_appointment_test.setText(test_name)
        # Данные выбранного теста, [(ID, тип)]
        self.__appointment_test_id = [i[::4] for i in self.__working_data_on_tests if test_name in i]


    @pyqtSlot()
    def __open_lesson(self):
        """
        Запускает виджет изучения материала
        :return None
        """
        if self.__lesson_id:
            self.hide()
            self.__main_window.open_lesson(self.__lesson_id)

    @pyqtSlot()
    def __open_testing(self, page):
        """
        Запускает тестирование. Параметр показывает какой кнопкой была вызвана функция.
        1 - со страницы тесты, 2 - со страницы назначенные тесты.
        :param page:
        :return None
        """
        if page == 1 and self.__test_id:
            self.hide()
            self.__main_window.open_testing(self.__test_id[0][0], self.__test_id[0][1])
        elif page == 2 and self.__appointment_test_id:
            self.hide()
            self.__main_window.open_testing(self.__appointment_test_id[0][0], self.__appointment_test_id[0][1])

    def __refresh_result(self):
        pass

    def __fill_appointment_test_list(self):
        """
        Заполнение списка назначенных тестов
        :return None
        """
        try:
            self.__assigned_tests = self.__db.get_assigned_tests_for_user(self.__user_id)

            for row in self.__assigned_tests:
                elem_lest = ''
                test = self.__db.get_name_time_type_note_on_test(row[0])
                if test == 1:
                    continue

                elem_lest += 'Название теста: ' + test[0] + ' | '
                elem_lest += 'Тип тестирования: ' + test[1] + ' | '
                elem_lest += 'Кол-во вопросов: ' + str(test[2]) + ' | '
                elem_lest += 'Время выполнения: ' + str(test[3]) + ' | '

                elem_lest += 'Назначен: ' + str(row[2])[:-7] + ' | '
                elem_lest += 'Конечный срок: ' + str(row[3]) + ' | '
                elem_lest += 'Состояние: ' + ('Пройден' if row[4] else 'Не пройден') + ' | '
                elem_lest += 'Кол-во попыток: ' + str(row[5]) + ' | '
                elem_lest += 'Примечание: ' + str(row[6]) + ' | '

                self.appointment_test_list_widget.addItem(elem_lest)
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)
