from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from custom import UIWindow
import controller.MoodController as MoodController


class Ui_Form(UIWindow):
    def setupUi(self, Form):
        self.moodController = MoodController.MoodController()

        Form.setObjectName("Mood Menu")
        Form.resize(1280, 786)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.OpeningPanel = QtWidgets.QFrame(Form)
        self.OpeningPanel.setStyleSheet("QPushButton {\n"
                                        "    background: rgb(240, 240, 240);\n"
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
        self.OpeningPanel.setObjectName("OpeningPanel")
        self.ReturnButton = QtWidgets.QPushButton(self.OpeningPanel)
        self.ReturnButton.setGeometry(QtCore.QRect(30, 650, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ReturnButton.setFont(font)
        self.ReturnButton.setAutoFillBackground(False)
        self.ReturnButton.setStyleSheet("")
        self.ReturnButton.setCheckable(False)
        self.ReturnButton.setChecked(False)
        self.ReturnButton.setAutoDefault(False)
        self.ReturnButton.setDefault(False)
        self.ReturnButton.setFlat(False)
        self.ReturnButton.setObjectName("ReturnButton")
        self.label_mood = QtWidgets.QLabel(self.OpeningPanel)
        self.label_mood.setGeometry(QtCore.QRect(30, 60, 271, 41))
        self.label_mood.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_mood.setFont(font)
        self.label_mood.setObjectName("label_mood")
        self.label_deskripsi = QtWidgets.QLabel(self.OpeningPanel)
        self.label_deskripsi.setGeometry(QtCore.QRect(30, 110, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_deskripsi.setFont(font)
        self.label_deskripsi.setObjectName("label_deskripsi")
        self.button1 = QtWidgets.QPushButton(
            self.OpeningPanel, clicked=lambda: self.onClick(":)"))
        self.button1.setGeometry(QtCore.QRect(30, 230, 41, 41))
        self.button1.setObjectName("button1")
        self.button6 = QtWidgets.QPushButton(
            self.OpeningPanel, clicked=lambda: self.onClick(":3"))
        self.button6.setGeometry(QtCore.QRect(90, 290, 41, 41))
        self.button6.setObjectName("button6")
        self.button4 = QtWidgets.QPushButton(
            self.OpeningPanel, clicked=lambda: self.onClick(":v"))
        self.button4.setGeometry(QtCore.QRect(210, 230, 41, 41))
        self.button4.setObjectName("button4")
        self.button5 = QtWidgets.QPushButton(
            self.OpeningPanel, clicked=lambda: self.onClick(":D"))
        self.button5.setGeometry(QtCore.QRect(30, 290, 41, 41))
        self.button5.setObjectName("button5")
        self.button2 = QtWidgets.QPushButton(
            self.OpeningPanel, clicked=lambda: self.onClick(":("))
        self.button2.setGeometry(QtCore.QRect(90, 230, 41, 41))
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(
            self.OpeningPanel, clicked=lambda: self.onClick(":O"))
        self.button3.setGeometry(QtCore.QRect(150, 230, 41, 41))
        self.button3.setObjectName("button3")
        self.button7 = QtWidgets.QPushButton(
            self.OpeningPanel, clicked=lambda: self.onClick(":|"))
        self.button7.setGeometry(QtCore.QRect(150, 290, 41, 41))
        self.button7.setObjectName("button7")
        self.button8 = QtWidgets.QPushButton(
            self.OpeningPanel, clicked=lambda: self.onClick(":\\"))
        self.button8.setGeometry(QtCore.QRect(210, 290, 41, 41))
        self.button8.setObjectName("button8")
        self.line_2 = QtWidgets.QFrame(self.OpeningPanel)
        self.line_2.setGeometry(QtCore.QRect(320, -30, 20, 811))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.frame = QtWidgets.QFrame(self.OpeningPanel)
        self.frame.setGeometry(QtCore.QRect(1080, 10, 121, 121))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(-40, 0, 191, 31))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_tanggal = QtWidgets.QLabel(self.frame_2)
        self.label_tanggal.setGeometry(QtCore.QRect(50, 0, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(False)
        self.label_tanggal.setFont(font)
        self.label_tanggal.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_tanggal.setObjectName("label_tanggal")
        self.label_mood_sekarang = QtWidgets.QLabel(self.frame)
        self.label_mood_sekarang.setGeometry(QtCore.QRect(0, 30, 121, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setUnderline(False)
        self.label_mood_sekarang.setFont(font)
        self.label_mood_sekarang.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mood_sekarang.setObjectName("label_mood_sekarang")
        self.label_frekuensi = QtWidgets.QLabel(self.OpeningPanel)
        self.label_frekuensi.setGeometry(QtCore.QRect(340, 10, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_frekuensi.setFont(font)
        self.label_frekuensi.setObjectName("label_frekuensi")
        self.label_mood_1 = QtWidgets.QLabel(self.OpeningPanel)
        self.label_mood_1.setGeometry(QtCore.QRect(360, 70, 41, 41))
        self.label_mood_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_mood_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mood_1.setObjectName("label_mood_1")
        self.progress_bar_1 = QtWidgets.QProgressBar(self.OpeningPanel)
        self.progress_bar_1.setGeometry(QtCore.QRect(420, 70, 601, 41))
        self.progress_bar_1.setProperty("value", 0)
        self.progress_bar_1.setObjectName("progress_bar_1")
        self.label_mood_2 = QtWidgets.QLabel(self.OpeningPanel)
        self.label_mood_2.setGeometry(QtCore.QRect(360, 130, 41, 41))
        self.label_mood_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_mood_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mood_2.setObjectName("label_mood_2")
        self.progress_bar_2 = QtWidgets.QProgressBar(self.OpeningPanel)
        self.progress_bar_2.setGeometry(QtCore.QRect(420, 130, 601, 41))
        self.progress_bar_2.setProperty("value", 0)
        self.progress_bar_2.setObjectName("progress_bar_2")
        self.label_mood_3 = QtWidgets.QLabel(self.OpeningPanel)
        self.label_mood_3.setGeometry(QtCore.QRect(360, 190, 41, 41))
        self.label_mood_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_mood_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mood_3.setObjectName("label_mood_3")
        self.progress_bar_3 = QtWidgets.QProgressBar(self.OpeningPanel)
        self.progress_bar_3.setGeometry(QtCore.QRect(420, 190, 601, 41))
        self.progress_bar_3.setProperty("value", 0)
        self.progress_bar_3.setObjectName("progress_bar_3")
        self.progress_bar_4 = QtWidgets.QProgressBar(self.OpeningPanel)
        self.progress_bar_4.setGeometry(QtCore.QRect(420, 250, 601, 41))
        self.progress_bar_4.setProperty("value", 0)
        self.progress_bar_4.setObjectName("progress_bar_4")
        self.label_mood_4 = QtWidgets.QLabel(self.OpeningPanel)
        self.label_mood_4.setGeometry(QtCore.QRect(360, 250, 41, 41))
        self.label_mood_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_mood_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mood_4.setObjectName("label_mood_4")
        self.progress_bar_7 = QtWidgets.QProgressBar(self.OpeningPanel)
        self.progress_bar_7.setGeometry(QtCore.QRect(420, 430, 601, 41))
        self.progress_bar_7.setProperty("value", 0)
        self.progress_bar_7.setObjectName("progress_bar_7")
        self.label_mood_8 = QtWidgets.QLabel(self.OpeningPanel)
        self.label_mood_8.setGeometry(QtCore.QRect(360, 490, 41, 41))
        self.label_mood_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_mood_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mood_8.setObjectName("label_mood_8")
        self.label_mood_7 = QtWidgets.QLabel(self.OpeningPanel)
        self.label_mood_7.setGeometry(QtCore.QRect(360, 430, 41, 41))
        self.label_mood_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_mood_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mood_7.setObjectName("label_mood_7")
        self.label_mood_5 = QtWidgets.QLabel(self.OpeningPanel)
        self.label_mood_5.setGeometry(QtCore.QRect(360, 310, 41, 41))
        self.label_mood_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_mood_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mood_5.setObjectName("label_mood_5")
        self.progress_bar_8 = QtWidgets.QProgressBar(self.OpeningPanel)
        self.progress_bar_8.setGeometry(QtCore.QRect(420, 490, 601, 41))
        self.progress_bar_8.setProperty("value", 0)
        self.progress_bar_8.setObjectName("progress_bar_8")
        self.progress_bar_5 = QtWidgets.QProgressBar(self.OpeningPanel)
        self.progress_bar_5.setGeometry(QtCore.QRect(420, 310, 601, 41))
        self.progress_bar_5.setProperty("value", 0)
        self.progress_bar_5.setObjectName("progress_bar_5")
        self.progress_bar_6 = QtWidgets.QProgressBar(self.OpeningPanel)
        self.progress_bar_6.setGeometry(QtCore.QRect(420, 370, 601, 41))
        self.progress_bar_6.setProperty("value", 0)
        self.progress_bar_6.setObjectName("progress_bar_6")
        self.label_mood_6 = QtWidgets.QLabel(self.OpeningPanel)
        self.label_mood_6.setGeometry(QtCore.QRect(360, 370, 41, 41))
        self.label_mood_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_mood_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mood_6.setObjectName("label_mood_6")
        self.label_deskripsi_3 = QtWidgets.QLabel(self.OpeningPanel)
        self.label_deskripsi_3.setGeometry(QtCore.QRect(30, 150, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_deskripsi_3.setFont(font)
        self.label_deskripsi_3.setObjectName("label_deskripsi_3")
        self.horizontalLayout.addWidget(self.OpeningPanel)

        self.retranslateUi(Form)
        self.updateView()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ReturnButton.setText(_translate("Form", "Kembali"))
        self.label_mood.setText(_translate("Form", "Mood"))
        self.label_deskripsi.setText(
            _translate("Form", "Bagaimana perasaanmu"))
        self.button1.setText(_translate("Form", ":)"))
        self.button6.setText(_translate("Form", ":3"))
        self.button4.setText(_translate("Form", ":v"))
        self.button5.setText(_translate("Form", ":D"))
        self.button2.setText(_translate("Form", ":("))
        self.button3.setText(_translate("Form", ":O"))
        self.button7.setText(_translate("Form", ":|"))
        self.button8.setText(_translate("Form", ":\\"))
        self.label_tanggal.setText(_translate(
            "Form", datetime.datetime.now().strftime("%d/%m/%Y")))
        self.label_mood_sekarang.setText(_translate("Form", ""))
        self.label_frekuensi.setText(_translate(
            "Form", "Frekuensi Mood 30 Hari Terakhir"))
        self.label_mood_1.setText(_translate("Form", ":)"))
        self.label_mood_2.setText(_translate("Form", ":("))
        self.label_mood_3.setText(_translate("Form", ":O"))
        self.label_mood_4.setText(_translate("Form", ":v"))
        self.label_mood_8.setText(_translate("Form", ":\\"))
        self.label_mood_7.setText(_translate("Form", ":|"))
        self.label_mood_5.setText(_translate("Form", ":D"))
        self.label_mood_6.setText(_translate("Form", ":3"))
        self.label_deskripsi_3.setText(_translate("Form", "hari ini?"))

    def onClick(self, mood):
        # Set current mood, insert to database, and update view
        self.label_mood_sekarang.setText(mood)
        self.moodController.addMood(mood)
        self.updateView()

    def updateView(self):
        # Set current mood
        currentMood = self.moodController.getCurrentMood()
        if currentMood != "NULL":
            self.label_mood_sekarang.setText(currentMood)

        # Set progress bar
        self.progress_bar_1.setValue(self.moodController.getPercentage(':)'))
        self.progress_bar_2.setValue(self.moodController.getPercentage(':('))
        self.progress_bar_3.setValue(self.moodController.getPercentage(':O'))
        self.progress_bar_4.setValue(self.moodController.getPercentage(':v'))
        self.progress_bar_5.setValue(self.moodController.getPercentage(':D'))
        self.progress_bar_6.setValue(self.moodController.getPercentage(':3'))
        self.progress_bar_7.setValue(self.moodController.getPercentage(':|'))
        self.progress_bar_8.setValue(self.moodController.getPercentage(':\\'))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
