from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Lesson(object):
    def setupUi(self, Lesson):
        Lesson.setObjectName("Lesson.py")
        Lesson.resize(400, 277)
        Lesson.setStyleSheet("background: rgb(13, 120, 149);\n"
                             "color: rgb(255, 255, 255);\n"
                             "")
        self.verticalLayout = QtWidgets.QVBoxLayout(Lesson)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lessons_text_browser = QtWidgets.QTextBrowser(Lesson)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lessons_text_browser.setFont(font)
        self.lessons_text_browser.setObjectName("lessons_text_browser")
        self.verticalLayout.addWidget(self.lessons_text_browser)

        self.retranslateUi(Lesson)
        QtCore.QMetaObject.connectSlotsByName(Lesson)

    def retranslateUi(self, Lesson):
        _translate = QtCore.QCoreApplication.translate
        Lesson.setWindowTitle(_translate("Lesson.py", "Form"))
        self.lessons_text_browser.setHtml(_translate("Lesson.py",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
