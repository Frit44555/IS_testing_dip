class DataBaseQuery:
    def __init__(self, connection, cursor):
        # Подключение к существующей базе данных
        self.__connection = connection
        # Курсор для выполнения операций с базой данных
        self.__cursor = cursor

    @property
    def connection(self):
        return self.__connection

    @property
    def cursor(self):
        return self.__cursor

    def find_admin(self, login, password):
        """
        Описание: Эта функция вернёт значение строку, если введенные логин и пароль правильные
                    и существуют в таблице администраторов. Если совпадений нет вернёт пустую выборку.
        Принимает аргументы: логин, пароль
        Возвращает: ID администратора, логин, имя, фамилия, отчество, примечания.
        :return list or errcode=1
        """
        self.__cursor.callproc('find_admin', [login, password])
        result = self.__cursor.fetchone()
        return result if result else 1

    def registration_admin_on_easy_tests(self, login, password, name, surname, patronymic=None, note=None):
        """
        Описание: Регистрация пользователя в базе данный easy_tests. Добавляет строку в таблицу "users",
                    при этом создаёт соль, с помощью этой соли хэширует пароль, а затем выполняет вставку.
        Принимает аргументы: логин, пароль, имя, фамилия, отчество.
        :return None
        """
        self.__cursor.callproc('registration_admin_on_easy_tests', [login, password, name, surname, patronymic, note])
        return

    def change_admin_password(self, admin_id, password):
        """
        Описание: Эта функция устанавливает новое значение поля группы у пользователя в таблице "user_groups".
        Принимает аргументы: ID пользователя, ID группы.
        :return None
        """
        self.__cursor.callproc('change_admin_password', [admin_id, password])
        return

    def registration_user_on_easy_tests(self, login, password, name, surname, patronymic=None):
        """
        Описание: Регистрация пользователя в базе данный easy_tests. Добавляет строку в таблицу "users",
                    при этом создаёт соль, с помощью этой соли хэширует пароль, а затем выполняет вставку.
        Принимает аргументы: логин, пароль, имя, фамилия, отчество.
        :return None
        """
        self.__cursor.callproc('registration_user_on_easy_tests', [login, password, name, surname, patronymic])
        return

    def find_user(self, login, password):
        """
        Описание: Эта функция вернёт значение строку, если введенные логин и пароль правильные
                    и существуют в таблице. Если совпадений нет вернёт пустую выборку.
        Принимает аргументы: логин, пароль.
        Возвращает: ID пользователя, ID группы, логин, имя, фамилия, отчество, дату регистрации, примечания.
        :return list or errcode=1
        """
        self.__cursor.callproc('find_user', [login, password])
        result = self.__cursor.fetchone()
        return result if result else 1

    def working_data_on_tests(self, group_user):
        """
        Описание: Эта функция вернёт данные, которые необходимы для сборки приложения.
        Принимает аргументы: ID группы пользователя.
        Возвращает: ID теста, массив ID вопросов, ID тега, название теста, тип теста, количество вопросов,
                    время прохождения, примечание.
        :return list or errcode=1
        """
        self.__cursor.callproc('working_data_on_tests', [group_user, ])
        result = self.__cursor.fetchall()
        return result if result else 1

    def working_data_on_lessons(self, group_user):
        """
        Описание: Эта функция вернёт данные, которые необходимы для сборки приложения.
        Принимает аргументы: ID группы пользователя.
        Возвращает: ID учебного материала и его название.
        :return list or errcode=1
        """
        self.__cursor.callproc('working_data_on_lessons', [group_user, ])
        result = self.__cursor.fetchall()
        return result if result else 1

    def return_bals_on_test(self, test_id):
        """
        Описание: Эта функция вернёт данные, которые необходимы для сборки приложения.
        Принимает аргументы: ID группы пользователя.
        Возвращает: ID учебного материала и его название.
        :return list or errcode=1
        """
        self.__cursor.callproc('return_bals_on_test', [test_id, ])
        result = self.__cursor.fetchall()
        return result if result else 1

    def get_name_time_type_note_on_test(self, test_id):
        """
        Описание: Эта функция вернёт названия теста, время прохождения, тип, количества вопросов и примечание.
        Принимает аргументы: ID теста.
        Возвращает: название теста, тип теста, количество вопросов, время прохождения, примечание.
        :return list or errcode=1
        """
        self.__cursor.callproc('get_name_time_type_note_on_test', [test_id, ])
        result = self.__cursor.fetchone()
        return result if result else 1

    def get_results_user(self, user_id):
        """
        Описание: Эта функция отправляет результаты пользователя.
        Принимает аргументы: ID пользователя.
        Возвращает: таблицу результатов.
        :return list or errcode=1
        """
        self.__cursor.callproc('get_results_user', [user_id, ])
        result = self.__cursor.fetchall()
        return result if result else 1

    def get_results_user_is_no_verified(self, user_id):
        """
        Описание: Эта функция отправляет не проверенные результаты пользователя.
        Принимает аргументы: ID пользователя.
        Возвращает: таблицу результатов.
        :return list or errcode=1
        """
        self.__cursor.callproc('get_results_user', [user_id, ])
        result = self.__cursor.fetchone()
        return result if result else 1

    def get_results_all(self):
        """
        Описание: Эта функция отправляет все результаты, предназначено для администратора.
        Возвращает: таблицу результатов.
        :return list or errcode=1
        """
        self.__cursor.callproc('get_results_all')
        result = self.__cursor.fetchall()
        return result if result else 1

    def get_lesson(self, lesson_id):
        """
        Описание: Эта функция вернёт содержимое учебного материала.
        Принимает аргументы: ID учебного материала.
        Возвращает: текст материала.
        :return list or errcode=1
        """
        self.__cursor.callproc('get_lesson', [lesson_id, ])
        result = self.__cursor.fetchone()
        return result if result else 1

    def get_lesson_via_tag(self, tag_name, group_id):
        """
        Описание: Эта функция вернёт ID и имя учебного материала найденного по заданному тегу и ограничителю
                    в виде группы пользователя.
        Принимает аргументы: ID учебного материала, ID группы.
        Возвращает: имя тега.
        :return list or errcode=1
        """
        self.__cursor.callproc('get_lesson_via_tag', [tag_name, group_id])
        result = self.__cursor.fetchall()
        return result if result else 1

    def get_test_via_teg(self, tag_name, group_id):
        """
        Описание: Эта функция вернёт данные тестов, по переданному тегу в соответствии с ограничением по группе.
        Принимает аргументы: ID учебного материала, ID группы.
        Возвращает: имя тега.
        :return list or errcode=1
        """
        self.__cursor.callproc('get_test_via_teg', [tag_name, group_id])
        result = self.__cursor.fetchall()
        return result if result else 1

    def get_questions(self, test_id):
        """
        Описание: Эта функция вернёт все вопросы по заданному тесту.
        Принимает аргументы: ID теста.
        Возвращает: таблицу вопросов.
        :return list or errcode=1
        """
        self.__cursor.callproc('get_questions', [test_id, ])
        result = self.__cursor.fetchall()
        return result if result else 1

    def get_answers(self, result_id):
        """
        Описание: Эта функция вернёт все ответы по заданному результату.
        Принимает аргументы: ID результата.
        Возвращает: таблицу ответов.
        :return list or errcode=1
        """
        self.__cursor.callproc('get_answers', [result_id, ])
        result = self.__cursor.fetchall()
        return result if result else 1

    def get_list_users(self):
        """
        Описание: Эта функция отправляет необходимую информацию по пользователям для администратора.
        Возвращает: ID пользователя, группу пользователя, логин, имя, фамилию, отчество, дату регистрации примечание.
        :return list or errcode=1
        """
        self.__cursor.callproc('get_list_users')
        result = self.__cursor.fetchall()
        return result if result else 1

    def get_sorted_questions(self, test_id):
        """
        Описание: Эта функция отправляет ответы на вопросы по заданному тесту в виде таблицы.
                    Отсортировано по колонке ID вопроса по убыванию.
        Принимает аргументы: ID теста.
        Возвращает: таблицу(ID вопроса, ID ответа, балл, верность решения).
        """
        self.__cursor.callproc('get_sorted_questions', [test_id, ])
        result = self.__cursor.fetchall()
        return result if result else 1

    def get_tags_on_group(self, group_id):
        """
        Описание: Эта функция отправляет доступные теги, по одной группе.
        Принимает аргументы: ID группы.
        Возвращает: таблицу тегов.
        :return list or errcode=1
        """
        self.__cursor.callproc('get_tags_on_group', [group_id, ])
        result = self.__cursor.fetchall()
        return result if result else 1

    def get_tags(self):
        """
        Описание: Эта функция отправляет все теги.
        Возвращает: таблицу тегов.
        :return list or errcode=1
        """
        self.__cursor.callproc('get_tags')
        result = self.__cursor.fetchall()
        return result if result else 1

    def ger_tests_all(self):
        """
        Описание: Эта функция вернёт все существующие тесты.
        Возвращает: таблицу тестов.
        :return list or errcode=1
        """
        self.__cursor.callproc('ger_tests_all')
        result = self.__cursor.fetchall()
        return result if result else 1

    def get_groups_users(self):
        """
        Описание: Эта функция вернёт все группы пользователей.
        Возвращает: таблицу (ID группы, название, массив доступных тегов).
        :return list or errcode=1
        """
        self.__cursor.callproc('get_groups_users')
        result = self.__cursor.fetchall()
        return result if result else 1

    def get_middle_bals_all(self):
        """
        Описание: Эта функция отправляет все средние баллы по тестам
        Возвращает: представление middle_bals
        :return list or errcode=1
        """
        self.__cursor.callproc('get_middle_bals_all')
        result = self.__cursor.fetchall()
        return result if result else 1

    def get_middle_bals_on_test(self, test_id):
        """
        Описание: Эта функция отправляет средниЙ балл по тесту
        Принимает аргументы: ID теста
        Возвращает: представление middle_bals
        :return list or errcode=1
        """
        self.__cursor.callproc('get_middle_bals_on_test', [test_id, ])
        result = self.__cursor.fetchone()
        return result if result else 1

    def get_assigned_tests_for_user(self, user_id):
        """
        Описание: Эта функция отправляет данные о назначенных тестах по конкретному пользователю.
        Принимает аргументы: ID пользователя.
        Возвращает: ID назначенного теста, ID теста, назначенное время, крайний срок, состояние о завершённости,
                    кол-во попыток, примечания.
        :return list or errcode=1
        """
        self.__cursor.callproc('get_assigned_tests_for_user', [user_id, ])
        result = self.__cursor.fetchall()
        return result if result else 1

    def set_user_group(self, user_id, group_id):
        """
        Описание: Эта функция устанавливает новое значение поля группы у пользователя в таблице "user_groups".
        Принимает аргументы: ID пользователя, ID группы.
        :return None
        """
        self.__cursor.callproc('set_user_group', [user_id, group_id])
        return

    def minus_number_of_attempts(self, assigned_test_id):
        """
        Описание: Эта функция количество попыток у нужной записи в таблице "assigned_test".
        Принимает аргументы: ID назначенного теста.
        :return None
        """
        self.__cursor.callproc('minus_number_of_attempts', [assigned_test_id, ])
        return

    def set_completed_in_assigned_test(self, assigned_test_id, completed=None):
        """
        Описание: Эта функция устанавливает значение поля "completed" у таблицы "assigned_test".
        Принимает аргументы: ID назначенный тест, состояние проверки.
        :return None
        """
        self.__cursor.callproc('set_completed_in_assigned_test', [assigned_test_id, completed])
        return

    def add_tag_in_groups_users(self, group_id, available_tag):
        """
        Описание: Эта функция добавляет тег в поле "available_tags" в таблице "groups_users".
        Принимает аргументы: имя, содержимое.
        :return None
        """
        self.__cursor.callproc('add_tag_in_groups_users', [group_id, available_tag])
        return

    def create_answer(self, quest_id, answered, correct=None):
        """
        ВНИМАНИЕ!!! РАБОТАЕТ В СВЯЗКЕ С create_result И ВЫЗЫВАЕТСЯ ДО НЕЁ. 1
        Описание: Эта функция создаёт запись ответа в таблице "answers".
        Принимает аргументы: ID вопроса, данный за задание ответ, правильность ответа.
        Возвращает: ID только что созданного ответов.
        :return tuple
        """
        self.__cursor.callproc('create_answer', [quest_id, answered, correct])
        result = self.__cursor.fetchone()
        return result if result else 1

    def create_result(self, user_id, test_id, answer_id, time_start, time_finish, comment_user=None, verified=False):
        """
        ВНИМАНИЕ!!! РАБОТАЕТ В СВЯЗКЕ С create_answer И ВЫЗЫВАЕТСЯ ПОСЛЕ НЕЁ. 2
        Описание: Эта функция создаёт запись результатов в таблицу "result".
        Принимает аргументы: ID пользователя, ID теста, массив ID ответов, время начала, время конца,
                    комментарии пользователя.
        :return None
        """
        self.__cursor.callproc('create_result', [user_id, test_id, answer_id, time_start,
                                                 time_finish, comment_user, verified])
        return

    def create_question(self, type_quest, question,
                        bals=None, image=None,
                        answer1=None, answer2=None,
                        answer3=None, answer4=None,
                        right_answer=None):
        """
        ВНИМАНИЕ!!! РАБОТАЕТ В СВЯЗКЕ С create_test И ВЫЗЫВАЕТСЯ ДО НЕЁ. 1
        Описание: Эта функция создаёт запись вопроса в таблице "questions".
        Принимает аргументы: тип вопроса, ВОПРОС, балл, картинка, четыре ответа, и правильный ответ.
        Возвращает: ID только что созданного вопроса.
        :return tuple
        """
        self.__cursor.callproc('create_question', [type_quest, question, bals, image, answer1, answer2,
                                                   answer3, answer4, right_answer])
        result = self.__cursor.fetchone()
        return result if result else 1

    def create_test(self, quest_id, tag_id, name, type_test, quantity_of_questions, time_to_complete, note=None):
        """
        ВНИМАНИЕ!!! РАБОТАЕТ В СВЯЗКЕ С create_question И ВЫЗЫВАЕТСЯ ПОСЛЕ НЕЁ. 2
        Описание: Эта функция создаёт запись теста в таблице "tests".
        Принимает аргументы: массив ID вопросов, ID тег, название, тип теста, количество заданий,
                    время выполнения теста, примечание.
        :return None
        """
        self.__cursor.callproc('create_test', [quest_id, tag_id, name, type_test, quantity_of_questions,
                                               time_to_complete, note])
        return

    def create_assigned_test(self, test_id, user_id, deadline, number_of_attempts=1, note=None):
        """
        Описание: Эта функция создаёт запись в таблице "assigned_test".
        Принимает аргументы: ID тест, ID пользователь, конечный срок, количество попыток, примечание.
        :return None
        """
        self.__cursor.callproc('create_assigned_test', [test_id, user_id, deadline, number_of_attempts, note])

    def create_lesson(self, name, content):
        """
        Описание: Эта функция создаёт запись в таблице "lessons".
        Принимает аргументы: название, содержимое.
        :return None
        """
        self.__cursor.callproc('create_lesson', [name, content])
        return

    def create_tag(self, name):
        """
        Описание: Эта функция создаёт запись в таблице "tags".
        Принимает аргументы: название тематики.
        :return None
        """
        self.__cursor.callproc('create_tag', [name, ])
        return

    def create_group_user(self, name, available_tag):
        """
        Описание: Эта функция создаёт запись в таблице "groups_users".
        Принимает аргументы: имя, массив доступных тегов.
        :return None
        """
        self.__cursor.callproc('create_group_user', [name, available_tag])
        return

    def delete_tag(self, tag_id):
        """
        Описание: Эта функция удаляет тег по заданному ID.
        Принимает аргументы: ID тега.
        :return None
        """
        self.__cursor.callproc('delete_tag', [tag_id, ])
        return

    def delete_group_user(self, group_id):
        """
        Описание: Эта функция удаляет группу по заданному ID.
        Принимает аргументы: ID группы.
        :return None
        """
        self.__cursor.callproc('delete_group_user', [group_id, ])
        return

    def delete_user(self, user_id):
        """
        Описание: Эта функция удаляет пользователя по заданному ID.
        Принимает аргументы: ID пользователя.
        :return None
        """
        self.__cursor.callproc('delete_user', [user_id, ])
        return

    def remove_tag_from_group(self, group_id, tag_id):
        """
        Описание: Эта функция удаляет тег из группы.
        Принимает аргументы: ID группы, ID тега.
        :return None
        """
        self.__cursor.callproc('remove_tag_from_group', [group_id, tag_id])
        return
