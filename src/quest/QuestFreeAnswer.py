from UI import ui_quest


class QuestFreeAnswer(ui_quest.Ui_QuestFreeAnswer):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def answered(self):
        pass
