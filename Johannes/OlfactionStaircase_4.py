from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
import sys
import os  # handy system and path functions
ThisScript = sys.argv[0]
ThisFolder = os.path.dirname(ThisScript)
sys.path.append(ThisFolder)


from psychopy import visual, core, data, event, logging, sound, gui, parallel
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle

from psychopy.hardware.emulator import launchScan
import numpy as np
import pandas as pd
from StaircaseFunctions import *

UseParallelPortFlag = True
if UseParallelPortFlag:
    ParallelPort = parallel.ParallelPort(address='0x0378')
else:
    ParallelPort = False

# EXPERIMENTAL INFORMATION
expName = u'OlfactStaircase'  # <<< This is where you specify the name of the experiment which makes it easier to differentiate the results files.
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# OUTPUT FILENAME
filename = 'data/%s_%s_%s.csv' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
#thisExp = data.ExperimentHandler(name=expName, version='',
#    extraInfo=expInfo, runtimeInfo=None,
#    originPath=None,
#    savePickle=False, saveWideText=True,
#    dataFileName=filename)

#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# MRI INFORMATION FOR SYNCHRONIZATION
# This is currently unused. It gets used when synchronizing an experiemnt to an MRI
MR_settings = { 
    'TR': 2.000, # duration (sec) per volume
    'volumes': 5, # number of whole-brain 3D volumes / frames
    'sync': 'equal', # character to use as the sync timing event; assumed to come at start of a volume
    'skip': 0, # number of volumes lacking a sync pulse at start of scan (for T1 stabilization)
    'sound': False # in test mode only, play a tone as a reminder of scanner noise
    }

# DISPLAY PARAMETERS FOR THE USER TO CONFIRM
# infoDlg = gui.DlgFromDict(MR_settings, title='MRI Settings')

# Present experimental parameters to user to confirm
ExpParameters = {
    'TextSize': 0.2,
    'DelayBetweenTrials': 1,
    'RedCrosshairTime':1,
    'LeftChannel':6,
    'RightChannel':9,
    'StepSize':0.200,
    'TurnPointLimit':4,
    'StartDur':0.500
}

# DISPLAY PARAMETERS FOR THE USER TO CONFIRM
infoDlg = gui.DlgFromDict(ExpParameters, title='Experimental Parameters')
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Decide which screen you would like to use. I prefer the partial screen for testing.

# FULL SCREEN WINDOW
#win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
#    monitor=u'testMonitor', color=[0,0,0], colorSpace=u'rgb',
#    blendMode=u'avg', useFBO=False,
#    )
    
# PARTIAL SCREEN WINDOW
win = visual.Window(size=[800,600], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace=u'rgb',
    blendMode=u'avg', useFBO=False,
    )
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# DEFINE ALL OF THE STIMULI PRESENTED DURING THE EXPERIMENT
Instructions = visual.TextStim(win=win, ori=0, name='text',
    text='If you perceive the odor in the left nostril, press the left arrow,\nIf you perceive the odor in the right nostril, press the right arrow.\n\nPress any key to start the experiment',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
   
RedCrossHair = visual.TextStim(win=win, ori=0, name='text',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=ExpParameters['TextSize'], wrapWidth=None,
    color=u'red', colorSpace=u'rgb', opacity=1,
    depth=0.0)   

GreenCrossHair = visual.TextStim(win=win, ori=0, name='text',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=ExpParameters['TextSize'], wrapWidth=None,
    color=u'green', colorSpace=u'rgb', opacity=1,
    depth=0.0)   

WhiteCrossHair = visual.TextStim(win=win, ori=0, name='text',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=ExpParameters['TextSize'], wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)   

OrangeCrossHair = visual.TextStim(win=win, ori=0, name='text',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=ExpParameters['TextSize'], wrapWidth=None,
    color=u'orange', colorSpace=u'rgb', opacity=1,
    depth=0.0)   

ThankYouScreen = visual.TextStim(win=win, ori=0, name='text',
    text=u'It is over.\nThanks',    font=u'Arial',
    pos=[0, 0], height=ExpParameters['TextSize'], wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)



# Set up the clocks
TrialClock = core.Clock()
CountDownClock = core.CountdownTimer()
ElapsedTimeClock = core.Clock()

# Prepare the data frame used for keeping track of what has been done
Data = pd.DataFrame(columns=('StimSide','Response','Correct','Duration','TurnPoint','ResponseTime','TrialStartTime','TrialDelay'))
StopFlag = False
print Data
# Present Instructions
InstructionFlag = True
Instructions.draw()
win.flip()
while InstructionFlag is True:
    theseKeys = event.getKeys()
    if 'escape' in theseKeys:
        win.flip()
        win.close()
        core.quit()
    if len(theseKeys) > 0: 
        # user pressed a key
        InstructionFlag = False
    
CountDownClock.reset()
ElapsedTimeClock.reset()
while StopFlag == False:
    # present white cross hair for forty seconds
    # Reset the countdown timer here because the time for response is variable
    
    CountDownClock.add(ExpParameters['DelayBetweenTrials'])
    WhiteCrossHair.draw()
    win.flip()
    while CountDownClock.getTime() > 0:
        theseKeys = event.getKeys()
        if "escape" in theseKeys:
            win.flip()
            win.close()
            core.quit()
    
    # present red cross hair for one second
    CountDownClock.add(ExpParameters['RedCrosshairTime'])
    RedCrossHair.draw()
    win.flip()
    # Here is when I can prepare for the next presentation
    # Decide how long to wait in seconds
    DelayBeforeOdor = np.round(np.random.rand()*1000 + 500)/1000
    # Decide which nostril to send to
    # This uses a function from the StaircaseFunctions code
    StimulusSide = ChooseSide()
    # 'Stimulus side: %d'%(StimulusSide)
    while CountDownClock.getTime() > 0:
        theseKeys = event.getKeys()
        if "escape" in theseKeys:
            win.flip()
            win.close()
            core.quit()
    # present green cross hair
    CountDownClock.add(DelayBeforeOdor)
    GreenCrossHair.draw()
    win.flip()
    # Here is when I can prepare for the next presentation
    # map the left/right coding of 0/1 onto the appropriate channels
    if StimulusSide == 0: #Left
        channel = ExpParameters['LeftChannel']
    elif StimulusSide == 1: #Right
        channel = ExpParameters['RightChannel']
    else:
        # received unknown response and sending a close signal
        channel = 0
    # decide on the duration for the trial
    DUR = DecDur(Data,StimulusSide,ExpParameters['StepSize'],0.500)

    # wait for between 500 and 1500ms
    while CountDownClock.getTime() > 0:
        theseKeys = event.getKeys()
        if "escape" in theseKeys:
            win.flip()
            win.close()
            core.quit()
    
    # trigger odor to start
    TrialStartTime = ElapsedTimeClock.getTime()
    # trigger odorant
    TriggerOdorant(UseParallelPortFlag,channel,win,ParallelPort)

    
    # Wait for duration of odorant presentation time
    #print "Odor presentation: %0.4f"%(DUR)
    CountDownClock.add(DUR)
    while CountDownClock.getTime() > 0:
        theseKeys = event.getKeys()
        if "escape" in theseKeys:
            win.flip()
            win.close()
            # if an escape key is pressed here make sure to turn off the odors
            TriggerOdorant(UseParallelPortFlag,0,win,ParallelPort)
            core.quit()    

    # trigger odor to stop
    TriggerOdorant(UseParallelPortFlag,0,win,ParallelPort)
    # present orange cross hair
    OrangeCrossHair.draw()
    win.flip()
    # wait for user to respond
    UserResponseFlag = False
    while not UserResponseFlag:
        theseKeys = event.getKeys()
        if "escape" in theseKeys:
            win.flip()
            win.close()
            core.quit() 
        elif len(theseKeys) > 0:
            # This must be a response
            CurrentRT = ElapsedTimeClock.getTime() - TrialStartTime
            print theseKeys
            if theseKeys[-1] == 'left':
                Response = 0
                UserResponseFlag = True
            elif theseKeys[-1] == 'right':
                Response = 1
                UserResponseFlag = True
    # The post stimulus calculcations and decisions may take some time, less than a second. 
    # But since there is a long inter-trial interval, they will take place during this time.
    # To do this the count down clock is reset here. Then the amount of time it take to do the 
    # following is subtracted from the clock and therefore take from the ITI.
    CountDownClock.reset()

    # Is response correct?
    Correct = IsResponseCorrect(StimulusSide,Response)
    #print 'Stim side: %d, Response side: %d, Correct: %d'%(StimulusSide,Response,Correct)
    
    Data = AddDataRow(Data,[StimulusSide,Response,Correct,DUR,-9999,CurrentRT,TrialStartTime,DelayBeforeOdor])
    
    DUR = DecDur(Data,StimulusSide,ExpParameters['StepSize'],ExpParameters['StartDur'])
    #Data.loc[len(Data.index)+1] = [StimulusSide,Response,Correct,DUR,-9999,CurrentRT,TrialStartTime,DelayBeforeOdor]
    
    
    #Data.loc[len(Data.index)+1] = [StimulusSide,Response,Correct,DUR,-9999]
        # It is not efficient to check the full file each time for turning points.
        # It would be better to just check the last trial.
        # Oh well!
    Data = FindTurningPoints(Data,StimulusSide)
    StopFlag = FindNumberOfTurnPoints(Data,ExpParameters['TurnPointLimit'])
    print Data

LeftThreshold, RightThreshold = AverageTurningPoints(Data, ExpParameters['TurnPointLimit'])
print "Left Threshold = %0.3f, Right Threshold = %0.3f"%(LeftThreshold, RightThreshold)



    # Put all data from this trial into the data frame
    # columns=('StimSide','Response','Correct','Duration','TurnPoint','ResponseTime','TrialStartTime','TrialDelay'))
#    Data.loc[len(Data.index)+1] = [StimulusSide,Response,Correct,DUR,-9999,CurrentRT,TrialStartTime,DelayBeforeOdor]
    #  Check to see if the last trial was a turning point
#    Data = FindTurningPoints(Data,0)
#    Data = FindTurningPoints(Data,1)
#    StopFlag = FindNumberOfTurnPoints(Data,ExpParameters['TurnPointLimit'])
    
    
# The program is done!


# Calculate turning point average thresholds
LeftThreshold, RightThreshold = AverageTurningPoints(Data, ExpParameters['TurnPointLimit'])
# add this info to the bottom of the data frame
Data = Data.append(['LeftThreshold',LeftThreshold,'RightThreshold',RightThreshold],ignore_index=True)

# reformat the float values
Data['ResponseTime'] = Data['ResponseTime'].map('{:.3f}'.format)
Data['TrialStartTime'] = Data['TrialStartTime'].map('{:.3f}'.format)
Data['TrialDelay'] = Data['TrialDelay'].map('{:.3f}'.format)

# Save the data

Data.to_csv(filename)



 