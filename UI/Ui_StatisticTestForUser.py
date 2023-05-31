# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StatisticTestForUser.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(215, 202)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(215, 202))
        Form.setMaximumSize(QtCore.QSize(215, 202))
        Form.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(13, 130, 149);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.hint_label = QtWidgets.QLabel(Form)
        self.hint_label.setMinimumSize(QtCore.QSize(210, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hint_label.setFont(font)
        self.hint_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hint_label.setObjectName("hint_label")
        self.verticalLayout_3.addWidget(self.hint_label)
        self.name_test_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_test_label.setFont(font)
        self.name_test_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_test_label.setObjectName("name_test_label")
        self.verticalLayout_3.addWidget(self.name_test_label)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.hint_label_2 = QtWidgets.QLabel(Form)
        self.hint_label_2.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hint_label_2.setFont(font)
        self.hint_label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.hint_label_2.setObjectName("hint_label_2")
        self.horizontalLayout_5.addWidget(self.hint_label_2)
        self.score_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.score_label.setFont(font)
        self.score_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.score_label.setObjectName("score_label")
        self.horizontalLayout_5.addWidget(self.score_label)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.hint_label_7 = QtWidgets.QLabel(Form)
        self.hint_label_7.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hint_label_7.setFont(font)
        self.hint_label_7.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.hint_label_7.setObjectName("hint_label_7")
        self.horizontalLayout_7.addWidget(self.hint_label_7)

        self.score_total_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.score_total_label.setFont(font)
        self.score_total_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.score_total_label.setObjectName("score_total_label")
        self.horizontalLayout_7.addWidget(self.score_total_label)

        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.hint_label_3 = QtWidgets.QLabel(Form)
        self.hint_label_3.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hint_label_3.setFont(font)
        self.hint_label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.hint_label_3.setObjectName("hint_label_3")
        self.horizontalLayout_4.addWidget(self.hint_label_3)
        self.right_quest_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.right_quest_label.setFont(font)
        self.right_quest_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.right_quest_label.setObjectName("right_quest_label")
        self.horizontalLayout_4.addWidget(self.right_quest_label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.hint_label_4 = QtWidgets.QLabel(Form)
        self.hint_label_4.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hint_label_4.setFont(font)
        self.hint_label_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.hint_label_4.setObjectName("hint_label_4")
        self.horizontalLayout_3.addWidget(self.hint_label_4)
        self.wrong_quest_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wrong_quest_label.setFont(font)
        self.wrong_quest_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.wrong_quest_label.setObjectName("wrong_quest_label")
        self.horizontalLayout_3.addWidget(self.wrong_quest_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hint_label_5 = QtWidgets.QLabel(Form)
        self.hint_label_5.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hint_label_5.setFont(font)
        self.hint_label_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.hint_label_5.setObjectName("hint_label_5")
        self.horizontalLayout_2.addWidget(self.hint_label_5)
        self.time_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.time_label.setFont(font)
        self.time_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_2.addWidget(self.time_label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.hint_label_6 = QtWidgets.QLabel(Form)
        self.hint_label_6.setMinimumSize(QtCore.QSize(210, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hint_label_6.setFont(font)
        self.hint_label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.hint_label_6.setObjectName("hint_label_6")
        self.verticalLayout_2.addWidget(self.hint_label_6)
        self.middle_score_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.middle_score_label.setFont(font)
        self.middle_score_label.setAlignment(QtCore.Qt.AlignCenter)
        self.middle_score_label.setObjectName("middle_score_label")
        self.verticalLayout_2.addWidget(self.middle_score_label)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.hint_label.setText(_translate("Form", "Название теста:"))
        self.name_test_label.setText(_translate("Form", "TextLabel"))
        self.hint_label_2.setText(_translate("Form", "Набранный балл:"))
        self.hint_label_7.setText(_translate("Form", "Максимальный балл:"))
        self.score_label.setText(_translate("Form", "TextLabel"))
        self.score_total_label.setText(_translate("Form", "TextLabel"))
        self.hint_label_3.setText(_translate("Form", "Правильных заданий:"))
        self.right_quest_label.setText(_translate("Form", "TextLabel"))
        self.hint_label_4.setText(_translate("Form", "Ошибочных заданий:"))
        self.wrong_quest_label.setText(_translate("Form", "TextLabel"))
        self.hint_label_5.setText(_translate("Form", "Время прохождения:"))
        self.time_label.setText(_translate("Form", "TextLabel"))
        self.hint_label_6.setText(_translate("Form", "Средний балл других тестируемых:"))
        self.middle_score_label.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
