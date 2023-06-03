from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.Ui_ListOfUser import Ui_ListOfUser
from psycopg2 import Error
from PyQt5.QtCore import pyqtSlot

# My widgets
from src.for_admin.dialog_admin.CreateTagDialog import CreateTagDialog
from src.for_admin.dialog_admin.ChangeUserGroup import ChangeUserGroup
from src.for_admin.dialog_admin.CreateGroup import CreateGroup
from src.for_admin.dialog_admin.ChangeGroup import ChangeGroup


class ListOfUser(QWidget, Ui_ListOfUser):
    def __init__(self, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__db = data_base
        self.__list_users = None
        self.__groups_user = None
        self.__tags_user = None

        self.__current_user = None
        self.__current_group = None
        self.__current_tag = None
        # ________________________________

        # Функции________________________________
        self.__fill_user_list()
        self.__fill_group_list()
        self.__fill_tag_list()
        self.__set_action()
        # ________________________________

        # Опции________________________________
        self.change_group_push_button.setEnabled(False)
        self.change_tags_group_push_button.setEnabled(False)
        self.delete_user_push_button.setEnabled(False)
        self.delete_group_push_button.setEnabled(False)
        self.delete_tag_push_button.setEnabled(False)
        # ________________________________

    def __set_action(self):
        self.create_tag_push_button.clicked.connect(self.__create_tag)
        self.create_group_push_button.clicked.connect(self.__create_group)
        self.change_group_push_button.clicked.connect(self.__change_user_group)
        self.change_tags_group_push_button.clicked.connect(self.__change_group)
        self.users_list_widget.clicked.connect(self.__get_user)
        self.groups_user_list_widget.clicked.connect(self.__get_group)
        self.tags_list_widget.clicked.connect(self.__get_tags)

    def __fill_user_list(self):
        """
        Заполнение списка назначенных тестов
        :return None
        """
        try:
            self.__list_users = self.__db.get_list_users()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        if self.__list_users == 1:
            return

        for row in self.__list_users:
            # ID пользователя, группу пользователя, логин, имя, фамилию, отчество, дату регистрации примечание
            elem_lest = ''
            elem_lest += 'Login: ' + row[2] + ' | '
            elem_lest += 'Группа: ' + str(row[1]) + ' | '
            elem_lest += 'Имя: ' + row[4] + ' | '
            elem_lest += 'Дата регистрации: ' + str(row[6]) + ' | '

            self.users_list_widget.addItem(elem_lest)

    def __fill_group_list(self):
        try:
            self.__groups_user = self.__db.get_groups_users()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        if self.__groups_user == 1:
            return

        for row in self.__groups_user:
            # ID тега, название
            elem_lest = ''
            elem_lest += 'ID: ' + str(row[0]) + ' | '
            elem_lest += 'Название: ' + row[1] + ' | '

            self.groups_user_list_widget.addItem(elem_lest)

    def __fill_tag_list(self):
        try:
            self.__tags_user = self.__db.get_tags()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        if self.__tags_user == 1:
            return

        for row in self.__tags_user:
            # ID тега, название
            elem_lest = ''
            elem_lest += 'ID: ' + str(row[0]) + ' | '
            elem_lest += 'Название: ' + row[1] + ' | '

            self.tags_list_widget.addItem(elem_lest)

    @pyqtSlot()
    def __create_tag(self):
        self.__dialog_tag = CreateTagDialog(data_base=self.__db)
        self.__dialog_tag.show()

    @pyqtSlot()
    def __create_group(self):
        self.__dialog_group = CreateGroup(data_base=self.__db)
        self.__dialog_group.show()

    @pyqtSlot()
    def __change_user_group(self):
        self.__dialog_user_group = ChangeUserGroup(data_base=self.__db, data=self.__current_user)
        self.__dialog_user_group.show()

    @pyqtSlot()
    def __change_group(self):
        self.__dialog_user_group = ChangeGroup(data_base=self.__db, data=self.__current_group)
        self.__dialog_user_group.show()

    def __get_user(self):
        self.change_group_push_button.setEnabled(True)
        self.delete_user_push_button.setEnabled(True)
        index = self.users_list_widget.selectedIndexes()[0].row()
        self.__current_user = self.__list_users[index]

    def __get_group(self):
        self.change_tags_group_push_button.setEnabled(True)
        self.delete_group_push_button.setEnabled(True)
        index = self.groups_user_list_widget.selectedIndexes()[0].row()
        self.__current_group = self.__groups_user[index]

    def __get_tags(self):
        self.delete_tag_push_button.setEnabled(True)
        index = self.tags_list_widget.selectedIndexes()[0].row()
        self.__current_tag = self.__tags_user[index]
