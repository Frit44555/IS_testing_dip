from PyQt5.QtWidgets import QWidget, QMessageBox
from UI.form_for_admin.Ui_ListOfUser import Ui_ListOfUser
from psycopg2 import Error
from PyQt5.QtCore import pyqtSlot
import src.Words as wrd

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
        """
        Устанавливает действия кнопкам.
        """
        self.create_tag_push_button.clicked.connect(self.__create_tag)
        self.create_group_push_button.clicked.connect(self.__create_group)
        self.change_group_push_button.clicked.connect(self.__change_user_group)
        self.change_tags_group_push_button.clicked.connect(self.__change_group)
        self.users_list_widget.clicked.connect(self.__get_user)
        self.groups_user_list_widget.clicked.connect(self.__get_group)
        self.tags_list_widget.clicked.connect(self.__get_tags)
        self.delete_tag_push_button.clicked.connect(self.__delete_tag)
        self.delete_group_push_button.clicked.connect(self.__delete_group_user)
        self.delete_user_push_button.clicked.connect(self.__delete_user)

    def __fill_user_list(self):
        """
        Заполнение списка пользователей.
        """
        try:
            self.__list_users = self.__db.get_list_users()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        if self.__list_users == 1:
            return

        self.users_list_widget.clear()
        for row in self.__list_users:
            # ID пользователя, группа пользователя, логин, имя, фамилию, отчество, дату регистрации примечание
            elem_list = ''
            elem_list += 'ID: ' + str(row[0]) + ' | '
            elem_list += 'Группа: ' + str(row[1]) + ' | '
            elem_list += 'Имя: ' + row[4] + ' | '
            elem_list += 'Дата регистрации: ' + str(row[6]) + ' | '

            self.users_list_widget.addItem(elem_list)

    def __fill_group_list(self):
        """
        Заполнение списка групп.
        """
        try:
            self.__groups_user = self.__db.get_groups_users()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        if self.__groups_user == 1:
            return

        self.groups_user_list_widget.clear()
        for row in self.__groups_user:
            # ID тега, название
            elem_list = ''
            elem_list += 'ID: ' + str(row[0]) + ' | '
            elem_list += 'Название: ' + row[1] + ' | '

            self.groups_user_list_widget.addItem(elem_list)

    def __fill_tag_list(self):
        """
        Заполнение списка тегов.
        """
        try:
            self.__tags_user = self.__db.get_tags()
        except (Exception, Error) as error:
            print('ERROR QUERY:', error)

        if self.__tags_user == 1:
            return

        self.tags_list_widget.clear()
        for row in self.__tags_user:
            # ID тега, название
            elem_list = ''
            elem_list += 'ID: ' + str(row[0]) + ' | '
            elem_list += 'Название: ' + row[1] + ' | '

            self.tags_list_widget.addItem(elem_list)

    @pyqtSlot()
    def __create_tag(self):
        """
        Метод вызывает окно создания тега.
        """
        self.__dialog_tag = CreateTagDialog(data_base=self.__db)
        self.__dialog_tag.show()

    @pyqtSlot()
    def __create_group(self):
        """
        Метод вызывает окно создания группы.
        """
        self.__dialog_group = CreateGroup(data_base=self.__db)
        self.__dialog_group.show()

    @pyqtSlot()
    def __change_user_group(self):
        """
        Метод вызывает окно изменения группы пользователя.
        """
        self.__dialog_user_group = ChangeUserGroup(data_base=self.__db, data=self.__current_user)
        self.__dialog_user_group.show()

    @pyqtSlot()
    def __change_group(self):
        """
        Метод вызывает окно редактирования группы.
        """
        self.__dialog_user_group = ChangeGroup(data_base=self.__db, data=self.__current_group)
        self.__dialog_user_group.show()

    def __get_user(self):
        """
        Метод запоминает выделенного пользователя в списке пользователей.
        """
        self.change_group_push_button.setEnabled(True)
        self.delete_user_push_button.setEnabled(True)
        index = self.users_list_widget.selectedIndexes()[0].row()
        self.__current_user = self.__list_users[index]

    def __get_group(self):
        """
        Метод запоминает выделенную группу в списке групп.
        """
        self.change_tags_group_push_button.setEnabled(True)
        self.delete_group_push_button.setEnabled(True)
        index = self.groups_user_list_widget.selectedIndexes()[0].row()
        self.__current_group = self.__groups_user[index]

    def __get_tags(self):
        """
        Метод запоминает выделенный тег в списке иегов.
        """
        self.delete_tag_push_button.setEnabled(True)
        index = self.tags_list_widget.selectedIndexes()[0].row()
        self.__current_tag = self.__tags_user[index]

    @pyqtSlot()
    def __delete_tag(self):
        """
        Метод удаляет тег из БД и заново заполняет список.
        """
        qm = QMessageBox
        reply = qm.question(self, wrd.hint_on_list_of_user['tags_delete_group_title'],
                            wrd.hint_on_list_of_user['tags_delete_group_text'],
                            qm.Yes | qm.No)
        # ответ
        if reply == qm.Yes:
            if self.__current_tag and self.__current_tag[0] != 1:
                # Удаление выделенного тега
                try:
                    self.__db.delete_tag(self.__current_tag[0])
                except (Exception, Error) as error:
                    print(error)
                # Выключение кнопки и удаление переменной текущего тега
                self.delete_tag_push_button.setEnabled(False)
                self.__current_tag = None

                self.__db.connection.commit()
                self.__fill_tag_list()

            elif self.__current_tag[0] == 1:
                # При попытке удалить тег по умолчанию
                QMessageBox.about(self, wrd.hint_on_list_of_user['delete_tag_one_title'],
                                  wrd.hint_on_list_of_user['delete_tag_one_text'])

            else:
                # остальные случаи
                QMessageBox.about(self, wrd.hint_on_list_of_user['delete_error_title'],
                                  wrd.hint_on_list_of_user['delete_error_text'])
        else:
            return

    @pyqtSlot()
    def __delete_group_user(self):
        """
        Метод удаляет группу из БД и заново заполняет список.
        """
        qm = QMessageBox
        reply = qm.question(self, wrd.hint_on_list_of_user['groups_users_delete_group_title'],
                            wrd.hint_on_list_of_user['groups_users_delete_group_text'],
                            qm.Yes | qm.No)
        # ответ
        if reply == qm.Yes:
            if self.__current_group and self.__current_group[0] != 1:
                # Удаление выделенного тега
                try:
                    self.__db.delete_group_user(self.__current_group[0])
                except (Exception, Error) as error:
                    print(error)
                # Выключение кнопки и удаление переменной текущей группы
                self.delete_group_push_button.setEnabled(False)
                self.__current_group = None

                self.__db.connection.commit()
                self.__fill_group_list()

            elif self.__current_group[0] == 1:
                # При попытке удалить группу по умолчанию
                QMessageBox.about(self, wrd.hint_on_list_of_user['delete_group_one_title'],
                                  wrd.hint_on_list_of_user['delete_group_one_text'])

            else:
                # остальные случаи
                QMessageBox.about(self, wrd.hint_on_list_of_user['delete_error_title'],
                                  wrd.hint_on_list_of_user['delete_error_text'])
        else:
            return

    @pyqtSlot()
    def __delete_user(self):
        """
        Метод удаляет пользователя из БД и заново заполняет список.
        """
        qm = QMessageBox
        reply = qm.question(self, wrd.hint_on_list_of_user['change_user_group_delete_user_title'],
                            wrd.hint_on_list_of_user['change_user_group_delete_user_text'],
                            qm.Yes | qm.No)
        # ответ
        if reply == qm.Yes:
            if self.__current_user:
                # Удаление выделенного пользователя
                try:
                    self.__db.delete_user(self.__current_user[0])
                except (Exception, Error) as error:
                    print(error)
                # Выключение кнопки и удаление переменной текущего пользователя
                self.delete_user_push_button.setEnabled(False)
                self.__current_user = None

                self.__db.connection.commit()
                self.__fill_user_list()

            else:
                # остальные случаи
                QMessageBox.about(self, wrd.hint_on_list_of_user['delete_error_title'],
                                  wrd.hint_on_list_of_user['delete_error_text'])
        else:
            return
