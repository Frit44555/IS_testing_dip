from PyQt5.QtWidgets import QWidget
from psycopg2 import Error
from UI.form_for_admin.Ui_CheckResultTesting import Ui_CheckResultTesting
from src.for_admin.CheckResultTestingQuest import CheckResultTestingQuest


class CheckResultTesting(QWidget, Ui_CheckResultTesting):
    def __init__(self, data_base, current_user, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        self.__current_user = current_user
        # ________________________________

        # Методы________________________________
        self.__set_action()
        # ________________________________

        # Опции________________________________
        self.complete_button.setEnabled(False)
        # ________________________________

    def __set_action(self):
        self.stop_button.clicked.connect(self.__close)

    def __enable_button(self):
        """
        Включает кнопку завершения проверки
        """
        self.complete_button.setEnabled(True)

    def __close(self):
        self.setParent(None)
        self.close()

    def __assembly_testing(self):
        """
        Собирает проверку
        """
        try:
            self.__quest = self.__db.get_results_user_is_no_verified(self.__current_user)
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        if self.__quest == 1:
            return

        self.__answers = self.__db.get_questions_require_verification(self.__quest[3])

        if self.__answers == 1:
            return

        # Заполнение вкладок TadWidget заданиями
        for i in range(self.__answers):
            # Текущий индекс виджета
            index = self.quests_tab_widget.count()
            # виджет который добавиться на вкладку
            tabPage = CheckResultTestingQuest(parent=self, data=self.__answers[:3])
            # добавление страницы на вкладку
            self.quests_tab_widget.insertTab(index, tabPage, f"{i + 1}")
            self.quests_tab_widget.setCurrentIndex(index)

        # установка текущей вкладки в 0, чтобы открывалась первое задание, а не последнее созданное
        self.quests_tab_widget.setCurrentIndex(0)

    def __add_answer(self):
        pass
