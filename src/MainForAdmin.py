from PyQt5.QtWidgets import QWidget, QVBoxLayout
from UI.form_for_admin.Ui_MainForAdmin import Ui_MainForAdmin
from psycopg2 import Error

# My widgets
from src.for_admin.ListOfUser import ListOfUser
from src.for_admin.Analysis import Analysis
from src.for_admin.CreateTesting import CreateTesting
from src.for_admin.CreateLesson import CreateLesson
from src.for_admin.CheckResultTesting import CheckResultTesting


class MainForAdmin(QWidget, Ui_MainForAdmin):
    def __init__(self, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        # ________________________________

        # Методы________________________________
        self.__set_action()
        self.__fill_combobox_users()
        # ________________________________

        # Объекты________________________________
        # tab user
        self.vertical_layout_tab_user = QVBoxLayout(self.tab_user)
        self.vertical_layout_tab_user.setObjectName("vertical_layout_tab_user")
        self.__list_user_group_tag = ListOfUser(parent=self.tab_user, data_base=data_base)
        self.vertical_layout_tab_user.addWidget(self.__list_user_group_tag)

        # tab analysis
        self.vertical_layout_tab_analysis = QVBoxLayout(self.tab_analysis)
        self.vertical_layout_tab_analysis.setObjectName("vertical_layout_tab_analysis")
        self.__analysis = Analysis(parent=self.tab_analysis, data_base=data_base)
        self.vertical_layout_tab_analysis.addWidget(self.__analysis)

        # tab create test
        self.vertical_layout_tab_create_test = QVBoxLayout(self.tab_create_test)
        self.vertical_layout_tab_create_test.setObjectName("vertical_layout_tab_create_test")
        self.__create_test = CreateTesting(parent=self.tab_create_test, data_base=data_base)
        self.vertical_layout_tab_create_test.addWidget(self.__create_test)

        # tab create lesson
        self.vertical_layout_tab_create_lesson = QVBoxLayout(self.tab_create_lesson)
        self.vertical_layout_tab_create_lesson.setObjectName("vertical_layout_tab_create_lesson")
        self.__create_lesson = CreateLesson(parent=self.tab_create_lesson, data_base=self.__db)
        self.vertical_layout_tab_create_lesson.addWidget(self.__create_lesson)
        # ________________________________

    def __set_action(self):
        self.start_check_push_button.clicked.connect(self.__start_check_result)

    def __fill_combobox_users(self):
        """
        Метод заполняет combobox всех тегов
        """
        self.check_user_combo_box.clear()
        try:
            # Получение списка пользователей
            self.__all_user = self.__db.get_list_users()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        # в случае если список будет пустым, то вернётся код 1, и смысла продолжать заполнение нет
        if self.__all_user == 1:
            return

        for row in self.__all_user:
            self.check_user_combo_box.addItem(row[4] + ' ' + row[3] + ' ' + row[5])

    def __start_check_result(self):
        # tab check
        current_user = self.__all_user[self.check_user_combo_box.currentIndex()]
        self.__check_form = CheckResultTesting(parent=self.tab_check, data_base=self.__db, current_user=current_user)
        self.vertical_layout_tab_check.addWidget(self.__check_form)
