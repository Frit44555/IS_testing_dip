from PyQt5.QtWidgets import QWidget
from UI.Ui_StatisticTestForUser import Ui_Form


class StatisticTestForUser(QWidget, Ui_Form):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Заполнение полей________________________________
        self.name_test_label.setText(data[0])
        self.score_label.setText(data[1])
        self.score_total_label.setText(data[2])
        self.right_quest_label.setText(data[3])
        self.wrong_quest_label.setText(data[4])
        self.time_label.setText(data[5])
        self.middle_score_label.setText(data[6])
        # ________________________________
