# -*- coding: utf-8 -*-# Form implementation generated from reading ui file '.\translate.ui'## Created by: PyQt4 UI code generator 4.11.4## WARNING! All changes made in this file will be lost!from PyQt4 import QtCore, QtGuitry:    _fromUtf8 = QtCore.QString.fromUtf8except AttributeError:    def _fromUtf8(s):        return stry:    _encoding = QtGui.QApplication.UnicodeUTF8    def _translate(context, text, disambig):        return QtGui.QApplication.translate(context, text, disambig, _encoding)except AttributeError:    def _translate(context, text, disambig):        return QtGui.QApplication.translate(context, text, disambig)class Ui_MainWindow(object):    def setupUi(self, MainWindow):        MainWindow.setObjectName(_fromUtf8("MainWindow"))        MainWindow.resize(800, 600)        self.centralwidget = QtGui.QWidget(MainWindow)        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))        self.widget = QtGui.QWidget(self.centralwidget)        self.widget.setObjectName(_fromUtf8("widget"))        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))        self.open_file_push_button = QtGui.QPushButton(self.widget)        self.open_file_push_button.setObjectName(_fromUtf8("open_file_push_button"))        self.horizontalLayout_2.addWidget(self.open_file_push_button)        self.translate_way_combobox = QtGui.QComboBox(self.widget)        self.translate_way_combobox.setObjectName(_fromUtf8("translate_way_combobox"))        self.translate_way_combobox.addItem(_fromUtf8(""))        self.translate_way_combobox.addItem(_fromUtf8(""))        self.translate_way_combobox.addItem(_fromUtf8(""))        self.horizontalLayout_2.addWidget(self.translate_way_combobox)        self.start_translate_push_button = QtGui.QPushButton(self.widget)        self.start_translate_push_button.setObjectName(_fromUtf8("start_translate_push_button"))        self.horizontalLayout_2.addWidget(self.start_translate_push_button)        self.output_push_button = QtGui.QPushButton(self.widget)        self.output_push_button.setObjectName(_fromUtf8("output_push_button"))        self.horizontalLayout_2.addWidget(self.output_push_button)        self.verticalLayout.addWidget(self.widget)        self.widget_2 = QtGui.QWidget(self.centralwidget)        self.widget_2.setObjectName(_fromUtf8("widget_2"))        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))        self.widget_3 = QtGui.QWidget(self.widget_2)        self.widget_3.setObjectName(_fromUtf8("widget_3"))        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_3)        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))        self.input_text_browser = QtGui.QTextBrowser(self.widget_3)        self.input_text_browser.setObjectName(_fromUtf8("input_text_browser"))        self.verticalLayout_2.addWidget(self.input_text_browser)        self.horizontalLayout.addWidget(self.widget_3)        self.widget_4 = QtGui.QWidget(self.widget_2)        self.widget_4.setObjectName(_fromUtf8("widget_4"))        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_4)        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))        self.output_text_browser = QtGui.QTextBrowser(self.widget_4)        self.output_text_browser.setObjectName(_fromUtf8("output_text_browser"))        self.verticalLayout_3.addWidget(self.output_text_browser)        self.horizontalLayout.addWidget(self.widget_4)        self.verticalLayout.addWidget(self.widget_2)        self.verticalLayout.setStretch(0, 1)        self.verticalLayout.setStretch(1, 5)        MainWindow.setCentralWidget(self.centralwidget)        self.menubar = QtGui.QMenuBar(MainWindow)        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))        self.menubar.setObjectName(_fromUtf8("menubar"))        MainWindow.setMenuBar(self.menubar)        self.statusbar = QtGui.QStatusBar(MainWindow)        self.statusbar.setObjectName(_fromUtf8("statusbar"))        MainWindow.setStatusBar(self.statusbar)        self.retranslateUi(MainWindow)        QtCore.QMetaObject.connectSlotsByName(MainWindow)    def retranslateUi(self, MainWindow):        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))        self.open_file_push_button.setText(_translate("MainWindow", u"打开文件", None))        self.translate_way_combobox.setItemText(0, _translate("MainWindow", u"讯飞中翻英", None))        self.translate_way_combobox.setItemText(1, _translate("MainWindow", u"讯飞英翻中", None))        self.translate_way_combobox.setItemText(2, _translate("MainWindow", u"百度", None))        self.start_translate_push_button.setText(_translate("MainWindow", u"开始翻译", None))        self.output_push_button.setText(_translate("MainWindow", u"输出到文件", None))