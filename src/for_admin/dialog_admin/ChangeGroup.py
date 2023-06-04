from PyQt5.QtWidgets import QWidget, QMessageBox
from UI.form_for_admin.dialog_admin.Ui_ChangeGroup import Ui_Ui_ChangeGroup
from psycopg2 import Error
import src.Words as wrd


class ChangeGroup(QWidget, Ui_Ui_ChangeGroup):
    def __init__(self, data_base, data, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        self.__data = data
        # ________________________________

        # Функции________________________________
        self.__set_action()
        self.__fill_combobox_exists_tags()
        self.__fill_combobox_access_tags()
        # ________________________________

        # Переменные________________________________
        self.apply_push_button.setEnabled(False)
        # ________________________________

        # Установка текста________________________________
        self.group_name_label.setText(data[1])
        # ________________________________

    def __set_action(self):
        """
        Установка действий кнопкам
        """
        self.cancel_push_button.clicked.connect(self.close)
        self.add_tag_push_button.clicked.connect(self.__add_tag)
        self.remove_tag_push_button_3.clicked.connect(self.__remove_tag)
        self.apply_push_button.clicked.connect(self.__apply)

    def __add_tag(self):
        """
        Метод добавления тега в группу
        """
        self.apply_push_button.setEnabled(True)
        index = self.all_tags_combo_box.currentIndex()
        tag_id = self.__all_tag[index][0]

        try:
            # запрос на добавление тега в доступные
            self.__db.add_tag_in_groups_users(self.__data[0], [tag_id, ])
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        self.__fill_combobox_access_tags()

    def __remove_tag(self):
        """
        Метод удаления одного доступного тега из группы
        """
        self.apply_push_button.setEnabled(True)
        if self.access_tags_combo_box.count() > 1:
            index = self.access_tags_combo_box.currentIndex()
            tag_id = self.__tag_on_group[index][0]

            if self.__data[0] == 1 and tag_id == 1:
                QMessageBox.about(self, wrd.hint_on_list_of_user['delete_tag_one_title'],
                                  wrd.hint_on_list_of_user['delete_tag_one_text'])
                return

            try:
                # удаление тегов из доступных
                self.__db.remove_tag_from_group(self.__data[0], tag_id)
            except (Exception, Error) as error:
                print('ERROR QUERY:', error)

            self.__fill_combobox_access_tags()

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
        self.access_tags_combo_box.clear()
        try:
            # Получение тегов доступных группе и всех тегов
            self.__tag_on_group = self.__db.get_tags_on_group(self.__data[0])
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        # в случае если список будет пустым, то вернётся код 1, и смысла продолжать заполнение нет
        if self.__tag_on_group == 1:
            return

        for row in self.__tag_on_group:
            self.access_tags_combo_box.addItem(row[1])

    def __apply(self):
        try:
            self.__db.connection.commit()
            self.close()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

