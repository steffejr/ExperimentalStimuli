import os
import ProcessAFile
import datetime
import ProcessData

BaseDir='/home/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/PartialTrialDIR/Scripts/PsychoPyTask_Win32/data'
subid = '1233'
Tag = 'tester'
#FileName = 'PartialTrial_62160613001_1_Run2_2016_06_13_1520.csv'

FileName = 'PartialTrial_62160613001_1_TrainOrderFB_2016_06_13_142.csv'
#FileName = 'PartialTrial_62160613001_1_TrainNoFB_2016_06_13_1422.csv'
inFile = os.path.join(BaseDir,FileName)

ProcessAFile.CreateAccSummaryString(inFile)

OutFile = file


df1 = ProcessData.loadBehDataFile(inFile)
    # Process the file
df1 = ProcessData.processBehavioralFile(df1)

    # Extract accuracy
ACCdata = df1.data.Acc.groupby(df1.data.LoadLevels).mean()

# Split the file name based