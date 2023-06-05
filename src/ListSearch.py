from UI.Ui_ListSearch import Ui_ListSearch
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QMessageBox
from PyQt5.QtCore import pyqtSlot
from psycopg2 import Error
from datetime import datetime
import Words as wrd

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
        self.__appointment_test = None
        self.__lesson_id = None
        self.__result_user = None
        self.__tags = None
        self.__appointment_test_id = []
        # ________________________________

        # Функции________________________________
        self.__fill_tabl_test()
        self.__fill_tabl_lesson()
        self.__set_action()
        self.__fill_appointment_test_list()
        # ________________________________

        # Опции________________________________
        self.test_table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lessons_table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # ________________________________

        # Объекты________________________________
        self.__result_user = ResultUser(parent=self, data=self.__db.get_results_user(user_id), data_base=self.__db)
        self.result_grid.addWidget(self.__result_user)
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
        self.find_test_button.clicked.connect(self.__find_test)
        self.find_lesson_button.clicked.connect(self.__find_lesson)
        self.refresh_test_button.clicked.connect(self.__refresh_table_test_search)
        self.refresh_lesson_button.clicked.connect(self.__refresh_table_lesson_search)

    def __fill_tabl_test(self):
        """
        Заполнение таблицы 'Тесты'.
        :return None
        """
        # Обновления тегов
        self.__tags = self.__db.get_tags_on_group(self.__group_user)
        # Получение рабочих данных по таблицам 'тесты' и 'уроки'
        try:
            self.__working_data_on_tests = self.__db.working_data_on_tests(self.__group_user)
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
            return  # Добавить QMessage

    def __fill_tabl_lesson(self):
        """
        Заполнение таблицы "Учебные материалы".
        :return None
        """
        try:
            self.__working_data_on_lessons = self.__db.working_data_on_lessons(self.__group_user)
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

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
            return  # Добавить QMessage

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
        row_id = self.lessons_table_widget.currentIndex().row()
        lesson_name = self.lessons_table_widget.item(row_id, 0).text()
        self.__lesson_id = [i[0] for i in self.__working_data_on_lessons if lesson_name in i][0]
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
        self.__appointment_test = [i[::4] for i in self.__working_data_on_tests if test_name in i]
        self.__appointment_test.append(self.__appointment_test_id[index.row()])

    @pyqtSlot()
    def __open_lesson(self):
        """
        Запускает виджет изучения материала.
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
            # Поиск количества заданий в тесте и время выполнения
            quantity_ant_time = [row[5:7] for row in self.__working_data_on_tests if row[0] == self.__test_id[0][0]]

            self.__main_window.open_testing(test_id=self.__test_id[0][0],
                                            type_testing=self.__test_id[0][1],
                                            quantity=quantity_ant_time[0][0],
                                            time=quantity_ant_time[0][1])
        elif page == 2 and self.__appointment_test:
            self.hide()
            # Поиск количества заданий в тесте и время выполнения
            quantity_ant_time = [row[5:7] for row in self.__working_data_on_tests if row[0] ==
                                 self.__appointment_test[0][0]
                                 ]

            self.__main_window.open_testing(test_id=self.__appointment_test[0][0],
                                            type_testing=self.__appointment_test[0][1],
                                            quantity=quantity_ant_time[0][0],
                                            time=quantity_ant_time[0][1])

            try:
                self.__db.minus_number_of_attempts(self.__appointment_test[1])
                self.__db.connection.commit()
            except (Exception, Error) as error:
                print('ERROR QUERY:', error)

    def __refresh_result(self):
        """
        Метод обновления списка результатов.
        :return None
        """
        if self.__result_user:
            self.__result_user.setParent(None)
            self.__result_user = None
            self.__result_user = ResultUser(parent=self, data=self.__db.get_results_user(self.__user_id),
                                            data_base=self.__db)
            self.result_grid.addWidget(self.__result_user)

    def __fill_appointment_test_list(self):
        """
        Заполнение списка назначенных тестов
        :return None
        """
        try:
            self.__assigned_tests = self.__db.get_assigned_tests_for_user(self.__user_id)
            if self.__assigned_tests == 1:
                return
            # Текущее время
            now = datetime.now()

            for row in self.__assigned_tests:
                # если deadline прошёл
                if row[3] < now and row[-2]:
                    continue

                test = self.__db.get_name_time_type_note_on_test(row[1])
                if test == 1:
                    continue
                # ID назначенного теста если он добавляется в список
                self.__appointment_test_id.append(row[0])

                elem_lest = ''
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

    def __get_name_test_from_search(self):
        """
        Метод получения ключевого слова из поисковой строки страницы "тесты".
        :return None
        """
        text = self.search_on_tests_line_edit.text().strip()
        if text:
            return text
        else:
            QMessageBox.about(self, wrd.search_test['wrong_search_title'], wrd.search_test['wrong_search_text'])
            return 1

    def __get_name_lesson_from_search(self):
        """
        Метод получения ключевого слова из поисковой строки страницы "учебный материалы".
        :return None
        """
        text = self.search_on_lessons_line_edit.text().strip()
        if text:
            return text
        else:
            QMessageBox.about(self, wrd.search_test['wrong_search_title'], wrd.search_test['wrong_search_text'])
            return 1

    @pyqtSlot()
    def __refresh_table_test_search(self):
        """
        Метод обновление таблицы "тесты" и очищение строки поиска.
        :return None
        """
        self.search_on_tests_line_edit.setText('')
        self.__fill_tabl_test()

    @pyqtSlot()
    def __refresh_table_lesson_search(self):
        """
        Метод обновление таблицы "учебные материалы" и очищение строки поиска.
        :return None
        """
        self.search_on_lessons_line_edit.setText('')
        self.__fill_tabl_lesson()

    @pyqtSlot()
    def __find_test(self):
        """
        Метод поиска теста в таблице тестов.
        :return None
        """
        key_word = self.__get_name_test_from_search()
        # Пользователь ничего не ввёл
        if key_word == 1:
            return

        if self.change_search_on_test_combo_box.currentText() == 'Имя':
            # Чистка таблицы
            self.test_table_widget.clear()
            self.test_table_widget.setHorizontalHeaderLabels(["Название", "Тип", "Вопросов", "Время"])
            self.test_table_widget.setRowCount(0)
            numcols = 4  # количество столбцов в таблице
            for row in self.__working_data_on_tests:
                # поиск по ключевому слову
                if key_word.lower() in row[3].lower():
                    numrows = self.test_table_widget.rowCount()
                    self.test_table_widget.setRowCount(numrows + 1)
                    # заполнение таблицы
                    for j in range(numcols):
                        self.test_table_widget.setItem(numrows, j, QTableWidgetItem(str(row[j + 3])))

        elif self.change_search_on_test_combo_box.currentText() == 'Тег':
            tests = None
            for row in self.__tags:
                if key_word.lower() in row[1].lower():
                    try:
                        tests = self.__db.get_test_via_teg(row[1], self.__group_user)
                    except (Exception, Error) as error:
                        print('ERROR QUERY:', error)

            if tests is None:
                QMessageBox.about(self, wrd.wrong_tag['wrong_name_title'], wrd.wrong_tag['wrong_name_text'])
                return

            if tests == 1:
                return

            self.test_table_widget.clear()
            self.test_table_widget.setHorizontalHeaderLabels(["Название", "Тип", "Вопросов", "Время"])
            self.test_table_widget.setRowCount(0)
            numcols = 4  # количество столбцов в таблице
            for row in tests:
                # поиск по ключевому слову
                numrows = self.test_table_widget.rowCount()
                self.test_table_widget.setRowCount(numrows + 1)
                # заполнение таблицы
                for j in range(numcols):
                    self.test_table_widget.setItem(numrows, j, QTableWidgetItem(str(row[j + 3])))

    @pyqtSlot()
    def __find_lesson(self):
        """
        Метод поиска учебного материала в соответствующей таблице.
        :return None
        """
        key_word = self.__get_name_lesson_from_search()
        # Пользователь ничего не ввёл
        if key_word == 1:
            return

        if self.change_search_on_lesson_combo.currentText() == 'Имя':
            # Чистка таблицы
            self.lessons_table_widget.clear()
            self.lessons_table_widget.setHorizontalHeaderLabels(["Название", ])
            self.lessons_table_widget.setRowCount(0)
            numcols = 1  # количество столбцов в таблице
            for row in self.__working_data_on_lessons:
                # поиск по ключевому слову
                if key_word.lower() in row[1].lower():
                    numrows = self.lessons_table_widget.rowCount()
                    self.lessons_table_widget.setRowCount(numrows + 1)
                    # заполнение таблицы
                    for j in range(numcols):
                        self.lessons_table_widget.setItem(numrows, j, QTableWidgetItem(str(row[j + 1])))

        elif self.change_search_on_lesson_combo.currentText() == 'Тег':
            tests = None
            for row in self.__tags:
                if key_word.lower() in row[1].lower():
                    try:
                        tests = self.__db.get_lesson_via_tag(row[1], self.__group_user)
                    except (Exception, Error) as error:
                        print('ERROR QUERY:', error)

            if tests is None:
                QMessageBox.about(self, wrd.wrong_tag['wrong_name_title'], wrd.wrong_tag['wrong_name_text'])
                return

            if tests == 1:
                return

            self.lessons_table_widget.clear()
            self.lessons_table_widget.setHorizontalHeaderLabels(["Название", ])
            self.lessons_table_widget.setRowCount(0)
            # заполнение таблицы
            numcols = 1  # количество столбцов в таблице
            for row in tests:
                numrows = self.lessons_table_widget.rowCount()
                self.lessons_table_widget.setRowCount(numrows + 1)
                for j in range(numcols):
                    self.lessons_table_widget.setItem(numrows, j, QTableWidgetItem(str(row[j + 1])))
