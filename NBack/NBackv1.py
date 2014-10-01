import numpy as np
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
from psychopy.hardware.emulator import launchScan

# EXPERIMENTAL INFORMATION
expName = u'NBack'  # <<< This is where you specify the name of the experiment which makes it easier to differentiate the results files.
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# OUTPUT FILENAME
filename = 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# MRI INFORMATION FOR SYNCHRONIZATION
MR_settings = { 
    'TR': 2.000, # duration (sec) per volume
    'volumes': 5, # number of whole-brain 3D volumes / frames
    'sync': '5', # character to use as the sync timing event; assumed to come at start of a volume
    'skip': 0, # number of volumes lacking a sync pulse at start of scan (for T1 stabilization)
    'sound': False # in test mode only, play a tone as a reminder of scanner noise
    }

# FULL SCREEN WINDOW
#win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
#    monitor=u'testMonitor', color=[0,0,0], colorSpace=u'rgb',
#    blendMode=u'avg', useFBO=True,
#    )
    
# PARTIAL SCREEN WINDOW
win = visual.Window(size=[800,600], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace=u'rgb',
    blendMode=u'avg', useFBO=True,
    )

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Create an N-back task
ExpParameters = {
    'NTrials': 60,
    'NBlocks': 5,
    'LoadLevels': range(0,3),
    'TimePerTrial': 2, # seconds
    'TrialPerBlock': 12,
    'StimList': 'ABCDEFGH',
    'NumCorrectPerBlock': 4
}

TextSize = 0.2

StimulusText = visual.TextStim(win=win, ori=0, name='text',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=TextSize, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

CrossHair = visual.TextStim(win=win, ori=0, name='text',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=TextSize, wrapWidth=None,
    color=u'red', colorSpace=u'rgb', opacity=1,
    depth=0.0)
    

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


LoadLevel = 2
CorrectLocations = CreateStim(LoadLevel,ExpParameters['TrialPerBlock'],ExpParameters['NumCorrectPerBlock'])
List = AssignStimuli(CorrectLocations,ExpParameters['TrialPerBlock'],ExpParameters['StimList'],LoadLevel)

ElapsedTimeClock = core.Clock()
# present a block of stimuli
for item in List:
    StimulusText = visual.TextStim(win=win, ori=0, name='text',
            text=item,    font=u'Arial',
            pos=[0, 0], height=TextSize, wrapWidth=None,
            color=u'white', colorSpace=u'rgb', opacity=1,
            depth=0.0)    
    StimulusText.draw()
    win.flip()
    ElapsedTimeClock.reset()
    while ElapsedTimeClock.getTime() < 1:
        if event.getKeys(keyList=["escape"]):
            core.quit() 
        else:
            # This must be a response
            print event.getKeys()
CrossHair.draw()
win.flip()
        
    