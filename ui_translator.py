# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'translatorSrMqtA.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_TranslatorMainWindow(object):
    def setupUi(self, TranslatorMainWindow):
        if not TranslatorMainWindow.objectName():
            TranslatorMainWindow.setObjectName(u"TranslatorMainWindow")
        TranslatorMainWindow.resize(710, 372)
        self.centralwidget = QWidget(TranslatorMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 691, 311))
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.translateTabWidget = QTabWidget(self.widget)
        self.translateTabWidget.setObjectName(u"translateTabWidget")
        self.textTranslate = QWidget()
        self.textTranslate.setObjectName(u"textTranslate")
        self.widget1 = QWidget(self.textTranslate)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(2, 10, 671, 228))
        self.horizontalLayout_12 = QHBoxLayout(self.widget1)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.textOriginLabel = QLabel(self.widget1)
        self.textOriginLabel.setObjectName(u"textOriginLabel")

        self.horizontalLayout_3.addWidget(self.textOriginLabel)

        self.textOriginComboBox = QComboBox(self.widget1)
        self.textOriginComboBox.addItem("")
        self.textOriginComboBox.addItem("")
        self.textOriginComboBox.setObjectName(u"textOriginComboBox")
        self.textOriginComboBox.setEditable(True)

        self.horizontalLayout_3.addWidget(self.textOriginComboBox)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.textOriginText = QTextEdit(self.widget1)
        self.textOriginText.setObjectName(u"textOriginText")

        self.verticalLayout_2.addWidget(self.textOriginText)


        self.horizontalLayout_12.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textDestLabel = QLabel(self.widget1)
        self.textDestLabel.setObjectName(u"textDestLabel")

        self.horizontalLayout_2.addWidget(self.textDestLabel)

        self.textDestComboBox = QComboBox(self.widget1)
        self.textDestComboBox.setObjectName(u"textDestComboBox")
        self.textDestComboBox.setEditable(True)

        self.horizontalLayout_2.addWidget(self.textDestComboBox)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.textDestText = QTextEdit(self.widget1)
        self.textDestText.setObjectName(u"textDestText")

        self.verticalLayout.addWidget(self.textDestText)


        self.horizontalLayout_12.addLayout(self.verticalLayout)

        self.translateTabWidget.addTab(self.textTranslate, "")
        self.fileTranslate = QWidget()
        self.fileTranslate.setObjectName(u"fileTranslate")
        self.widget2 = QWidget(self.fileTranslate)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 10, 671, 228))
        self.horizontalLayout_10 = QHBoxLayout(self.widget2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.fileOriginComboBoxLabel = QLabel(self.widget2)
        self.fileOriginComboBoxLabel.setObjectName(u"fileOriginComboBoxLabel")

        self.horizontalLayout_6.addWidget(self.fileOriginComboBoxLabel)

        self.fileOriginComboBox = QComboBox(self.widget2)
        self.fileOriginComboBox.setObjectName(u"fileOriginComboBox")
        self.fileOriginComboBox.setEditable(True)

        self.horizontalLayout_6.addWidget(self.fileOriginComboBox)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.addFilePushButton = QPushButton(self.widget2)
        self.addFilePushButton.setObjectName(u"addFilePushButton")

        self.horizontalLayout_8.addWidget(self.addFilePushButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.tableWidget_3 = QTableWidget(self.widget2)
        if (self.tableWidget_3.columnCount() < 2):
            self.tableWidget_3.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.verticalLayout_5.addWidget(self.tableWidget_3)


        self.horizontalLayout_10.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.fileDestLabel = QLabel(self.widget2)
        self.fileDestLabel.setObjectName(u"fileDestLabel")

        self.horizontalLayout_7.addWidget(self.fileDestLabel)

        self.fileDestComboBox = QComboBox(self.widget2)
        self.fileDestComboBox.setObjectName(u"fileDestComboBox")
        self.fileDestComboBox.setEditable(True)

        self.horizontalLayout_7.addWidget(self.fileDestComboBox)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.fileDestTableWidget = QTableWidget(self.widget2)
        if (self.fileDestTableWidget.columnCount() < 2):
            self.fileDestTableWidget.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.fileDestTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.fileDestTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.fileDestTableWidget.setObjectName(u"fileDestTableWidget")

        self.verticalLayout_4.addWidget(self.fileDestTableWidget)


        self.horizontalLayout_10.addLayout(self.verticalLayout_4)

        self.translateTabWidget.addTab(self.fileTranslate, "")

        self.verticalLayout_6.addWidget(self.translateTabWidget)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.translateHL = QHBoxLayout()
        self.translateHL.setObjectName(u"translateHL")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.engineLabel = QLabel(self.widget)
        self.engineLabel.setObjectName(u"engineLabel")

        self.horizontalLayout_4.addWidget(self.engineLabel)

        self.engineComboBox = QComboBox(self.widget)
        self.engineComboBox.setObjectName(u"engineComboBox")

        self.horizontalLayout_4.addWidget(self.engineComboBox)


        self.translateHL.addLayout(self.horizontalLayout_4)

        self.translatePushButton = QPushButton(self.widget)
        self.translatePushButton.setObjectName(u"translatePushButton")

        self.translateHL.addWidget(self.translatePushButton)


        self.horizontalLayout_5.addLayout(self.translateHL)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        TranslatorMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TranslatorMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 710, 22))
        self.helpMenu = QMenu(self.menubar)
        self.helpMenu.setObjectName(u"helpMenu")
        TranslatorMainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(TranslatorMainWindow)
        self.statusBar.setObjectName(u"statusBar")
        TranslatorMainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.helpMenu.menuAction())

        self.retranslateUi(TranslatorMainWindow)

        self.translateTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TranslatorMainWindow)
    # setupUi

    def retranslateUi(self, TranslatorMainWindow):
        TranslatorMainWindow.setWindowTitle(QCoreApplication.translate("TranslatorMainWindow", u"\u8c37\u6b4c\u7ffb\u8bd1", None))
        self.textOriginLabel.setText(QCoreApplication.translate("TranslatorMainWindow", u"\u6e90\u8bed\u8a00\uff1a", None))
        self.textOriginComboBox.setItemText(0, QCoreApplication.translate("TranslatorMainWindow", u"zh-cn", None))
        self.textOriginComboBox.setItemText(1, QCoreApplication.translate("TranslatorMainWindow", u"en", None))

        self.textOriginText.setHtml(QCoreApplication.translate("TranslatorMainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hello World</p></body></html>", None))
        self.textDestLabel.setText(QCoreApplication.translate("TranslatorMainWindow", u"\u76ee\u6807\u8bed\u8a00\uff1a", None))
        self.textDestComboBox.setCurrentText(QCoreApplication.translate("TranslatorMainWindow", u"en", None))
        self.textDestText.setPlaceholderText(QCoreApplication.translate("TranslatorMainWindow", u"\u4f60\u597d", None))
        self.translateTabWidget.setTabText(self.translateTabWidget.indexOf(self.textTranslate), QCoreApplication.translate("TranslatorMainWindow", u"\u6587\u672c\u7ffb\u8bd1", None))
        self.fileOriginComboBoxLabel.setText(QCoreApplication.translate("TranslatorMainWindow", u"\u6e90\u8bed\u8a00:", None))
        self.fileOriginComboBox.setCurrentText(QCoreApplication.translate("TranslatorMainWindow", u"en", None))
        self.addFilePushButton.setText(QCoreApplication.translate("TranslatorMainWindow", u"Add File", None))
        ___qtablewidgetitem = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TranslatorMainWindow", u"\u6587\u4ef6\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TranslatorMainWindow", u"\u6587\u4ef6\u8def\u5f84", None));
        self.fileDestLabel.setText(QCoreApplication.translate("TranslatorMainWindow", u"\u76ee\u6807\u8bed\u8a00:", None))
        self.fileDestComboBox.setCurrentText(QCoreApplication.translate("TranslatorMainWindow", u"en", None))
        ___qtablewidgetitem2 = self.fileDestTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TranslatorMainWindow", u"\u6587\u4ef6\u540d\u79f0", None));
        ___qtablewidgetitem3 = self.fileDestTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TranslatorMainWindow", u"\u6587\u4ef6\u8def\u5f84", None));
        self.translateTabWidget.setTabText(self.translateTabWidget.indexOf(self.fileTranslate), QCoreApplication.translate("TranslatorMainWindow", u"\u6587\u4ef6\u7ffb\u8bd1", None))
        self.engineLabel.setText(QCoreApplication.translate("TranslatorMainWindow", u"\u7ffb\u8bd1\u5f15\u64ce:", None))
        self.translatePushButton.setText(QCoreApplication.translate("TranslatorMainWindow", u"Translate", None))
        self.helpMenu.setTitle(QCoreApplication.translate("TranslatorMainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

