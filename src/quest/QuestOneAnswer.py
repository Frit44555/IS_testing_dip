from UI import ui_quest


class QuestOneAnswer(ui_quest.Ui_QuestOneAnswer):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def answered(self):
        pass
