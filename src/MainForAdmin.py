from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.Ui_MainForAdmin import Ui_MainForAdmin


class MainForAdmin(QWidget, Ui_MainForAdmin):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)