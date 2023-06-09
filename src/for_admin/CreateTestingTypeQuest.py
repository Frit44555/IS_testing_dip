from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.Ui_CreateTestingTypeQuest import Ui_CreateTestingTypeQuest

# My widgets
from src.for_admin.quest_forms.QuestOneAnswer import QuestOneAnswer
from src.for_admin.quest_forms.QuestManyAnswers import QuestManyAnswers
from src.for_admin.quest_forms.QuestScale import QuestScale
from src.for_admin.quest_forms.QuestFreeAnswer import QuestFreeAnswer


class CreateTestingTypeQuest(QWidget, Ui_CreateTestingTypeQuest):
    def __init__(self, types, tags, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__root = parent
        self.__types = types
        self.__tags = tags
        # ________________________________

        # Опции и Методы________________________________
        self.__set_actions()
        self.type_testing_combo_box.addItems(self.__types)
        # ________________________________

    def __set_actions(self):
        self.check_properties.clicked.connect(self.__add_form)

    def __add_form(self):
        current_type = self.type_testing_combo_box.currentText()
        self.worl_vertical_layout.addWidget(self.__what_test(current_type))

    def __what_test(self, type):
        """
        Определяет тип задания.
        Возвращает: Объект "задание тестирования".
        :return str
        """
        if type == 'ONE ANSWER':
            return QuestOneAnswer(parent=self, root=self.__root)

        elif type == 'MANY ANSWERS':
            return QuestManyAnswers(parent=self, root=self.__root)

        elif type == 'SCALE':
            return QuestScale(parent=self, root=self.__root)

        elif type == 'FREE RESPONSE':
            return QuestFreeAnswer(parent=self, root=self.__root)

