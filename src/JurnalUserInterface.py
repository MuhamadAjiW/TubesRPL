# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jurnal_tmp_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from custom import *
import Jurnal as Jurnal
from JurnalController import JurnalController
from StatisticWithLabel import *
from os import path
import datetime
from calendar import monthrange
import sys


class SleepOverlay(CustomOverlay):
    def __init__(self, codeIdx, controller, parent=None):
        super(SleepOverlay, self).__init__(parent)
        self.controller = controller
        self.codeIdx = codeIdx
    
        self.block = QFrame(self)
        self.block.setFrameShape(QFrame.StyledPanel)
        self.block.setStyleSheet(
                                "background-color: rgb(255, 255, 255);"
                                "border-width: 2;"
                                "border-style: solid;"
                                )
        self.block.move(300, 100)
        self.block.resize(600, 480)

        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)

        self.titleLabel = QLabel("Judul: ", self.block)
        self.titleLabel.setStyleSheet("border-width: 0;")
        self.titleLabel.move(10,15)
        self.titleLabel.setContentsMargins(5, 0, 0, 0)
        self.titleLabel.setFont(font)
        
        self.titleInput = QLineEdit(self.block)
        self.titleInput.setGeometry(10,45, 580, 40)
        self.titleInput.setContentsMargins(5, 0, 0, 0)
        self.titleInput.setFont(font)

        self.titleLabel = QLabel("Isi: ", self.block)
        self.titleLabel.setStyleSheet("border-width: 0;")
        self.titleLabel.move(10, 105)
        self.titleLabel.setContentsMargins(5, 0, 0, 0)
        self.titleLabel.setFont(font)
        
        self.jurnalInput = QTextEdit(self.block)
        self.jurnalInput.setGeometry(15,135, 575, 290)
        self.jurnalInput.setContentsMargins(5, 0, 0, 0)
        self.jurnalInput.setFont(font)

        if (codeIdx != 0):
            rows = self.controller.daftarJurnal
            self.titleInput.setText(rows[codeIdx - 1].judul)
            self.jurnalInput.setText(rows[codeIdx - 1].isi)
            self.titleInput.setReadOnly(True)
            self.jurnalInput.setReadOnly(True)

        self.closeButton = CustomSVGButton(path.join(self.resources, "cancelIcon.svg"), path.join(self.resources, "cancelIconH.svg"), self.block)
        self.closeButton.setGeometry(QRect(525, 434, 23, 23))
        self.closeButton.setObjectName("CloseButton")
        self.closeButton.clicked.connect(self._onclose)

        self.confirmButton = CustomSVGButton(path.join(self.resources, "confirmIcon.svg"), path.join(self.resources, "confirmIconH.svg"), self.block)
        self.confirmButton.setGeometry(QRect(565, 434, 23, 23))
        self.confirmButton.setObjectName("ConfirmButton")
        self.confirmButton.clicked.connect(self._onconfirm)

    def _onconfirm(self):
        if(self.codeIdx == 0):
            self.signals.confirm.emit(self.codeIdx)
        else:
            self.signals.close.emit()


class JurnalForm(UIWindow):
    def setupUi(self, Form):
        self.controller = JurnalController()

        self.parent = Form
        self.entries = 1
        self.mode = "List"

        Form.setObjectName("FormJurnal")
        Form.resize(1280, 786)
        
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.OpeningPanel = QFrame(Form)
        self.OpeningPanel.setObjectName("OpeningPanel")
        self.OpeningPanel.setStyleSheet(
"QFrame#OpeningPanel {\n"
"    background: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    border-radius: 0px;\n"
"}"
"QPushButton {\n"
"    background: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(130, 130, 130);\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgb(215, 215, 215);\n"
"}\n"
"QPushButton:pressed {\n"
"    background: rgb(200, 200, 200);\n"
"}")
        
        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(22)
        
        self.JurnalTitle = QLabel(self.OpeningPanel)
        self.JurnalTitle.setGeometry(QRect(30, 64, 240, 35))
        self.JurnalTitle.setFont(font)
        self.JurnalTitle.setObjectName("JurnalTitle")
        self.JurnalTitle.setAlignment(Qt.AlignLeft|Qt.AlignTop)

        font.setPointSize(13)
    
        self.JurnalSubtitle = QLabel(self.OpeningPanel)
        self.JurnalSubtitle.setGeometry(QRect(30, 128, 240, 40))
        self.JurnalSubtitle.setFont(font)
        self.JurnalSubtitle.setWordWrap(True)
        self.JurnalSubtitle.setObjectName("JurnalSubtitle")
        self.JurnalSubtitle.setAlignment(Qt.AlignLeft|Qt.AlignTop)

        self.ReturnButton = QPushButton(self.OpeningPanel)
        self.ReturnButton.setGeometry(QRect(30, 650, 190, 40))
        self.ReturnButton.setFont(font)
        self.ReturnButton.setAutoFillBackground(False)
        self.ReturnButton.setStyleSheet("text-align: left;\n"
                                      "padding: 5px;\n")
        self.ReturnButton.setCheckable(False)
        self.ReturnButton.setChecked(False)
        self.ReturnButton.setAutoDefault(False)
        self.ReturnButton.setDefault(False)
        self.ReturnButton.setFlat(False)
        self.ReturnButton.setObjectName("ReturnButton")
        self.ReturnButton.clicked.connect(lambda: self._onswitch("Home"))

        self.StatisticsButton = QPushButton(self.OpeningPanel)
        self.StatisticsButton.setGeometry(QRect(30, 600, 190, 40))
        self.StatisticsButton.setFont(font)
        self.StatisticsButton.setStyleSheet("text-align: left;\n"
                                           "padding: 5px;\n")
        self.StatisticsButton.setCheckable(False)
        self.StatisticsButton.setChecked(False)
        self.StatisticsButton.setAutoDefault(False)
        self.StatisticsButton.setDefault(False)
        self.StatisticsButton.setFlat(False)
        self.StatisticsButton.setObjectName("StatisticsButton")
        self.StatisticsButton.clicked.connect(self._onStatistics)
        
        self.content = QFrame()
        self.content.setContentsMargins(40, 64, 20, -1)
        self.content.setObjectName("content")
        self.content.setStyleSheet(
"QFrame#content {\n"
"    background: rgb(200, 200, 200);\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    border-radius: 0px;\n"
"}\n"
"QPushButton {\n"
"    background: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(130, 130, 130);\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgb(215, 215, 215);\n"
"}\n"
"QPushButton:pressed {\n"
"    background: rgb(200, 200, 200);\n"
"}")
        
        self.scrollArea = QScrollArea(self.content)
        self.scrollAreaHeight = 70
        self.scrollArea.setGeometry(QRect(30, 30, 890, self.scrollAreaHeight))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet(
"QWidget {\n"
"    background: rgb(200, 200, 200);\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    background: rgb(255, 255, 255);\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(130, 130, 130);\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    background: rgb(255, 255, 255);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    background: rgb(255, 255, 255);\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
"}"

"QPushButton {\n"
"    background: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    padding-left: 10px;\n"
"    font: 11pt \"MS Shell Dlg 2\";\n"
"    min-height: 50px;\n"
"    text-align: left;\n"
"\n"
"    margin-left: 20px;\n"
"    margin-right: 30px;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgb(215, 215, 215);\n"
"}\n"
"QPushButton:pressed {\n"
"    background: rgb(200, 200, 200);\n"
"}\n"
"")
        self.listWrapper = QWidget()
        self.listWrapper.setGeometry(QRect(0, 0, 960, 786))
        
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWrapper.sizePolicy().hasHeightForWidth())

        self.listWrapper.setSizePolicy(sizePolicy)

        self.list = QVBoxLayout(self.listWrapper)
        self.list.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.list.setObjectName("list")

        self.addButton = QPushButton(self.content)
        self.addButton.setObjectName("pushButton")
        self.addButton.setFont(font)
        self.addButton.clicked.connect(lambda: self._onpopup(0))

        self.list.addWidget(self.addButton)

        self.scrollArea.setWidget(self.listWrapper)

        self.horizontalLayout.addWidget(self.OpeningPanel)
        self.horizontalLayout.addWidget(self.content)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        
        self.horizontalLayout.addWidget(self.OpeningPanel)
        self.horizontalLayout.addWidget(self.content)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.statistics = QFrame(Form)
        self.pageLabel = QLabel("Frekuensi Jurnal Pada Tahun", self.statistics)
        self.pageLabel.setGeometry(QRect(30, 30, 240, 30))
        self.pageLabel.setFont(font)
        self.pageLabel.setObjectName("pageLabel")

        self.pageDetail = QSpinBox(self.statistics)
        self.pageDetail.setObjectName('pageDetail')
        self.pageDetail.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.pageDetail.setMinimum(2010)
        self.pageDetail.setMaximum(3000)
        self.pageDetail.setValue(datetime.date.today().year)
        self.pageDetail.setGeometry(QRect(270, 30, 120, 30))
        self.pageDetail.lineEdit().setReadOnly(True)
        self.pageDetail.valueChanged.connect(self.updateStatistics)
        self.pageDetail.setFont(font)

        self.statisticsScrollArea = QScrollArea(self.statistics)
        self.statisticsScrollAreaHeight = 560
        self.statisticsScrollArea.setGeometry(QRect(30, 80, 890, self.statisticsScrollAreaHeight))
        self.statisticsScrollArea.setWidgetResizable(True)
        self.statisticsScrollArea.setObjectName("statisticsScrollArea")  

        self.statistics.setContentsMargins(40, 64, 20, -1)
        self.statistics.setObjectName("statistics")
        self.statistics.setStyleSheet(
"QFrame#statistics {\n"
"    background: rgb(200, 200, 200);\n"
"    border: 1px solid rgb(130, 130, 130);\n"
"    border-radius: 0px;\n"
"}\n"
"QPushButton {\n"
"    background: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(130, 130, 130);\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgb(215, 215, 215);\n"
"}\n"
"QPushButton:pressed {\n"
"    background: rgb(200, 200, 200);\n"
"}")

        self.statisticsScrollAreaWidget = QWidget()
        self.statisticsScrollAreaWidget.setObjectName("statisticsList")

        self.statisticsVerticalLayout = QVBoxLayout(self.statisticsScrollAreaWidget)
        self.statisticsVerticalLayout.setObjectName('statisticsVerticalLayout')

        self.statistic_1 = StatisticWithLabel(labelText='Januari')
        self.statistic_2 = StatisticWithLabel(labelText='Februari')
        self.statistic_3 = StatisticWithLabel(labelText='Maret')
        self.statistic_4 = StatisticWithLabel(labelText='April')
        self.statistic_5 = StatisticWithLabel(labelText='Mei')
        self.statistic_6 = StatisticWithLabel(labelText='Juni')
        self.statistic_7 = StatisticWithLabel(labelText='Juli')
        self.statistic_8 = StatisticWithLabel(labelText='Agustus')
        self.statistic_9 = StatisticWithLabel(labelText='September')
        self.statistic_10 = StatisticWithLabel(labelText='Oktober')
        self.statistic_11 = StatisticWithLabel(labelText='November')
        self.statistic_12 = StatisticWithLabel(labelText='Desember')

        self.statisticsList = [self.statistic_1, 
                               self.statistic_2,
                               self.statistic_3,
                               self.statistic_4, 
                               self.statistic_5,
                               self.statistic_6,
                               self.statistic_7, 
                               self.statistic_8,
                               self.statistic_9,
                               self.statistic_10, 
                               self.statistic_11,
                               self.statistic_12,]
        
        self.updateStatistics()

        for x in self.statisticsList:
            self.statisticsVerticalLayout.addLayout(x)

        self.statisticsScrollArea.setWidget(self.statisticsScrollAreaWidget)
        
        self.statistics.hide()

        self.retranslateUi(Form)
        self.controller.foreach(self.addJurnal)
        QMetaObject.connectSlotsByName(Form)

    def addJurnal(self, jurnal: Jurnal.Jurnal):
        _translate = QCoreApplication.translate
        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(13)

        exec("self.entry%d = QPushButton(self.content)" % self.entries)
        exec("self.entry%d.setObjectName('entry%d')" % (self.entries, self.entries))
        exec("self.list.insertWidget(1, self.entry%d)" % self.entries)
        exec("self.entry%d.setText(_translate('Form', '     %s | %s'))" % (self.entries, jurnal.waktuEdit, jurnal.judul.replace("'", "\\'").replace('"', '\\"')))
        exec("self.entry%d.clicked.connect(lambda: self._onpopup(%d))" % (self.entries, self.entries), locals())
        exec("self.entry%d.setFont(font)" % self.entries)

        self.entries += 1
        self.scrollAreaHeight = min(726, self.entries * 70)
        self.scrollArea.setGeometry(QRect(30, 30, 890, self.scrollAreaHeight))
        self.updateStatistics()

    def updateStatistics(self):
        year = int(self.pageDetail.text())
        freq = self.controller.getFrequencyArray(year)
        for i in range(len(self.statisticsList)):
            self.statisticsList[i].bar.setMaximum(monthrange(year, i+1)[1])
            self.statisticsList[i].bar.setValue(freq[i])
            self.statisticsList[i].refreshBar()

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.JurnalSubtitle.setText(_translate("Form", "Apa yang kamu pikirkan hari ini?"))
        self.JurnalTitle.setText(_translate("Form", "Jurnal"))
        self.ReturnButton.setText(_translate("Form", "Kembali"))
        self.StatisticsButton.setText(_translate("Form", "Statistik"))
        self.addButton.setText(_translate("Form", "     +          Tambah Jurnal Baru"))

    def _onStatistics(self):
        if self.mode == "List":
            self.mode = "Statistic"
            self.horizontalLayout.replaceWidget(self.content, self.statistics)
            self.content.hide()
            self.statistics.show()
        else:
            self.mode = "List"
            self.horizontalLayout.replaceWidget(self.statistics, self.content)
            self.statistics.hide()
            self.content.show()

    def _onpopup(self, codeIdx):
        self.popup = SleepOverlay(codeIdx, self.controller, self.parent)
        self.popup.move(0, 0)
        self.popup.resize(self.parent.width(), self.parent.height())
        self.popup.signals.close.connect(self._closepopup)
        self.popup.signals.confirm.connect(self._onconfirm)
        self.popup.codeIdx = codeIdx
        self.popup.show()

    def _closepopup(self):
        self.popup.close()

    def _onconfirm(self):
        try:
            self.controller.checkToday()
            self.controller.addJurnal(self.popup.titleInput.text(), self.popup.jurnalInput.toPlainText())
            
            for i in range(1, self.entries):
                exec("self.entry%d.deleteLater()" % i)

            self.entries = 1
            self.controller.foreach(self.addJurnal)
            self.scrollAreaHeight = min(726, self.entries * 70)
            self.scrollArea.setGeometry(QRect(30, 30, 890, self.scrollAreaHeight))

        except Exception as e:
            msg = QMessageBox()
            msg.setWindowTitle("Terjadi kesalahan!")
            msg.setText(str(e))
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
        
        self.popup.close()

if __name__ == "__main__":
    abspath = path.join(path.dirname(path.abspath(__file__)), '../img')
    app = QApplication(sys.argv)
    _id = QFontDatabase.addApplicationFont(path.join(abspath, "Helvetica/Helvetica.ttf"))    

    Form = QWidget()
    ui = JurnalForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
