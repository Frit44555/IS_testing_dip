from PyQt5.QtWidgets import QWidget, QMessageBox
from UI.form_for_admin.dialog_admin.Ui_CreateGroup import Ui_Ui_CreateGroup
from psycopg2 import Error
import src.Words as wrd


class CreateGroup(QWidget, Ui_Ui_CreateGroup):
    def __init__(self, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        self.__access_tags = []
        # ________________________________

        # Функции________________________________
        self.__set_action()
        self.__fill_combobox_exists_tags()
        # ________________________________

        # Переменные________________________________
        self.create_group_push_button.setEnabled(False)
        # ________________________________

    def __set_action(self):
        self.cancel_push_button.clicked.connect(self.close)
        self.add_tag_push_button.clicked.connect(self.__add_tag)
        self.remove_tag_push_button_3.clicked.connect(self.__remove_tag)
        self.create_group_push_button.clicked.connect(self.__apply)

    def __add_tag(self):
        self.create_group_push_button.setEnabled(True)
        index = self.all_tags_combo_box.currentIndex()
        tag = self.__all_tag[index]
        self.__access_tags.append(tag)

        self.__fill_combobox_access_tags()

    def __remove_tag(self):
        self.create_group_push_button.setEnabled(True)
        if self.access_tags_combo_box.count() > 1:
            index = self.access_tags_combo_box.currentIndex()
            tag_id = self.__access_tags[index]
            self.__access_tags.remove(tag_id)

            self.__fill_combobox_access_tags()

        elif self.access_tags_combo_box.count() == 0:
            QMessageBox.about(self, wrd.hint_on_list_of_user['create_group_tag_equals_zero_title'],
                              wrd.hint_on_list_of_user['create_group_tag_equals_zero_text'])

        else:
            QMessageBox.about(self, wrd.hint_on_list_of_user['delete_group_tag_less_then_one_title'],
                              wrd.hint_on_list_of_user['delete_group_tag_less_then_one_text'])

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

    def __fill_combobox_access_tags(self):
        """
        Метод заполняет combobox доступных группе
        """
        if not self.__access_tags:
            return

        self.access_tags_combo_box.clear()
        for row in self.__access_tags:
            self.access_tags_combo_box.addItem(row[1])

    def __apply(self):
        name = self.name_line_edit.text().strip()
        print(name)
        if not name:
            QMessageBox.about(self, wrd.hint_on_list_of_user['create_group_no_name_title'],
                              wrd.hint_on_list_of_user['create_group_no_name_text'])
            return

        if self.__access_tags:
            tags = [elem[0] for elem in self.__access_tags]
            try:
                self.__db.create_group_user(name, tags)
                self.__db.connection.commit()
                self.close()
            except (Exception, Error) as error:
                print('ERROR QUERY:', error)

        else:
            QMessageBox.about(self, wrd.hint_on_list_of_user['create_group_tag_less_then_one_title'],
                              wrd.hint_on_list_of_user['create_group_tag_less_then_one_text'])
