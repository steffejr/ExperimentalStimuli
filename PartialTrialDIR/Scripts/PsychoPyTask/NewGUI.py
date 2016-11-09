import sys
sys.path.append('C:\Users\jsteffen\AppData\Local\Enthought\Canopy32\App\appdata\canopy-1.6.2.3262.win-x86\Lib\site-packages\PySide')

from PySide import QtGui, QtCore
import PartialTrialFunction
global reply
class MyButtons(QtGui.QMainWindow):
        """"""
        def __init__(self):
                super(MyButtons, self).__init__()
                self.initUI()
        def initUI(self):      
                self.reply = QtGui.QInputDialog.getText(None, "Enter Subject ID","Enter your thoughts for the day:")
                print self.reply
                option1Button = QtGui.QPushButton("Instructions")
                option1Button.clicked.connect(self.onOption1)
                option2Button = QtGui.QPushButton("Training in order with FB")
                option2Button.clicked.connect(self.onOption2)
                option3Button = QtGui.QPushButton("Training with FB")
                option3Button.clicked.connect(self.onOption3)
                option4Button = QtGui.QPushButton("Training NO FB")
                option4Button.clicked.connect(self.onOption4)
                option5Button = QtGui.QPushButton("Run 1")
                option5Button.clicked.connect(self.onOption5)
                option6Button = QtGui.QPushButton("Run 2")
                option6Button.clicked.connect(self.onOption6)
                option7Button = QtGui.QPushButton("Optional Run 3")
                option7Button.clicked.connect(self.onOption7)

                #
                buttonBox = QtGui.QDialogButtonBox()
                buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
                buttonBox.addButton(option1Button, QtGui.QDialogButtonBox.ActionRole)
                buttonBox.addButton(option2Button, QtGui.QDialogButtonBox.ActionRole)
                buttonBox.addButton(option3Button, QtGui.QDialogButtonBox.ActionRole)
                buttonBox.addButton(option4Button, QtGui.QDialogButtonBox.ActionRole)
                buttonBox.addButton(option5Button, QtGui.QDialogButtonBox.ActionRole)
                buttonBox.addButton(option6Button, QtGui.QDialogButtonBox.ActionRole)
                buttonBox.addButton(option7Button, QtGui.QDialogButtonBox.ActionRole)
                #
                mainLayout = QtGui.QVBoxLayout()
                mainLayout.addWidget(buttonBox)
                self.setLayout(mainLayout)
                # define window         xLoc,yLoc,xDim,yDim
                self.setGeometry(       250, 250, 0, 50)
                self.setWindowTitle("Participant: %s"%(self.reply[0]))
                self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        def onOption1(self):
                self.retStatus = 1
                self.close()
        def onOption2(self):
                self.retStatus = 2
                self.close()

        def onOption3(self):
                self.retStatus = 3
                self.close()
        def onOption4(self):
                self.retStatus = 4
                self.close()
        def onOption5(self):
                self.retStatus = 5
                self.close()
        def onOption6(self):
                self.retStatus = 6
                self.close()
        def onOption7(self):
                self.retStatus = 7
                self.close()
def routine1():
        print 'routine 1'

        
form = MyButtons()

if form.retStatus==1:
        PartialTrialFunction.Instructions()
elif form.retStatus==2:
        PartialTrialFunction.Test('1111','2222')

elif form.retStatus==3:
        print "Hello World!"

elif form.retStatus==4:
        routine4()
elif form.retStatus==5:
        routine5()