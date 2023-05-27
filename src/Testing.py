from UI import Ui_Testing


class Testing(Ui_Testing):
    def __init__(self, user_id, test_id, data_base, parent=None):
        super().__init__(parent)
        self.setuoUi(self)

        # Переменные________________________________
        self.__user = user_id
        self.__test = test_id
        self.__db = data_base
        # ________________________________

    def __assembly_testing(self, test):
        """
        Собирает тестирование
        :param test:
        :return None
        """
        pass

    def __what_test(self):
        """
        Определяет тип задания.
        Возвращает: тип тестирования.
        :return str
        """
        pass

    def __add_test(self):
        """
        Добавляет задание в тестирование
        :return None
        """
        pass
