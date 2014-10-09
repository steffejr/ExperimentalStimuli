import os
import sys
from NBackFunctions import *

ThisScript = sys.argv[0]
ThisFolder = os.path.dirname(ThisScript)

print ThisScript
print ThisFolder
TotalDurDLG = gui.Dlg(title='Time')
TotalDurDLG.addText('Total Duration of Experiment')
TotalDurDLG.addText(str(ExpectedTotalTime))
TotalDurDLG.show()
