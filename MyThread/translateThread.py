# coding: utf-8
'''
Created on 2017

@author: raytine
'''
from PyQt4.QtCore import QThread, pyqtSignal
from translateWay import baidu, xunfei
import traceback

class WorkThread(QThread):
    update_single = pyqtSignal(str)
    error_single = pyqtSignal(str)
    def __init__(self, input_message, way):  
        super(WorkThread,self).__init__()
        self.__input_mesaage = input_message
        self.__way = way
    
    def baiduTranslate(self):
        index = 1
        while index *50 < len(self.__input_mesaage):
            result = baidu.translate('\n'.join(self.__input_mesaage[(index-1) *50 : index*50]))
            self.update_single.emit('\n'.join(result))
            index += 1
        result = baidu.translate('\n'.join(self.__input_mesaage[(index-1)*50:]))
        self.update_single.emit('\n'.join(result))
    
    def xunfeiEnglishToChineseTranslate(self):
        for item in self.__input_mesaage:
            result = xunfei.englishTranslate(item)
            self.update_single.emit(result)
            
    def xunfeiChineseToEnglishTranslate(self):
        for item in self.__input_mesaage:
            result = xunfei.chineseTranslate(item)
            self.update_single.emit(result)
        
    def translate(self):
        switch = {u'baidu': self.baiduTranslate, u'xunfei_chinese_to_english': self.xunfeiChineseToEnglishTranslate, u'xunfei_english_to_chinese': self.xunfeiEnglishToChineseTranslate}
        translate = switch[self.__way]
        translate()
    def run(self, *args, **kwargs):
        try:
            self.translate()
        except:
            self.error_single.emit(traceback.format_exc())
if __name__ == '__main__':
    test = '''apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
apple
pear
pen
'''
    thread = WorkThread(test.split('\n'), u'baidu')
    thread.translate()