from PyQt5.QtWidgets import QMenuBar
import Words as wrd


class MainMenu(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Вкладки________________________________
        help_menu = self.addMenu(wrd.main_menu['help'])
        # ________________________________

        # Пункты________________________________
        self.__about = help_menu.addAction(wrd.main_menu['about_program'])
        # ________________________________

    @property
    def about(self):
        return self.__about
