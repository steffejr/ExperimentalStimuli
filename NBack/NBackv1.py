import numpy as np
# Create an N-back task
ExpParameters = {
    'NTrials': 60,
    'NBlocks': 5,
    'LoadLevels': range(0,4),
    'TimePerTrial': 2, # seconds
    'TrialPerBlock': 12,
    'StimList': 'ABCDEFGH',
    'NumCorrectPerBlock': 4
}
# Create stimuli
def CreateStim(LoadLevel,TrialPerBlock,NumCorrectPerBlock):
    # pick NumCorPerBlock unique numbers between 1 and TrialPerBlock
    # make sure that the numbers are seperated by at least the load level number of items 
    AllTrue = False
    while AllTrue == False:
        test = np.round(np.random.uniform(TrialPerBlock*np.ones(NumCorrectPerBlock)))
        test.sort()
        UniqueFlag = len(set(test)) == len(test)
        FirstEntryFlag = test[0] > LoadLevel
        SpacingFlag = True
        PreviousLoc = test[0]
        for i in range(1,len(test)):
            if test[i] < test[i-1] + LoadLevel:
                SpacingFlag = False
        #print test
        #print UniqueFlag
        #print FirstEntryFlag
        #print SpacingFlag
        AllTrue = UniqueFlag == True & FirstEntryFlag == True & SpacingFlag == True
    return test
def AssignStimuli(CorrectLocations,TrialPerBlock,Stimuli):
    