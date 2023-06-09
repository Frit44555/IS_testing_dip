from PyQt5.QtWidgets import QWidget, QMessageBox
from UI.form_for_admin.Ui_CreateTesting import Ui_CreateTesting
import src.Words as wrd
from psycopg2 import Error

# My widgets
from src.for_admin.CreateTestingTypeQuest import CreateTestingTypeQuest


class CreateTesting(QWidget, Ui_CreateTesting):
    def __init__(self, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        self.__dialog = None
        self.__time = None
        self.__quantity = None
        self.__current_quantity = 0
        self.__questions = []
        self.__type_test = {
            'Предопределенные ответы': 'PREDEFINED',
            'Смешанный (без шкал)': 'MIXED',
            'Только шкалы (от 0 до 10)': 'SCALE',
            'Только свободные ответы': 'FREE RESPONSE'
        }
        # ________________________________

        # Функции________________________________
        self.__set_action()
        self.__fill_combobox_exists_tags()
        # ________________________________

        # Опции________________________________
        self.create_testing_push_button.setEnabled(False)
        self.close_push_button.setEnabled(False)
        # ________________________________

    @property
    def questions(self):
        return self.__questions

    @questions.setter
    def questions(self, i):
        self.__questions.append(i)

    def __set_action(self):
        """
        Устанавливает действия кнопкам.
        """
        self.check_properties.clicked.connect(self.__check)
        self.close_push_button.clicked.connect(self._close_creator)
        self.create_testing_push_button.clicked.connect(self.__create_test)

    def __fill_combobox_exists_tags(self):
        """
        Метод заполняет combobox всех тегов
        """
        self.all_tags_combo_box.clear()
        try:
            # Получение тегов доступных группе и всех тегов
            self.__all_tag = self.__db.get_tags()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        # в случае если список будет пустым, то вернётся код 1, и смысла продолжать заполнение нет
        if self.__all_tag == 1:
            return

        for row in self.__all_tag:
            self.all_tags_combo_box.addItem(row[1])

    def __check(self):
        """
        Проверка формы перед созданием.
        """
        if self.type_testing_combo_box.currentText() == 'Предопределенные ответы':
            self.__assembly_testing(types=['ONE ANSWER', 'MANY ANSWERS'])
        elif self.type_testing_combo_box.currentText() == 'Смешанный (без шкал)':
            self.__assembly_testing(types=['ONE ANSWER', 'MANY ANSWERS', 'FREE RESPONSE'])
        elif self.type_testing_combo_box.currentText() == 'Только шкалы (от 0 до 10)':
            self.__assembly_testing(types=['SCALE', ])
        elif self.type_testing_combo_box.currentText() == 'Только свободные ответы':
            self.__assembly_testing(types=['FREE RESPONSE', ])

    def __assembly_testing(self, types):
        """
        Собирает тестирование
        :param test:
        :return None
        """
        self.__time = self.time_spin_box.value()
        self.__quantity = self.quantity_spin_box.value()

        # Заполнение вкладок TadWidget заданиями
        for i in range(self.__quantity):
            # Текущий индекс виджета
            index = self.create_quests_tab_widget.count()
            # виджет который добавиться на вкладку
            tabPage = CreateTestingTypeQuest(parent=self, types=types, tags=self.__db.get_tags())
            # добавление страницы на вкладку
            self.create_quests_tab_widget.insertTab(index, tabPage, f"{i + 1}")
            self.create_quests_tab_widget.setCurrentIndex(index)

        # установка текущей вкладки в 0, чтобы открывалась первое задание, а не последнее созданное
        self.create_quests_tab_widget.setCurrentIndex(0)

        # выключение кнопок
        self.type_testing_combo_box.setEnabled(False)
        self.quantity_spin_box.setEnabled(False)
        self.time_spin_box.setEnabled(False)
        self.check_properties.setEnabled(False)

        # включение кнопки закрыть и создать
        self.close_push_button.setEnabled(True)
        self.create_testing_push_button.setEnabled(True)

    def _close_creator(self):
        if self.__dialog:
            self.__dialog = None
        self.__time = None
        self.__quantity = None
        self.create_quests_tab_widget.clear()
        self.__questions.clear()

        # включение кнопок
        self.type_testing_combo_box.setEnabled(True)
        self.quantity_spin_box.setEnabled(True)
        self.time_spin_box.setEnabled(True)
        self.check_properties.setEnabled(True)

        # выключение кнопки закрыть и создать
        self.close_push_button.setEnabled(False)
        self.create_testing_push_button.setEnabled(False)

    def __create_test(self):  # , tag_id, name, type_testing, quantity_of_questions):
        if self.__quantity != len(self.__questions):
            QMessageBox.about(self, wrd.creater_testing['create_test_difference_quantity_quest_title'],
                              wrd.creater_testing['create_test_difference_quantity_quest_text'])
            return

        # создание вопросов
        quest_id = []  # ID заданий
        for row in self.__questions:
            try:
                #  тип вопроса, ВОПРОС, балл, картинка, четыре ответа, и правильный ответ.
                quest_id.extend(self.__db.create_question(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                                          row[7], row[8]))
            except (Exception, Error) as error:
                print('ERROR QUERY:', error)

        name = self.name_line_edit.text()
        tag_id = self.all_tags_combo_box.currentIndex()
        type_testing = self.__type_test[self.type_testing_combo_box.currentText()]
        quantity_of_questions = self.quantity_spin_box.value()
        time_to_complete = self.time_spin_box.value()
        try:
            self.__db.create_test(quest_id, self.__all_tag[tag_id][0], name, type_testing,
                                  quantity_of_questions, time_to_complete)
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        try:
            self.__db.connection.commit()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        self._close_creator()
