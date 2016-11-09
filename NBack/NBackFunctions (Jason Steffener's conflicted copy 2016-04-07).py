import numpy as np
# Create stimuli
def CreateStim(LoadLevel,TrialPerBlock,NumCorrectPerBlock):
    # pick NumCorPerBlock unique numbers between 1 and TrialPerBlock
    # make sure that the numbers are seperated by at least the load level number of items 
    AllTrue = False
    count = 0
    SuccessFlag = False
    while (AllTrue == False) and count < 1000:
        test = np.round(np.random.uniform(TrialPerBlock*np.ones(NumCorrectPerBlock)))
        test.sort()
        UniqueFlag = len(set(test)) == len(test)
        FirstEntryFlag = test[0] > LoadLevel
        SpacingFlag = True
        PreviousLoc = test[0]
        for i in range(1,len(test)):
            if test[i] < test[i-1] + LoadLevel:
                SpacingFlag = False
        # Make sure all conditions are true
        AllTrue = UniqueFlag == True & FirstEntryFlag == True & SpacingFlag == True
        count += 1
        
    if AllTrue == True:
        print "It took %d attempts to create this list"%count
        return test
    else:
        print "Could not find a solution in %d attempts"%count
        return -99
    

def AssignStimuli(CorrectLocations,TrialPerBlock,Stimuli,LoadLevel):
    List = ['-99']*TrialPerBlock
    NCor = len(CorrectLocations)
    NStim = len(Stimuli)
    # Place random stimuli in the correct locations
    for i in CorrectLocations:
        RandomPick = int(np.round(np.random.uniform(1*NStim)))
        List[int(i)-1] = Stimuli[RandomPick-1]
    # go through and set the previous stimuli appropriately
    for i in range(0,TrialPerBlock,1):
        if List[i] != '-99':
            if List[i-LoadLevel] != '-99':
                List[i] = List[i-LoadLevel]
            else:
                List[i-LoadLevel] = List[i]
    # Find the unused stimuli
    UnusedStimuli = []
    for i in Stimuli:
        if i not in List:
            UnusedStimuli.append(i)
    # fill in the empty trials
    for i in range(0,TrialPerBlock,1):
        if List[i] == '-99':
            RandomPick = int(np.round(np.random.uniform(1*len(UnusedStimuli))))
            # remove the stimuli from the list
            List[i] = UnusedStimuli[RandomPick-1]
            UnusedStimuli.pop(RandomPick-1)
    return List
