# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateTesting.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateTesting(object):
    def setupUi(self, CreateTesting):
        CreateTesting.setObjectName("CreateTesting")
        CreateTesting.resize(880, 473)
        CreateTesting.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(13, 130, 149);\n"
                                    "")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CreateTesting)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontal_layout_top = QtWidgets.QHBoxLayout()
        self.horizontal_layout_top.setObjectName("horizontal_layout_top")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_top.addItem(spacerItem)
        self.eror_label = QtWidgets.QLabel(CreateTesting)
        self.eror_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.eror_label.setText("")
        self.eror_label.setObjectName("eror_label")
        self.horizontal_layout_top.addWidget(self.eror_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_top.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontal_layout_top)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clue_label_type = QtWidgets.QLabel(CreateTesting)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.clue_label_type.setFont(font)
        self.clue_label_type.setObjectName("clue_label_type")
        self.horizontalLayout.addWidget(self.clue_label_type)
        self.type_testing_combo_box = QtWidgets.QComboBox(CreateTesting)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.type_testing_combo_box.setFont(font)
        self.type_testing_combo_box.setObjectName("choose_user_combo_box")
        self.type_testing_combo_box.addItem("")
        self.type_testing_combo_box.addItem("")
        self.type_testing_combo_box.addItem("")
        self.type_testing_combo_box.addItem("")
        self.type_testing_combo_box.setStyleSheet("QComboBox { background-color: rgb(213, 122, 9);}\n"
                                                    "QComboBox:enabled{ color: rgb(255, 255, 255); }\n"
                                                    "QComboBox:disabled{ background:#a2979c; }")
        self.horizontalLayout.addWidget(self.type_testing_combo_box)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.clue_label_quantity = QtWidgets.QLabel(CreateTesting)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.clue_label_quantity.setFont(font)
        self.clue_label_quantity.setObjectName("clue_label_quantity")
        self.gridLayout.addWidget(self.clue_label_quantity, 0, 0, 1, 1)
        self.quantity_spin_box = QtWidgets.QSpinBox(CreateTesting)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.quantity_spin_box.setFont(font)
        self.quantity_spin_box.setMinimum(5)
        self.quantity_spin_box.setMaximum(60)
        self.quantity_spin_box.setStyleSheet("QSpinBox { background-color: rgb(213, 122, 9);}\n"
                                         "QSpinBox:enabled{ color: rgb(255, 255, 255); }\n"
                                         "QSpinBox:disabled{ background:#a2979c; }")
        self.quantity_spin_box.setObjectName("quantity_spin_box")
        self.gridLayout.addWidget(self.quantity_spin_box, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 2, 1, 1)
        self.clue_label_time = QtWidgets.QLabel(CreateTesting)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.clue_label_time.setFont(font)
        self.clue_label_time.setObjectName("clue_label_time")
        self.gridLayout.addWidget(self.clue_label_time, 1, 0, 1, 1)
        self.time_spin_box = QtWidgets.QSpinBox(CreateTesting)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.time_spin_box.setFont(font)
        self.time_spin_box.setMinimum(5)
        self.time_spin_box.setMaximum(60)
        self.time_spin_box.setStyleSheet("QSpinBox { background-color: rgb(213, 122, 9);}\n"
                                                    "QSpinBox:enabled{ color: rgb(255, 255, 255); }\n"
                                                    "QSpinBox:disabled{ background:#a2979c; }")
        self.time_spin_box.setObjectName("time_spin_box")
        self.gridLayout.addWidget(self.time_spin_box, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.check_properties = QtWidgets.QPushButton(CreateTesting)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.check_properties.setFont(font)
        self.check_properties.setStyleSheet("QPushButton { background-color: rgb(213, 122, 9);}\n"
                                                    "QPushButton:enabled{ color: rgb(255, 255, 255); }\n"
                                                    "QPushButton:disabled{ background:#a2979c; }")
        self.check_properties.setObjectName("check_properties")
        self.horizontalLayout_2.addWidget(self.check_properties)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.create_quests_tab_widget = QtWidgets.QTabWidget(CreateTesting)
        self.create_quests_tab_widget.setMinimumSize(QtCore.QSize(550, 275))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.create_quests_tab_widget.setFont(font)
        self.create_quests_tab_widget.setStyleSheet("QTabWidget::pane\n"
                                                    "{\n"
                                                    "    border:1px;\n"
                                                    "    background: rgb(203, 122, 9);\n"
                                                    "}\n"
                                                    "\n"
                                                    "QTabBar::tab\n"
                                                    "{\n"
                                                    "    color: white;\n"
                                                    "    background: rgb(13, 120, 149);\n"
                                                    "    min-width: 25ex;\n"
                                                    "    min-height: 8ex;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QTabBar::tab::selected\n"
                                                    "{\n"
                                                    "    background: rgb(213, 122, 9);\n"
                                                    "}\n"
                                                    "\n"
                                                    "QTabBar::tab::hover\n"
                                                    "{\n"
                                                    "    background: rgb(203, 112, 9);\n"
                                                    "}\n"
                                                    "")
        self.create_quests_tab_widget.setObjectName("create_quests_tab_widget")
        self.verticalLayout_2.addWidget(self.create_quests_tab_widget)
        self.horizontal_layout_bottom = QtWidgets.QHBoxLayout()
        self.horizontal_layout_bottom.setObjectName("horizontal_layout_bottom")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_bottom.addItem(spacerItem6)
        self.create_testing_push_button = QtWidgets.QPushButton(CreateTesting)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.create_testing_push_button.setFont(font)
        self.create_testing_push_button.setStyleSheet("QPushButton { background-color: rgb(213, 122, 9);}\n"
                                                    "QPushButton:enabled{ color: rgb(255, 255, 255); }\n"
                                                    "QPushButton:disabled{ background:#a2979c; }")
        self.create_testing_push_button.setObjectName("create_testing_push_button")
        self.horizontal_layout_bottom.addWidget(self.create_testing_push_button)
        self.close_push_button = QtWidgets.QPushButton(CreateTesting)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.close_push_button.setFont(font)
        self.close_push_button.setStyleSheet("QPushButton { background-color: rgb(213, 122, 9);}\n"
                                                    "QPushButton:enabled{ color: rgb(255, 255, 255); }\n"
                                                    "QPushButton:disabled{ background:#a2979c; }")
        self.close_push_button.setObjectName("close_push_button")
        self.horizontal_layout_bottom.addWidget(self.close_push_button)
        self.verticalLayout_2.addLayout(self.horizontal_layout_bottom)

        self.retranslateUi(CreateTesting)
        QtCore.QMetaObject.connectSlotsByName(CreateTesting)

    def retranslateUi(self, CreateTesting):
        _translate = QtCore.QCoreApplication.translate
        CreateTesting.setWindowTitle(_translate("CreateTesting", "Form"))
        self.clue_label_type.setText(_translate("CreateTesting", "Тип тестирования:"))
        self.type_testing_combo_box.setItemText(0, _translate("CreateTesting", "Предопределенные ответы"))
        self.type_testing_combo_box.setItemText(1, _translate("CreateTesting", "Смешанный (без шкал)"))
        self.type_testing_combo_box.setItemText(2, _translate("CreateTesting", "Только шкалы (от 0 до 10)"))
        self.type_testing_combo_box.setItemText(3, _translate("CreateTesting", "Только свободные ответы"))
        self.clue_label_quantity.setText(_translate("CreateTesting", "Количество заданий в тесте:"))
        self.clue_label_time.setText(_translate("CreateTesting", "Время на выполнение теста:"))
        self.check_properties.setText(_translate("CreateTesting", "Создать форму"))
        self.create_testing_push_button.setText(_translate("CreateTesting", "Создать тест"))
        self.close_push_button.setText(_translate("CreateTesting", "Закрыть"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    CreateTesting = QtWidgets.QWidget()
    ui = Ui_CreateTesting()
    ui.setupUi(CreateTesting)
    CreateTesting.show()
    sys.exit(app.exec_())
