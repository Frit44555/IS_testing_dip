# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_CreateGroup.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ui_ChangeGroup(object):
    def setupUi(self, Ui_CreateGroup):
        Ui_CreateGroup.setObjectName("Ui_CreateGroup")
        Ui_CreateGroup.resize(345, 230)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ui_CreateGroup.sizePolicy().hasHeightForWidth())
        Ui_CreateGroup.setSizePolicy(sizePolicy)
        Ui_CreateGroup.setMinimumSize(QtCore.QSize(345, 230))
        Ui_CreateGroup.setMaximumSize(QtCore.QSize(345, 230))
        font = QtGui.QFont()
        font.setPointSize(10)
        Ui_CreateGroup.setFont(font)
        Ui_CreateGroup.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(13, 130, 149);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Ui_CreateGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hint_name_label = QtWidgets.QLabel(Ui_CreateGroup)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hint_name_label.setFont(font)
        self.hint_name_label.setObjectName("hint_name_label")
        self.horizontalLayout.addWidget(self.hint_name_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.group_name_label = QtWidgets.QLabel(Ui_CreateGroup)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.group_name_label.setFont(font)
        self.group_name_label.setObjectName("group_name_label")
        self.horizontalLayout.addWidget(self.group_name_label)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.hint_tags_label = QtWidgets.QLabel(Ui_CreateGroup)
        self.hint_tags_label.setObjectName("hint_tags_label")
        self.horizontalLayout_6.addWidget(self.hint_tags_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.all_tags_combo_box = QtWidgets.QComboBox(Ui_CreateGroup)
        self.all_tags_combo_box.setObjectName("all_tags_combo_box")
        self.horizontalLayout_5.addWidget(self.all_tags_combo_box)
        self.add_tag_push_button = QtWidgets.QPushButton(Ui_CreateGroup)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_tag_push_button.setFont(font)
        self.add_tag_push_button.setStyleSheet("QPushButton { background-color: rgb(213, 122, 9);}\n"
                                               "QPushButton:enabled{ color: rgb(255, 255, 255); }\n"
                                               "QPushButton:disabled{ background:#a2979c; }")
        self.add_tag_push_button.setObjectName("add_tag_push_button")
        self.horizontalLayout_5.addWidget(self.add_tag_push_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.hint_accesse_tag_label = QtWidgets.QLabel(Ui_CreateGroup)
        self.hint_accesse_tag_label.setObjectName("hint_accesse_tag_label")
        self.horizontalLayout_4.addWidget(self.hint_accesse_tag_label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.access_tags_combo_box = QtWidgets.QComboBox(Ui_CreateGroup)
        self.access_tags_combo_box.setObjectName("access_tags_combo_box")
        self.horizontalLayout_3.addWidget(self.access_tags_combo_box)
        self.remove_tag_push_button_3 = QtWidgets.QPushButton(Ui_CreateGroup)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.remove_tag_push_button_3.setFont(font)
        self.remove_tag_push_button_3.setStyleSheet("QPushButton { background-color: rgb(213, 122, 9);}\n"
                                                    "QPushButton:enabled{ color: rgb(255, 255, 255); }\n"
                                                    "QPushButton:disabled{ background:#a2979c; }")
        self.remove_tag_push_button_3.setObjectName("remove_tag_push_button_3")
        self.horizontalLayout_3.addWidget(self.remove_tag_push_button_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.create_group_push_button = QtWidgets.QPushButton(Ui_CreateGroup)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.create_group_push_button.setFont(font)
        self.create_group_push_button.setStyleSheet("QPushButton { background-color: rgb(213, 122, 9);}\n"
                                                    "QPushButton:enabled{ color: rgb(255, 255, 255); }\n"
                                                    "QPushButton:disabled{ background:#a2979c; }")
        self.create_group_push_button.setObjectName("create_group_push_button")
        self.horizontalLayout_2.addWidget(self.create_group_push_button)
        self.cancel_push_button = QtWidgets.QPushButton(Ui_CreateGroup)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancel_push_button.setFont(font)
        self.cancel_push_button.setStyleSheet("QPushButton { background-color: rgb(213, 122, 9);}\n"
                                              "QPushButton:enabled{ color: rgb(255, 255, 255); }\n"
                                              "QPushButton:disabled{ background:#a2979c; }")
        self.cancel_push_button.setObjectName("cancel_push_button")
        self.horizontalLayout_2.addWidget(self.cancel_push_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Ui_CreateGroup)
        QtCore.QMetaObject.connectSlotsByName(Ui_CreateGroup)

    def retranslateUi(self, Ui_CreateGroup):
        _translate = QtCore.QCoreApplication.translate
        Ui_CreateGroup.setWindowTitle(_translate("Ui_CreateGroup", "Form"))
        self.hint_name_label.setText(_translate("Ui_CreateGroup", "Название группы"))
        self.hint_tags_label.setText(_translate("Ui_CreateGroup", "Теги"))
        self.add_tag_push_button.setText(_translate("Ui_CreateGroup", "Добавить"))
        self.hint_accesse_tag_label.setText(_translate("Ui_CreateGroup", "Теги доступные группе"))
        self.remove_tag_push_button_3.setText(_translate("Ui_CreateGroup", "Удалить"))
        self.create_group_push_button.setText(_translate("Ui_CreateGroup", "Изменить"))
        self.cancel_push_button.setText(_translate("Ui_CreateGroup", "Закрыть"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Ui_CreateGroup = QtWidgets.QWidget()
    ui = Ui_Ui_ChangeGroup()
    ui.setupUi(Ui_CreateGroup)
    Ui_CreateGroup.show()
    sys.exit(app.exec_())
