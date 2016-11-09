from ProcessData import PTdata
import ProcessData
#import WriteToGoogleSpreadSheet
from FileSelectClass import Example
import pandas as pd
import ProcessAFile

#def ProcessAFile(inputFile,subid,Tag):
#    df1 = ProcessData.loadBehDataFile(inputFile)
#    df1 = ProcessData.processBehavioralFile(df1)
#    wkB = WriteToGoogleSpreadSheet.openWorkBook()
#    wkS = WriteToGoogleSpreadSheet.createWorksheet(wkB, subid)
#    writeSummaryBehavioralDataToFile(df1, wkS, Tag)


ex = Example()
# This will ask you to select one or more files
ex.showDialog()
# Extract the filename
# How many files were selected?
# load each file and create the dataframes
if len(ex.fileName) == 2:
    inFile1 = ex.fileName[0][0]
    inFile2 = ex.fileName[0][1]
    if inFile1.find('Run1') > 0:
        df1 = ProcessData.loadBehDataFile(inFile1)
    elif inFile1.find('Run2') > 0 :
        df2 = ProcessData.loadBehDataFile(inFile1)
    if inFile2.find('Run2') > 0 :
        df2 = ProcessData.loadBehDataFile(inFile2)
    elif inFile2.find('Run1') > 0 :
        df1 = ProcessData.loadBehDataFile(inFile2)
        

df1 = ProcessData.processBehavioralFile(df1)
df2 = ProcessData.processBehavioralFile(df2)
# Create a dataframe from joinging the two dataframes
dfB = pd.DataFrame(np.concatenate((df1.data.LoadLevels,df2.data.LoadLevels),axis = 0),columns = ['Load'])
dfB['RT'] = np.concatenate((df1.data.RT,df2.data.RT),axis = 0)
dfB['Acc'] = np.concatenate((df1.data.Acc,df2.data.Acc),axis = 0)
dfB.RT.groupby(dfB.Load).mean()
dfB.Acc.groupby(dfB.Load).mean()

# Which dataframe is first?
# Concatenate the dataframes
#concatTwoDataFrames(dataFrame1, dataFrame2)
# Extract the summary measures from the data
RTmean1 = df1.data.RT.groupby(df1.data.LoadLevels).mean()
RTmed1 = df1.data.RT.groupby(df1.data.LoadLevels).median()
Accmean1 = df1.data.Acc.groupby(df1.data.LoadLevels).mean()
Accnum1 = df1.data.Acc.groupby(df1.data.LoadLevels).sum()
RTmean2 = df2.data.RT.groupby(df2.data.LoadLevels).mean()
RTmed2 = df2.data.RT.groupby(df2.data.LoadLevels).median()
Accmean2 = df2.data.Acc.groupby(df2.data.LoadLevels).mean()
Accnum2 = df2.data.Acc.groupby(df2.data.LoadLevels).sum()
RTmeanB = dfB.RT.groupby(dfB.Load).mean()
RTmedB = dfB.RT.groupby(dfB.Load).median()
AccmeanB = dfB.Acc.groupby(dfB.Load).mean()
AccnumB = dfB.Acc.groupby(dfB.Load).sum()
# Write the summary measures to the screen for easy copy and paste into a spreadsheet.
# Variable names will be Run#Load#RTmean,Run#Load#RTmed,RunBothLoad#RTmean,
# Combine all variables into a single series
AllBeh = np.concatenate((RTmeanB,RTmedB,AccmeanB,AccnumB,RTmean1,RTmed1,Accmean1,Accnum1,RTmean2,RTmed2,Accmean2,Accnum2),axis = 0)
# write as a single row of numbers
print(df1.Subid+','+','.join(map(str,AllBeh)))

### CHECK ON THE CREATION OF THE STR FOR FEEDBACK ON THE GUI
ex = Example()
# This will ask you to select one or more files
ex.showDialog()
inFile1 = ex.fileName[0][0]
SumStr = ProcessAFile.CreateAccSummaryString(inFile1)

### #################################################
ex = Example()
# This will ask you to select one or more files
ex.showDialog()
inFile1 = ex.fileName[0][0]
df1 = ProcessData.loadBehDataFile(inFile1)
df1 = ProcessData.processBehavioralFile(df1)
OutBaseName = os.path.join('/media/jsteffen/Data001/PartialTrialPilot/ProcMRIData',df1.Subid,'V001')
OutFolder = os.path.join(OutBaseName,'DesignMatrices')
OutFile = os.path.join(OutFolder,df1.Subid+df1.RunType+"_SPMDesign.mat")
if not os.path.exists(OutFolder):
    os.mkdir(OutFolder)

ProcessData.createSPMDesignMatrix(df1, OutFile)

### #################################################

df2 = ProcessData.loadBehDataFile(ex.fileName[0][1])
df2 = ProcessData.processBehavioralFile(df2)
ProcessData.createSPMDesignMatrix(df1, 'P00002001_S0001_Run2_DM')


wkB = WriteToGoogleSpreadSheet.openWorkBook()
wkS = WriteToGoogleSpreadSheet.createWorksheet(wkB, '2001')
writeSummaryBehavioralDataToFile(df1, wkS, 'Run1')

###########################################################################
ex = Example()
ex.showDialog()
inFile1 = ex.fileName[0][0]
df1 = ProcessData.loadBehDataFile(inFile1)
df1 = ProcessData.processBehavioralFile(df1)

OutPath = '/media/jsteffen/Data001/PartialTrialPilot/ProcMRIData/62160810004/V001'
OutFileName = os.path.join(OutPath, df1.Subid+"_TEST_"+df1.RunType+".mat")

ProcessData.createSPMDesignMatrix(df1, OutFileName)
###########################################################################
# Can I extract the trial start times and group them the same way?
# Stim On Times
LoadLevels = numpy.unique(dataFrame.data.LoadLevels) 
# Load level 1
TrialsToKeep = (dataFrame.data.LoadLevels==1) & (df1.data.Acc != -1)
S1on = numpy.array(df1.data.TrialStart[TrialsToKeep])
S1dur = numpy.array(df1.data.StimDur[TrialsToKeep])
TrialsToKeep = (df1.data.LoadLevels==1) & (df1.data.RetDur > 0) & (df1.data.Acc != -1)
R1on = numpy.array(df1.data.TrialStart[TrialsToKeep] + df1.data.RetDur[TrialsToKeep])
R1dur = numpy.array(df1.data.RetDur[TrialsToKeep] + df1.data.RetDur[TrialsToKeep])
TrialsToKeep = (df1.data.LoadLevels==1) & (df1.data.ProbeDur > 0) & (df1.data.Acc != -1)
P1on = numpy.array(df1.data.TrialStart[] + df1.data.ProbeDur[(df1.data.LoadLevels==1)& (df1.data.ProbeDur > 0)])
P1dur = numpy.array(df1.data.ProbeDur[(df1.data.LoadLevels==1)& (df1.data.ProbeDur > 0)] + df1.data.ProbeDur[(df1.data.LoadLevels==1)& (df1.data.ProbeDur > 0)])

# Load level 2
S1on = numpy.array(df1.data.TrialStart[(df1.data.LoadLevels==1) & (df1.data.Acc != -1)])
S1dur = numpy.array(df1.data.StimDur[(df1.data.LoadLevels==1) & (df1.data.Acc != -1)])
# Load level 3
S1on = numpy.array(df1.data.TrialStart[(df1.data.LoadLevels==1) & (df1.data.Acc != -1)])
S1dur = numpy.array(df1.data.StimDur[(df1.data.LoadLevels==1) & (df1.data.Acc != -1)])
# Load level 4
S1on = numpy.array(df1.data.TrialStart[(df1.data.LoadLevels==1) & (df1.data.Acc != -1)])
S1dur = numpy.array(df1.data.StimDur[(df1.data.LoadLevels==1) & (df1.data.Acc != -1)])
# Load level 5
S1on = numpy.array(df1.data.TrialStart[(df1.data.LoadLevels==1) & (df1.data.Acc != -1)])
S1dur = numpy.array(df1.data.StimDur[(df1.data.LoadLevels==1) & (df1.data.Acc != -1)])
# Load level 6
S1on = numpy.array(df1.data.TrialStart[(df1.data.LoadLevels==1) & (df1.data.Acc != -1)])
S1dur = numpy.array(df1.data.StimDur[(df1.data.LoadLevels==1) & (df1.data.Acc != -1)])

# Ret On Times
R1on = numpy.array(df1.data.TrialStart[(df1.data.LoadLevels==1)& (df1.data.RetDur > 0)] + df1.data.RetDur[(df1.data.LoadLevels==1)& (df1.data.RetDur > 0)])
R1dur = numpy.array(df1.data.RetDur[(df1.data.LoadLevels==1)& (df1.data.RetDur > 0)] + df1.data.RetDur[(df1.data.LoadLevels==1)& (df1.data.RetDur > 0)])

# Probe On Times
P1on = numpy.array(df1.data.TrialStart[(df1.data.LoadLevels==1)& (df1.data.ProbeDur > 0)] + df1.data.ProbeDur[(df1.data.LoadLevels==1)& (df1.data.ProbeDur > 0)])
P1dur = numpy.array(df1.data.ProbeDur[(df1.data.LoadLevels==1)& (df1.data.ProbeDur > 0)] + df1.data.ProbeDur[(df1.data.LoadLevels==1)& (df1.data.ProbeDur > 0)])

# specify names
s1=numpy.empty([1,3],dtype=object)
s1[0,0]='Cond1'
s1[0,1]='Cond2'
s1[0,2]='Cond3'

df1.data.TrialStart[(df1.data.TrialDur == 9)&(df1.data.LoadLevels==1)]
# Write out data as a matlab structure for use with SPM


d1 = {'names': s1,'onsets':[S1on,R1on,P1on],'durations':[S1dur,R1dur,P1dur]}
sio.savemat("StructName",d1)


