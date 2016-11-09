# import statements
#http://www.freecadweb.org/wiki/index.php?title=PySide_Medium_Examples#Window_Display
from PySide import QtGui, QtCore
import sys
sys.path.append('C:\Program Files\PsychoPy2\lib')
sys.path.append('C:\Program Files\PsychoPy2\Lib\site-packages\PsychoPy-1.83.04-py2.7.egg\psychopy\app')

import PartialTrialFunction
import os
import ProcessAFile
import datetime
# UI Class definitions
 
class ExampleNonmodalGuiClass(QtGui.QMainWindow):
	""""""
	def __init__(self):
		super(ExampleNonmodalGuiClass, self).__init__()
		self.initUI()
	def initUI(self):
                self.ExpName = 'PartialTrial'
		# create our window
		# define window		xLoc,yLoc,xDim,yDim
		self.setGeometry(	250, 250, 400, 240)
		self.setWindowTitle("Partial Trial Experiment")
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
		self.setMouseTracking(True)
		
           	self.label1 = QtGui.QLabel("Participant ID", self)
                self.label1.setFont('Courier') # set to a non-proportional font
                self.label1.setFixedWidth(190)
                self.label1.move(20, 0)
	
		self.textInput = QtGui.QLineEdit(self)
                self.textInput.setText("9999")
                self.textInput.setFixedWidth(190)
                self.textInput.move(20, 25)

		pushButton0 = QtGui.QPushButton("Instructions", self)
		pushButton0.clicked.connect(self.onPushButton0)
		pushButton0.setMinimumWidth(200)
		pushButton0.move(20, 70)
		
		pushButton1 = QtGui.QPushButton("Training in Order with FB", self)
		pushButton1.clicked.connect(self.onPushButton1)
		pushButton1.setMinimumWidth(200)
		pushButton1.move(20, 90)

		pushButton2 = QtGui.QPushButton("Training with FB", self)
		pushButton2.clicked.connect(self.onPushButton2)
		pushButton2.setMinimumWidth(200)
		pushButton2.move(20, 110)
		
		pushButton3 = QtGui.QPushButton("Training NO FB", self)
		pushButton3.clicked.connect(self.onPushButton3)
		pushButton3.setMinimumWidth(200)
		pushButton3.move(20, 130)
		
		pushButton4 = QtGui.QPushButton("Run 1", self)
		pushButton4.clicked.connect(self.onPushButton4)
		pushButton4.setMinimumWidth(200)
                pushButton4.move(20, 150)

		pushButton5 = QtGui.QPushButton("Run 2", self)
		pushButton5.clicked.connect(self.onPushButton5)
		pushButton5.setMinimumWidth(200)
		pushButton5.move(20, 170)

		pushButton6 = QtGui.QPushButton("Run 3, optional", self)
		pushButton6.clicked.connect(self.onPushButton6 )
		pushButton6.setMinimumWidth(200)
		pushButton6.move(20, 190)				
		
		# OK button
		okButton = QtGui.QPushButton('OK', self)
		okButton.clicked.connect(self.onOk)
		okButton.move(260, 110)
		# now make the window visible
		self.show()
		#

	def createOutputName(self,Tag):
	    subid = self.textInput.text()
	    visitid = '1'
	    cur = datetime.datetime.now()
	    OutName = "%s_%s_%s_%s_%d_%02d_%02d_%d%d"%(subid,visitid,self.ExpName,Tag,cur.year,cur.month,cur.day,cur.hour,cur.minute)
	    print OutName
	    OutFile = os.path.join(os.getcwd(),'data',OutName)
	    return OutFile


	def onPushButton0(self):
            c1 = datetime.datetime.now()
	    Tag = 'Instructions'
            self.hide()   
            command = "python -c \"import PartialTrialFunction; PartialTrialFunction.Instructions()\""
            command
            os.system(command)
            self.show()
            print "%s took: %s"%(Tag,datetime.datetime.now() - c1)

                
	def onPushButton1(self):
	    c1 = datetime.datetime.now()
	    Tag = 'TrainOrderFB'
            self.hide()   
            CondFile = '/Users/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/PartialTrialDIR/ExperimentalTrials/Training30TrialsInOrder.csv'
            # OutFile = '/Users/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/PartialTrialDIR/Scripts/PsychoPyTask/data/test'
            OutFile = self.createOutputName(Tag)
            command = "python -c \"import PartialTrialFunction; PartialTrialFunction.PartialTrialFeedback(\'%s\',\'%s\',%s,%s)\""%(CondFile,OutFile,self.textInput.text(),'1')
            command
            os.system(command)
            self.show()
            ProcessAFile.ProcessAFile(OutFile+'.csv',self.textInput.text(),Tag,2)
            print "%s took: %s"%(Tag,datetime.datetime.now() - c1)

                
	def onPushButton2(self):
	    c1 = datetime.datetime.now()
	    Tag = 'TrainFB'
            self.hide()   
            CondFile = '/Users/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/PartialTrialDIR/ExperimentalTrials/Practice30Trials6LoadsVer1.csv'
            #OutFile = '/Users/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/PartialTrialDIR/Scripts/PsychoPyTask/data/test'
            OutFile = self.createOutputName(Tag)
            command = "python -c \"import PartialTrialFunction; PartialTrialFunction.PartialTrialFeedback(\'%s\',\'%s\',%s,%s)\""%(CondFile,OutFile,self.textInput.text(),'1')
            command
            os.system(command)
            self.show()
            ProcessAFile.ProcessAFile(OutFile+'.csv',self.textInput.text(),Tag,5)
            print "%s took: %s"%(Tag,datetime.datetime.now() - c1)

        def onPushButton3(self):
            c1 = datetime.datetime.now()
            Tag = 'TrainNoFB'
            self.hide()   
            CondFile = '/Users/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/PartialTrialDIR/ExperimentalTrials/Practice30Trials6LoadsVer2.csv'
            #OutFile = '/Users/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/PartialTrialDIR/Scripts/PsychoPyTask/data/test'
            OutFile = self.createOutputName(Tag)
            command = "python -c \"import PartialTrialFunction; PartialTrialFunction.PartialTrial(\'%s\',\'%s\',%s,%s)\""%(CondFile,OutFile,self.textInput.text(),'1')
            command
            os.system(command)
            self.show()
            ProcessAFile.ProcessAFile(OutFile+'.csv',self.textInput.text(),Tag,8)
	    print "%s took: %s"%(Tag,datetime.datetime.now() - c1)
	    
	def onPushButton4(self):
	    c1 = datetime.datetime.now()
	    Tag = 'Run1'
            self.hide()   
            CondFile = '/Users/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/PartialTrialDIR/ExperimentalTrials/Optimized72Trials_6LoadsVer1.csv'
            #OutFile = '/Users/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/PartialTrialDIR/Scripts/PsychoPyTask/data/test'
            OutFile = self.createOutputName(Tag)
            command = "python -c \"import PartialTrialFunction; PartialTrialFunction.PartialTrial(\'%s\',\'%s\',%s,%s)\""%(CondFile,OutFile,self.textInput.text(),'1')
            command
            os.system(command)
            self.show()
            ProcessAFile.ProcessAFile(OutFile+'.csv',self.textInput.text(),Tag,11)
	    print "%s took: %s"%(Tag,datetime.datetime.now() - c1)


	def onPushButton5(self):
	    c1 = datetime.datetime.now()
            Tag = 'Run2'
            self.hide()   
            CondFile = '/Users/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/PartialTrialDIR/ExperimentalTrials/Optimized72Trials_6LoadsVer2.csv'
            #OutFile = '/Users/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/PartialTrialDIR/Scripts/PsychoPyTask/data/test'
            OutFile = self.createOutputName(Tag)
            command = "python -c \"import PartialTrialFunction; PartialTrialFunction.PartialTrial(\'%s\',\'%s\',%s,%s)\""%(CondFile,OutFile,self.textInput.text(),'1')
            command
            os.system(command)
            self.show()
            ProcessAFile.ProcessAFile(OutFile+'.csv',self.textInput.text(),Tag,14)
	    print "%s took: %s"%(Tag,datetime.datetime.now() - c1)

        def onPushButton6(self):
            c1 = datetime.datetime.now()
            Tag = 'Run3'
            self.hide()   
            CondFile = '/Users/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/PartialTrialDIR/ExperimentalTrials/Training30TrialsInOrder.csv'
            #OutFile = '/Users/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/PartialTrialDIR/Scripts/PsychoPyTask/data/test'
            OutFile = self.createOutputName(Tag)
            command = "python -c \"import PartialTrialFunction; PartialTrialFunction.PartialTrialFeedback(\'%s\',\'%s\',%s,%s)\""%(CondFile,OutFile,self.textInput.text(),'1')
            command
            os.system(command)
            self.show()
            ProcessAFile.ProcessAFile(OutFile+'.csv',self.textInput.text(),Tag,17)
	    print "%s took: %s"%(Tag,datetime.datetime.now() - c1)
            
	def onOk(self):
		self.result			= userOK
		self.close()
		
	def RunPsychoPyCode():
	    fullPath= fullPath.replace(' ','\ ')#for unix this signifies a space in a filename
            pythonExec = sys.executable.replace(' ','\ ')#for unix this signifies a space in a filename
            command = '%s -u %s' %(pythonExec, fullPath)# the quotes would break a unix system command
            self.scriptProcessID = wx.Execute(command, wx.EXEC_ASYNC| wx.EXEC_MAKE_GROUP_LEADER, self.scriptProcess)

# Class definitions
 
# Function definitions
 
# Constant definitions
global userOK

userOK			= "OK"
 
# code ***********************************************************************************
 
form = ExampleNonmodalGuiClass()
#
#OS: Mac OS X
#Word size: 64-bit
#Version: 0.14.3703 (Git)
#Branch: releases/FreeCAD-0-14
#Hash: c6edd47334a3e6f209e493773093db2b9b4f0e40
#Python version: 2.7.5
#Qt version: 4.8.6
#Coin version: 3.1.3
#SoQt version: 1.5.0
#OCC version: 6.7.0
#