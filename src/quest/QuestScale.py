from UI import ui_quest


class QuestScale(ui_quest.Ui_QuestScale):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def answered(self):
        pass
