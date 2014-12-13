import numpy as np
import pandas as pd
# stairCase

StartDur = 500
StepSize = 200
TurnPointLimit = 6

def TriggerOdorant(UseParallelPortFlag,channel,win,p_port):
    if UseParallelPortFlag is True:
        win.callOnFlip(p_port.setData, int(channel))
    else:
        print "Sending to channel %d"%(channel)
        
def RunExample(StartDur = 500, StepSize = 200,TurnPointLimit = 6):
    # Here is a little simulated example
    Data = pd.DataFrame(columns=('StimSide','Response','Correct','Duration','TurnPoint'))
    StopFlag = False
    while StopFlag == False:
    
        SS = ChooseSide()
        RR = ChooseSide()
        CC = IsResponseCorrect(SS,RR)
        DUR = DecDur(Data,SS,StepSize,StartDur)
        Data.loc[len(Data.index)+1] = [SS,RR,CC,DUR,-9999]
        # It is not efficient to check the full file each time for turning points.
        # It would be better to just check the last trial.
        # Oh well!
        Data = FindTurningPoints(Data,SS)
        StopFlag = FindNumberOfTurnPoints(Data,TurnPointLimit)
    
    LeftThreshold, RightThreshold = AverageTurningPoints(Data, TurnPointLimit)
    print "Left Threshold = %d, Right Threshold = %d"%(LeftThreshold, RightThreshold)
    
    return Data, LeftThreshold, RightThreshold

def AverageTurningPoints(Data, TurnPointLimit):
    # average the first set of turning points even if there are more than needed
    # on one side.
    # Left Side
    LeftThreshold = Data[Data['TurnPoint']==0]['Duration'][0:TurnPointLimit].mean()
    # Right Side
    RightThreshold = Data[Data['TurnPoint']==1]['Duration'][0:TurnPointLimit].mean()
    
    return LeftThreshold, RightThreshold


def FindTurningPoints(Data, StimSide):
    # Find the turning points in the data and set them accordingly
    # Right Side turning points
    Side = Data[Data['StimSide'] == StimSide]
    if len(Side) > 3:
        Last = Side.loc[Side['Correct'].index[-1]]
        OneBack = Side.loc[Side['Correct'].index[-2]]
        TwoBack = Side.loc[Side['Correct'].index[-3]]
        # A turning point occurs when a string of at least two correct responses
        # is followed by 
        # an incorrect response
        if (Last['Correct'] == 0) & (OneBack['Correct'] == 1) & (TwoBack['Correct'] == 1):
            Data.loc[Side.index[-1],'TurnPoint'] = StimSide
        # OR a turning point occurs when an incorrect response is followed by at two correct 
        # responses
        elif (Last['Correct'] == 1) & (OneBack['Correct'] == 1) & (TwoBack['Correct'] == 0):
            Data.loc[Side.index[-1],'TurnPoint'] = StimSide
       # print "<<<<< TURNING POINT <<<<<<"
    return Data

def FindNumberOfTurnPoints(Data,TurnPointLimit):
    # Check the data to determine if enough turning points have been reached.
    NumberLeft = len(Data[Data['TurnPoint'] == 0])
    NumberRight = len(Data[Data['TurnPoint'] == 1])
    if (NumberLeft >= TurnPointLimit) & (NumberRight >= TurnPointLimit):
        StopFlag = True
    else:
        StopFlag = False

    return StopFlag

    
def DecDur(Data,StimSide,StepSize,StartDur):
    # This is the logic of whether to lengthen, shorten or do nothing to the 
    # duration of the stimulus.
    # AKA this is the hard part
    #
    MinimumDuration = 0.100
    MaximumDuration = 2.100
    # Is there a trial on this side before the current one?
    OneBackIndex = FindPreviousIndex(Data, StimSide, -1)
    if OneBackIndex != -9999:
        # There is previous trial on this side
        if Data.iloc[OneBackIndex]['Correct'] == 1:
            # The previous trial on this side was correct
            TwoBackIndex = FindPreviousIndex(Data, StimSide, OneBackIndex-1)
            if TwoBackIndex != -9999:
                # There are at least two previous trials on this side
                if Data.iloc[TwoBackIndex]['Correct'] == 1:             
                    
                    # The last two trials were both correct
                    # Make sure the last two correct trials are the SAME Duration
                    if Data.iloc[TwoBackIndex]['Duration'] == Data.iloc[OneBackIndex]['Duration']:
                        print Data.iloc[TwoBackIndex]['Duration']
                        # Make sure the Duration does not get smaller than the step size
                        if Data.iloc[OneBackIndex]['Duration'] > MinimumDuration:
                            Duration = Data.iloc[OneBackIndex]['Duration'] - StepSize
                        else:
                            Duration = Data.iloc[OneBackIndex]['Duration']
                    else:
                        Duration = Data.iloc[OneBackIndex]['Duration']
                else:
                    # Only the previous trial was correct, the one BEFORE that
                    # was NOT correct
                    Duration = Data.iloc[OneBackIndex]['Duration']
            else:
                # There has only been one trial on this side so far
                Duration = Data.iloc[OneBackIndex]['Duration']
        else:
            # The previous trial on this side was NOT correct
            Duration = Data.iloc[OneBackIndex]['Duration'] + StepSize
    else:
        # This is the first trial on this side
        Duration = StartDur
    return Duration
    
def FindPreviousIndex(Data, Stim, StartPoint):
    # Using a specified starting point, iterate over the data to find the previous
    # trial on the same side.
    # Note that iteration is starting from the end and going towards the beginning 
    # of the data and that is why the numbers are all negative.
    Index = -9999
    for i in range(StartPoint,-1*len(Data.index)-1,-1):
        if Data.iloc[i]['StimSide'] == Stim:
            Index = i
            break
            
    return Index

def RunTrial(Duration):
    # run a trial and prepare the information to add to the experimental list
    StimSide = ChooseSide()
    ResponseSide = AskForResponse()
    Correct = IsResponseCorrect(StimSide,ResponseSide)
    if StimSide == 0: # Left
        Output = [1,0,ResponseSide,Correct,Duration]
    else:
        Output = [0,1,ResponseSide,Correct,Duration]
    return Output
            
def ChooseSide():
    # Randomly decide which side to present to
    # 0 is left
    # 1 is right
    return np.round(np.random.rand())
    
def IsResponseCorrect(StimSide,ResponseSide):
    # Determine if the response is correct
    if StimSide == ResponseSide:
        Correct = 1
    else:
        Correct = 0
    return Correct

def AskForResponse():
    # Ask the user to respond
    Response = -1
    while Response == -1:
        print "Press (L)eft or (R)ight"
        choice = raw_input()
        if choice.upper() == 'L':
            Response = 0
        elif choice.upper() == 'R':
            Response = 1
    return Response
    
    