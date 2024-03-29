# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CheckResultTestingQuest.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CheckResultTestingQuest(object):
    def setupUi(self, CheckResultTestingQuest):
        CheckResultTestingQuest.setObjectName("CheckResultTestingQuest")
        CheckResultTestingQuest.resize(872, 331)
        CheckResultTestingQuest.setStyleSheet("color: rgb(255, 255, 255);\n"
                                              "background-color: rgb(13, 122, 149);")
        self.verticalLayout = QtWidgets.QVBoxLayout(CheckResultTestingQuest)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.clue2 = QtWidgets.QLabel(CheckResultTestingQuest)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clue2.setFont(font)
        self.clue2.setObjectName("clue2")
        self.verticalLayout.addWidget(self.clue2)
        self.question_text_browser = QtWidgets.QTextBrowser(CheckResultTestingQuest)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question_text_browser.sizePolicy().hasHeightForWidth())
        self.question_text_browser.setSizePolicy(sizePolicy)
        self.question_text_browser.setMinimumSize(QtCore.QSize(0, 50))
        self.question_text_browser.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.question_text_browser.setFont(font)
        self.question_text_browser.setObjectName("question_text_browser")
        self.verticalLayout.addWidget(self.question_text_browser)
        self.clue3 = QtWidgets.QLabel(CheckResultTestingQuest)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clue3.setFont(font)
        self.clue3.setObjectName("clue3")
        self.verticalLayout.addWidget(self.clue3)
        self.answer_text_browser = QtWidgets.QTextBrowser(CheckResultTestingQuest)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.answer_text_browser.setFont(font)
        self.answer_text_browser.setObjectName("answer_text_browser")
        self.verticalLayout.addWidget(self.answer_text_browser)
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.label_7 = QtWidgets.QLabel(CheckResultTestingQuest)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontal_layout.addWidget(self.label_7)
        self.result_check_comb_box = QtWidgets.QComboBox(CheckResultTestingQuest)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.result_check_comb_box.setFont(font)
        self.result_check_comb_box.setObjectName("result_check_comb_box")
        self.result_check_comb_box.addItem("")
        self.result_check_comb_box.addItem("")
        self.horizontal_layout.addWidget(self.result_check_comb_box)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontal_layout)
        self.clue4 = QtWidgets.QLabel(CheckResultTestingQuest)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clue4.setFont(font)
        self.clue4.setObjectName("clue4")
        self.verticalLayout.addWidget(self.clue4)
        self.comment_admin_text_edit = QtWidgets.QTextEdit(CheckResultTestingQuest)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comment_admin_text_edit.setFont(font)
        self.comment_admin_text_edit.setObjectName("comment_admin_text_edit")
        self.verticalLayout.addWidget(self.comment_admin_text_edit)
        self.apply_push_button = QtWidgets.QPushButton(CheckResultTestingQuest)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.apply_push_button.setFont(font)
        self.apply_push_button.setStyleSheet("background-color: rgb(213, 122, 9);")
        self.apply_push_button.setObjectName("apply_push_button")
        self.verticalLayout.addWidget(self.apply_push_button)

        self.retranslateUi(CheckResultTestingQuest)
        QtCore.QMetaObject.connectSlotsByName(CheckResultTestingQuest)

    def retranslateUi(self, CheckResultTestingQuest):
        _translate = QtCore.QCoreApplication.translate
        CheckResultTestingQuest.setWindowTitle(_translate("CheckResultTestingQuest", "Form"))
        self.clue2.setText(_translate("CheckResultTestingQuest", "Вопрос:"))
        self.clue3.setText(_translate("CheckResultTestingQuest", "Введёный ответ:"))
        self.label_7.setText(_translate("CheckResultTestingQuest", "Задание зачтено как:"))
        self.result_check_comb_box.setItemText(0, _translate("CheckResultTestingQuest", "Верное"))
        self.result_check_comb_box.setItemText(1, _translate("CheckResultTestingQuest", "Неверное"))
        self.clue4.setText(_translate("CheckResultTestingQuest", "Комментарий к тесту:"))
        self.comment_admin_text_edit.setPlaceholderText(_translate("CheckResultTestingQuest", "Ваш комментарий..."))
        self.apply_push_button.setText(_translate("CheckResultTestingQuest", "Принять"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    CheckResultTestingQuest = QtWidgets.QWidget()
    ui = Ui_CheckResultTestingQuest()
    ui.setupUi(CheckResultTestingQuest)
    CheckResultTestingQuest.show()
    sys.exit(app.exec_())
