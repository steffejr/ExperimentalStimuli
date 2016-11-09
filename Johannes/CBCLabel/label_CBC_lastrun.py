#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Wed 04 May 2016 02:39:52 PM EDT
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui, parallel
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'label_fr_flo'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/home/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/Johannes/CBCLabel/label_CBC.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1200, 1920), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "temps_reaction1"
temps_reaction1Clock = core.Clock()
text_9 = visual.TextStim(win=win, ori=0, name='text_9',
    text=u'Before starting the experiment, let\u2019s practice. During practice no odor will be delivered.\n\nWhen the red text appears, please exhale. Once the text turns blue, please inhale and press the left arrow button as fast as possible.\n\nPress any button to start.\n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "temps_reaction2"
temps_reaction2Clock = core.Clock()
text_10 = visual.TextStim(win=win, ori=0, name='text_10',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_11 = visual.TextStim(win=win, ori=0, name='text_11',
    text='exhale',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_12 = visual.TextStim(win=win, ori=0, name='text_12',
    text='inhale',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='blue', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_13 = visual.TextStim(win=win, ori=0, name='text_13',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='blue', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text=u'Great!\nNow let\u2019s practice the pleasantness rating.\n\nPlease use the arrow buttons to indicate how pleasant the odor was and confirm by pressing "Enter".\nIf you did not receive any odor, please just press "Enter".\n\nPress a button to start.\n',    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "pleasantness_rating"
pleasantness_ratingClock = core.Clock()
agreabilite = visual.RatingScale(win=win, name='agreabilite', marker='triangle', size=1.0, pos=[0.0, -0.4], low=0, high=10, labels=['very unpleasant', ' very pleasant'], scale='Pleasantness', markerStart='5', showAccept=False)

# Initialize components for Routine "instructions_2"
instructions_2Clock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'Awesome!\nLet\u2019s start the experiment.\nPlease look at the screen. At some point you will receive a very brief description of the next odor. When the text turns red, please exhale. Once the text turns blue, inhale and the odor will be delivered.\n\nIf you smell an odor please press the left arrow button as fast as possible. If you do not smell any odor, do not press any button.\n\nNext, please use the arrow buttons to indicate how pleasant the odor was and confirm by pressing "Enter".\nIf you did not receive any odor, please just press "Enter".\n',    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "isi"
isiClock = core.Clock()
ISI_2 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "stimulus"
stimulusClock = core.Clock()

Label = visual.TextStim(win=win, ori=0, name='Label',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='blue', colorSpace='rgb', opacity=1,
    depth=-3.0)
p_port = parallel.ParallelPort(address=u'/dev/parport0')

# Initialize components for Routine "pleasantness_rating"
pleasantness_ratingClock = core.Clock()
agreabilite = visual.RatingScale(win=win, name='agreabilite', marker='triangle', size=1.0, pos=[0.0, -0.4], low=0, high=10, labels=['very unpleasant', ' very pleasant'], scale='Pleasantness', markerStart='5', showAccept=False)

# Initialize components for Routine "kreuz"
kreuzClock = core.Clock()
text_7 = visual.TextStim(win=win, ori=0, name='text_7',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text_8 = visual.TextStim(win=win, ori=0, name='text_8',
    text='The experiment is over, thank you very much.\n\nPlease press any button to terminate. ',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "temps_reaction1"-------
t = 0
temps_reaction1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
temps_reaction1Components = []
temps_reaction1Components.append(text_9)
temps_reaction1Components.append(key_resp_5)
for thisComponent in temps_reaction1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "temps_reaction1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = temps_reaction1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if t >= 0.0 and text_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_9.tStart = t  # underestimates by a little under one frame
        text_9.frameNStart = frameN  # exact frame index
        text_9.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in temps_reaction1Components:
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

#-------Ending Routine "temps_reaction1"-------
for thisComponent in temps_reaction1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "temps_reaction2"-------
t = 0
temps_reaction2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_6.status = NOT_STARTED
# keep track of which components have finished
temps_reaction2Components = []
temps_reaction2Components.append(text_10)
temps_reaction2Components.append(text_11)
temps_reaction2Components.append(text_12)
temps_reaction2Components.append(key_resp_6)
temps_reaction2Components.append(text_13)
for thisComponent in temps_reaction2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "temps_reaction2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = temps_reaction2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if t >= 0.0 and text_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_10.tStart = t  # underestimates by a little under one frame
        text_10.frameNStart = frameN  # exact frame index
        text_10.setAutoDraw(True)
    elif text_10.status == STARTED and t >= (0.0 + (8-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_10.setAutoDraw(False)
    
    # *text_11* updates
    if t >= 8 and text_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_11.tStart = t  # underestimates by a little under one frame
        text_11.frameNStart = frameN  # exact frame index
        text_11.setAutoDraw(True)
    elif text_11.status == STARTED and t >= (8 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_11.setAutoDraw(False)
    
    # *text_12* updates
    if t >= 9 and text_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_12.tStart = t  # underestimates by a little under one frame
        text_12.frameNStart = frameN  # exact frame index
        text_12.setAutoDraw(True)
    elif text_12.status == STARTED and t >= (9 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_12.setAutoDraw(False)
    
    # *key_resp_6* updates
    if t >= 9 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t  # underestimates by a little under one frame
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['left'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *text_13* updates
    if t >= 11 and text_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_13.tStart = t  # underestimates by a little under one frame
        text_13.frameNStart = frameN  # exact frame index
        text_13.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in temps_reaction2Components:
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

#-------Ending Routine "temps_reaction2"-------
for thisComponent in temps_reaction2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
instructionsComponents = []
instructionsComponents.append(text_6)
instructionsComponents.append(key_resp_3)
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # underestimates by a little under one frame
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
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

#-------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "pleasantness_rating"-------
t = 0
pleasantness_ratingClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
agreabilite.reset()
# keep track of which components have finished
pleasantness_ratingComponents = []
pleasantness_ratingComponents.append(agreabilite)
for thisComponent in pleasantness_ratingComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "pleasantness_rating"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = pleasantness_ratingClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *agreabilite* updates
    if t > 0.0:
        agreabilite.draw()
        continueRoutine = agreabilite.noResponse
        if agreabilite.noResponse == False:
            agreabilite.response = agreabilite.getRating()
            agreabilite.rt = agreabilite.getRT()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pleasantness_ratingComponents:
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

#-------Ending Routine "pleasantness_rating"-------
for thisComponent in pleasantness_ratingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('agreabilite.response', agreabilite.getRating())
thisExp.addData('agreabilite.rt', agreabilite.getRT())
thisExp.nextEntry()

#------Prepare to start Routine "instructions_2"-------
t = 0
instructions_2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_7.status = NOT_STARTED
# keep track of which components have finished
instructions_2Components = []
instructions_2Components.append(text)
instructions_2Components.append(key_resp_7)
for thisComponent in instructions_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions_2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructions_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t  # underestimates by a little under one frame
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_2Components:
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

#-------Ending Routine "instructions_2"-------
for thisComponent in instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=u'/home/jason/Dropbox/SteffenerColumbia/Scripts/ExperimentalStimuli/Johannes/CBCLabel/label_CBC.psyexp',
    trialList=data.importConditions('olfacto1ang.xlsx'),
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
    
    #------Prepare to start Routine "isi"-------
    t = 0
    isiClock.reset()  # clock 
    frameN = -1
    routineTimer.add(25.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    isiComponents = []
    isiComponents.append(ISI_2)
    isiComponents.append(text_5)
    for thisComponent in isiComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "isi"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = isiClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if t >= 0.0 and text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_5.tStart = t  # underestimates by a little under one frame
            text_5.frameNStart = frameN  # exact frame index
            text_5.setAutoDraw(True)
        elif text_5.status == STARTED and t >= (0.0 + (25-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_5.setAutoDraw(False)
        # *ISI_2* period
        if t >= 0.0 and ISI_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_2.tStart = t  # underestimates by a little under one frame
            ISI_2.frameNStart = frameN  # exact frame index
            ISI_2.start(5)
        elif ISI_2.status == STARTED: #one frame should pass before updating params and completing
            ISI_2.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "isi"-------
    for thisComponent in isiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "stimulus"-------
    t = 0
    stimulusClock.reset()  # clock 
    frameN = -1
    routineTimer.add(12.000000)
    # update component parameters for each repeat
    onset = 7.1+ random()
    
    Label.setText(label)
    text_2.setText(label)
    text_3.setText(label)
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    # keep track of which components have finished
    stimulusComponents = []
    stimulusComponents.append(Label)
    stimulusComponents.append(text_2)
    stimulusComponents.append(text_3)
    stimulusComponents.append(key_resp_2)
    stimulusComponents.append(p_port)
    for thisComponent in stimulusComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "stimulus"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimulusClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *Label* updates
        if t >= 0.0 and Label.status == NOT_STARTED:
            # keep track of start time/frame for later
            Label.tStart = t  # underestimates by a little under one frame
            Label.frameNStart = frameN  # exact frame index
            Label.setAutoDraw(True)
        elif Label.status == STARTED and t >= (0.0 + (6-win.monitorFramePeriod*0.75)): #most of one frame period left
            Label.setAutoDraw(False)
        
        # *text_2* updates
        if t >= 6 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        elif text_2.status == STARTED and t >= (6 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_2.setAutoDraw(False)
        
        # *text_3* updates
        if t >= 7 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        elif text_3.status == STARTED and t >= (7 + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_3.setAutoDraw(False)
        
        # *key_resp_2* updates
        if t >= onset and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif key_resp_2.status == STARTED and t >= (onset + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
            key_resp_2.status = STOPPED
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_2.keys == []:  # then this was the first keypress
                    key_resp_2.keys = theseKeys[0]  # just the first key pressed
                    key_resp_2.rt = key_resp_2.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_2.keys == str(corrAns)) or (key_resp_2.keys == corrAns):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        # *p_port* updates
        if t >= onset and p_port.status == NOT_STARTED:
            # keep track of start time/frame for later
            p_port.tStart = t  # underestimates by a little under one frame
            p_port.frameNStart = frameN  # exact frame index
            p_port.status = STARTED
            win.callOnFlip(p_port.setData, int(channel))
        elif p_port.status == STARTED and t >= (onset + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            p_port.status = STOPPED
            win.callOnFlip(p_port.setData, int(0))
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimulusComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "stimulus"-------
    for thisComponent in stimulusComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
       key_resp_2.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': key_resp_2.corr = 1  # correct non-response
       else: key_resp_2.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    trials.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    if p_port.status == STARTED:
        win.callOnFlip(p_port.setData, int(0))
    
    #------Prepare to start Routine "pleasantness_rating"-------
    t = 0
    pleasantness_ratingClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    agreabilite.reset()
    # keep track of which components have finished
    pleasantness_ratingComponents = []
    pleasantness_ratingComponents.append(agreabilite)
    for thisComponent in pleasantness_ratingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pleasantness_rating"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = pleasantness_ratingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *agreabilite* updates
        if t > 0.0:
            agreabilite.draw()
            continueRoutine = agreabilite.noResponse
            if agreabilite.noResponse == False:
                agreabilite.response = agreabilite.getRating()
                agreabilite.rt = agreabilite.getRT()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pleasantness_ratingComponents:
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
    
    #-------Ending Routine "pleasantness_rating"-------
    for thisComponent in pleasantness_ratingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('agreabilite.response', agreabilite.getRating())
    trials.addData('agreabilite.rt', agreabilite.getRT())
    
    #------Prepare to start Routine "kreuz"-------
    t = 0
    kreuzClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    kreuzComponents = []
    kreuzComponents.append(text_7)
    for thisComponent in kreuzComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "kreuz"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = kreuzClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if t >= 0.0 and text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_7.tStart = t  # underestimates by a little under one frame
            text_7.frameNStart = frameN  # exact frame index
            text_7.setAutoDraw(True)
        elif text_7.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_7.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in kreuzComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "kreuz"-------
    for thisComponent in kreuzComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials'


#------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
thanksComponents = []
thanksComponents.append(text_8)
thanksComponents.append(key_resp_4)
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "thanks"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if t >= 0.0 and text_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_8.tStart = t  # underestimates by a little under one frame
        text_8.frameNStart = frameN  # exact frame index
        text_8.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
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

#-------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

win.close()
core.quit()
