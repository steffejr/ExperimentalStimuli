#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.03), Tue Sep  8 21:08:42 2015
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
expName = 'LetSternberg'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup filename for saving
filename = 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/LetterSternberg/LetSternberg.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=[800,600], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
LetterStimulus = visual.TextStim(win=win, ori=0, name='LetterStimulus',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
BlankRetention = visual.TextStim(win=win, ori=0, name='BlankRetention',
    text=' ',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
Probe = visual.TextStim(win=win, ori=0, name='Probe',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
BlankITI = visual.TextStim(win=win, ori=0, name='BlankITI',
    text=' ',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method=u'sequential', 
    extraInfo=expInfo, originPath=u'/Users/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/LetterSternberg/LetSternberg.psyexp',
    trialList=data.importConditions('/Users/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/LetterSternberg/LetterSternbergConditions.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        print paramName
        exec(paramName + '= thisTrial.' + paramName)
# Need to add trial times
# probe letters are not being presented.


for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            print paramName
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    LetterStimulus.setText(StimLetters)
    Probe.setText(ProbeLetter)
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    trialComponents.append(LetterStimulus)
    trialComponents.append(BlankRetention)
    trialComponents.append(ProbeLetter)
    trialComponents.append(BlankITI)
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
        
        # *LetterStimulus* updates
        if t >= 0.0 and LetterStimulus.status == NOT_STARTED:
            # keep track of start time/frame for later
            LetterStimulus.tStart = t  # underestimates by a little under one frame
            LetterStimulus.frameNStart = frameN  # exact frame index
            LetterStimulus.setAutoDraw(True)
        elif LetterStimulus.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            LetterStimulus.setAutoDraw(False)
        
        # *BlankRetention* updates
        if t >= 3 and BlankRetention.status == NOT_STARTED:
            # keep track of start time/frame for later
            BlankRetention.tStart = t  # underestimates by a little under one frame
            BlankRetention.frameNStart = frameN  # exact frame index
            BlankRetention.setAutoDraw(True)
        elif BlankRetention.status == STARTED and t >= (3 + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
            BlankRetention.setAutoDraw(False)
        
        # *ProbeLetter* updates
        if t >= 8 and ProbeLetter.status == NOT_STARTED:
            # keep track of start time/frame for later
            Probe.tStart = t  # underestimates by a little under one frame
            Probe.frameNStart = frameN  # exact frame index
            Probe.setAutoDraw(True)
        elif Probe.status == STARTED and t >= (8 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            Probe.setAutoDraw(False)
        
        # *BlankITI* updates
        if t >= 0.0 and BlankITI.status == NOT_STARTED:
            # keep track of start time/frame for later
            BlankITI.tStart = t  # underestimates by a little under one frame
            BlankITI.frameNStart = frameN  # exact frame index
            BlankITI.setAutoDraw(True)
        elif BlankITI.status == STARTED and t >= (0.0 + (ITI-win.monitorFramePeriod*0.75)): #most of one frame period left
            BlankITI.setAutoDraw(False)
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
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials'

win.close()
core.quit()
