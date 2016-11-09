from ProcessData import PTdata
import ProcessData
import WriteToGoogleSpreadSheet
from FileSelectClass import Example

def ProcessAFile(inputFile,subid,Tag):
    df1 = ProcessData.loadBehDataFile(inputFile)
    df1 = ProcessData.processBehavioralFile(df1)
    wkB = WriteToGoogleSpreadSheet.openWorkBook()
    wkS = WriteToGoogleSpreadSheet.createWorksheet(wkB, subid)
    writeSummaryBehavioralDataToFile(df1, wkS, Tag)

ex = Example()
# This will ask you to select on or more files
ex.showDialog()
df1 = ProcessData.loadBehDataFile(ex.fileName[0][0])
df1 = ProcessData.processBehavioralFile(df1)
ProcessData.createSPMDesignMatrix(df1, 'P00002001_S0001_Run1_DM')
df2 = ProcessData.loadBehDataFile(ex.fileName[0][1])
df2 = ProcessData.processBehavioralFile(df2)
ProcessData.createSPMDesignMatrix(df1, 'P00002001_S0001_Run2_DM')


wkB = WriteToGoogleSpreadSheet.openWorkBook()
wkS = WriteToGoogleSpreadSheet.createWorksheet(wkB, '2001')
writeSummaryBehavioralDataToFile(df1, wkS, 'Run1')




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


grp2 = df1.data.TrialStart.groupby(df1.data.LoadLevels)


len(df1.data)
df1.data.drop(numpy.isnan(df1.data.RetDur))
len(df1.data)



df1.rowsContainingData()
df1.whatLoadIsThisRow()
df1.areResponsesCorrect()
df1.LoadLevelAccuracy()
df1.getTrialStartTimes()

df.rowsContainingData()
df.whatLoadIsThisRow()
df.areResponsesCorrect()
df.LoadLevelAccuracy()
getTrialStartTimes

df.LoadAccuracyFull
df.LoadMeanRespTimeFull
df.LoadNumExpRespFull
df.LoadNumResponseFull
df.LoadNumExpResp_SR
df.LoadNumResponse_SR
df.LoadNumResponseFull
df.LoadNumExpRespFull
