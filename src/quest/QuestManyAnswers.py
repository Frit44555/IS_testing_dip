from UI import ui_quest


class QuestManyAnswers(ui_quest.Ui_QuestManyAnswers):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def answered(self):
        pass
