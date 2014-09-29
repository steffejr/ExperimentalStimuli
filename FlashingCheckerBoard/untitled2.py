#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.03), Sat Sep 20 20:39:42 2014
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
expName = u'untitled'  # from the Builder filename that created this script
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
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
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
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
grating1 = visual.GratingStim(win=win, name='grating1',
    tex=u'sqrXsqr', mask=None,
    ori=0, pos=[0, 0], size=[0.7, 0.7], sf=6, phase=0.0,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
grating2 = visual.GratingStim(win=win, name='grating2',
    tex=u'sqrXsqr', mask=None,
    ori=0, pos=[0, 0], size=[0.7, 0.7], sf=6, phase=0.0,
    color=[-1,-1,-1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.2, wrapWidth=None,
    color=u'red', colorSpace=u'rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

RestDuration = 15
OnTimeDuration = 15;
NBlocks = 10;
BlockDur = RestDuration + OnTimeDuration
flashRate = 8 # Hertz
flashPeriod = 1/flashRate #seconds for one B-W cycle (ie 1/Hz)

t = 0

for BlockIndex in range(0,NBlocks,1):
    # Start block with a cross-hair
    ElaspedTime = (BlockIndex*BlockDur) + RestDuration    
    while t < ElaspedTime:
        t = globalClock.getTime()
        text.draw()
        win.flip()
        if event.getKeys(keyList=["escape"]):
            core.quit()    
    ElaspedTime += OnTimeDuration
    while t < ElaspedTime and not 'escape' in event.getKeys():#for 5 secs
        t = globalClock.getTime()
        if (t%flashPeriod) < (flashPeriod/2.0):# (NB more accurate to use number of frames)
            stim = grating1
        else:
            stim=grating2
        
        #stim.setOri(t*rotationRate*360.0)
        stim.draw()
        win.flip()
        if event.getKeys(keyList=["escape"]):
            core.quit()
ElaspedTime = (NBlocks*BlockDur) + RestDuration    
while t < ElaspedTime:
    t = globalClock.getTime()
    text.draw()
    win.flip()
    if event.getKeys(keyList=["escape"]):
        core.quit()   
    
    
# completed 5 repeats of 'BlockLoop'

win.close()
core.quit()
