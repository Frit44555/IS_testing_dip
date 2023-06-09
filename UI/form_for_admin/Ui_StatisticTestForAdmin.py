# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_StatisticTestForAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StatisticTestForAdmin(object):
    def setupUi(self, StatisticTestForAdmin):
        StatisticTestForAdmin.setObjectName("StatisticTestForAdmin")
        StatisticTestForAdmin.resize(296, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StatisticTestForAdmin.sizePolicy().hasHeightForWidth())
        StatisticTestForAdmin.setSizePolicy(sizePolicy)
        StatisticTestForAdmin.setMinimumSize(QtCore.QSize(296, 200))
        StatisticTestForAdmin.setMaximumSize(QtCore.QSize(296, 200))
        StatisticTestForAdmin.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "background-color: rgb(13, 130, 149);")
        self.verticalLayout = QtWidgets.QVBoxLayout(StatisticTestForAdmin)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.hint_label = QtWidgets.QLabel(StatisticTestForAdmin)
        self.hint_label.setMinimumSize(QtCore.QSize(210, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hint_label.setFont(font)
        self.hint_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hint_label.setObjectName("hint_label")
        self.verticalLayout_3.addWidget(self.hint_label)
        self.name_test_label = QtWidgets.QLabel(StatisticTestForAdmin)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_test_label.setFont(font)
        self.name_test_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_test_label.setObjectName("name_test_label")
        self.verticalLayout_3.addWidget(self.name_test_label)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.frame = QtWidgets.QFrame(StatisticTestForAdmin)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.hint_quantity_quests_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hint_quantity_quests_label.setFont(font)
        self.hint_quantity_quests_label.setObjectName("hint_quantity_quests_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.hint_quantity_quests_label)
        self.quantity_quests_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.quantity_quests_label.setFont(font)
        self.quantity_quests_label.setObjectName("quantity_quests_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.quantity_quests_label)
        self.hint_quantity_quessts_in_testing_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hint_quantity_quessts_in_testing_label.setFont(font)
        self.hint_quantity_quessts_in_testing_label.setObjectName("hint_quantity_quessts_in_testing_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.hint_quantity_quessts_in_testing_label)
        self.quantity_quessts_in_testing_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.quantity_quessts_in_testing_label.setFont(font)
        self.quantity_quessts_in_testing_label.setObjectName("quantity_quessts_in_testing_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.quantity_quessts_in_testing_label)
        self.hint_average_label = QtWidgets.QLabel(self.frame)
        self.hint_average_label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hint_average_label.setFont(font)
        self.hint_average_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.hint_average_label.setObjectName("hint_average_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.hint_average_label)
        self.average_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.average_label.setFont(font)
        self.average_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.average_label.setObjectName("average_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.average_label)
        self.hint_reliability_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hint_reliability_label.setFont(font)
        self.hint_reliability_label.setObjectName("hint_reliability_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.hint_reliability_label)
        self.reliability_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reliability_label.setFont(font)
        self.reliability_label.setObjectName("reliability_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.reliability_label)
        self.hint_difficulty_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hint_difficulty_label.setFont(font)
        self.hint_difficulty_label.setObjectName("hint_difficulty_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.hint_difficulty_label)
        self.difficulty_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.difficulty_label.setFont(font)
        self.difficulty_label.setObjectName("difficulty_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.difficulty_label)
        self.verticalLayout.addWidget(self.frame)
        spacerItem = QtWidgets.QSpacerItem(20, 11, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(StatisticTestForAdmin)
        QtCore.QMetaObject.connectSlotsByName(StatisticTestForAdmin)

    def retranslateUi(self, StatisticTestForAdmin):
        _translate = QtCore.QCoreApplication.translate
        StatisticTestForAdmin.setWindowTitle(_translate("StatisticTestForAdmin", "Form"))
        self.hint_label.setText(_translate("StatisticTestForAdmin", "Название теста:"))
        self.name_test_label.setText(_translate("StatisticTestForAdmin", "TextLabel"))
        self.hint_quantity_quests_label.setText(_translate("StatisticTestForAdmin", "Всего заданий для теста:"))
        self.quantity_quests_label.setText(_translate("StatisticTestForAdmin", "TextLabel"))
        self.hint_quantity_quessts_in_testing_label.setText(
            _translate("StatisticTestForAdmin", "Заданий в тестировании:"))
        self.quantity_quessts_in_testing_label.setText(_translate("StatisticTestForAdmin", "TextLabel"))
        self.hint_average_label.setText(_translate("StatisticTestForAdmin", "Средний балл тестируемых:"))
        self.average_label.setText(_translate("StatisticTestForAdmin", "TextLabel"))
        self.hint_reliability_label.setText(_translate("StatisticTestForAdmin", "Коэффициент надёжности теста:"))
        self.reliability_label.setText(_translate("StatisticTestForAdmin", "TextLabel"))
        self.hint_difficulty_label.setText(_translate("StatisticTestForAdmin", "Трудность теста:"))
        self.difficulty_label.setText(_translate("StatisticTestForAdmin", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StatisticTestForAdmin = QtWidgets.QWidget()
    ui = Ui_StatisticTestForAdmin()
    ui.setupUi(StatisticTestForAdmin)
    StatisticTestForAdmin.show()
    sys.exit(app.exec_())