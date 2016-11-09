#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.01), Mon Jan 25 07:56:04 2016
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'SetupDisplay'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

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

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=[800, 600], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='add', useFBO=True,
    units='use preferences')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
TopUpperLine = visual.Line(win=win, name='TopUpperLine',units='norm', 
    start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
    ori=0, pos=[0, 0.65],
    lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
    fillColor='[1,1,-1]', fillColorSpace='rgb',
    opacity=1,depth=-1.0, 
interpolate=True)
UpperText = visual.TextStim(win=win, ori=0, name='UpperText',
    text='default text',    font='Courier',
    units='norm', pos=[0, 0.4], height=0.2, wrapWidth=1.5,
    color=[0,0,0], colorSpace='rgb', opacity=1,
    depth=-2.0)
UpperBrackets = visual.TextStim(win=win, ori=0, name='UpperBrackets',
    text='default text',    font='Courier',
    units='norm', pos=[0, 0.4], height=0.2, wrapWidth=1.5,
    color='yellow', colorSpace='rgb', opacity=1,
    depth=-3.0)
BotUpperLine = visual.Line(win=win, name='BotUpperLine',units='norm', 
    start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
    ori=0, pos=[0, 0.15],
    lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
    fillColor='yellow', fillColorSpace='rgb',
    opacity=1,depth=-4.0, 
interpolate=True)
TopLowerLine = visual.Line(win=win, name='TopLowerLine',units='norm', 
    start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
    ori=0, pos=[0, -0.15],
    lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
    fillColor='cyan', fillColorSpace='rgb',
    opacity=1,depth=-5.0, 
interpolate=True)
LowerText = visual.TextStim(win=win, ori=0, name='LowerText',
    text='default text',    font='Courier',
    units='norm', pos=[0, -0.4], height=0.2, wrapWidth=2,
    color=[0,0,0], colorSpace='rgb', opacity=1,
    depth=-6.0)
LowerBrackets = visual.TextStim(win=win, ori=0, name='LowerBrackets',
    text='+',    font='Courier',
    units='norm', pos=[0, -0.4], height=0.2, wrapWidth=None,
    color='cyan', colorSpace='rgb', opacity=1,
    depth=-7.0)
BotLowerLine = visual.Line(win=win, name='BotLowerLine',units='norm', 
    start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
    ori=0, pos=[0, -0.65],
    lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
    fillColor='cyan', fillColorSpace='rgb',
    opacity=1,depth=-8.0, 
interpolate=True)
TrialCrossHair = visual.TextStim(win=win, ori=0, name='TrialCrossHair',
    text='+',    font='Arial',
    units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
    color='green', colorSpace='rgb', opacity=1,
    depth=-9.0)
RestCrossHair = visual.TextStim(win=win, ori=0, name='RestCrossHair',
    text='+',    font='Arial',
    units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'../ExperimentalTrials/Test72Trials_6Loads.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    UpperText.setText(StimSet)
    UpperBrackets.setText(UpBrack)
    LowerText.setText(ProbeLet)
    KeyboardResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyboardResp.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    trialComponents.append(TopUpperLine)
    trialComponents.append(UpperText)
    trialComponents.append(UpperBrackets)
    trialComponents.append(BotUpperLine)
    trialComponents.append(TopLowerLine)
    trialComponents.append(LowerText)
    trialComponents.append(LowerBrackets)
    trialComponents.append(BotLowerLine)
    trialComponents.append(TrialCrossHair)
    trialComponents.append(RestCrossHair)
    trialComponents.append(KeyboardResp)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TopUpperLine* updates
        if t >= 0 and TopUpperLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopUpperLine.tStart = t  # underestimates by a little under one frame
            TopUpperLine.frameNStart = frameN  # exact frame index
            TopUpperLine.setAutoDraw(True)
        if TopUpperLine.status == STARTED and t >= (0 + (TrialITIDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopUpperLine.setAutoDraw(False)
        
        # *UpperText* updates
        if t >= 0 and UpperText.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperText.tStart = t  # underestimates by a little under one frame
            UpperText.frameNStart = frameN  # exact frame index
            UpperText.setAutoDraw(True)
        if UpperText.status == STARTED and t >= (0 + (StimDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperText.setAutoDraw(False)
        
        # *UpperBrackets* updates
        if t >= 0.0 and UpperBrackets.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBrackets.tStart = t  # underestimates by a little under one frame
            UpperBrackets.frameNStart = frameN  # exact frame index
            UpperBrackets.setAutoDraw(True)
        if UpperBrackets.status == STARTED and t >= (0.0 + (StimDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBrackets.setAutoDraw(False)
        
        # *BotUpperLine* updates
        if t >= 0.0 and BotUpperLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotUpperLine.tStart = t  # underestimates by a little under one frame
            BotUpperLine.frameNStart = frameN  # exact frame index
            BotUpperLine.setAutoDraw(True)
        if BotUpperLine.status == STARTED and t >= (0.0 + (TrialITIDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotUpperLine.setAutoDraw(False)
        
        # *TopLowerLine* updates
        if t >= 0.0 and TopLowerLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopLowerLine.tStart = t  # underestimates by a little under one frame
            TopLowerLine.frameNStart = frameN  # exact frame index
            TopLowerLine.setAutoDraw(True)
        if TopLowerLine.status == STARTED and t >= (0.0 + (TrialITIDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopLowerLine.setAutoDraw(False)
        
        # *LowerText* updates
        if t >= ProbeStart and LowerText.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerText.tStart = t  # underestimates by a little under one frame
            LowerText.frameNStart = frameN  # exact frame index
            LowerText.setAutoDraw(True)
        if LowerText.status == STARTED and t >= (ProbeStart + (ProbeDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerText.setAutoDraw(False)
        
        # *LowerBrackets* updates
        if t >= ProbeStart and LowerBrackets.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerBrackets.tStart = t  # underestimates by a little under one frame
            LowerBrackets.frameNStart = frameN  # exact frame index
            LowerBrackets.setAutoDraw(True)
        if LowerBrackets.status == STARTED and t >= (ProbeStart + (ProbeDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerBrackets.setAutoDraw(False)
        
        # *BotLowerLine* updates
        if t >= 0.0 and BotLowerLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotLowerLine.tStart = t  # underestimates by a little under one frame
            BotLowerLine.frameNStart = frameN  # exact frame index
            BotLowerLine.setAutoDraw(True)
        if BotLowerLine.status == STARTED and t >= (0.0 + (TrialITIDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotLowerLine.setAutoDraw(False)
        
        # *TrialCrossHair* updates
        if t >= 0 and TrialCrossHair.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialCrossHair.tStart = t  # underestimates by a little under one frame
            TrialCrossHair.frameNStart = frameN  # exact frame index
            TrialCrossHair.setAutoDraw(True)
        if TrialCrossHair.status == STARTED and t >= (0 + (TrialDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            TrialCrossHair.setAutoDraw(False)
        
        # *RestCrossHair* updates
        if t >= TrialDur and RestCrossHair.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair.tStart = t  # underestimates by a little under one frame
            RestCrossHair.frameNStart = frameN  # exact frame index
            RestCrossHair.setAutoDraw(True)
        if RestCrossHair.status == STARTED and t >= (TrialDur + (ITI-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair.setAutoDraw(False)
        
        # *KeyboardResp* updates
        if t >= ProbeStart and KeyboardResp.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyboardResp.tStart = t  # underestimates by a little under one frame
            KeyboardResp.frameNStart = frameN  # exact frame index
            KeyboardResp.status = STARTED
            # keyboard checking is just starting
            KeyboardResp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if KeyboardResp.status == STARTED and t >= (ProbeStart + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyboardResp.status = STOPPED
        if KeyboardResp.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                KeyboardResp.keys.extend(theseKeys)  # storing all keys
                KeyboardResp.rt.append(KeyboardResp.clock.getTime())
                # was this 'correct'?
                if (KeyboardResp.keys == str(Correct)) or (KeyboardResp.keys == Correct):
                    KeyboardResp.corr = 1
                else:
                    KeyboardResp.corr = 0
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(1)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyboardResp.keys in ['', [], None]:  # No response was made
       KeyboardResp.keys=None
       # was no response the correct answer?!
       if str(Correct).lower() == 'none': KeyboardResp.corr = 1  # correct non-response
       else: KeyboardResp.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('KeyboardResp.keys',KeyboardResp.keys)
    trials.addData('KeyboardResp.corr', KeyboardResp.corr)
    if KeyboardResp.keys != None:  # we had a response
        trials.addData('KeyboardResp.rt', KeyboardResp.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

win.close()
core.quit()
