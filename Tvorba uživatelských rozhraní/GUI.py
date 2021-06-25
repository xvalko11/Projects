# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeui.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QuizzApp(object):
    def setupUi(self, QuizzApp):
        QuizzApp.setObjectName("QuizzApp")
        QuizzApp.resize(800, 840)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QuizzApp.sizePolicy().hasHeightForWidth())
        QuizzApp.setSizePolicy(sizePolicy)
        QuizzApp.setMaximumSize(QtCore.QSize(1900, 1133))
        QuizzApp.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(QuizzApp)
        self.centralwidget.setStyleSheet("background-color:#222629;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.homepage = QtWidgets.QWidget()
        self.homepage.setObjectName("homepage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.homepage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.nadpis = QtWidgets.QLabel(self.homepage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nadpis.sizePolicy().hasHeightForWidth())
        self.nadpis.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Saab")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.nadpis.setFont(font)
        self.nadpis.setStyleSheet("color:#696969;")
        self.nadpis.setObjectName("nadpis")
        self.gridLayout_2.addWidget(self.nadpis, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.btn3 = QtWidgets.QPushButton(self.homepage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        self.btn3.setBaseSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.btn3.setFont(font)
        self.btn3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn3.setStyleSheet("QPushButton{border-image: url(./icons/historystock.jpg);\n"
"color:#A4A4A4; }\n"
"QPushButton:hover{\n"
"    border-image: url(./icons/historyhover.jpg);\n"
"color:black;\n"
"}\n"
"QPushButton:pressed { border-image: url(./icons/historystock.jpg) }")
        self.btn3.setObjectName("btn3")
        self.gridLayout.addWidget(self.btn3, 1, 2, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.homepage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy)
        self.btn8.setBaseSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.btn8.setFont(font)
        self.btn8.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn8.setStyleSheet("QPushButton{border-image: url(./icons/gamesstock.jpg); \n"
"color:#A4A4A4;}\n"
"QPushButton:hover{\n"
"    border-image: url(./icons/gameshover.jpg);\n"
"color:black;\n"
"}\n"
"QPushButton:pressed { border-image: url(./icons/gamesstock.jpg) }")
        self.btn8.setObjectName("btn8")
        self.gridLayout.addWidget(self.btn8, 3, 1, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.homepage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        self.btn1.setBaseSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.btn1.setFont(font)
        self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn1.setStyleSheet("\n"
"QPushButton{border-image: url(./icons/naturestock.jpg);\n"
"color:#A4A4A4; }\n"
"QPushButton:hover{\n"
"    border-image: url(./icons/naturehover.jpg);\n"
"color:black;\n"
"}\n"
"QPushButton:pressed { border-image: url(./icons/naturestock.jpg) }\n"
"\n"
"")
        self.btn1.setObjectName("btn1")
        self.gridLayout.addWidget(self.btn1, 1, 0, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.homepage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy)
        self.btn5.setBaseSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.btn5.setFont(font)
        self.btn5.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn5.setStyleSheet("QPushButton{border-image: url(./icons/techstock.jpg); \n"
"color:#A4A4A4;}\n"
"QPushButton:hover{\n"
"    border-image: url(./icons/techhover.jpg);\n"
"color:black;\n"
"}\n"
"QPushButton:pressed { border-image: url(./icons/techstock.jpg) }")
        self.btn5.setObjectName("btn5")
        self.gridLayout.addWidget(self.btn5, 2, 1, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.homepage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        self.btn2.setBaseSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.btn2.setFont(font)
        self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn2.setStyleSheet("QPushButton{border-image: url(./icons/musicstock.jpg); \n"
"color:#A4A4A4;}\n"
"QPushButton:hover{\n"
"    border-image: url(./icons/musichover.jpg);\n"
"color:black;\n"
"}\n"
"QPushButton:pressed { border-image: url(./icons/musicstock.jpg) }")
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 1, 1, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.homepage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy)
        self.btn4.setBaseSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.btn4.setFont(font)
        self.btn4.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn4.setStyleSheet("QPushButton{border-image: url(./icons/sciencestock.jpg);\n"
"color:#A4A4A4; }\n"
"QPushButton:hover{\n"
"    border-image: url(./icons/sciencehover.jpg);\n"
"color:black;\n"
"}\n"
"QPushButton:pressed { border-image: url(./icons/sciencestock.jpg) }")
        self.btn4.setObjectName("btn4")
        self.gridLayout.addWidget(self.btn4, 2, 0, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.homepage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy)
        self.btn6.setBaseSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.btn6.setFont(font)
        self.btn6.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn6.setStyleSheet("QPushButton{border-image: url(./icons/geostock.jpg);\n"
"color:#A4A4A4; }\n"
"QPushButton:hover{\n"
"    border-image: url(./icons/geohover.jpg);\n"
"color:black;\n"
"}\n"
"QPushButton:pressed { border-image: url(./icons/geostock.jpg) }")
        self.btn6.setObjectName("btn6")
        self.gridLayout.addWidget(self.btn6, 2, 2, 1, 1)
        self.btn9 = QtWidgets.QPushButton(self.homepage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy)
        self.btn9.setBaseSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.btn9.setFont(font)
        self.btn9.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn9.setStyleSheet("QPushButton{border-image: url(./icons/filmstock.jpg); \n"
"color:#A4A4A4;}\n"
"QPushButton:hover{\n"
"    border-image: url(./icons/filmhover.jpg);\n"
"color:black;\n"
"}\n"
"QPushButton:pressed { border-image: url(./icons/filmstock.jpg) }")
        self.btn9.setObjectName("btn9")
        self.gridLayout.addWidget(self.btn9, 3, 2, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.homepage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy)
        self.btn7.setBaseSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.btn7.setFont(font)
        self.btn7.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn7.setStyleSheet("QPushButton{border-image: url(./icons/spacestock.jpg); \n"
"color:#A4A4A4;}\n"
"QPushButton:hover{\n"
"    border-image: url(./icons/spacehover.jpg);\n"
"color:black;\n"
"}\n"
"QPushButton:pressed { border-image: url(./icons/spacestock.jpg) }")
        self.btn7.setObjectName("btn7")
        self.gridLayout.addWidget(self.btn7, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 0, 1, 3)
        self.stackedWidget.addWidget(self.homepage)
        self.categorypage = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("ori1Uni")
        font.setPointSize(30)
        self.categorypage.setFont(font)
        self.categorypage.setObjectName("categorypage")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.categorypage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backToHomeBtn = QtWidgets.QPushButton(self.categorypage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backToHomeBtn.sizePolicy().hasHeightForWidth())
        self.backToHomeBtn.setSizePolicy(sizePolicy)
        self.backToHomeBtn.setMinimumSize(QtCore.QSize(150, 0))
        self.backToHomeBtn.setMaximumSize(QtCore.QSize(50000, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.backToHomeBtn.setFont(font)
        self.backToHomeBtn.setStyleSheet("QPushButton {\n"
"background-color: #86C232; \n"
"color: white;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white; \n"
"  color: black;\n"
"  border: 5px solid #86C232; \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #86C232; \n"
"color: white;\n"
"}")
        self.backToHomeBtn.setObjectName("backToHomeBtn")
        self.horizontalLayout.addWidget(self.backToHomeBtn)
        self.addQuizBtn = QtWidgets.QPushButton(self.categorypage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addQuizBtn.sizePolicy().hasHeightForWidth())
        self.addQuizBtn.setSizePolicy(sizePolicy)
        self.addQuizBtn.setMinimumSize(QtCore.QSize(1, 50))
        self.addQuizBtn.setMaximumSize(QtCore.QSize(5000, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addQuizBtn.setFont(font)
        self.addQuizBtn.setStyleSheet("QPushButton {\n"
"background-color: #86C232; \n"
"color: white;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white; \n"
"  color: black;\n"
"  border: 5px solid #86C232; \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #86C232; \n"
"color: white;\n"
"}")
        self.addQuizBtn.setObjectName("addQuizBtn")
        self.horizontalLayout.addWidget(self.addQuizBtn, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lineEdit = QtWidgets.QLineEdit(self.categorypage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setStyleSheet("QLineEdit{color: gray;\n"
"              }\n"
"")
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.categorypage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(375, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(500, 16777215))
        self.listWidget.setBaseSize(QtCore.QSize(500, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QListView{\n"
"color:white\n"
"}\n"
"QListView::item { \n"
"height: 65px;\n"
"font }\n"
"\n"
"QListView::item:alternate {\n"
" }\n"
"\n"
"QListView::item:hover {\n"
"    background: #474B4F\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    background: #696969;\n"
"}")
        self.listWidget.setAlternatingRowColors(False)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout_2.addWidget(self.listWidget, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.nOfQuestionText = QtWidgets.QTextEdit(self.categorypage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nOfQuestionText.sizePolicy().hasHeightForWidth())
        self.nOfQuestionText.setSizePolicy(sizePolicy)
        self.nOfQuestionText.setMaximumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nOfQuestionText.setFont(font)
        self.nOfQuestionText.setStyleSheet("QTextEdit{\n"
"color:#696969}")
        self.nOfQuestionText.setPlaceholderText("")
        self.nOfQuestionText.setObjectName("nOfQuestionText")
        self.verticalLayout_4.addWidget(self.nOfQuestionText)
        self.nOfFinishedText = QtWidgets.QTextEdit(self.categorypage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nOfFinishedText.sizePolicy().hasHeightForWidth())
        self.nOfFinishedText.setSizePolicy(sizePolicy)
        self.nOfFinishedText.setMaximumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nOfFinishedText.setFont(font)
        self.nOfFinishedText.setStyleSheet("QTextEdit{\n"
"color:#696969}")
        self.nOfFinishedText.setPlaceholderText("")
        self.nOfFinishedText.setObjectName("nOfFinishedText")
        self.verticalLayout_4.addWidget(self.nOfFinishedText)
        self.descriptionText = QtWidgets.QTextEdit(self.categorypage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.descriptionText.sizePolicy().hasHeightForWidth())
        self.descriptionText.setSizePolicy(sizePolicy)
        self.descriptionText.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.descriptionText.setFont(font)
        self.descriptionText.setStyleSheet("QTextEdit{\n"
"color:#696969}")
        self.descriptionText.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.descriptionText.setPlaceholderText("")
        self.descriptionText.setObjectName("descriptionText")
        self.verticalLayout_4.addWidget(self.descriptionText)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.startQuizButton = QtWidgets.QPushButton(self.categorypage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startQuizButton.sizePolicy().hasHeightForWidth())
        self.startQuizButton.setSizePolicy(sizePolicy)
        self.startQuizButton.setMinimumSize(QtCore.QSize(60, 50))
        self.startQuizButton.setMaximumSize(QtCore.QSize(2000, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startQuizButton.setFont(font)
        self.startQuizButton.setStyleSheet("QPushButton {\n"
"background-color: #86C232; \n"
"color: white;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white; \n"
"  color:black;\n"
"  border: 5px solid #86C232; \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #86C232; \n"
"color: white;\n"
"}")
        self.startQuizButton.setObjectName("startQuizButton")
        self.verticalLayout.addWidget(self.startQuizButton)
        self.stackedWidget.addWidget(self.categorypage)
        self.quizzpage = QtWidgets.QWidget()
        self.quizzpage.setObjectName("quizzpage")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.quizzpage)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setContentsMargins(30, -1, 30, -1)
        self.gridLayout_7.setHorizontalSpacing(30)
        self.gridLayout_7.setVerticalSpacing(25)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.BButton = QtWidgets.QPushButton(self.quizzpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BButton.sizePolicy().hasHeightForWidth())
        self.BButton.setSizePolicy(sizePolicy)
        self.BButton.setStyleSheet("QPushButton {\n"
"background-color:      #696969; \n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white; \n"
"  color: black;\n"
"  border: 5px solid      #696969; \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #696969; \n"
"color: white;\n"
"}")
        self.BButton.setObjectName("BButton")
        self.gridLayout_7.addWidget(self.BButton, 2, 0, 1, 1)
        self.AButton = QtWidgets.QPushButton(self.quizzpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AButton.sizePolicy().hasHeightForWidth())
        self.AButton.setSizePolicy(sizePolicy)
        self.AButton.setStyleSheet("QPushButton {\n"
"background-color:      #696969; \n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white; \n"
"  color: black;\n"
"  border: 5px solid      #696969; \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #696969; \n"
"color: white;\n"
"}")
        self.AButton.setObjectName("AButton")
        self.gridLayout_7.addWidget(self.AButton, 1, 0, 1, 1)
        self.CButton = QtWidgets.QPushButton(self.quizzpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CButton.sizePolicy().hasHeightForWidth())
        self.CButton.setSizePolicy(sizePolicy)
        self.CButton.setStyleSheet("QPushButton {\n"
"background-color:      #696969; \n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white; \n"
"  color: black;\n"
"  border: 5px solid      #696969; \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #696969; \n"
"color: white;\n"
"}")
        self.CButton.setObjectName("CButton")
        self.gridLayout_7.addWidget(self.CButton, 3, 0, 1, 1)
        self.QuestionText = QtWidgets.QTextEdit(self.quizzpage)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.QuestionText.setFont(font)
        self.QuestionText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QuestionText.setStyleSheet("QTextEdit{\n"
"color:#696969}")
        self.QuestionText.setObjectName("QuestionText")
        self.gridLayout_7.addWidget(self.QuestionText, 0, 0, 1, 1)
        self.DButton = QtWidgets.QPushButton(self.quizzpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DButton.sizePolicy().hasHeightForWidth())
        self.DButton.setSizePolicy(sizePolicy)
        self.DButton.setStyleSheet("QPushButton {\n"
"background-color:      #696969; \n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white; \n"
"  color: black;\n"
"  border: 5px solid      #696969; \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #696969; \n"
"color: white;\n"
"}")
        self.DButton.setObjectName("DButton")
        self.gridLayout_7.addWidget(self.DButton, 4, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 4, 0, 1, 3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.qCountText = QtWidgets.QLineEdit(self.quizzpage)
        self.qCountText.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qCountText.sizePolicy().hasHeightForWidth())
        self.qCountText.setSizePolicy(sizePolicy)
        self.qCountText.setAutoFillBackground(False)
        self.qCountText.setStyleSheet("color:#696969")
        self.qCountText.setFrame(False)
        self.qCountText.setReadOnly(True)
        self.qCountText.setObjectName("qCountText")
        self.horizontalLayout_5.addWidget(self.qCountText)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.endQuizButton = QtWidgets.QPushButton(self.quizzpage)
        self.endQuizButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.endQuizButton.setStyleSheet("QPushButton {\n"
"background-color:  #FF0000; \n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white; \n"
"  color: red;\n"
"  border: 2px solid      red; \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: red; \n"
"color: white;\n"
"}")
        self.endQuizButton.setObjectName("endQuizButton")
        self.horizontalLayout_5.addWidget(self.endQuizButton)
        self.gridLayout_6.addLayout(self.horizontalLayout_5, 1, 0, 1, 3)
        self.stackedWidget.addWidget(self.quizzpage)
        self.endingPage = QtWidgets.QWidget()
        self.endingPage.setObjectName("endingPage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.endingPage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.phraseText = QtWidgets.QLineEdit(self.endingPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phraseText.sizePolicy().hasHeightForWidth())
        self.phraseText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.phraseText.setFont(font)
        self.phraseText.setStyleSheet("QLineEdit{\n"
"color:#696969}")
        self.phraseText.setText("")
        self.phraseText.setFrame(False)
        self.phraseText.setAlignment(QtCore.Qt.AlignCenter)
        self.phraseText.setReadOnly(True)
        self.phraseText.setObjectName("phraseText")
        self.verticalLayout_5.addWidget(self.phraseText)
        self.pointsText = QtWidgets.QLineEdit(self.endingPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pointsText.sizePolicy().hasHeightForWidth())
        self.pointsText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.pointsText.setFont(font)
        self.pointsText.setStyleSheet("QLineEdit{\n"
"color:#696969}")
        self.pointsText.setText("")
        self.pointsText.setFrame(False)
        self.pointsText.setAlignment(QtCore.Qt.AlignCenter)
        self.pointsText.setReadOnly(True)
        self.pointsText.setObjectName("pointsText")
        self.verticalLayout_5.addWidget(self.pointsText)
        self.againButton = QtWidgets.QPushButton(self.endingPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.againButton.sizePolicy().hasHeightForWidth())
        self.againButton.setSizePolicy(sizePolicy)
        self.againButton.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.againButton.setFont(font)
        self.againButton.setStyleSheet("QPushButton {\n"
"background-color: #86C232; \n"
"color: white;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white; \n"
"  color:black;\n"
"  border: 5px solid #86C232; \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #86C232; \n"
"color: white;\n"
"}")
        self.againButton.setObjectName("againButton")
        self.verticalLayout_5.addWidget(self.againButton)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.endingPage)
        self.addquizpage = QtWidgets.QWidget()
        self.addquizpage.setObjectName("addquizpage")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.addquizpage)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setContentsMargins(-1, 20, -1, 20)
        self.gridLayout_8.setHorizontalSpacing(6)
        self.gridLayout_8.setVerticalSpacing(20)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.answerD = QtWidgets.QTextEdit(self.addquizpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerD.sizePolicy().hasHeightForWidth())
        self.answerD.setSizePolicy(sizePolicy)
        self.answerD.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.answerD.setFont(font)
        self.answerD.setStyleSheet("QTextEdit{color:gray}")
        self.answerD.setObjectName("answerD")
        self.gridLayout_8.addWidget(self.answerD, 4, 0, 1, 1)
        self.radioC = QtWidgets.QRadioButton(self.addquizpage)
        self.radioC.setStyleSheet("QRadioButton {\n"
"    color:                  white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  15px;\n"
"    height:                 15px;\n"
"    border-radius:          9px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:  #61892F;\n"
"    border:                 2px solid black;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    border:                 2px solid black;\n"
"}")
        self.radioC.setText("")
        self.radioC.setObjectName("radioC")
        self.gridLayout_8.addWidget(self.radioC, 3, 1, 1, 1)
        self.answerB = QtWidgets.QTextEdit(self.addquizpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerB.sizePolicy().hasHeightForWidth())
        self.answerB.setSizePolicy(sizePolicy)
        self.answerB.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.answerB.setFont(font)
        self.answerB.setStyleSheet("QTextEdit{color:gray}")
        self.answerB.setObjectName("answerB")
        self.gridLayout_8.addWidget(self.answerB, 2, 0, 1, 1)
        self.answerC = QtWidgets.QTextEdit(self.addquizpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerC.sizePolicy().hasHeightForWidth())
        self.answerC.setSizePolicy(sizePolicy)
        self.answerC.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.answerC.setFont(font)
        self.answerC.setStyleSheet("QTextEdit{color:gray}")
        self.answerC.setObjectName("answerC")
        self.gridLayout_8.addWidget(self.answerC, 3, 0, 1, 1)
        self.radioB = QtWidgets.QRadioButton(self.addquizpage)
        self.radioB.setStyleSheet("QRadioButton {\n"
"    color:                  white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  15px;\n"
"    height:                 15px;\n"
"    border-radius:          9px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:  #61892F;\n"
"    border:                 2px solid black;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    border:                 2px solid black;\n"
"}")
        self.radioB.setText("")
        self.radioB.setChecked(False)
        self.radioB.setObjectName("radioB")
        self.gridLayout_8.addWidget(self.radioB, 2, 1, 1, 1)
        self.answerA = QtWidgets.QTextEdit(self.addquizpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answerA.sizePolicy().hasHeightForWidth())
        self.answerA.setSizePolicy(sizePolicy)
        self.answerA.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.answerA.setFont(font)
        self.answerA.setStyleSheet("QTextEdit{color:gray}")
        self.answerA.setObjectName("answerA")
        self.gridLayout_8.addWidget(self.answerA, 1, 0, 1, 1)
        self.radioA = QtWidgets.QRadioButton(self.addquizpage)
        self.radioA.setMinimumSize(QtCore.QSize(25, 0))
        self.radioA.setToolTip("")
        self.radioA.setToolTipDuration(3000)
        self.radioA.setWhatsThis("")
        self.radioA.setStyleSheet("QRadioButton {\n"
"    color:                  white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  15px;\n"
"    height:                 15px;\n"
"    border-radius:          9px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:  #61892F;\n"
"    border:                 2px solid black;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    border:                 2px solid black;\n"
"}")
        self.radioA.setText("")
        self.radioA.setChecked(True)
        self.radioA.setObjectName("radioA")
        self.gridLayout_8.addWidget(self.radioA, 1, 1, 1, 1)
        self.radioD = QtWidgets.QRadioButton(self.addquizpage)
        self.radioD.setStyleSheet("QRadioButton {\n"
"    color:                  white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  15px;\n"
"    height:                 15px;\n"
"    border-radius:          9px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:  #61892F;\n"
"    border:                 2px solid black;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    border:                 2px solid black;\n"
"}")
        self.radioD.setText("")
        self.radioD.setObjectName("radioD")
        self.gridLayout_8.addWidget(self.radioD, 4, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 1, 1, 1, 2)
        self.finishQuizBtn = QtWidgets.QPushButton(self.addquizpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finishQuizBtn.sizePolicy().hasHeightForWidth())
        self.finishQuizBtn.setSizePolicy(sizePolicy)
        self.finishQuizBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.finishQuizBtn.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.finishQuizBtn.setFont(font)
        self.finishQuizBtn.setStyleSheet("QPushButton {\n"
"background-color: #86C232; \n"
"color: white;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white; \n"
"  color: black;\n"
"  border: 5px solid #86C232; \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #86C232; \n"
"color: white;\n"
"}")
        self.finishQuizBtn.setObjectName("finishQuizBtn")
        self.gridLayout_9.addWidget(self.finishQuizBtn, 2, 2, 1, 2)
        self.prevQuestionBtn = QtWidgets.QPushButton(self.addquizpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevQuestionBtn.sizePolicy().hasHeightForWidth())
        self.prevQuestionBtn.setSizePolicy(sizePolicy)
        self.prevQuestionBtn.setMaximumSize(QtCore.QSize(35, 600))
        self.prevQuestionBtn.setStyleSheet("QPushButton{background-color:#696969}")
        self.prevQuestionBtn.setObjectName("prevQuestionBtn")
        self.gridLayout_9.addWidget(self.prevQuestionBtn, 1, 0, 1, 1)
        self.nextQuestionBtn = QtWidgets.QPushButton(self.addquizpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextQuestionBtn.sizePolicy().hasHeightForWidth())
        self.nextQuestionBtn.setSizePolicy(sizePolicy)
        self.nextQuestionBtn.setMinimumSize(QtCore.QSize(10, 0))
        self.nextQuestionBtn.setMaximumSize(QtCore.QSize(35, 600))
        self.nextQuestionBtn.setBaseSize(QtCore.QSize(60, 0))
        self.nextQuestionBtn.setStyleSheet("QPushButton{background-color:#696969}")
        self.nextQuestionBtn.setObjectName("nextQuestionBtn")
        self.gridLayout_9.addWidget(self.nextQuestionBtn, 1, 3, 1, 1)
        self.addQuestionText = QtWidgets.QTextEdit(self.addquizpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addQuestionText.sizePolicy().hasHeightForWidth())
        self.addQuestionText.setSizePolicy(sizePolicy)
        self.addQuestionText.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.addQuestionText.setFont(font)
        self.addQuestionText.setStyleSheet("QTextEdit{color:grey}")
        self.addQuestionText.setObjectName("addQuestionText")
        self.gridLayout_9.addWidget(self.addQuestionText, 0, 0, 1, 4)
        self.backToNamingBtn = QtWidgets.QPushButton(self.addquizpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backToNamingBtn.sizePolicy().hasHeightForWidth())
        self.backToNamingBtn.setSizePolicy(sizePolicy)
        self.backToNamingBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.backToNamingBtn.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.backToNamingBtn.setFont(font)
        self.backToNamingBtn.setStyleSheet("QPushButton {\n"
"background-color: #FD3030; \n"
"color: white;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white; \n"
"  color: black;\n"
"  border: 5px solid #FD3030; \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #FD3030; \n"
"color: white;\n"
"}")
        self.backToNamingBtn.setObjectName("backToNamingBtn")
        self.gridLayout_9.addWidget(self.backToNamingBtn, 2, 0, 1, 2)
        self.stackedWidget.addWidget(self.addquizpage)
        self.namequizpage = QtWidgets.QWidget()
        self.namequizpage.setObjectName("namequizpage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.namequizpage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.namequizpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("color:#696969")
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lineEdit_3)
        self.categoryComboBox = QtWidgets.QComboBox(self.namequizpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryComboBox.sizePolicy().hasHeightForWidth())
        self.categoryComboBox.setSizePolicy(sizePolicy)
        self.categoryComboBox.setMinimumSize(QtCore.QSize(0, 35))
        self.categoryComboBox.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.categoryComboBox.setFont(font)
        self.categoryComboBox.setStyleSheet("QComboBox { \n"
"color: #696969;\n"
"}\n"
"")
        self.categoryComboBox.setObjectName("categoryComboBox")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.categoryComboBox)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.nameText = QtWidgets.QTextEdit(self.namequizpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameText.sizePolicy().hasHeightForWidth())
        self.nameText.setSizePolicy(sizePolicy)
        self.nameText.setMinimumSize(QtCore.QSize(0, 0))
        self.nameText.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.nameText.setFont(font)
        self.nameText.setStyleSheet("QTextEdit{color:#696969}")
        self.nameText.setObjectName("nameText")
        self.verticalLayout_3.addWidget(self.nameText)
        self.descText = QtWidgets.QTextEdit(self.namequizpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.descText.sizePolicy().hasHeightForWidth())
        self.descText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.descText.setFont(font)
        self.descText.setStyleSheet("QTextEdit{color:#696969}\n"
"")
        self.descText.setObjectName("descText")
        self.verticalLayout_3.addWidget(self.descText)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.deleteNamingQuizBtn = QtWidgets.QPushButton(self.namequizpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteNamingQuizBtn.sizePolicy().hasHeightForWidth())
        self.deleteNamingQuizBtn.setSizePolicy(sizePolicy)
        self.deleteNamingQuizBtn.setMinimumSize(QtCore.QSize(35, 35))
        self.deleteNamingQuizBtn.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.deleteNamingQuizBtn.setFont(font)
        self.deleteNamingQuizBtn.setStyleSheet("QPushButton {\n"
"background-color: #FD3030; \n"
"color: white;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white; \n"
"  color: black;\n"
"  border: 5px solid #FD3030; \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #FD3030; \n"
"color: white;\n"
"}")
        self.deleteNamingQuizBtn.setObjectName("deleteNamingQuizBtn")
        self.horizontalLayout_3.addWidget(self.deleteNamingQuizBtn)
        self.addQuestionsBtn = QtWidgets.QPushButton(self.namequizpage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addQuestionsBtn.sizePolicy().hasHeightForWidth())
        self.addQuestionsBtn.setSizePolicy(sizePolicy)
        self.addQuestionsBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.addQuestionsBtn.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addQuestionsBtn.setFont(font)
        self.addQuestionsBtn.setStyleSheet("QPushButton {\n"
"background-color: #86C232; \n"
"color: white;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white; \n"
"  color: black;\n"
"  border: 5px solid #86C232; \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #86C232; \n"
"color: white;\n"
"}")
        self.addQuestionsBtn.setObjectName("addQuestionsBtn")
        self.horizontalLayout_3.addWidget(self.addQuestionsBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.namequizpage)
        self.gridLayout_3.addWidget(self.stackedWidget, 1, 1, 1, 1)
        QuizzApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(QuizzApp)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(QuizzApp)

    def retranslateUi(self, QuizzApp):
        _translate = QtCore.QCoreApplication.translate
        QuizzApp.setWindowTitle(_translate("QuizzApp", "QuizzApp"))
        self.nadpis.setText(_translate("QuizzApp", "Kategórie kvízov"))
        self.btn3.setText(_translate("QuizzApp", "Dejiny"))
        self.btn8.setText(_translate("QuizzApp", "Hry"))
        self.btn1.setText(_translate("QuizzApp", "Príroda"))
        self.btn5.setText(_translate("QuizzApp", "Technika"))
        self.btn2.setText(_translate("QuizzApp", "Hudba"))
        self.btn4.setText(_translate("QuizzApp", "Veda"))
        self.btn6.setText(_translate("QuizzApp", "Geografia"))
        self.btn9.setText(_translate("QuizzApp", "Filmy"))
        self.btn7.setText(_translate("QuizzApp", "Vesmír"))
        self.backToHomeBtn.setText(_translate("QuizzApp", "Výber kategórie"))
        self.addQuizBtn.setText(_translate("QuizzApp", "Pridať nový kvíz"))
        self.lineEdit.setPlaceholderText(_translate("QuizzApp", "hľadať"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("QuizzApp", "test"))
        item = self.listWidget.item(1)
        item.setText(_translate("QuizzApp", "test2"))
        item = self.listWidget.item(2)
        item.setText(_translate("QuizzApp", "test3"))
        item = self.listWidget.item(3)
        item.setText(_translate("QuizzApp", "test4"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.nOfQuestionText.setHtml(_translate("QuizzApp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
        self.startQuizButton.setText(_translate("QuizzApp", "Spustiť kvíz"))
        self.BButton.setText(_translate("QuizzApp", "b"))
        self.AButton.setText(_translate("QuizzApp", "a"))
        self.CButton.setText(_translate("QuizzApp", "c"))
        self.QuestionText.setHtml(_translate("QuizzApp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.DButton.setText(_translate("QuizzApp", "d"))
        self.qCountText.setText(_translate("QuizzApp", "        5/5"))
        self.endQuizButton.setText(_translate("QuizzApp", "Ukončiť"))
        self.againButton.setText(_translate("QuizzApp", "Výber kategórie"))
        self.answerD.setPlaceholderText(_translate("QuizzApp", "Odpoveď D"))
        self.answerB.setPlaceholderText(_translate("QuizzApp", "Odpoveď B"))
        self.answerC.setPlaceholderText(_translate("QuizzApp", "Odpoveď C"))
        self.answerA.setHtml(_translate("QuizzApp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:21pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.answerA.setPlaceholderText(_translate("QuizzApp", "Odpoveď A"))
        self.finishQuizBtn.setText(_translate("QuizzApp", "Pridať kvíz"))
        self.prevQuestionBtn.setText(_translate("QuizzApp", "<-"))
        self.nextQuestionBtn.setText(_translate("QuizzApp", "+"))
        self.addQuestionText.setPlaceholderText(_translate("QuizzApp", "Otázka"))
        self.backToNamingBtn.setText(_translate("QuizzApp", "Späť"))
        self.lineEdit_3.setText(_translate("QuizzApp", "Vyberte kategóriu:"))
        self.categoryComboBox.setItemText(0, _translate("QuizzApp", "Priroda"))
        self.categoryComboBox.setItemText(1, _translate("QuizzApp", "Hudba"))
        self.categoryComboBox.setItemText(2, _translate("QuizzApp", "Dejiny"))
        self.categoryComboBox.setItemText(3, _translate("QuizzApp", "Veda"))
        self.categoryComboBox.setItemText(4, _translate("QuizzApp", "Technika"))
        self.categoryComboBox.setItemText(5, _translate("QuizzApp", "Geografia"))
        self.categoryComboBox.setItemText(6, _translate("QuizzApp", "Vesmir"))
        self.categoryComboBox.setItemText(7, _translate("QuizzApp", "Hry"))
        self.categoryComboBox.setItemText(8, _translate("QuizzApp", "Filmy"))
        self.nameText.setHtml(_translate("QuizzApp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.nameText.setPlaceholderText(_translate("QuizzApp", "Názov kvízu"))
        self.descText.setHtml(_translate("QuizzApp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:29pt;\"><br /></p></body></html>"))
        self.descText.setPlaceholderText(_translate("QuizzApp", "Popis"))
        self.deleteNamingQuizBtn.setText(_translate("QuizzApp", "Zrušiť"))
        self.addQuestionsBtn.setText(_translate("QuizzApp", "Pridať otázky"))
