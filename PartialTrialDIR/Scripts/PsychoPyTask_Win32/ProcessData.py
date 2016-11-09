import sys
import scipy.io as sio
import pandas as pd
import array
from itertools import compress
import numpy
import WriteToGoogleSpreadSheet
import os

# These are the functions for working with the behavioral data files
class PTdata():            
    def loadData(self,InDataFile):
        self.data = pd.read_csv(InDataFile)
        # psychopy puts dots inthe coulmn names which python cannot work with
        # The dots are replaced with underscores
        cols = self.data.columns
        cols = cols.map(lambda x: x.replace('.', '_') if isinstance(x, (str, unicode)) else x)
        self.data.columns = cols

#        float(df.KeyboardResp_rt[30][1:-1])

    def onlyKeepDataRows(self):
        # before reoving the extra rows make sure to keep the start and stop times
        self.StartTime = self.data.TrialStartTime[1]
        self.StopTime = self.data.TrialStartTime.iloc[-1]
        # remove extra rows
        self.data = self.data[~numpy.isnan(self.data.RetDur)]
        # update the index
        self.NRows = len(self.data)
        self.data.index = range(0,self.NRows)
        
    def whatLoadIsThisRow(self):
        # create an array of load levels
        # load is determined by the number of letters contained in brackets
        LoadLevels = numpy.array((0,)*len(self.data))
        #ResponseExpected = numpy.array((0,)*self.NRows)
        count = 0
        for i in self.data.index:
            LoadLevels[count] = len(str(int(self.data.UpBrack[i])))
            count = count +1
        self.data['LoadLevels'] = pd.Series(LoadLevels, index = self.data.index)
        


    def areResponsesCorrect(self):
        # The following is to account for the situation where the subject does 
        # not have their fingers ob the correct buttons.
        # Responses the subject made 
        # If the run type is training then use down and right as correct/incorrect
        # If the run type is MRI then use 2 and 3.
        if 'Run' in self.RunType:
            # The MRI runs use 2 and 3 as correct and incorrect.
            # But the data/design file has them coded as 6 and 7.
            print 'MRI Run'
            self.Yes = '2' ## or 7
            self.No = '3' ## or 8
            self.ExpectYes = 6
            self.ExpectNo = 7
        elif 'Train' in self.RunType:
            print 'Training Run'
            self.Yes = 'down'
            self.No = 'right'
            self.ExpectYes = 'down'
            self.ExpectNo = 'right'

        Accuracy = numpy.array((0.0,)*self.NRows)
        ResponseTimes = numpy.array((0.0,)*self.NRows)
        for i in self.data.index:
            # was a response made?
            if self.data.KeyboardResp_keys[i] == 'None':
                Accuracy[i] = numpy.nan
                ResponseTimes[i] = numpy.nan
            else:
                CurrentResp = self.data.KeyboardResp_keys[i]
                CurrentRT = self.data.KeyboardResp_rt[i]

                # is the RT in brackets or not?
                # The version of this task with feedback only records the LAST response. 
                # This is because the FB version scores the responses on a trial by trial
                # basis and discards any extraneous responses.
                # The version without feedback keeps all responses which are stored in a list.
                #
                if type(CurrentRT) is numpy.float64:
                    # If this is TRUE then the run is a training run with feedback

                    ResponseTimes[i] = CurrentRT
                    if CurrentResp == self.Yes:
                        if (self.data.Correct[i] == self.ExpectYes):
                            Accuracy[i] = 1
                        else:
                            Accuracy[i] = 0
                    elif CurrentResp == self.No:
                        if (self.data.Correct[i] == self.ExpectNo):             
                            Accuracy[i] = 1
                        else:                    
                            Accuracy[i] = 0
                else:
                    # pull off the brackets
                    CurrentResp = CurrentResp[1:-1]
                    CurrentRT = CurrentRT[1:-1]                
                    # Get the last response in case multiple buttons were pressed
                    # is the response equal to the expected Yes response?
                    # is it SUPPOSED to be a Yes response?

                    if (CurrentResp.split(',')[-1].split('\'')[1] == self.Yes): #
                        if (self.data.Correct[i] == self.ExpectYes):
                            Accuracy[i] = 1
                        else:
                            Accuracy[i] = 0
                    elif (CurrentResp.split(',')[-1].split('\'')[1] == self.No): # 
                        if (self.data.Correct[i] == self.ExpectNo):             
                            Accuracy[i] = 1
                        else:                    
                            Accuracy[i] = 0

                    ResponseTimes[i] = float(CurrentRT.split(',')[-1])
        # Now that response times and accuracies have been extracted add them 
        # back to the data frame        
        self.data['RT'] = pd.Series(ResponseTimes, index = self.data.index)
        self.data['Acc'] = pd.Series(Accuracy, index = self.data.index)

    def LoadLevelAccuracy(self):
        count = 0
        self.LoadAccuracyFull = numpy.zeros(len(self.Loads))
        self.LoadAccuracy_SR = numpy.zeros(len(self.Loads))
        # How many responses did the participant make
        self.LoadNumResponseFull = numpy.zeros(len(self.Loads)) 
        self.LoadNumResponse_SR = numpy.zeros(len(self.Loads))        
        # How many responses was the participant EXPECTED to make        
        self.LoadNumExpRespFull = numpy.zeros(len(self.Loads)) 
        self.LoadNumExpResp_SR = numpy.zeros(len(self.Loads))          
        # What is the mean response time
        self.LoadMeanRespTimeFull = numpy.zeros(len(self.Loads))
        self.LoadMeanRespTime_SR = numpy.zeros(len(self.Loads))      
        # What is the median response time
        self.LoadMedianRespTimeFull = numpy.zeros(len(self.Loads))
        self.LoadMedianRespTime_SR = numpy.zeros(len(self.Loads))      

        for i in self.Loads:
            # Full trials
            TotalPossibleFull = len(numpy.where((self.LoadLevels == i)  & (self.data.TrialDur[self.DataRows]==9))[0])
            TotalCorrectFull = len(numpy.where((self.LoadLevels == i) & (self.Accuracy == 1) & (self.data.TrialDur[self.DataRows]==9))[0])
            self.LoadNumExpRespFull[count] = TotalPossibleFull
            self.LoadNumResponseFull[count] = TotalCorrectFull
         
            self.LoadAccuracyFull[count] = float(TotalCorrectFull)/float(TotalPossibleFull)
            self.ResponseTimes[numpy.where((self.LoadLevels == i)  & (self.data.TrialDur[self.DataRows]==9))[0]].mean()
            self.LoadMeanRespTimeFull[count] = self.ResponseTimes[numpy.where((self.LoadLevels == i)  & (self.data.TrialDur[self.DataRows]==9))[0]].mean()
            self.LoadMedianRespTimeFull[count] = numpy.median(self.ResponseTimes[numpy.where((self.LoadLevels == i)  & (self.data.TrialDur[self.DataRows]==9))[0]])

            # Partial trials
            TotalPossible_SR = len(numpy.where((self.LoadLevels == i)  & (self.data.TrialDur[self.DataRows]==4))[0])
            TotalCorrect_SR = len(numpy.where((self.LoadLevels == i) & (self.Accuracy == 1) & (self.data.TrialDur[self.DataRows]==4))[0])
            self.LoadNumExpResp_SR[count] = TotalPossible_SR
            self.LoadNumResponse_SR[count] = TotalCorrect_SR

            self.LoadAccuracy_SR[count] = float(TotalCorrect_SR)/float(TotalPossible_SR)
            self.LoadMeanRespTime_SR[count] = self.ResponseTimes[numpy.where((self.LoadLevels == i)  & (self.data.TrialDur[self.DataRows]==4))[0]].mean()
            self.LoadMedianRespTime_SR[count] = numpy.median(self.ResponseTimes[numpy.where((self.LoadLevels == i)  & (self.data.TrialDur[self.DataRows]==4))[0]])
            count = count + 1
        
    def getTrialStartTimes(self):
        TrialStartTimes = numpy.zeros(self.NRows)
        for i in self.data.index:
            TrialStartTimes[i] = self.data.TrialStartTime[i]-self.StartTime
        self.data['TrialStart'] = pd.Series(TrialStartTimes, index = self.data.index)
            
def loadBehDataFile(inFile):
    # create object
    dataFrame = PTdata()
    # read file
    # df1.InputFile = ex.fileName[0][0]
    dataFrame.InputFile = inFile
    # df1.loadData(ex.fileName[0][0])
    dataFrame.loadData(inFile)
    # Find out if this is a training run or an MRI run
    dataFrame.RunType = os.path.basename(inFile).split('_')[3]
    # Get subject ID
    dataFrame.Subid = os.path.basename(inFile).split('_')[1]
    return dataFrame
    
def concatTwoDataFrames(dataFrame1, dataFrame2):
    # Concat the two files and calculate their performance across the two files.
    # Before concat, update the indices
    dataFrame2.data.index = dataFrame2.data.index + len(dataFrame1.data.index)
    frames = [dataFrame1.data, dataFrame2.data]
    dataFrame = pd.concat(frames)
    return dataFrame
    
def processBehavioralFile(dataFrame):
    # extract data from file
    dataFrame.onlyKeepDataRows()
    # find load levels
    dataFrame.whatLoadIsThisRow()
    # check for accuracy
    dataFrame.areResponsesCorrect()
    # get trial start times
    dataFrame.getTrialStartTimes()
    return dataFrame

def writeSummaryBehavioralDataToFile(dataFrame, workSheet, Tag, col):
    # Write the row names
    LoadLevels = numpy.unique(dataFrame.data.LoadLevels)
    WriteToGoogleSpreadSheet.writeData(workSheet, LoadLevels, 1, 2,'Load')

    data1 = dataFrame.data.RT.groupby(dataFrame.data.LoadLevels).mean()
    title1 = '%s_meanRT'%(Tag)
    col1 = col + 1
    rowStart = 2
    WriteToGoogleSpreadSheet.writeData(workSheet, data1, col1, rowStart,title1)

    data2 = dataFrame.data.Acc.groupby(dataFrame.data.LoadLevels).mean()
    title2 = '%s_meanAcc'%(Tag)
    col2 = col + 2
    rowStart = 2
    WriteToGoogleSpreadSheet.writeData(workSheet, data2, col2, rowStart,title2)

    data3 = dataFrame.data.Acc.groupby(dataFrame.data.LoadLevels).sum()
    title3 = '%s_numCorr'%(Tag)
    col3 = col + 3
    rowStart = 2
    WriteToGoogleSpreadSheet.writeData(workSheet, data3, col3, rowStart,title3)

def createSPMDesignMatrix(dataFrame, OutFileName):
    print "Hello World"
    # The first two scans are discarded so the timing has to be shifted by that amount
    TR = 2
    DiscardNumber = 2
    TimeShift = TR*DiscardNumber
    # Look for time outs
    # First find the trials where a response was expected
    TOTrialsToKeep = (numpy.isnan(dataFrame.data.Acc)) & ((dataFrame.data.TrialDur == 9) | (dataFrame.data.TrialDur == 4))
    IncTrialsToKeep = dataFrame.data.Acc == 0
    
    # Find Time Out Trials
    # The time out trials are being corectly identified and classified as incorrect.
    # However, they are still included as being correct.
    
    # Find the incorrect trials
    TrialsToKeep = TOTrialsToKeep | IncTrialsToKeep
    SincOn = numpy.array(dataFrame.data.TrialStart[TrialsToKeep]) - TimeShift
    RincOn = numpy.array(dataFrame.data.TrialStart[TrialsToKeep] + dataFrame.data.StimDur[TrialsToKeep]) - TimeShift
    PincOn = numpy.array(dataFrame.data.TrialStart[TrialsToKeep] + dataFrame.data.StimDur[TrialsToKeep] + dataFrame.data.RetDur[TrialsToKeep]) - TimeShift
    SincDur = numpy.array(dataFrame.data.StimDur[TrialsToKeep])
    RincDur = numpy.array(dataFrame.data.RetDur[TrialsToKeep])
    PincDur = numpy.array(dataFrame.data.ProbeDur[TrialsToKeep])
    
    LoadLevels = numpy.unique(dataFrame.data.LoadLevels) 
    # Load level 1
    TrialsToKeep = (dataFrame.data.LoadLevels==1) & (dataFrame.data.Acc != -1) & (~(numpy.isnan(dataFrame.data.Acc)))
    S1on = numpy.array(dataFrame.data.TrialStart[TrialsToKeep]) - TimeShift
    S1dur = numpy.array(dataFrame.data.StimDur[TrialsToKeep])
    TrialsToKeep = (dataFrame.data.LoadLevels==1) & (dataFrame.data.RetDur > 0) & (dataFrame.data.Acc != -1) & (~(numpy.isnan(dataFrame.data.Acc)))
    R1on = numpy.array(dataFrame.data.TrialStart[TrialsToKeep] + dataFrame.data.StimDur[TrialsToKeep]) - TimeShift
    R1dur = numpy.array(dataFrame.data.RetDur[TrialsToKeep])
    TrialsToKeep = (dataFrame.data.LoadLevels==1) & (dataFrame.data.ProbeDur > 0) & (dataFrame.data.Acc != -1) & (~(numpy.isnan(dataFrame.data.Acc)))
    P1on = numpy.array(dataFrame.data.TrialStart[TrialsToKeep] + dataFrame.data.StimDur[TrialsToKeep] + dataFrame.data.RetDur[TrialsToKeep]) - TimeShift
    P1dur = numpy.array(dataFrame.data.RT[TrialsToKeep])
    
    # Load level 2
    TrialsToKeep = (dataFrame.data.LoadLevels==2) & (dataFrame.data.Acc != -1) & (~(numpy.isnan(dataFrame.data.Acc)))
    S2on = numpy.array(dataFrame.data.TrialStart[TrialsToKeep]) - TimeShift
    S2dur = numpy.array(dataFrame.data.StimDur[TrialsToKeep])
    TrialsToKeep = (dataFrame.data.LoadLevels==2) & (dataFrame.data.RetDur > 0) & (dataFrame.data.Acc != -1) & (~(numpy.isnan(dataFrame.data.Acc)))
    R2on = numpy.array(dataFrame.data.TrialStart[TrialsToKeep] + dataFrame.data.StimDur[TrialsToKeep]) - TimeShift
    R2dur = numpy.array(dataFrame.data.RetDur[TrialsToKeep])
    TrialsToKeep = (dataFrame.data.LoadLevels==2) & (dataFrame.data.ProbeDur > 0) & (dataFrame.data.Acc != -1) & (~(numpy.isnan(dataFrame.data.Acc)))
    P2on = numpy.array(dataFrame.data.TrialStart[TrialsToKeep] + dataFrame.data.StimDur[TrialsToKeep] + dataFrame.data.RetDur[TrialsToKeep]) - TimeShift
    P2dur = numpy.array(dataFrame.data.RT[TrialsToKeep])
    
    # Load level 3
    TrialsToKeep = (dataFrame.data.LoadLevels==3) & (dataFrame.data.Acc != -1) & (~(numpy.isnan(dataFrame.data.Acc)))
    S3on = numpy.array(dataFrame.data.TrialStart[TrialsToKeep]) - TimeShift
    S3dur = numpy.array(dataFrame.data.StimDur[TrialsToKeep])
    TrialsToKeep = (dataFrame.data.LoadLevels==3) & (dataFrame.data.RetDur > 0) & (dataFrame.data.Acc != -1) & (~(numpy.isnan(dataFrame.data.Acc)))
    R3on = numpy.array(dataFrame.data.TrialStart[TrialsToKeep] + dataFrame.data.StimDur[TrialsToKeep]) - TimeShift
    R3dur = numpy.array(dataFrame.data.RetDur[TrialsToKeep])
    TrialsToKeep = (dataFrame.data.LoadLevels==3) & (dataFrame.data.ProbeDur > 0) & (dataFrame.data.Acc != -1) & (~(numpy.isnan(dataFrame.data.Acc)))
    P3on = numpy.array(dataFrame.data.TrialStart[TrialsToKeep] + dataFrame.data.StimDur[TrialsToKeep] + dataFrame.data.RetDur[TrialsToKeep]) - TimeShift
    P3dur = numpy.array(dataFrame.data.RT[TrialsToKeep])
    
    # Load level 4
    TrialsToKeep = (dataFrame.data.LoadLevels==4) & (dataFrame.data.Acc != -1) & (~(numpy.isnan(dataFrame.data.Acc)))
    S4on = numpy.array(dataFrame.data.TrialStart[TrialsToKeep]) - TimeShift
    S4dur = numpy.array(dataFrame.data.StimDur[TrialsToKeep])
    TrialsToKeep = (dataFrame.data.LoadLevels==4) & (dataFrame.data.RetDur > 0) & (dataFrame.data.Acc != -1) & (~(numpy.isnan(dataFrame.data.Acc)))
    R4on = numpy.array(dataFrame.data.TrialStart[TrialsToKeep] + dataFrame.data.StimDur[TrialsToKeep]) - TimeShift
    R4dur = numpy.array(dataFrame.data.RetDur[TrialsToKeep])
    TrialsToKeep = (dataFrame.data.LoadLevels==4) & (dataFrame.data.ProbeDur > 0) & (dataFrame.data.Acc != -1) & (~(numpy.isnan(dataFrame.data.Acc)))
    P4on = numpy.array(dataFrame.data.TrialStart[TrialsToKeep] + dataFrame.data.StimDur[TrialsToKeep] + dataFrame.data.RetDur[TrialsToKeep]) - TimeShift
    P4dur = numpy.array(dataFrame.data.RT[TrialsToKeep])
    
    # Load level 5
    TrialsToKeep = (dataFrame.data.LoadLevels==5) & (dataFrame.data.Acc != -1) & (~(numpy.isnan(dataFrame.data.Acc)))
    S5on = numpy.array(dataFrame.data.TrialStart[TrialsToKeep]) - TimeShift
    S5dur = numpy.array(dataFrame.data.StimDur[TrialsToKeep])
    TrialsToKeep = (dataFrame.data.LoadLevels==5) & (dataFrame.data.RetDur > 0) & (dataFrame.data.Acc != -1) & (~(numpy.isnan(dataFrame.data.Acc)))
    R5on = numpy.array(dataFrame.data.TrialStart[TrialsToKeep] + dataFrame.data.StimDur[TrialsToKeep]) - TimeShift
    R5dur = numpy.array(dataFrame.data.RetDur[TrialsToKeep])
    TrialsToKeep = (dataFrame.data.LoadLevels==5) & (dataFrame.data.ProbeDur > 0) & (dataFrame.data.Acc != -1) & (~(numpy.isnan(dataFrame.data.Acc)))
    P5on = numpy.array(dataFrame.data.TrialStart[TrialsToKeep] + dataFrame.data.StimDur[TrialsToKeep] + dataFrame.data.RetDur[TrialsToKeep]) - TimeShift
    P5dur = numpy.array(dataFrame.data.RT[TrialsToKeep])
    
    # Load level 6
    TrialsToKeep = (dataFrame.data.LoadLevels==6) & (dataFrame.data.Acc != -1) & (~(numpy.isnan(dataFrame.data.Acc)))
    S6on = numpy.array(dataFrame.data.TrialStart[TrialsToKeep]) - TimeShift
    S6dur = numpy.array(dataFrame.data.StimDur[TrialsToKeep])
    TrialsToKeep = (dataFrame.data.LoadLevels==6) & (dataFrame.data.RetDur > 0) & (dataFrame.data.Acc != -1) & (~(numpy.isnan(dataFrame.data.Acc)))
    R6on = numpy.array(dataFrame.data.TrialStart[TrialsToKeep] + dataFrame.data.StimDur[TrialsToKeep]) - TimeShift
    R6dur = numpy.array(dataFrame.data.RetDur[TrialsToKeep])
    TrialsToKeep = (dataFrame.data.LoadLevels==6) & (dataFrame.data.ProbeDur > 0) & (dataFrame.data.Acc != -1) & (~(numpy.isnan(dataFrame.data.Acc)))
    P6on = numpy.array(dataFrame.data.TrialStart[TrialsToKeep] + dataFrame.data.StimDur[TrialsToKeep] + dataFrame.data.RetDur[TrialsToKeep]) - TimeShift
    P6dur = numpy.array(dataFrame.data.RT[TrialsToKeep])
    
    
    # specify names
    if len(SincOn) > 0:
        s1=numpy.empty([1,21],dtype=object)
    else:
        s1=numpy.empty([1,18],dtype=object)
    s1[0,0]='S1'
    s1[0,1]='R1'
    s1[0,2]='P1'
    s1[0,3]='S2'
    s1[0,4]='R2'
    s1[0,5]='P2'
    s1[0,6]='S3'
    s1[0,7]='R3'
    s1[0,8]='P3'
    s1[0,9]='S4'
    s1[0,10]='R4'
    s1[0,11]='P4'
    s1[0,12]='S5'
    s1[0,13]='R5'
    s1[0,14]='P5'
    s1[0,15]='S6'
    s1[0,16]='R6'
    s1[0,17]='P6'
    if len(SincOn) > 0:
        s1[0,18] = 'Sinc'
        s1[0,19] = 'Rinc'
        s1[0,20] = 'Pinc'
        
    # Write out data as a matlab structure for use with SPM
    if len(SincOn) > 0:
        onsets = [S1on,R1on,P1on,S2on,R2on,P2on,S3on,R3on,P3on,S4on,R4on,P4on,S5on,R5on,P5on,S6on,R6on,P6on,SincOn,RincOn,PincOn]
        durations = [S1dur,R1dur,P1dur,S2dur,R2dur,P2dur,S3dur,R3dur,P3dur,S4dur,R4dur,P4dur,S5dur,R5dur,P5dur,S6dur,R6dur,P6dur,SincDur,RincDur,PincDur]
    else:
        onsets = [S1on,R1on,P1on,S2on,R2on,P2on,S3on,R3on,P3on,S4on,R4on,P4on,S5on,R5on,P5on,S6on,R6on,P6on]
        durations = [S1dur,R1dur,P1dur,S2dur,R2dur,P2dur,S3dur,R3dur,P3dur,S4dur,R4dur,P4dur,S5dur,R5dur,P5dur,S6dur,R6dur,P6dur]

    d1 = {'names': s1,'onsets':onsets,'durations':durations}
    sio.savemat(OutFileName,d1)

