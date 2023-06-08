from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QuestOneAnswer(object):
    def setupUi(self, QuesOneAnswer):
        QuesOneAnswer.setObjectName("QuesOneAnswer")
        QuesOneAnswer.resize(900, 500)
        QuesOneAnswer.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(13, 130, 149);")
        self.verticalLayout = QtWidgets.QVBoxLayout(QuesOneAnswer)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontal_layout_top = QtWidgets.QHBoxLayout()
        self.horizontal_layout_top.setObjectName("horizontal_layout_top")
        self.hint_quest = QtWidgets.QLabel(QuesOneAnswer)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hint_quest.setFont(font)
        self.hint_quest.setObjectName("hint_quest")
        self.horizontal_layout_top.addWidget(self.hint_quest)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_top.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontal_layout_top)
        self.horizontal_layout_quest = QtWidgets.QHBoxLayout()
        self.horizontal_layout_quest.setObjectName("horizontal_layout_quest")
        self.question_text_edit = QtWidgets.QTextEdit(QuesOneAnswer)
        self.question_text_edit.setMinimumSize(QtCore.QSize(500, 50))
        self.question_text_edit.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.question_text_edit.setFont(font)
        self.question_text_edit.setObjectName("question_text_edit")
        self.horizontal_layout_quest.addWidget(self.question_text_edit)
        self.picture_label = QtWidgets.QLabel(QuesOneAnswer)
        self.picture_label.setText("")
        self.picture_label.setObjectName("picture_label")
        self.horizontal_layout_quest.addWidget(self.picture_label)
        self.verticalLayout.addLayout(self.horizontal_layout_quest)
        self.horizontal_layout_buttom = QtWidgets.QHBoxLayout()
        self.horizontal_layout_buttom.setObjectName("horizontal_layout_buttom")
        self.hint_answers = QtWidgets.QLabel(QuesOneAnswer)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hint_answers.setFont(font)
        self.hint_answers.setObjectName("hint_answers")
        self.horizontal_layout_buttom.addWidget(self.hint_answers)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_buttom.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontal_layout_buttom)
        self.answers_form_layout = QtWidgets.QFormLayout()
        self.answers_form_layout.setObjectName("answers_form_layout")
        self.answer1_radio_button = QtWidgets.QRadioButton(QuesOneAnswer)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.answer1_radio_button.setFont(font)
        self.answer1_radio_button.setText("")
        self.answer1_radio_button.setObjectName("answer1_radio_button")
        self.answers_form_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.answer1_radio_button)
        self.answer1_text_edit = QtWidgets.QTextEdit(QuesOneAnswer)
        self.answer1_text_edit.setMinimumSize(QtCore.QSize(500, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.answer1_text_edit.setFont(font)
        self.answer1_text_edit.setObjectName("answer1_text_edit")
        self.answers_form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.answer1_text_edit)
        self.answer2_radio_button = QtWidgets.QRadioButton(QuesOneAnswer)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.answer2_radio_button.setFont(font)
        self.answer2_radio_button.setText("")
        self.answer2_radio_button.setObjectName("answer2_radio_button")
        self.answers_form_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.answer2_radio_button)
        self.answer2_text_edit = QtWidgets.QTextEdit(QuesOneAnswer)
        self.answer2_text_edit.setMinimumSize(QtCore.QSize(500, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.answer2_text_edit.setFont(font)
        self.answer2_text_edit.setObjectName("answer2_text_edit")
        self.answers_form_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.answer2_text_edit)
        self.answer3_radio_button = QtWidgets.QRadioButton(QuesOneAnswer)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.answer3_radio_button.setFont(font)
        self.answer3_radio_button.setText("")
        self.answer3_radio_button.setObjectName("answer3_radio_button")
        self.answers_form_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.answer3_radio_button)
        self.answer3_text_edit = QtWidgets.QTextEdit(QuesOneAnswer)
        self.answer3_text_edit.setMinimumSize(QtCore.QSize(500, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.answer3_text_edit.setFont(font)
        self.answer3_text_edit.setObjectName("answer3_text_edit")
        self.answers_form_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.answer3_text_edit)
        self.answer4_radio_button = QtWidgets.QRadioButton(QuesOneAnswer)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.answer4_radio_button.setFont(font)
        self.answer4_radio_button.setText("")
        self.answer4_radio_button.setObjectName("answer4_radio_button")
        self.answers_form_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.answer4_radio_button)
        self.answer4_text_edit = QtWidgets.QTextEdit(QuesOneAnswer)
        self.answer4_text_edit.setMinimumSize(QtCore.QSize(500, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.answer4_text_edit.setFont(font)
        self.answer4_text_edit.setObjectName("answer4_text_edit")
        self.answers_form_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.answer4_text_edit)
        self.verticalLayout.addLayout(self.answers_form_layout)
        self.confirm_push_button = QtWidgets.QPushButton(QuesOneAnswer)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.confirm_push_button.setFont(font)
        self.confirm_push_button.setStyleSheet("QPushButton { background-color: rgb(213, 122, 9);}\n"
                                                    "QPushButton:enabled{ color: rgb(255, 255, 255); }\n"
                                                    "QPushButton:disabled{ background:#a2979c; }")
        self.confirm_push_button.setObjectName("confirm_push_button")
        self.verticalLayout.addWidget(self.confirm_push_button)

        self.retranslateUi(QuesOneAnswer)
        QtCore.QMetaObject.connectSlotsByName(QuesOneAnswer)

    def retranslateUi(self, QuesOneAnswer):
        _translate = QtCore.QCoreApplication.translate
        QuesOneAnswer.setWindowTitle(_translate("QuesOneAnswer", "Form"))
        self.hint_quest.setText(_translate("QuesOneAnswer", "Вопрос:"))
        self.hint_answers.setText(_translate("QuesOneAnswer", "Выберите ответ:"))
        self.answer1_text_edit.setHtml(_translate("QuesOneAnswer",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.confirm_push_button.setText(_translate("QuesOneAnswer", "Подтвердить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateLesson = QtWidgets.QWidget()
    ui = Ui_QuestOneAnswer()
    ui.setupUi(CreateLesson)
    CreateLesson.show()
    sys.exit(app.exec_())
