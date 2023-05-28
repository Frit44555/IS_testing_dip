from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Testing(object):
    def setupUi(self, Testing):
        Testing.setObjectName("Testing")
        Testing.resize(912, 502)
        Testing.setStyleSheet("background: rgb(13, 120, 149);\n"
                              "color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Testing)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.questions_tab_widget = QtWidgets.QTabWidget(Testing)
        self.questions_tab_widget.setStyleSheet("QTabWidget::pane\n"
                                                "{\n"
                                                "    border:1px;\n"
                                                "    background: rgb(203, 122, 9);\n"
                                                "}\n"
                                                "QTabBar::tab\n"
                                                "{\n"
                                                "    color: white;\n"
                                                "    background: rgb(13, 120, 149);\n"
                                                "    min-width: 25ex;\n"
                                                "    min-height: 8ex;\n"
                                                "}\n"
                                                "QTabBar::tab::selected { background: rgb(213, 122, 9); }\n"
                                                "QTabBar::tab::hover\n"
                                                "{ background: rgb(203, 112, 9); }")
        self.questions_tab_widget.setObjectName("questions_tab_widget")
        self.verticalLayout.addWidget(self.questions_tab_widget)
        spacerItem = QtWidgets.QSpacerItem(20, 118, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontal_layout_bottom = QtWidgets.QHBoxLayout()
        self.horizontal_layout_bottom.setObjectName("horizontal_layout_bottom")
        self.timer_label = QtWidgets.QLabel(Testing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timer_label.sizePolicy().hasHeightForWidth())
        self.timer_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.timer_label.setFont(font)
        self.timer_label.setText("")
        self.timer_label.setObjectName("timer_label")
        self.horizontal_layout_bottom.addWidget(self.timer_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout_bottom.addItem(spacerItem1)
        self.complete_push_button = QtWidgets.QPushButton(Testing)
        self.complete_push_button.setMinimumSize(QtCore.QSize(90, 27))
        self.complete_push_button.setMaximumSize(QtCore.QSize(90, 27))
        self.complete_push_button.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.complete_push_button.setFont(font)
        self.complete_push_button.setStyleSheet("background-color: rgb(213, 122, 9);")
        self.complete_push_button.setObjectName("complete_push_button")
        self.horizontal_layout_bottom.addWidget(self.complete_push_button)
        self.verticalLayout.addLayout(self.horizontal_layout_bottom)

        self.retranslateUi(Testing)
        QtCore.QMetaObject.connectSlotsByName(Testing)

    def retranslateUi(self, Testing):
        _translate = QtCore.QCoreApplication.translate
        Testing.setWindowTitle(_translate("Testing", "Form"))
        self.complete_push_button.setText(_translate("Testing", "Завершить"))
