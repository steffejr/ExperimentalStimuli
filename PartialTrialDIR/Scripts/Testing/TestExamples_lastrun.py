#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Tue Jan  5 16:59:46 2016
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
expName = u'TestExamples'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/PartialTrialDIR/TestExamples.psyexp',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=[800, 600], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='add', useFBO=True,
    units='norm')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
TopUpperLine_2 = visual.Line(win=win, name='TopUpperLine_2',units='norm', 
    start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
    ori=0, pos=[0, 0.65],
    lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
    fillColor='[1,1,-1]', fillColorSpace='rgb',
    opacity=1,depth=-1.0, 
interpolate=True)
UpperText_2 = visual.TextStim(win=win, ori=0, name='UpperText_2',
    text='default text',    font=u'Courier',
    units='norm', pos=[0, 0.4], height=0.2, wrapWidth=1.5,
    color=[0,0,0], colorSpace='rgb', opacity=1,
    depth=-2.0)
UpperBrackets_2 = visual.TextStim(win=win, ori=0, name='UpperBrackets_2',
    text='default text',    font=u'Courier',
    units='norm', pos=[0, 0.4], height=0.2, wrapWidth=1.5,
    color=u'yellow', colorSpace='rgb', opacity=1,
    depth=-3.0)
BotUpperLine_2 = visual.Line(win=win, name='BotUpperLine_2',units='norm', 
    start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
    ori=0, pos=[0, 0.15],
    lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
    fillColor='yellow', fillColorSpace='rgb',
    opacity=1,depth=-4.0, 
interpolate=True)
TopLowerLine_2 = visual.Line(win=win, name='TopLowerLine_2',units='norm', 
    start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
    ori=0, pos=[0, -0.15],
    lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
    fillColor='cyan', fillColorSpace='rgb',
    opacity=1,depth=-5.0, 
interpolate=True)
LowerText_2 = visual.TextStim(win=win, ori=0, name='LowerText_2',
    text='default text',    font=u'Courier',
    units='norm', pos=[0, -0.4], height=0.2, wrapWidth=2,
    color=[0,0,0], colorSpace='rgb', opacity=1,
    depth=-6.0)
LowerBrackets_2 = visual.TextStim(win=win, ori=0, name='LowerBrackets_2',
    text=u'      { }    ',    font=u'Courier',
    units='norm', pos=[0, -0.4], height=0.2, wrapWidth=None,
    color=u'cyan', colorSpace='rgb', opacity=1,
    depth=-7.0)
BotLowerLine_2 = visual.Line(win=win, name='BotLowerLine_2',units='norm', 
    start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
    ori=0, pos=[0, -0.65],
    lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
    fillColor='cyan', fillColorSpace='rgb',
    opacity=1,depth=-8.0, 
interpolate=True)
TrialCrossHair_2 = visual.TextStim(win=win, ori=0, name='TrialCrossHair_2',
    text='+',    font='Arial',
    units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
    color='green', colorSpace='rgb', opacity=1,
    depth=-9.0)
RestCrossHair_2 = visual.TextStim(win=win, ori=0, name='RestCrossHair_2',
    text='+',    font='Arial',
    units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-10.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock 
frameN = -1
routineTimer.add(13.000000)
# update component parameters for each repeat
UpperText_2.setText(u' L K R G M X ')
UpperBrackets_2.setText(u'  {         }')
LowerText_2.setText(u'btygqj')
KeyboardResp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
KeyboardResp_2.status = NOT_STARTED
# keep track of which components have finished
trialComponents = []
trialComponents.append(ISI)
trialComponents.append(TopUpperLine_2)
trialComponents.append(UpperText_2)
trialComponents.append(UpperBrackets_2)
trialComponents.append(BotUpperLine_2)
trialComponents.append(TopLowerLine_2)
trialComponents.append(LowerText_2)
trialComponents.append(LowerBrackets_2)
trialComponents.append(BotLowerLine_2)
trialComponents.append(TrialCrossHair_2)
trialComponents.append(RestCrossHair_2)
trialComponents.append(KeyboardResp_2)
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "trial"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TopUpperLine_2* updates
    if t >= 0 and TopUpperLine_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        TopUpperLine_2.tStart = t  # underestimates by a little under one frame
        TopUpperLine_2.frameNStart = frameN  # exact frame index
        TopUpperLine_2.setAutoDraw(True)
    if TopUpperLine_2.status == STARTED and t >= (0 + (13-win.monitorFramePeriod*0.75)): #most of one frame period left
        TopUpperLine_2.setAutoDraw(False)
    
    # *UpperText_2* updates
    if t >= 0 and UpperText_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        UpperText_2.tStart = t  # underestimates by a little under one frame
        UpperText_2.frameNStart = frameN  # exact frame index
        UpperText_2.setAutoDraw(True)
    if UpperText_2.status == STARTED and t >= (0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        UpperText_2.setAutoDraw(False)
    
    # *UpperBrackets_2* updates
    if t >= 0.0 and UpperBrackets_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        UpperBrackets_2.tStart = t  # underestimates by a little under one frame
        UpperBrackets_2.frameNStart = frameN  # exact frame index
        UpperBrackets_2.setAutoDraw(True)
    if UpperBrackets_2.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        UpperBrackets_2.setAutoDraw(False)
    
    # *BotUpperLine_2* updates
    if t >= 0.0 and BotUpperLine_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        BotUpperLine_2.tStart = t  # underestimates by a little under one frame
        BotUpperLine_2.frameNStart = frameN  # exact frame index
        BotUpperLine_2.setAutoDraw(True)
    if BotUpperLine_2.status == STARTED and t >= (0.0 + (13-win.monitorFramePeriod*0.75)): #most of one frame period left
        BotUpperLine_2.setAutoDraw(False)
    
    # *TopLowerLine_2* updates
    if t >= 0.0 and TopLowerLine_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        TopLowerLine_2.tStart = t  # underestimates by a little under one frame
        TopLowerLine_2.frameNStart = frameN  # exact frame index
        TopLowerLine_2.setAutoDraw(True)
    if TopLowerLine_2.status == STARTED and t >= (0.0 + (13-win.monitorFramePeriod*0.75)): #most of one frame period left
        TopLowerLine_2.setAutoDraw(False)
    
    # *LowerText_2* updates
    if t >= 7 and LowerText_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        LowerText_2.tStart = t  # underestimates by a little under one frame
        LowerText_2.frameNStart = frameN  # exact frame index
        LowerText_2.setAutoDraw(True)
    if LowerText_2.status == STARTED and t >= (7 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        LowerText_2.setAutoDraw(False)
    
    # *LowerBrackets_2* updates
    if t >= 7 and LowerBrackets_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        LowerBrackets_2.tStart = t  # underestimates by a little under one frame
        LowerBrackets_2.frameNStart = frameN  # exact frame index
        LowerBrackets_2.setAutoDraw(True)
    if LowerBrackets_2.status == STARTED and t >= (7 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        LowerBrackets_2.setAutoDraw(False)
    
    # *BotLowerLine_2* updates
    if t >= 0.0 and BotLowerLine_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        BotLowerLine_2.tStart = t  # underestimates by a little under one frame
        BotLowerLine_2.frameNStart = frameN  # exact frame index
        BotLowerLine_2.setAutoDraw(True)
    if BotLowerLine_2.status == STARTED and t >= (0.0 + (13-win.monitorFramePeriod*0.75)): #most of one frame period left
        BotLowerLine_2.setAutoDraw(False)
    
    # *TrialCrossHair_2* updates
    if t >= 0 and TrialCrossHair_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        TrialCrossHair_2.tStart = t  # underestimates by a little under one frame
        TrialCrossHair_2.frameNStart = frameN  # exact frame index
        TrialCrossHair_2.setAutoDraw(True)
    if TrialCrossHair_2.status == STARTED and t >= (0 + (9-win.monitorFramePeriod*0.75)): #most of one frame period left
        TrialCrossHair_2.setAutoDraw(False)
    
    # *RestCrossHair_2* updates
    if t >= 9 and RestCrossHair_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        RestCrossHair_2.tStart = t  # underestimates by a little under one frame
        RestCrossHair_2.frameNStart = frameN  # exact frame index
        RestCrossHair_2.setAutoDraw(True)
    if RestCrossHair_2.status == STARTED and t >= (9 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
        RestCrossHair_2.setAutoDraw(False)
    
    # *KeyboardResp_2* updates
    if t >= 7 and KeyboardResp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        KeyboardResp_2.tStart = t  # underestimates by a little under one frame
        KeyboardResp_2.frameNStart = frameN  # exact frame index
        KeyboardResp_2.status = STARTED
        # keyboard checking is just starting
        KeyboardResp_2.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if KeyboardResp_2.status == STARTED and t >= (7 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        KeyboardResp_2.status = STOPPED
    if KeyboardResp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            KeyboardResp_2.keys.extend(theseKeys)  # storing all keys
            KeyboardResp_2.rt.append(KeyboardResp_2.clock.getTime())
            # was this 'correct'?
            if (KeyboardResp_2.keys == str(Correct)) or (KeyboardResp_2.keys == Correct):
                KeyboardResp_2.corr = 1
            else:
                KeyboardResp_2.corr = 0
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
if KeyboardResp_2.keys in ['', [], None]:  # No response was made
   KeyboardResp_2.keys=None
   # was no response the correct answer?!
   if str(Correct).lower() == 'none': KeyboardResp_2.corr = 1  # correct non-response
   else: KeyboardResp_2.corr = 0  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('KeyboardResp_2.keys',KeyboardResp_2.keys)
thisExp.addData('KeyboardResp_2.corr', KeyboardResp_2.corr)
if KeyboardResp_2.keys != None:  # we had a response
    thisExp.addData('KeyboardResp_2.rt', KeyboardResp_2.rt)
thisExp.nextEntry()
win.close()
core.quit()
