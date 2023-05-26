from PyQt5.QtWidgets import QMainWindow
from UI.Ui_MainWindow import Ui_MainWindow
from Authentication import Authentication
from ListSearch import ListSearch
from Lesson import Lesson


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        self.__user = None
        self.__list_search = None
        self.__lesson = None
        # ________________________________

        # Функции________________________________
        self.authentication = Authentication(main_window=self, data_base=self.__db)
        self.work_vertical_layout.addWidget(self.authentication)
        # ________________________________

        # Опции________________________________
        self.to_main_push_button.setEnabled(False)
        self.exit_push_button.setEnabled(False)
        self.update_push_button.setEnabled(False)
        # ________________________________

    def __set_action(self):
        self.to_main_push_button.setEnabled(True)
        self.exit_push_button.setEnabled(True)
        self.update_push_button.setEnabled(True)
        self.to_main_push_button.clicked.connect(self.destroy_active_widget)

    def __to_main_page(self):
        if self.__list_search:
            self.__list_search.show()
            self.__destroy_active_widget()

    def destroy_active_widget(self):
        if self.__lesson:
            try:
                self.__lesson.setParent(None)
                self.__list_search.show()
            except BaseException as BE:
                print('FATAL ERROR:', BE)

    def put_form_for_user(self, user):
        try:
            del self.authentication
            self.__user = user
            self.__set_action()
            self.__list_search = ListSearch(main_window=self, data_base=self.__db, group_user=user[1])
            self.work_vertical_layout.addWidget(self.__list_search)
        except BaseException as BE:
            print('FATAL ERROR:', BE)

    def put_form_for_admin(self, user):
        try:
            del self.authentication
            self.__user = user
            self.__set_action()
        except BaseException as BE:
            print('FATAL ERROR:', BE)

    def open_lesson(self, lesson_id):
        # ПЕРЕДАЙ ID МАТЕРИАЛА А НЕ ГРУППЫ
        try:
            self.__lesson = Lesson(data_base=self.__db, lesson_id=lesson_id)
            self.work_vertical_layout.addWidget(self.__lesson)
        except BaseException as BE:
            print('FATAL ERROR:', BE)

