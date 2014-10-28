import numpy as np
import pandas as pd
# stairCase

def RunExample(StartDur = 500, StepSize = 200,TurnPointLimit = 4):
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
        # It woudl be better to just check the last trial.
        # Oh well!
        Data = FindTurningPoints(Data)
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


def FindTurningPoints(Data):
    # Find the turning points in the data and set them accordingly
    # Right Side turning points
    R = Data[Data['StimSide'] == 1]
    Data.loc[R.loc[R['Duration'].diff().abs()>0].index,'TurnPoint'] = 1   
    # Left Side turning points
    L = Data[Data['StimSide'] == 0]
    Data.loc[L.loc[L['Duration'].diff().abs()>0].index,'TurnPoint'] = 0   

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
                    # Make sure the Duration does not get smaller than the step size
                    if Data.iloc[OneBackIndex]['Duration'] > MinimumDuration:
                        Duration = Data.iloc[OneBackIndex]['Duration'] - StepSize
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
    
    