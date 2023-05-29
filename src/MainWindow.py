from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSlot
from UI.Ui_MainWindow import Ui_MainWindow
import Words as wrd

# My widgets
from Authentication import Authentication
from ListSearch import ListSearch
from Lesson import Lesson
from MainMenu import MainMenu
from Testing import Testing


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        self.__list_search = None
        self.__lesson = None
        self.__authentication = None
        self.__testing = None

        # Картеж
        # Для пользователя (ID пользователя, ID группы, логин, имя, фамилия, отчество, дату регистрации, примечания)
        # Для администратора (ID администратора, логин, имя, фамилия, отчество, примечания)
        self.__user = None
        # ________________________________

        # Объекты________________________________
        self.__authentication = Authentication(main_window=self, data_base=self.__db, parent=self)
        self.work_vertical_layout.addWidget(self.__authentication)
        # ________________________________

        # Опции________________________________
        self.to_main_push_button.setEnabled(False)
        self.exit_push_button.setEnabled(False)
        self.refresh_push_button.setEnabled(False)
        # ________________________________

        # MenuBar________________________________
        main_menu = MainMenu(parent=self)
        self.setMenuBar(main_menu)
        main_menu.about.triggered.connect(self.__about_program)
        # ________________________________

    def __set_action(self):
        """
        Устанавливает состояния и действия виджетам.
        :return None
        """
        # Опции________________________________
        self.to_main_push_button.setEnabled(True)
        self.exit_push_button.setEnabled(True)
        self.refresh_push_button.setEnabled(True)
        # ________________________________

        # Действия________________________________
        self.to_main_push_button.clicked.connect(self.__to_main_page)
        self.refresh_push_button.clicked.connect(self.__refresh_data)
        self.exit_push_button.clicked.connect(self.__authentication_again)
        # ________________________________

    @pyqtSlot()
    def __to_main_page(self):
        """
        Выполняет переход к главному виджету, в зависимости от авторизированного пользователя.
        :return None
        """
        # Включение кнопок "Выйти" и "Обновить"
        self.exit_push_button.setEnabled(True)
        self.refresh_push_button.setEnabled(True)
        if len(self.__user) == 8:
            try:
                if self.__lesson:
                    self.__destroy_active_widget(self.__lesson)
                if self.__testing:
                    self.__destroy_active_widget(self.__testing)
                self.__list_search.show()
            except BaseException as BE:
                print('FATAL ERROR:', BE)

    @pyqtSlot()
    def __refresh_data(self):
        """
        Обновляет данные таблиц и списков главных виджетов.
        :return None
        """
        if len(self.__user) == 8:
            try:
                self.__destroy_active_widget(self.__list_search)
                self.__list_search = ListSearch(main_window=self, data_base=self.__db, user_id=self.__user[0],
                                                group_user=self.__user[1], parent=self)
                self.work_vertical_layout.addWidget(self.__list_search)
            except BaseException as BE:
                print('EXECUTION ERROR:', BE)

    @pyqtSlot()
    def __authentication_again(self):
        """
        Переход в аутентификации из рабочей среды. Закрывает все рабочие виджеты в зависимости от
        авторизированного пользователя.
        :return None
        """
        # Опции________________________________
        self.to_main_push_button.setEnabled(False)
        self.exit_push_button.setEnabled(False)
        self.refresh_push_button.setEnabled(False)
        # ________________________________

        self.__user = None
        if self.__list_search:
            self.__destroy_active_widget(self.__list_search)
        if self.__lesson:
            self.__destroy_active_widget(self.__lesson)
        if self.__authentication:
            self.__destroy_active_widget(self.__authentication)
        if self.__testing:
            self.__destroy_active_widget(self.__testing)

        self.__authentication = Authentication(main_window=self, data_base=self.__db, parent=self)
        self.work_vertical_layout.addWidget(self.__authentication)

    @pyqtSlot()
    def __about_program(self):
        """
        Показывает сведения о разработанной системе.
        :return None
        """
        QMessageBox.about(self, wrd.main_menu['about_program'], wrd.main_menu['about_program_action_text'])

    def __destroy_active_widget(self, active_widget):
        """
        Закрывает переданный виджет.
        :return None
        """
        active_widget.setParent(None)
        if isinstance(active_widget, Lesson):
            self.__lesson = None
        elif isinstance(active_widget, ListSearch):
            self.__list_search = None
        elif isinstance(active_widget, Authentication):
            self.__authentication = None
        elif isinstance(active_widget, Testing):
            self.__testing = None

    def put_form_for_user(self, user):
        """
        Заполнение главного окна, виджетами для пользователя.
        :param user:
        :return None
        """
        try:
            # Закрытие объекта аутентификации
            self.__destroy_active_widget(self.__authentication)
            self.__user = user
            self.__set_action()
            self.__list_search = ListSearch(main_window=self, data_base=self.__db, group_user=user[1],
                                            user_id=user[0], parent=self)
            self.work_vertical_layout.addWidget(self.__list_search)
        except BaseException as BE:
            print('FATAL ERROR:', BE)

    def put_form_for_admin(self, user):
        """
        Заполнение главного окна, для администратора.
        :param user:
        :return None
        """
        try:
            # Закрытие объекта аутентификации
            self.__destroy_active_widget(self.__authentication)
            self.__user = user
            self.__set_action()
        except BaseException as BE:
            print('FATAL ERROR:', BE)

    def open_lesson(self, lesson_id):
        """
        Открывает виджет изучения учебного материала
        :param lesson_id:
        :return None
        """
        # Выключение кнопок "Выйти" и "Обновить"
        self.exit_push_button.setEnabled(False)
        self.refresh_push_button.setEnabled(False)

        self.__lesson = Lesson(data_base=self.__db, lesson_id=lesson_id, parent=self)
        self.work_vertical_layout.addWidget(self.__lesson)

    def open_testing(self, test_id, type_testing):
        """
        Открывает виджет прохождения тестирования
        :param test_id:
        :return:
        """
        # Выключение кнопок "Выйти" и "Обновить"
        self.exit_push_button.setEnabled(False)
        self.refresh_push_button.setEnabled(False)

        try:
            questions = self.__db.get_questions(test_id)
        except BaseException as BE:
            print('EXECUTION ERROR:', BE)

        self.__testing = Testing(data_base=self.__db, test_id=test_id, questions=questions,
                                 user_id=self.__user[0], type_testing=type_testing, parent=self)
        self.work_vertical_layout.addWidget(self.__testing)
