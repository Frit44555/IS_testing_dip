from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QuestScale(object):
    def setupUi(self, QuestScale):
        QuestScale.setObjectName("QuestScale")
        QuestScale.resize(900, 500)
        QuestScale.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(13, 130, 149);")
        self.verticalLayout = QtWidgets.QVBoxLayout(QuestScale)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontal_layout_top_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_top_2.setObjectName("horizontal_layout_top_2")
        self.clue_quest_2 = QtWidgets.QLabel(QuestScale)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clue_quest_2.setFont(font)
        self.clue_quest_2.setObjectName("clue_quest_2")
        self.horizontal_layout_top_2.addWidget(self.clue_quest_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_top_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontal_layout_top_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.question_text_browser = QtWidgets.QTextBrowser(QuestScale)
        self.question_text_browser.setMinimumSize(QtCore.QSize(500, 50))
        self.question_text_browser.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.question_text_browser.setFont(font)
        self.question_text_browser.setObjectName("question_text_browser")
        self.horizontalLayout.addWidget(self.question_text_browser)
        self.picture_label = QtWidgets.QLabel(QuestScale)
        self.picture_label.setText("")
        self.picture_label.setObjectName("picture_label")
        self.horizontalLayout.addWidget(self.picture_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontal_layout_middle = QtWidgets.QHBoxLayout()
        self.horizontal_layout_middle.setObjectName("horizontal_layout_middle")
        self.clue_answer = QtWidgets.QLabel(QuestScale)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clue_answer.setFont(font)
        self.clue_answer.setObjectName("clue_answer")
        self.horizontal_layout_middle.addWidget(self.clue_answer)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_middle.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontal_layout_middle)
        self.horizontal_layout_digital = QtWidgets.QHBoxLayout()
        self.horizontal_layout_digital.setObjectName("horizontal_layout_digital")
        self.a0 = QtWidgets.QLabel(QuestScale)
        self.a0.setObjectName("a0")
        self.horizontal_layout_digital.addWidget(self.a0)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_digital.addItem(spacerItem2)
        self.a1 = QtWidgets.QLabel(QuestScale)
        self.a1.setObjectName("a1")
        self.horizontal_layout_digital.addWidget(self.a1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_digital.addItem(spacerItem3)
        self.a2 = QtWidgets.QLabel(QuestScale)
        self.a2.setObjectName("a2")
        self.horizontal_layout_digital.addWidget(self.a2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_digital.addItem(spacerItem4)
        self.a3 = QtWidgets.QLabel(QuestScale)
        self.a3.setObjectName("a3")
        self.horizontal_layout_digital.addWidget(self.a3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_digital.addItem(spacerItem5)
        self.a4 = QtWidgets.QLabel(QuestScale)
        self.a4.setObjectName("a4")
        self.horizontal_layout_digital.addWidget(self.a4)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_digital.addItem(spacerItem6)
        self.a5 = QtWidgets.QLabel(QuestScale)
        self.a5.setObjectName("a5")
        self.horizontal_layout_digital.addWidget(self.a5)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_digital.addItem(spacerItem7)
        self.a6 = QtWidgets.QLabel(QuestScale)
        self.a6.setObjectName("a6")
        self.horizontal_layout_digital.addWidget(self.a6)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_digital.addItem(spacerItem8)
        self.a7 = QtWidgets.QLabel(QuestScale)
        self.a7.setObjectName("a7")
        self.horizontal_layout_digital.addWidget(self.a7)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_digital.addItem(spacerItem9)
        self.a8 = QtWidgets.QLabel(QuestScale)
        self.a8.setObjectName("a8")
        self.horizontal_layout_digital.addWidget(self.a8)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_digital.addItem(spacerItem10)
        self.a9 = QtWidgets.QLabel(QuestScale)
        self.a9.setObjectName("a9")
        self.horizontal_layout_digital.addWidget(self.a9)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_digital.addItem(spacerItem11)
        self.a10 = QtWidgets.QLabel(QuestScale)
        self.a10.setObjectName("a10")
        self.horizontal_layout_digital.addWidget(self.a10)
        self.verticalLayout.addLayout(self.horizontal_layout_digital)
        self.answer_horizontal_slider = QtWidgets.QSlider(QuestScale)
        self.answer_horizontal_slider.setStyleSheet("QSlider::groove:horizontal {  \n"
                                                    "                height: 10px;\n"
                                                    "                margin: 0px;\n"
                                                    "                border-radius: 5px;\n"
                                                    "                background: #B0AEB1;\n"
                                                    "            }\n"
                                                    "QSlider::handle:horizontal {\n"
                                                    "                background: rgb(213, 122, 9);\n"
                                                    "                border: 1px solid  rgb(203, 122, 9);\n"
                                                    "                width: 17px;\n"
                                                    "                margin: -5px 0; \n"
                                                    "                border-radius: 8px;\n"
                                                    "            }")
        self.answer_horizontal_slider.setOrientation(QtCore.Qt.Horizontal)
        self.answer_horizontal_slider.setObjectName("answer_horizontal_slider")
        self.answer_horizontal_slider.setPageStep(1)
        self.answer_horizontal_slider.setRange(0, 10)
        self.verticalLayout.addWidget(self.answer_horizontal_slider)
        spacerItem12 = QtWidgets.QSpacerItem(20, 301, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem12)
        self.confirm_push_button = QtWidgets.QPushButton(QuestScale)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.confirm_push_button.setFont(font)
        self.confirm_push_button.setStyleSheet("background-color: rgb(213, 122, 9);")
        self.confirm_push_button.setObjectName("confirm_push_button")
        self.verticalLayout.addWidget(self.confirm_push_button)

        self.retranslateUi(QuestScale)
        QtCore.QMetaObject.connectSlotsByName(QuestScale)

    def retranslateUi(self, QuestScale):
        _translate = QtCore.QCoreApplication.translate
        QuestScale.setWindowTitle(_translate("QuestScale", "Form"))
        self.clue_quest_2.setText(_translate("QuestScale", "Вопрос:"))
        self.clue_answer.setText(_translate("QuestScale", "На сколько верно?"))
        self.a0.setText(_translate("QuestScale", "0"))
        self.a1.setText(_translate("QuestScale", "1"))
        self.a2.setText(_translate("QuestScale", "2"))
        self.a3.setText(_translate("QuestScale", "3"))
        self.a4.setText(_translate("QuestScale", "4"))
        self.a5.setText(_translate("QuestScale", "5"))
        self.a6.setText(_translate("QuestScale", "6"))
        self.a7.setText(_translate("QuestScale", "7"))
        self.a8.setText(_translate("QuestScale", "8"))
        self.a9.setText(_translate("QuestScale", "9"))
        self.a10.setText(_translate("QuestScale", "10"))
        self.confirm_push_button.setText(_translate("QuestScale", "Подтвердить"))
