#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.06), Mon Sep 21 20:49:45 2015
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
from numpy import arange
# Store info about the experiment session
expName = 'PartialTrialDIR'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u'999'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup filename for saving
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

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=[800, 600], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='add', useFBO=True,
    units='use preferences')
    
#win = visual.Window(size=(1200, 1920), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
#    monitor=u'testMonitor', color=[0,0,0], colorSpace=u'rgb',
#    blendMode=u'add', useFBO=True,
#    units=u'use preferences')

# ######################################################################################
LetLen = 6
LetWidth = 0.8 # what portion of the screen to use
LetPos = arange(-LetWidth,LetWidth+0.001,(LetWidth*2)/(LetLen-1))
LetSize = 0.2
UpperLetTopPos = 0.7
LowerLetTopPos = -0.7
UpperLetColor = [0,0,0] # This is grey
UpperBracketColor = [1,1,-1] # This is yellow

LetStartTime = 0
StimDur = 0.25
RetDur = 4

ProbeStartTime = 2 #StimDur + RetDur
ProbeDur = 2
LowerLetColor = [0,0,0] # This is grey
LowerBracketColor = [-1,0.875,0.875] # cyan

# The lines above and below the upper letters
UpperLineColor = [1,1,-1]
UpperLineWidth = 2
UpperTopLetLinePos = UpperLetTopPos + 1.5*(LetSize/2)
UpperBotLetLinePos = UpperLetTopPos - 1.5*(LetSize/2)
UpperTopLineDur = 2 # Duration of the line
UpperBotLineDur = 2 # Duration of the line

# The lines above and below the lower letters
LowerLineColor = [-1,0.875,0.875] # This is supposed to be cyan
LowerLineWidth = 2
LowerTopLetLinePos = LowerLetTopPos + 1.5*(LetSize/2)
LowerBotLetLinePos = LowerLetTopPos - 1.5*(LetSize/2)
LowerTopLineDur = 2 # Duration of the line
LowerBotLineDur = 2 # Duration of the line

# ######################################################################################

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Stimulus = visual.TextStim(win=win, ori=0, name='Stimulus',
    text='default text',    font=u'Arial',
    units=u'norm', pos=[0, 0.7], height=LetSize, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
Probe = visual.TextStim(win=win, ori=0, name='Probe',
    text='default text',    font=u'Arial',
    units=u'norm', pos=[0, 0.7], height=LetSize, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
CrossHair = visual.TextStim(win=win, ori=0, name='CrossHair',
    text='+',    font=u'Arial',
    units=u'norm', pos=[0, 0], height=LetSize, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0) 
    
UpperTopLine = visual.Line(win=win, name='UpperTopLine',units=u'norm', 
    start=(-[-2, 0.9][0]/2.0, 0), end=(+[-2, 0.9][0]/2.0, 0),
    ori=0, pos=[0, UpperTopLetLinePos],
    lineWidth=UpperLineWidth, lineColor=UpperLineColor, lineColorSpace=u'rgb',
    fillColor=[1,1,1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True)
UpperBotLine = visual.Line(win=win, name='UpperBotLine',units=u'norm', 
    start=(-[-2, 0.9][0]/2.0, 0), end=(+[-2, 0.9][0]/2.0, 0),
    ori=0, pos=[0, UpperBotLetLinePos],
    lineWidth=UpperLineWidth, lineColor=UpperLineColor, lineColorSpace=u'rgb',
    fillColor=[1,1,1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True)
LowerTopLine = visual.Line(win=win, name='LowerTopLine',units=u'norm', 
    start=(-[-2, 0.9][0]/2.0, 0), end=(+[-2, 0.9][0]/2.0, 0),
    ori=0, pos=[0, LowerTopLetLinePos],
    lineWidth=LowerLineWidth, lineColor=LowerLineColor, lineColorSpace=u'rgb',
    fillColor=[1,1,1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True)
LowerBotLine = visual.Line(win=win, name='LowerBotLine',units=u'norm', 
    start=(-[-2, 0.9][0]/2.0, 0), end=(+[-2, 0.9][0]/2.0, 0),
    ori=0, pos=[0, LowerBotLetLinePos],
    lineWidth=LowerLineWidth, lineColor=LowerLineColor, lineColorSpace=u'rgb',
    fillColor=[1,1,1], fillColorSpace=u'rgb',
    opacity=1,interpolate=True)
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method=u'sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'TrialListShort1.xlsx'),
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
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    ###Stimulus.setText(StimSet)
    LetCount = 0
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    trialComponents.append(Stimulus)
    trialComponents.append(UpperTopLine)
    trialComponents.append(UpperBotLine)
    trialComponents.append(LowerTopLine)
    trialComponents.append(LowerBotLine)
    trialComponents.append(CrossHair)
    trialComponents.append(Probe)
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
        
        # *Stimulus* updates
        if t >= 0.5 and Stimulus.status == NOT_STARTED:
            # keep track of start time/frame for later
            Stimulus.tStart = t  # underestimates by a little under one frame
            Stimulus.frameNStart = frameN  # exact frame index
            #Stimulus.setAutoDraw(True)
            #print StimSet
            LetCount = -1
            for i in range(0,len(StimSet),1):
                if (StimSet[i] != '{')&(StimSet[i] !='}'):
                    LetCount = LetCount + 1
                    Stimulus.setColor(UpperLetColor,'rgb')
                    Stimulus.setText(StimSet[i])
                    Stimulus.setPos([LetPos[LetCount],UpperLetTopPos])
                    Stimulus.draw()
                elif StimSet[i] == '{':
                    Stimulus.setText(StimSet[i])
                    Stimulus.setColor(UpperBracketColor,'rgb')
                    # Check to see if the left bracket is the first character
                    if LetCount == -1:
                        Stimulus.setPos([LetPos[0]-0.1,UpperLetTopPos])
                    else:
                        Stimulus.setPos([LetPos[LetCount+1]-0.1,UpperLetTopPos])
                    Stimulus.draw()
                elif StimSet[i] == '}':
                    Stimulus.setText(StimSet[i])
                    Stimulus.setColor(UpperBracketColor,'rgb')
                    Stimulus.setPos([LetPos[LetCount]+0.1,UpperLetTopPos])
                    Stimulus.draw()
        elif Stimulus.status == STARTED and t >= (0.5 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            # When the stimulus set time is over the letters need to be removed!
            # HOW????
            Stimulus.setAutoDraw(False)
        if t >= 1.0 and CrossHair.status == NOT_STARTED:
            # keep track of start time/frame for later
            CrossHair.tStart = t  # underestimates by a little under one frame
            CrossHair.frameNStart = frameN  # exact frame index
            CrossHair.setAutoDraw(True)
        if CrossHair.status == STARTED and t >= (1 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            CrossHair.setAutoDraw(False)
        # *PROBE* updates
        if t >= 3 and Probe.status == NOT_STARTED:
            # keep track of start time/frame for later
            Probe.tStart = t  # underestimates by a little under one frame
            Probe.frameNStart = frameN  # exact frame index
            #Stimulus.setAutoDraw(True)
            #print StimSet
            ProCount = -1
            for i in range(0,len(ProbeLet),1):
                if (ProbeLet[i] != '{')&(ProbeLet[i] !='}'):
                    ProCount = ProCount + 1
                    Probe.setColor(UpperLetColor,'rgb')
                    Probe.setText(ProbeLet[i])
                    Probe.setPos([LetPos[ProCount],LowerLetTopPos])
                    Probe.draw()
                elif ProbeLet[i] == '{':
                    Probe.setText(ProbeLet[i])
                    Probe.setColor(LowerBracketColor,'rgb')
                    # Check to see if the left bracket is the first character
                    if LetCount == -1:
                        Probe.setPos([LetPos[0]-0.1,LowerLetTopPos])
                    else:
                        Probe.setPos([LetPos[ProCount+1]-0.1,LowerLetTopPos])
                    Probe.draw()
                elif StimSet[i] == '}':
                    Probe.setText(ProbeLet[i])
                    Probe.setColor(LowerBracketColor,'rgb')
                    Probe.setPos([LetPos[ProCount]+0.1,LowerLetTopPos])
                    Probe.draw()
        elif Probe.status == STARTED and t >= (3 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            Probe.setAutoDraw(False)
        # *UpperTopLine* updates
        if t >= 0.0 and UpperTopLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperTopLine.tStart = t  # underestimates by a little under one frame
            UpperTopLine.frameNStart = frameN  # exact frame index
            UpperTopLine.setAutoDraw(True)
        elif UpperTopLine.status == STARTED and t >= (0.0 + (UpperTopLineDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperTopLine.setAutoDraw(False)
        
        # *UpperBotLine* updates
        if t >= 0.0 and UpperBotLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBotLine.tStart = t  # underestimates by a little under one frame
            UpperBotLine.frameNStart = frameN  # exact frame index
            UpperBotLine.setAutoDraw(True)
        elif UpperBotLine.status == STARTED and t >= (0.0 + (UpperBotLineDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBotLine.setAutoDraw(False)

        # *LowerTopLine* updates
        if t >= 0.0 and LowerTopLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerTopLine.tStart = t  # underestimates by a little under one frame
            LowerTopLine.frameNStart = frameN  # exact frame index
            LowerTopLine.setAutoDraw(True)
        elif LowerTopLine.status == STARTED and t >= (0.0 + (LowerTopLineDur-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerTopLine.setAutoDraw(False)
        
        # *LowerBotLine* updates
        if t >= 0.0 and LowerBotLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerBotLine.tStart = t  # underestimates by a little under one frame
            LowerBotLine.frameNStart = frameN  # exact frame index
            LowerBotLine.setAutoDraw(True)
        elif LowerBotLine.status == STARTED and t >= (0.0 + (LowerBotLineDur-win.monitorFramePeriod*0.75)): #most of one frame period left
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
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

win.close()
core.quit()
