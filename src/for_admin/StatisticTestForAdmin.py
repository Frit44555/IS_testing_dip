from PyQt5.QtWidgets import QWidget
from UI.form_for_admin.Ui_StatisticTestForAdmin import Ui_StatisticTestForAdmin
from math import floor


class StatisticTestForAdmin(QWidget, Ui_StatisticTestForAdmin):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Заполнение полей________________________________
        self.name_test_label.setText(data[0])
        self.quantity_quests_label.setText(str(data[1]))
        self.quantity_quessts_in_testing_label.setText(str(data[2]))
        self.average_label.setText(str(data[3]))
        self.reliability_label.setText(str(floor(data[4])))
        self.difficulty_label.setText(str(round(sum(data[5]) / len(data[5]), 2)))
        # ________________________________
