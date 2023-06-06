from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.Ui_StatisticTestForAdmin import Ui_StatisticTestForAdmin


class StatisticTestForAdmin(QWidget, Ui_StatisticTestForAdmin):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setupUi(self)
