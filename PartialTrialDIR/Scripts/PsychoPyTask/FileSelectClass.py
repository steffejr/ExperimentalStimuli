from PySide import QtGui
# This is used to select the file(s) of interest
class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        #self.initUI()
        
    def initUI(self):      

        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        
        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 22)
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()
        
    def showDialog(self):
        self.fileName = QtGui.QFileDialog.getOpenFileNames(self, 'Dialog Title', '/Users/jason/Dropbox/SteffenerColumbia/Scripts', selectedFilter='*.csv')
        if self.fileName:
            print self.fileName
        return self.fileName