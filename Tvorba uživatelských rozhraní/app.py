from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QTimer
from tinydb import TinyDB, Query, where
from pathlib import Path
import sys
import random
import time
import os
import GUI


class Controller(QtWidgets.QMainWindow, GUI.Ui_QuizzApp):

	db=TinyDB(Path("database/nature.json"))
	answerCounter=0
	nOfCorrectAns=0
	question=[]
	ansA=[]
	ansB=[]
	ansC=[]
	ansD=[]
	correct=[]
	name=''
	desc=''
	nOfQ=0
	quizCategory=0

	
	#funkcia hlada kvizy podla nazvu
	def searchBarUpdate(self, text):
		toSearch=str(text)
		for i in range(self.listWidget.count()):
			item = self.listWidget.item(i)
			itemName=str(item.text())
			if toSearch in itemName:
				self.listWidget.setRowHidden(i,False)
			else:
				self.listWidget.setRowHidden(i,True)

	
	#funkcia vypise informacie (nazov,popis,pocet otazok) k zvolenemu kvizu
	def printOtherInfo(self):
		selectedIndex=self.listWidget.currentRow()+1
		quiz=self.db.get(doc_id=selectedIndex)
		self.descriptionText.clear()
		self.nOfQuestionText.clear()
		self.nOfFinishedText.clear()
		finishedtext='Počet dokončení: %d' %(random.randrange(10))
		nofqtext='Počet otázok: %d'%(quiz['nOfQ'])
		self.nOfFinishedText.insertPlainText(finishedtext)
		self.nOfQuestionText.insertPlainText(nofqtext)
		self.descriptionText.insertPlainText(quiz['desc'])
	
	
	#funkcia ukonci kviz a vypise vysledok
	def quizEnding(self):
		selectedIndex=self.listWidget.currentRow()+1
		quiz=self.db.get(doc_id=selectedIndex)
		pointstext='%d/%d' % (self.nOfCorrectAns,quiz['nOfQ'])
		self.stackedWidget.setCurrentIndex(3)
		self.answerCounter=0
		self.nOfCorrectAns=0
		self.pointsText.setText(pointstext)
		self.phraseText.setText('Tvoj výsledok je ')

	def correctButton(self,choice):
		if choice=='a':
			self.AButton.setStyleSheet("QPushButton {\n""background-color: #86C232; \n""color: white;\n""border-radius: 10px;\n""border-style: outset;\n""}")
			self.BButton.setStyleSheet("QPushButton {\n""background-color: #FD3030; \n""color: white;\n""border-radius: 10px;\n""border-style: outset;\n""}")
			self.CButton.setStyleSheet("QPushButton {\n""background-color: #FD3030; \n""color: white;\n""border-radius: 10px;\n""border-style: outset;\n""}")
			self.DButton.setStyleSheet("QPushButton {\n""background-color: #FD3030; \n""color: white;\n""border-radius: 10px;\n""border-style: outset;\n""}")
		elif choice=='b':
			self.AButton.setStyleSheet("QPushButton {\n""background-color: #FD3030; \n""color: white;\n""border-radius: 10px;\n""border-style: outset;\n""}")
			self.BButton.setStyleSheet("QPushButton {\n""background-color: #86C232; \n""color: white;\n""border-radius: 10px;\n""border-style: outset;\n""}")
			self.CButton.setStyleSheet("QPushButton {\n""background-color: #FD3030; \n""color: white;\n""border-radius: 10px;\n""border-style: outset;\n""}")
			self.DButton.setStyleSheet("QPushButton {\n""background-color: #FD3030; \n""color: white;\n""border-radius: 10px;\n""border-style: outset;\n""}")
		elif choice=='c':
			self.AButton.setStyleSheet("QPushButton {\n""background-color: #FD3030; \n""color: white;\n""border-radius: 10px;\n""border-style: outset;\n""}")
			self.BButton.setStyleSheet("QPushButton {\n""background-color: #FD3030; \n""color: white;\n""border-radius: 10px;\n""border-style: outset;\n""}")
			self.CButton.setStyleSheet("QPushButton {\n""background-color: #86C232; \n""color: white;\n""border-radius: 10px;\n""border-style: outset;\n""}")
			self.DButton.setStyleSheet("QPushButton {\n""background-color: #FD3030; \n""color: white;\n""border-radius: 10px;\n""border-style: outset;\n""}")
		elif choice=='d':
			self.AButton.setStyleSheet("QPushButton {\n""background-color: #FD3030; \n""color: white;\n""border-radius: 10px;\n""border-style: outset;\n""}")
			self.BButton.setStyleSheet("QPushButton {\n""background-color: #FD3030; \n""color: white;\n""border-radius: 10px;\n""border-style: outset;\n""}")
			self.CButton.setStyleSheet("QPushButton {\n""background-color: #FD3030; \n""color: white;\n""border-radius: 10px;\n""border-style: outset;\n""}")
			self.DButton.setStyleSheet("QPushButton {\n""background-color: #86C232; \n""color: white;\n""border-radius: 10px;\n""border-style: outset;\n""}")
		
	
	#funkcia vyhodnocuje spravnu odpoved a po zodpovedani vola dalsiu otazku/ukonci kviz
	def chooseAnswer(self,choice):
		selectedIndex=self.listWidget.currentRow()+1
		quiz=self.db.get(doc_id=selectedIndex)
		correctWithIndex='CORRECT%d' %(self.answerCounter-1)
		if quiz[correctWithIndex]==choice:
			self.nOfCorrectAns+=1
			self.correctButton(choice)
		else:
			self.correctButton(quiz[correctWithIndex])

		#ak je zodpovedana posledna otazka ukonci kviz
		if self.answerCounter == int(quiz['nOfQ']):
			QTimer.singleShot(2000, lambda: self.quizEnding())
			
		#inak nacitaj dalsiu otazku
		else:
			QTimer.singleShot(2000, lambda: self.startQuestion())
			




	
	#funkcia vypise prislusnu otazku a odpovede
	def startQuestion(self):
		self.AButton.setStyleSheet("QPushButton {\n""background-color: #696969; \n""color: white;\n""}\n""\n""QPushButton:hover {\n""  background-color: white; \n""  color: black;\n""  border: 5px solid      #696969; \n""}\n""\n""QPushButton:pressed{\n""background-color: #696969; \n""color: white;\n""}")
		self.BButton.setStyleSheet("QPushButton {\n""background-color: #696969; \n""color: white;\n""}\n""\n""QPushButton:hover {\n""  background-color: white; \n""  color: black;\n""  border: 5px solid      #696969; \n""}\n""\n""QPushButton:pressed{\n""background-color: #696969; \n""color: white;\n""}")
		self.CButton.setStyleSheet("QPushButton {\n""background-color: #696969; \n""color: white;\n""}\n""\n""QPushButton:hover {\n""  background-color: white; \n""  color: black;\n""  border: 5px solid      #696969; \n""}\n""\n""QPushButton:pressed{\n""background-color: #696969; \n""color: white;\n""}")
		self.DButton.setStyleSheet("QPushButton {\n""background-color: #696969; \n""color: white;\n""}\n""\n""QPushButton:hover {\n""  background-color: white; \n""  color: black;\n""  border: 5px solid      #696969; \n""}\n""\n""QPushButton:pressed{\n""background-color: #696969; \n""color: white;\n""}")
		self.QuestionText.clear()
		self.stackedWidget.setCurrentIndex(2)
		selectedIndex=self.listWidget.currentRow()+1
		quiz=self.db.get(doc_id=selectedIndex)
		curQText='        %d/%d' %(self.answerCounter+1,int(quiz['nOfQ']))
		self.qCountText.setText(curQText)
		qWithIndex='Q%d' %(self.answerCounter)
		aWithIndex='A%d' %(self.answerCounter)
		bWithIndex='B%d' %(self.answerCounter)
		cWithIndex='C%d' %(self.answerCounter)
		dWithIndex='D%d' %(self.answerCounter)
		self.QuestionText.insertPlainText(quiz[qWithIndex])
		self.AButton.setText(quiz[aWithIndex])
		self.BButton.setText(quiz[bWithIndex])
		self.CButton.setText(quiz[cWithIndex])
		self.DButton.setText(quiz[dWithIndex])
		self.answerCounter+=1

	
	#funkcia vycisti listy a pripravi ich na pripadne vlozenie dalsieho kvizu
	def clearLists(self):
		self.question.clear()
		self.ansA.clear()
		self.ansB.clear()
		self.ansC.clear()
		self.ansD.clear()
		self.correct.clear()

	#prepnutie na predchadzajuce okno
	def backToNaming(self):
		self.stackedWidget.setCurrentIndex(5)

	#funkcia ulozi jednu otazku do listu a pripravi ju na vlozenie do db
	def saveQuestion(self):
		self.question.append(self.addQuestionText.toPlainText())
		self.ansA.append(self.answerA.toPlainText())
		self.ansB.append(self.answerB.toPlainText())
		self.ansC.append(self.answerC.toPlainText())
		self.ansD.append(self.answerD.toPlainText())
		if self.radioA.isChecked() == True:
			self.correct.append('a')
		if self.radioB.isChecked() == True:
			self.correct.append('b')
		if self.radioC.isChecked() == True:
			self.correct.append('c')
		if self.radioD.isChecked() == True:
			self.correct.append('d')
		self.addQuestionText.clear()
		self.answerA.clear()
		self.answerB.clear()
		self.answerC.clear()
		self.answerD.clear()

	#funkcia vlozi hotovy kviz do databazy
	def insertQuiz(self):
		#query sluzi na vyhladanie kvizu do ktoreho chcem vlozit otazky
		quizToUpdate=Query()
		#nacitanie vybranej databazy do ktorej vlozime kviz
		if self.quizCategory==1:
			self.db=TinyDB('database/nature.json')
		if self.quizCategory==2:
			self.db=TinyDB('database/music.json')
		if self.quizCategory==3:
			self.db=TinyDB('database/history.json')
		if self.quizCategory==4:
			self.db=TinyDB('database/science.json')
		if self.quizCategory==5:
			self.db=TinyDB('database/technology.json')
		if self.quizCategory==6:
			self.db=TinyDB('database/geography.json')
		if self.quizCategory==7:
			self.db=TinyDB('database/space.json')
		if self.quizCategory==8:
			self.db=TinyDB('database/games.json')
		if self.quizCategory==9:
			self.db=TinyDB('database/movies.json')
		#pomenovanie kvizu
		self.db.insert({'name': self.name, 'desc': self.desc, 'nOfQ':0})
		i=0
		#vlozenie vsetkych ulozenych otazok do databazy
		for it in self.question:
			qWithIndex='Q%d' %(i)
			aWithIndex='A%d' %(i)
			bWithIndex='B%d' %(i)
			cWithIndex='C%d' %(i)
			dWithIndex='D%d' %(i)
			correctWithIndex='CORRECT%d' %(i)
			self.db.update({'nOfQ':i+1,qWithIndex:self.question[i],aWithIndex:self.ansA[i],bWithIndex:self.ansB[i],cWithIndex:self.ansC[i],dWithIndex:self.ansD[i],correctWithIndex:self.correct[i]},quizToUpdate.name==self.name)#,correctWithIndex:correct[i]})
			i+=1
		self.stackedWidget.setCurrentIndex(0)
		self.clearLists()


	#funkcia ulozi meno popis a kategoriu kvizu ktory sa chystam pridat
	def addQuestions(self):
		self.name=self.nameText.toPlainText()
		self.desc=self.descText.toPlainText()
		self.quizCategory=(self.categoryComboBox.currentIndex() + 1)

		self.stackedWidget.setCurrentIndex(4)

	#prepnutie sa na okno pomenovania kvizu
	def nameQuiz(self):
		self.stackedWidget.setCurrentIndex(5)

	#funkcia skoci na vyber kategorie a vymaze list nacitanych kvizov
	def goToHomePage(self):
		self.descriptionText.clear()
		self.nOfQuestionText.clear()
		self.nOfFinishedText.clear()
		self.stackedWidget.setCurrentIndex(0)
		self.listWidget.clear()

	#funkcia vyplni list kvizov zo zadanej kategorie
	def printQuizListView(self):
		counter=1
		for i in self.db:
			foundItem=self.db.get(doc_id=counter)
			counter+=1
			self.listWidget.addItem(foundItem['name'])

	#funkcia nacita kategoriu a posle ju funkcii printQuizListView
	def chooseCategory(self,num):
		self.descriptionText.clear()
		self.nOfQuestionText.clear()
		self.nOfFinishedText.clear()
		self.listWidget.clear()
		self.stackedWidget.setCurrentIndex(1)
		if num==1:
			self.db=TinyDB('database/nature.json')
		if num==2:
			self.db=TinyDB('database/music.json')
		if num==3:
			self.db=TinyDB('database/history.json')
		if num==4:
			self.db=TinyDB('database/science.json')
		if num==5:
			self.db=TinyDB('database/technology.json')
		if num==6:
			self.db=TinyDB('database/geography.json')
		if num==7:
			self.db=TinyDB('database/space.json')
		if num==8:
			self.db=TinyDB('database/games.json')
		if num==9:
			self.db=TinyDB('database/movies.json')
		self.printQuizListView()
	def endQuizEarly(self):
		self.stackedWidget.setCurrentIndex(1)
		self.answerCounter=0
		self.nOfCorrectAns=0

	#Hlavna funkcia ktora prepaja funkcionalitu s GUI
	def connectButtons(self):
		self.btn1.clicked.connect(lambda:self.chooseCategory(1))
		self.btn2.clicked.connect(lambda:self.chooseCategory(2))
		self.btn3.clicked.connect(lambda:self.chooseCategory(3))
		self.btn4.clicked.connect(lambda:self.chooseCategory(4))
		self.btn5.clicked.connect(lambda:self.chooseCategory(5))
		self.btn6.clicked.connect(lambda:self.chooseCategory(6))
		self.btn7.clicked.connect(lambda:self.chooseCategory(7))
		self.btn8.clicked.connect(lambda:self.chooseCategory(8))
		self.btn9.clicked.connect(lambda:self.chooseCategory(9))
		self.AButton.clicked.connect(lambda:self.chooseAnswer('a'))
		self.BButton.clicked.connect(lambda:self.chooseAnswer('b'))
		self.CButton.clicked.connect(lambda:self.chooseAnswer('c'))
		self.DButton.clicked.connect(lambda:self.chooseAnswer('d'))
		self.backToHomeBtn.clicked.connect(lambda:self.goToHomePage())
		self.addQuestionsBtn.clicked.connect(lambda:self.addQuestions())
		self.startQuizButton.clicked.connect(lambda:self.startQuestion())
		self.endQuizButton.clicked.connect(lambda:self.endQuizEarly())
		self.addQuizBtn.clicked.connect(lambda:self.nameQuiz())
		self.backToNamingBtn.clicked.connect(lambda:self.backToNaming())
		self.deleteNamingQuizBtn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
		self.finishQuizBtn.clicked.connect(lambda:self.insertQuiz())
		self.nextQuestionBtn.clicked.connect(lambda:self.saveQuestion())
		self.lineEdit.textChanged.connect(self.searchBarUpdate)
		self.listWidget.itemSelectionChanged.connect(lambda:self.printOtherInfo())
		self.againButton.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))




	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		self.stackedWidget.setCurrentIndex(0)
		self.connectButtons()



def main():
    app = QApplication(sys.argv)
    form = Controller()
    form.show()
    app.exec_()


##
# automatic
if __name__ == '__main__':
    main()

