#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.06), Thu Sep 17 20:50:30 2015
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

# Store info about the experiment session
expName = u'PartialTrialDIR'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u'999'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup filename for saving
filename = 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/PartialTrialDIR/PartialTrialDIR.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=[600, 400], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace=u'rgb',
    blendMode=u'avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
UpperTopLine = visual.Line(win=win, name='UpperTopLine',
    start=(-[0.95, 0.95][0]/2.0, 0), end=(+[0.95, 0.95][0]/2.0, 0),
    ori=0, pos=[0, 0.45],
    lineWidth=1, lineColor=u'yellow', lineColorSpace=u'rgb',
    fillColor=u'yellow', fillColorSpace=u'rgb',
    opacity=1,interpolate=True)
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Stimulus = visual.TextStim(win=win, ori=0, name='Stimulus',
    text='default text',    font=u'Arial',
    pos=[0, 0.7], height=0.2, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-2.0)
UpperBracket = visual.TextStim(win=win, ori=0, name='UpperBracket',
    text='default text',    font=u'Arial',
    pos=[0,0.7], height=0.2, wrapWidth=None,
    color=u'yellow', colorSpace=u'rgb', opacity=1,
    depth=-3.0)
LowerTopLine = visual.Line(win=win, name='LowerTopLine',
    start=(-[0.95, 0.95][0]/2.0, 0), end=(+[0.95, 0.95][0]/2.0, 0),
    ori=0, pos=[0.0, 0.9],
    lineWidth=1, lineColor=u'yellow', lineColorSpace=u'rgb',
    fillColor=u'yellow', fillColorSpace=u'rgb',
    opacity=1,interpolate=True)
Probe = visual.TextStim(win=win, ori=0, name='Probe',
    text='default text',    font=u'Arial',
    pos=[0, -0.50], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=-5.0)
TrialCrossHair = visual.TextStim(win=win, ori=0, name='TrialCrossHair',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'green', colorSpace=u'rgb', opacity=1,
    depth=-7.0)
ITICrossHair = visual.TextStim(win=win, ori=0, name='ITICrossHair',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'red', colorSpace=u'rgb', opacity=1,
    depth=-8.0)
UpperBotLine = visual.Line(win=win, name='UpperBotLine',
    start=(-[0.95, 0.95][0]/2.0, 0), end=(+[0.95, 0.95][0]/2.0, 0),
    ori=0, pos=[0, -0.450],
    lineWidth=1, lineColor=u'cyan', lineColorSpace=u'rgb',
    fillColor=u'cyan', fillColorSpace=u'rgb',
    opacity=1,interpolate=True)
LowerBotLine = visual.Line(win=win, name='LowerBotLine',
    start=(-[0.95, 0.95][0]/2.0, 0), end=(+[0.95, 0.95][0]/2.0, 0),
    ori=0, pos=[0, -0.9],
    lineWidth=1, lineColor=u'cyan', lineColorSpace=u'rgb',
    fillColor=u'cyan', fillColorSpace=u'rgb',
    opacity=1,interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method=u'sequential', 
    extraInfo=expInfo, originPath=u'/Users/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/PartialTrialDIR/PartialTrialDIR.psyexp',
    trialList=data.importConditions(u'PartialTrial1.xlsx'),
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
    Stimulus.setText(StimSet)
    UpperBracket.setText(UpBrack)
    Probe.setText(ProbeLet)
    Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    Resp.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(UpperTopLine)
    trialComponents.append(ISI)
    trialComponents.append(Stimulus)
    trialComponents.append(UpperBracket)
    trialComponents.append(LowerTopLine)
    trialComponents.append(Probe)
    trialComponents.append(Resp)
    trialComponents.append(TrialCrossHair)
    trialComponents.append(ITICrossHair)
    trialComponents.append(UpperBotLine)
    trialComponents.append(LowerBotLine)
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
        
        # *UpperTopLine* updates
        if t >= 0.0 and UpperTopLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperTopLine.tStart = t  # underestimates by a little under one frame
            UpperTopLine.frameNStart = frameN  # exact frame index
            UpperTopLine.setAutoDraw(True)
        elif UpperTopLine.status == STARTED and t >= (0.0 + (TrialDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperTopLine.setAutoDraw(False)
        
        # *Stimulus* updates
        if t >= 0.0 and Stimulus.status == NOT_STARTED:
            # keep track of start time/frame for later
            Stimulus.tStart = t  # underestimates by a little under one frame
            Stimulus.frameNStart = frameN  # exact frame index
            Stimulus.setAutoDraw(True)
        elif Stimulus.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            Stimulus.setAutoDraw(False)
        
        # *UpperBracket* updates
        if t >= 0.0 and UpperBracket.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBracket.tStart = t  # underestimates by a little under one frame
            UpperBracket.frameNStart = frameN  # exact frame index
            UpperBracket.setAutoDraw(True)
        elif UpperBracket.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBracket.setAutoDraw(False)
        
        # *LowerTopLine* updates
        if t >= 0.0 and LowerTopLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerTopLine.tStart = t  # underestimates by a little under one frame
            LowerTopLine.frameNStart = frameN  # exact frame index
            LowerTopLine.setAutoDraw(True)
        elif LowerTopLine.status == STARTED and t >= (0.0 + (TrialDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerTopLine.setAutoDraw(False)
        
        # *Probe* updates
        if t >= ProbeStart and Probe.status == NOT_STARTED:
            # keep track of start time/frame for later
            Probe.tStart = t  # underestimates by a little under one frame
            Probe.frameNStart = frameN  # exact frame index
            Probe.setAutoDraw(True)
        elif Probe.status == STARTED and t >= (ProbeStart + (ProbeDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            Probe.setAutoDraw(False)
        
        # *Resp* updates
        if t >= ProbeStart and Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            Resp.tStart = t  # underestimates by a little under one frame
            Resp.frameNStart = frameN  # exact frame index
            Resp.status = STARTED
            # keyboard checking is just starting
            Resp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif Resp.status == STARTED and t >= (ProbeStart + (RespDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            Resp.status = STOPPED
        if Resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Resp.keys.extend(theseKeys)  # storing all keys
                Resp.rt.append(Resp.clock.getTime())
                # was this 'correct'?
                if (Resp.keys == str(ProbeCor)) or (Resp.keys == ProbeCor):
                    Resp.corr = 1
                else:
                    Resp.corr = 0
        
        # *TrialCrossHair* updates
        if t >= 0.0 and TrialCrossHair.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialCrossHair.tStart = t  # underestimates by a little under one frame
            TrialCrossHair.frameNStart = frameN  # exact frame index
            TrialCrossHair.setAutoDraw(True)
        elif TrialCrossHair.status == STARTED and t >= (0.0 + (TrialDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            TrialCrossHair.setAutoDraw(False)
        
        # *ITICrossHair* updates
        if t >= TrialDur and ITICrossHair.status == NOT_STARTED:
            # keep track of start time/frame for later
            ITICrossHair.tStart = t  # underestimates by a little under one frame
            ITICrossHair.frameNStart = frameN  # exact frame index
            ITICrossHair.setAutoDraw(True)
        elif ITICrossHair.status == STARTED and t >= (TrialDur + (ITIDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            ITICrossHair.setAutoDraw(False)
        
        # *UpperBotLine* updates
        if t >= 0.0 and UpperBotLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBotLine.tStart = t  # underestimates by a little under one frame
            UpperBotLine.frameNStart = frameN  # exact frame index
            UpperBotLine.setAutoDraw(True)
        elif UpperBotLine.status == STARTED and t >= (0.0 + (TrialDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBotLine.setAutoDraw(False)
        
        # *LowerBotLine* updates
        if t >= 0.0 and LowerBotLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerBotLine.tStart = t  # underestimates by a little under one frame
            LowerBotLine.frameNStart = frameN  # exact frame index
            LowerBotLine.setAutoDraw(True)
        elif LowerBotLine.status == STARTED and t >= (0.0 + (TrialDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerBotLine.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
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
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Resp.keys in ['', [], None]:  # No response was made
       Resp.keys=None
       # was no response the correct answer?!
       if str(ProbeCor).lower() == 'none': Resp.corr = 1  # correct non-response
       else: Resp.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('Resp.keys',Resp.keys)
    trials.addData('Resp.corr', Resp.corr)
    if Resp.keys != None:  # we had a response
        trials.addData('Resp.rt', Resp.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

win.close()
core.quit()
