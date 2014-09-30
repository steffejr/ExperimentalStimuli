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
from psychopy.hardware.emulator import launchScan

# EXPERIMENTAL INFORMATION
expName = u'FlashCB'  # <<< This is where you specify the name of the experiment which makes it easier to differentiate the results files.
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

# Initialize components for Routine "trial"

ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# PREPARE THE STIMULI
grating1 = visual.GratingStim(win=win, name='grating1',
    tex=u'sqrXsqr', mask=None,
    ori=0, pos=[0, 0], size=[0.9, 0.9], sf=5, phase=0.0,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)

grating2 = visual.GratingStim(win=win, name='grating2',
    tex=u'sqrXsqr', mask=None,
    ori=0, pos=[0, 0], size=[0.9, 0.9], sf=5, phase=0.0,
    color=[-1,-1,-1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-2.0)

CrossHair = visual.TextStim(win=win, ori=0, name='text',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.2, wrapWidth=None,
    color=u'red', colorSpace=u'rgb', opacity=1,
    depth=0.0)
   

# TIMERS
globalClock = core.CountdownTimer()
ElapsedTimeClock = core.Clock()
FlashClock = core.Clock()
# EXPERIMENTAL PARAMETERS USED 
ExpParamaters = {
    'IntroOffDuration': 5,
    'OffDuration' : 5,
    'OnDuration' : 5,
    'NBlocks' : 2,
    'flashRate' : 4 # Hertz
    }
# DISPLAY PARAMETERS FOR THE USER TO CONFIRM
infoDlg = gui.DlgFromDict(ExpParamaters, title='Experimental Parameters')

# CALCULATED PARAMETERS
flashPeriod = 1/ExpParamaters['flashRate'] #seconds for one B-W cycle (ie 1/Hz)
BlockDur = ExpParamaters['OffDuration'] + ExpParamaters['OnDuration']

# PRESENT THE SCREEN TO WAIT FOR THE MRI TRIGGER
vol = launchScan(win, MR_settings,  mode='Scan')
#vol = launchScan(win, MR_settings, globalClock=globalClock)

# Reset the clocks
globalClock.reset()
ElapsedTimeClock.reset()
globalClock.add(ExpParamaters['IntroOffDuration'])
FlashClock.reset()
ElapsedTime = 0

# INTRO OFF PERIOD
# Prepare the screen before the timing sequence starts
CrossHair.draw()
win.flip()
while globalClock.getTime() > 0:
    if event.getKeys(keyList=["escape"]):
        core.quit()    
ElapsedTime += ExpParamaters['IntroOffDuration']

# CYCLE OVER BLOCKS
for i in range(0,ExpParamaters['NBlocks'],1):
    # ON BLOCK
    # Write to the file when this event started
    thisExp.addData('Event','StartOnBlock_%03d'%(i+1))
    thisExp.addData('ExpectedElapsedTime',ElapsedTime)
    thisExp.addData('ActualElapsedTime',ElapsedTimeClock.getTime())
    thisExp.nextEntry()

    # reset the global clock, than add the needed time to it
    globalClock.add(ExpParamaters['OnDuration'])
    # reset the clock used for the flashing
    FlashClock.reset()
    while globalClock.getTime() > 0:
        if (FlashClock.getTime()%flashPeriod) < (flashPeriod/2.0):# (NB more accurate to use number of frames)
            stim = grating1
        else:
            stim = grating2
        
        #stim.setOri(t*rotationRate*360.0)
        stim.draw()
        win.flip()
        if event.getKeys(keyList=["escape"]):
            core.quit()
    # update the expected elapsed time
    ElapsedTime += ExpParamaters['OnDuration']
    # OFF BLOCK
    # Write to the file whenthis event started
    thisExp.addData('Event','StartOffBlock_%03d'%(i+1))
    thisExp.addData('ExpectedElapsedTime',ElapsedTime)
    thisExp.addData('ActualElapsedTime',ElapsedTimeClock.getTime())
    thisExp.nextEntry()
    # Present the off period now
    globalClock.add(ExpParamaters['OffDuration'])
    CrossHair.draw()
    win.flip()
    while globalClock.getTime() > 0:
        if event.getKeys(keyList=["escape"]):
            core.quit() 
    # update the expected elapsed time
    ElapsedTime += ExpParamaters['OffDuration']

win.close()
core.quit()
