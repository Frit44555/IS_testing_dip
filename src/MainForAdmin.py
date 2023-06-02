from PyQt5.QtWidgets import QWidget, QVBoxLayout
from UI.form_for_admin.Ui_MainForAdmin import Ui_MainForAdmin

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

        # Функции________________________________
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
        self.__create_lesson = CreateLesson(parent=self.tab_create_lesson)
        self.vertical_layout_tab_create_lesson.addWidget(self.__create_lesson)

        # tab check
        self.__check_form = CheckResultTesting(parent=self.tab_check)
        self.vertical_layout_tab_check.addWidget(self.__check_form)
        # ________________________________
