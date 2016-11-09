from FileSelectClass import Example
import ProcessAFile
import ProcessData
import WriteToGoogleSpreadSheet
ex = Example()


inFile = ex.showDialog()

subid = '2003'

print inFile
Tag = 'TrNoFB'
col = 8
ProcessAFile.ProcessAFile(inFile[0][0],subid,Tag,col)

df1 = ProcessData.loadBehDataFile(inFile[0][0])
df1.onlyKeepDataRows()
    # find load levels
df1.whatLoadIsThisRow()
    # check for accuracy
df1.areResponsesCorrect()

df1 = ProcessData.processBehavioralFile(df1)  



Tag = 'Run1'
col = 4
ProcessAFile.ProcessAFile(inFile[0][0],subid,Tag,col)

# Create SPM design matrices
ex = Example()
inFile = ex.showDialog()
df1 = ProcessData.loadBehDataFile(inFile[0][0])
df1 = ProcessData.processBehavioralFile(df1)  
OutFileName = '/media/jason/OSDisk/Data/PartialTrialPilot/Subjects/P00002003/S0001/fmriStats/model1/Run2Model'
ProcessData.createSPMDesignMatrix(df1, OutFileName)