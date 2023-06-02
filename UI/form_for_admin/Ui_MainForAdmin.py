# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MainForAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainForAdmin(object):
    def setupUi(self, MainForAdmin):
        MainForAdmin.setObjectName("MainForAdmin")
        MainForAdmin.resize(853, 485)
        MainForAdmin.setMinimumSize(QtCore.QSize(630, 0))
        MainForAdmin.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(13, 130, 149);")
        self.verticalLayout = QtWidgets.QVBoxLayout(MainForAdmin)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(MainForAdmin)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane\n"
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
"QTabBar::tab::hover { background: rgb(203, 112, 9); }")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_user = QtWidgets.QWidget()
        self.tab_user.setObjectName("tab_user")
        self.tabWidget.addTab(self.tab_user, "")
        self.tab_analysis = QtWidgets.QWidget()
        self.tab_analysis.setObjectName("tab_analysis")
        self.tabWidget.addTab(self.tab_analysis, "")
        self.tab_creat_test = QtWidgets.QWidget()
        self.tab_creat_test.setObjectName("tab_creat_test")
        self.tabWidget.addTab(self.tab_creat_test, "")
        self.tab_create_lesson = QtWidgets.QWidget()
        self.tab_create_lesson.setObjectName("tab_create_lesson")
        self.tabWidget.addTab(self.tab_create_lesson, "")
        self.tab_check = QtWidgets.QWidget()
        self.tab_check.setObjectName("tab_check")
        self.tabWidget.addTab(self.tab_check, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(MainForAdmin)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainForAdmin)

    def retranslateUi(self, MainForAdmin):
        _translate = QtCore.QCoreApplication.translate
        MainForAdmin.setWindowTitle(_translate("MainForAdmin", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_user), _translate("MainForAdmin", "Пользователи"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_analysis), _translate("MainForAdmin", "Анализ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_creat_test), _translate("MainForAdmin", "Создать тест"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_create_lesson), _translate("MainForAdmin", "Создать учебный материал"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_check), _translate("MainForAdmin", "Проверить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForAdmin = QtWidgets.QWidget()
    ui = Ui_MainForAdmin()
    ui.setupUi(MainForAdmin)
    MainForAdmin.show()
    sys.exit(app.exec_())
