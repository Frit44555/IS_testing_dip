from PyQt5.QtWidgets import QWidget
from UI.Ui_Authentication import Ui_Authentication
from psycopg2 import Error
import Words as wrd
import re
import PrimaryHash as PH


class Authentication(QWidget, Ui_Authentication):
    def __init__(self, main_window, data_base, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Переменные________________________________
        self.__main_window = main_window
        self.__db = data_base
        # ________________________________

        # Функции________________________________
        self.__set_action()
        # ________________________________

    def __set_action(self):
        """
        Устанавливает действия кнопкам.
        :return None
        """
        self.login_button.clicked.connect(self.__check_radio_button)
        self.register_button.clicked.connect(self.__registration_user)

    def __check_radio_button(self):
        """
        Определяет кто заходит в систему.
        :return None
        """
        if self.how_user_radio_button.isChecked():
            self.__authorization_user()
        else:
            self.__authorization_admin()

    def __check_login_password(self, login, password, label):
        """
        Реализация для пароля временная! Поменяй!
        Проверка пароля и логина на правильность. При неверном значении устанавливает в переданный label текст ошибки.
        :return 0 or 1
        """
        # Проверка на соответствие длины
        if len(login) < 4:
            label.setText(wrd.hint_authentication['wrong_length_login'])
            return 1
        elif len(password) < 8:
            label.setText(wrd.hint_authentication['wrong_length_password'])
            return 1
        # Проверка содержимого
        pattern = r"^[a-zA-Z0-9_]+$"
        # Логин
        if not re.fullmatch(pattern, login):
            label.setText(wrd.hint_authentication['wrong_login'])
            return 1
        # Пароль
        elif re.fullmatch(pattern, password):
            # Есть ли цифры
            num = len([c for c in password if 48 <= ord(c) <= 57])
            # Есть ли заглавные буквы
            upper = len([c for c in password if 65 <= ord(c) <= 90])
            # Есть ли строчные буквы
            lower = len([c for c in password if 97 <= ord(c) <= 122])
            if num and upper and lower:
                return 0
            else:
                label.setText(wrd.hint_authentication['wrong_password'])
                return 1

    def __authorization_user(self):
        """
        Авторизация пользователя. При успешном нахождении пользователя в БД, запускает
        сборку виджетов главного окна для пользователя и закрывает форму авторизации.
        :return None
        """
        # Получить текст с эдитов
        login = self.login_line_edit.text()
        password = self.password_line_edit.text()
        # Проверка правильности логина и пароля
        if self.__check_login_password(login, password, self.hint_authorization_text_browser):
            return
        else:
            try:
                user = self.__db.find_user(login, PH.primary_hash(password))
                if user != 1:
                    # Передать кортеж с информацией о пользователе главному окну
                    self.__main_window.put_form_for_user(user)
                    # закрыть форму авторизации
                    self.close()
                else:
                    self.hint_authorization_text_browser.setText(wrd.hint_authentication['wrong_login_or_password'])
            except (Exception, Error) as error:
                print('ERROR QUERY:', error)

    def __authorization_admin(self):
        """
        Авторизация администратора. При успешном нахождении админа в БД, запускает
        сборку виджетов главного окна для админа и закрывает форму авторизации.
        :return None
        """
        # Получить текст с эдитов
        login = self.login_line_edit.text()
        password = self.password_line_edit.text()
        # Проверка правильности логина и пароля
        if self.__check_login_password(login, password, self.hint_authorization_text_browser):
            return
        else:
            try:
                user = self.__db.find_admin(login, PH.primary_hash(password))
                if user != 1:
                    # Передать кортеж с информацией об администраторе главному окну
                    self.__main_window.put_form_for_admin(user)
                    # закрыть форму авторизации
                    self.close()
                else:
                    self.hint_authorization_text_browser.setText(wrd.hint_authentication['wrong_login_or_password'])
            except (Exception, Error) as error:
                print('ERROR QUERY:', error)

    def __registration_user(self):
        """
        Регистрация пользователя в системе.
        :return None
        """
        print(1)
        # Получить текст с эдитов
        surname = self.surname_line_edit.text()
        print(1)
        name = self.name_line_edit.text()
        print(1)
        patronymic = self.patronymic_line_edit.text()
        print(1)
        login = self.login_line_edit_register.text()
        print(1)
        password = self.password_line_edit_register.text()
        print(2)
        # Проверка ФИО
        if len(surname.split()) != 1:
            self.hint_registration_text_browser.setText(wrd.hint_authentication['wrong_surname'])
            return
        elif len(name.split()) != 1:
            self.hint_registration_text_browser.setText(wrd.hint_authentication['wrong_name'])
            return
        elif not 0 <= len(patronymic.split()) <= 1:
            self.hint_registration_text_browser.setText(wrd.hint_authentication['wrong_patronymic'])
            return
        print(3)
        # Проверка правильности логина и пароля
        if self.__check_login_password(login, password, self.hint_registration_text_browser):
            return
        else:
            try:
                # Вызов запроса на авторизацию пользователя
                self.__db.registration_user_on_easy_tests(login, PH.primary_hash(password), name, surname, patronymic)
                # При записи/изменении данных в БД, не забывай про коммит
                self.__db.connection.commit()
                # Вернуть созданного пользователя
                user = self.__db.find_user(login, PH.primary_hash(password))
                if user != 1:
                    # Передать кортеж с информацией о пользователе главному окну
                    self.__main_window.put_form_for_user(user)
                    # закрыть форму авторизации
                    self.close()
                else:
                    self.hint_registration_text_browser.setText(wrd.hint_authentication['oops'])
            except (Exception, Error) as error:
                print('ERROR QUERY:', error)
