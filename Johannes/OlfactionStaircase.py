from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
import sys
import os  # handy system and path functions
ThisScript = sys.argv[0]
ThisFolder = os.path.dirname(ThisScript)
sys.path.append(ThisFolder)


from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle

from psychopy.hardware.emulator import launchScan
import numpy as np
from StaircaseFunctions import *





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
    savePickle=False, saveWideText=True,
    dataFileName=filename)

#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# MRI INFORMATION FOR SYNCHRONIZATION
MR_settings = { 
    'TR': 2.000, # duration (sec) per volume
    'volumes': 5, # number of whole-brain 3D volumes / frames
    'sync': 'equal', # character to use as the sync timing event; assumed to come at start of a volume
    'skip': 0, # number of volumes lacking a sync pulse at start of scan (for T1 stabilization)
    'sound': False # in test mode only, play a tone as a reminder of scanner noise
    }

# DISPLAY PARAMETERS FOR THE USER TO CONFIRM
infoDlg = gui.DlgFromDict(MR_settings, title='MRI Settings')

# Create an N-back task
ExpParameters = {
    'TextSize': 0.2
}

# DISPLAY PARAMETERS FOR THE USER TO CONFIRM
infoDlg = gui.DlgFromDict(ExpParameters, title='Experimental Parameters')
ExpectedTotalTime = ExpParameters['IntroOffDuration'] + ExpParameters['NBlocks'] * (ExpParameters['OffDuration'] + ExpParameters['InstrTime'] + (ExpParameters['InterStimulusDelay']+ExpParameters['TimePerTrial'])*ExpParameters['TrialPerBlock'])
print "Expected Duration: %d"%ExpectedTotalTime

TotalDurDLG = gui.Dlg(title='Time')
TotalDurDLG.addText('Total Duration of Experiment')
TotalDurDLG.addText('%d seconds'%ExpectedTotalTime)
TotalDurDLG.show()


# FULL SCREEN WINDOW
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace=u'rgb',
    blendMode=u'avg', useFBO=True,
    )
    
# PARTIAL SCREEN WINDOW
#win = visual.Window(size=[800,600], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
#    monitor=u'testMonitor', color=[0,0,0], colorSpace=u'rgb',
#    blendMode=u'avg', useFBO=True,
#    )

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

ThankYouScreen = visual.TextStim(win=win, ori=0, name='text',
    text=u'It is over.\nThanks',    font=u'Arial',
    pos=[0, 0], height=ExpParameters['TextSize'], wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)

ParallelPort = parallel.ParallelPort(address='0x0378')
# Prepare the data frame used for keeping track of what has been done

Data = pd.DataFrame(columns=('StimSide','Response','Correct','Duration','TurnPoint','ResponseTime'))
StopFlag = False
while StopFlag == False:
    # present odor
    # Which side will the odor be presented on?
    SS = ChooseSide()
    # map the left/right coding of 0/1 onto the appropriate channels
    # decide on the duration for the trial
    DUR = DecDur(Data,SS,StepSize,StartDur)
    
    # Start a timer
    # trigger the odorant
    
    win.callOnFlip(p_port.setData, int(channel))
    # present red cross hair for one second
    # present green cross hair for two seconds
    
    # Record response
    # Map the response to 0/1
    # Was the response correct?
    CC = IsResponseCorrect(SS,RR)

    Data.loc[len(Data.index)+1] = [SS,RR,CC,DUR,-9999]
        # It is not efficient to check the full file each time for turning points.
        # It woudl be better to just check the last trial.
        # Oh well!
        Data = FindTurningPoints(Data)
        StopFlag = FindNumberOfTurnPoints(Data,TurnPointLimit)

# Parallel port info
        if t >= 1.2 and p_port.status == NOT_STARTED:
            # keep track of start time/frame for later
            p_port.tStart = t  # underestimates by a little under one frame
            p_port.frameNStart = frameN  # exact frame index
            p_port.status = STARTED
            win.callOnFlip(p_port.setData, int(channel))
        elif p_port.status == STARTED and t >= (1.2 + (level-win.monitorFramePeriod*0.75)): #most of one frame period left
            p_port.status = STOPPED
            win.callOnFlip(p_port.setData, int(0))