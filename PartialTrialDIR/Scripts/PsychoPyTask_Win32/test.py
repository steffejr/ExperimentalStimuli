import os
import sys


BaseDir = os.path.join('C:\\','Users','jsteffen','Dropbox','SteffenerColumbia','Scripts','ExperimentalStimuli','PartialTrialDIR')
sys.path.append(os.path.join(BaseDir,'Scripts','PsychoPyTask_Win32'))
import PartialTrialFunction

CondFile = os.path.join(BaseDir,'ExperimentalTrials','Training30TrialsInOrder.csv')

OutFile = os.path.join(BaseDir,'TEST.csv')
            
PartialTrialFunction.PartialTrialFeedback(CondFile,OutFile,66,66)


OutFile = 'C:\Users\jsteffen\Dropbox\SteffenerColumbia\Scripts\ExperimentalStimuli\PartialTrialDIR\Scripts\PsychoPyTask_Win32\data\PartialTrial_123456_1_TrainOrderFB_2016_04_13_1055.csv'

import ProcessAFile
import ProcessData
# Create a summary string to the researcher.
# Read the file
def CreateAccSummaryString(OutFile):
    df1 = ProcessData.loadBehDataFile(OutFile)
    # Process the file
    df1 = ProcessData.processBehavioralFile(df1)
    # Extract accuracy
    ACCdata = df1.data.Acc.groupby(df1.data.LoadLevels).mean()
    # Create a string of accuracy at each load level
    SumString = ""
    count = 1
    for i in ACCdata:
        SumString = "%s,%d:%2.0f"%(SumString,count,i*100)
        count = count + 1;
    return SumString[1:]



______            _ _                _    
|  ___|          | | |              | |   
| |_ ___  ___  __| | |__   __ _  ___| | __
|  _/ _ \/ _ \/ _` | '_ \ / _` |/ __| |/ /
| ||  __/  __/ (_| | |_) | (_| | (__|   < 
\_| \___|\___|\__,_|_.__/ \__,_|\___|_|\_\
                                          
                                          
