import ui_translator
import sys
from PySide6.QtCore import QCoreApplication, Signal, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox
from enum import Enum
from google_translate import GoogleTranslator


class Translator(QMainWindow):
    def __init__(self):
        """ 创建软件界面。
        """
        super(Translator, self).__init__()
        self.translatorUi = ui_translator.Ui_TranslatorMainWindow()
        self.translatorUi.setupUi(self)
        self.languages = [u"af", u"sq", u"am", u"ar", u"hy", u"az", u"eu", u"be", u"bn", u"bs",
                          u"bg", u"ca", u"ceb", u"ny", u"zh-cn", u"zh-tw", u"co", u"hr", u"cs",
                          u"da", u"nl", u"en", u"eo", u"et", u"tl", u"fi", u"fr", u"fy", u"gl",
                          u"ka", u"de", u"el", u"gu", u"ht", u"ha", u"haw", u"iw", u"he", u"hi",
                          u"hmn", u"hu", u"is", u"ig", u"id", u"ga", u"it", u"ja", u"jw", u"kn",
                          u"kk", u"km", u"ko", u"ku", u"ky", u"lo", u"la", u"lv", u"lt", u"lb",
                          u"mk", u"mg", u"ms", u"ml", u"mt", u"mi", u"mr", u"mn", u"my", u"ne",
                          u"no", u"or", u"ps", u"fa", u"pl", u"pt", u"pa", u"ro", u"ru", u"sm",
                          u"gd", u"sr", u"st", u"sn", u"sd", u"si", u"sk", u"sl", u"so", u"es",
                          u"su", u"sw", u"sv", u"tg", u"ta", u"te", u"th", u"tr", u"uk", u"ur",
                          u"ug", u"uz", u"vi", u"cy", u"xh", u"yi", u"yo", u"zu"]
        self.transalteEngine = [u"Google", u"Tencent"]
        self.SetLanguageComboBoxes()
        self.SetTranslateEngineComboBoxes()
        self.translatorUi.textOriginComboBox.setCurrentIndex(21)
        self.translatorUi.textDestComboBox.setCurrentIndex(14)
        self.translatorUi.fileOriginComboBox.setCurrentIndex(21)
        self.translatorUi.fileDestComboBox.setCurrentIndex(14)
        self.translatorUi.engineComboBox.setCurrentIndex(0)
        self.translatorUi.textOriginText.setFontFamily("Sarasa Mono SC")
        self.translatorUi.textDestText.setFontFamily("Sarasa Mono SC")
        # 连接信号与槽，点击翻译按钮时启动翻译
        self.translatorUi.translatePushButton.clicked.connect(self.Translate)
        return

    def SetLanguageItem(self, comboBox: QComboBox):
        """设置当前支持的语言。

        Args:
            comboBox (QComboBox): 带设定的文本框。
        """
        comboBox.clear()
        length = len(self.languages)
        for i in range(0, length):
            comboBox.insertItem(i, QCoreApplication.translate(
                "Translator", self.languages[i], None))
        return

    def SetLanguageComboBoxes(self):
        """设定界面上所有的语言选择框。
        """
        self.SetLanguageItem(self.translatorUi.textOriginComboBox)
        self.SetLanguageItem(self.translatorUi.textDestComboBox)
        self.SetLanguageItem(self.translatorUi.fileDestComboBox)
        self.SetLanguageItem(self.translatorUi.fileOriginComboBox)

    def SetTranslateEngineItem(self, comboBox: QComboBox):
        """设定当前支持的翻译引擎。

        Args:
            comboBox (QComboBox): [description]
        """
        comboBox.clear()
        length = len(self.transalteEngine)
        for i in range(0, length):
            comboBox.insertItem(i, QCoreApplication.translate(
                "Translator", self.transalteEngine[i], None))
        return

    def SetTranslateEngineComboBoxes(self):
        """设定当前界面上所有的搜索引擎列表。

        Args:
            self (Translator): [description]
        """
        self.SetTranslateEngineItem(self.translatorUi.engineComboBox)
        return

    def TranslateTextGoogle(self, text:str, src:str, dest:str):
        """使用谷歌翻译引擎翻译文本。

        Args:
            text (str): 待翻译的文本
            src (str): 源语言
            dest (str): 目标语言
        """
        googleTranslator = GoogleTranslator()
        result = googleTranslator.GoogleTranslatText(text, src, dest)
        print(result)
        self.translatorUi.textDestText.setPlainText(result)
        return

    def TranslateText(self):
        engine = self.translatorUi.engineComboBox.currentIndex()
        text = self.translatorUi.textOriginText.toPlainText()
        src = self.translatorUi.textOriginComboBox.currentText()
        dest = self.translatorUi.textDestComboBox.currentText()
        if engine == 0:
            self.TranslateTextGoogle(text, src, dest)
        elif engine == 1:
            pass
        else:
            print("engine set error.")
        return

    def TranslateFile(self):
        engine = self.translatorUi.engineComboBox.currentIndex()
        pass

    @Slot()
    def Translate(self):
        mode = self.translatorUi.translateTabWidget.currentIndex()

        if mode == 0:
            self.TranslateText()
        elif mode == 1:
            self.TranslateFile()
        else:
            pass
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator = Translator()
    translator.show()
    app.exec_()
