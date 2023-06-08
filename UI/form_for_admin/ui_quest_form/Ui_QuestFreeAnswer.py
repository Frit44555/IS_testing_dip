from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QuestFreeAnswer(object):
    def setupUi(self, QuestFreeAnswer):
        QuestFreeAnswer.setObjectName("QuestFreeAnswer")
        QuestFreeAnswer.resize(900, 500)
        QuestFreeAnswer.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(13, 130, 149);")
        self.verticalLayout = QtWidgets.QVBoxLayout(QuestFreeAnswer)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontal_layout_top_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_top_2.setObjectName("horizontal_layout_top_2")
        self.hint_quest = QtWidgets.QLabel(QuestFreeAnswer)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hint_quest.setFont(font)
        self.hint_quest.setObjectName("hint_quest")
        self.horizontal_layout_top_2.addWidget(self.hint_quest)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_top_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontal_layout_top_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.question_text_edit = QtWidgets.QTextEdit(QuestFreeAnswer)
        self.question_text_edit.setMinimumSize(QtCore.QSize(500, 50))
        self.question_text_edit.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.question_text_edit.setFont(font)
        self.question_text_edit.setObjectName("question_text_edit")
        self.horizontalLayout.addWidget(self.question_text_edit)
        self.picture_label = QtWidgets.QLabel(QuestFreeAnswer)
        self.picture_label.setText("")
        self.picture_label.setObjectName("picture_label")
        self.horizontalLayout.addWidget(self.picture_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontal_layout_middle = QtWidgets.QHBoxLayout()
        self.horizontal_layout_middle.setObjectName("horizontal_layout_middle")
        self.hint_answer = QtWidgets.QLabel(QuestFreeAnswer)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hint_answer.setFont(font)
        self.hint_answer.setObjectName("hint_answer")
        self.horizontal_layout_middle.addWidget(self.hint_answer)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_middle.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontal_layout_middle)
        self.answer_text_edit = QtWidgets.QTextEdit(QuestFreeAnswer)
        self.answer_text_edit.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.answer_text_edit.setFont(font)
        self.answer_text_edit.setObjectName("answer_text_edit")
        self.verticalLayout.addWidget(self.answer_text_edit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 161, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.confirm_push_button = QtWidgets.QPushButton(QuestFreeAnswer)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.confirm_push_button.setFont(font)
        self.confirm_push_button.setStyleSheet("QPushButton { background-color: rgb(213, 122, 9);}\n"
                                                    "QPushButton:enabled{ color: rgb(255, 255, 255); }\n"
                                                    "QPushButton:disabled{ background:#a2979c; }")
        self.confirm_push_button.setObjectName("confirm_push_button")
        self.verticalLayout.addWidget(self.confirm_push_button)

        self.retranslateUi(QuestFreeAnswer)
        QtCore.QMetaObject.connectSlotsByName(QuestFreeAnswer)

    def retranslateUi(self, QuestFreeAnswer):
        _translate = QtCore.QCoreApplication.translate
        QuestFreeAnswer.setWindowTitle(_translate("QuestFreeAnswer", "Form"))
        self.hint_quest.setText(_translate("QuestFreeAnswer", "Вопрос:"))
        self.hint_answer.setText(_translate("QuestFreeAnswer", "Введите ответ"))
        self.answer_text_edit.setPlaceholderText(_translate("QuestFreeAnswer", "Введите ответ здесь..."))
        self.confirm_push_button.setText(_translate("QuestFreeAnswer", "Подтвердить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateLesson = QtWidgets.QWidget()
    ui = Ui_QuestFreeAnswer()
    ui.setupUi(CreateLesson)
    CreateLesson.show()
    sys.exit(app.exec_())
