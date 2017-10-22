# coding: utf-8
'''
Created on 2017年10月22日

@author: raytine
'''
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog, QTextCursor, QMessageBox
from ui.translate_ui import Ui_MainWindow
from MyThread import translateThread
import sys
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.text = []
        
        self.open_file_push_button.clicked.connect(self.fileOpen)
        self.start_translate_push_button.clicked.connect(self.startTranslate)
        self.output_push_button.clicked.connect(self.outputToFile)
    
    def fileOpen(self):
        self.input_text_browser.setPlainText("")
        self.output_text_browser.setPlainText("")
        file_name = QFileDialog.getOpenFileName(parent=None)
        with open(file_name) as fp:
            for line in fp:
                self.updateInputBroswer(line)
    
    def updateInputBroswer(self, line):
        self.input_text_browser.moveCursor(QTextCursor.End)
        self.input_text_browser.textCursor().insertText(line)
    
    def updateOutputBroswer(self, line):
        self.output_text_browser.moveCursor(QTextCursor.End)
        self.output_text_browser.textCursor().insertText(line)
    
    def startTranslate(self):
        way = {u'百度':'baidu', u'讯飞': 'xunfei'}
        text = unicode(self.translate_way_combobox.currentText())
        message = unicode(self.input_text_browser.toPlainText()).split('\n')
        self.translate_thread = translateThread.WorkThread(message,way[text])
        self.translate_thread.update_single.connect(self.updateOutputBroswer)
        self.translate_thread.error_single.connect(self.error)
        self.translate_thread.start()
    
    def outputToFile(self):
        with open('result.txt', 'w') as fp:
            fp.write(self.output_text_browser.toPlainText().toUtf8())

    def error(self, message):
        QMessageBox.information(self,                         #使用infomation信息框  
                                    u"错误",  
                                    message,  
                                    QMessageBox.Yes)
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())