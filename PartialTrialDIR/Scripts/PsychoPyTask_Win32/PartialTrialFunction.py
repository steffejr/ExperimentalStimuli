#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.01), Thu 24 Sep 2015 11:35:23 AM EDT
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
# from psychopy.hardware.emulator import launchScan
import time
import sys
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

global expName
global AllowedInputKeys
AllowedInputKeys = ['1', '2','3','4','5','6','7','8','9','down','right']
global FullScreenFlag 

FullScreenFlag = True
ScreenToUse = None
expName='PartT'

def TestSomething(subid=9999,visitid=0001):
    expInfo = {u'Visit ID': u'9999', u'Participant ID': u'1'}
    print 'subid is %s'%(subid)
    if subid == '9999':
        dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    else:
        expInfo['Participant ID']=subid
        expInfo['Visit ID']=visitid
    return expInfo

def PartialTrial(INPUTFILE,filename,subid=9999,visitid=9999):
    #INPUTFILE = 'Optimized60trialsLoads12467_1.xlsx'
    # INPUTFILE = 'TrialListLoads123466_6Repeats_121415_2.csv'
    # INPUTFILE = 'TwoTrials.xlsx'
    IntroTime = 10
    End = 10 # This should be set so that it is at least ten seconds and so the experiment 
    # total duration is a multiple of two seconds.

    MaxLetters = 6
    if MaxLetters == 6:
        SETwrapWidth = 1.5 # The wrap width of text needs to be adjusted based on how manty letters there are
        SETletCycle = 13 # # Spaces are added between letters and this controls the loop which does it
    elif MaxLetters == 7:
        SETwrapWidth = 1.7
        SETletCycle = 15
    expInfo = {u'Visit ID': u'001', u'Participant ID': u''}
    if subid == '9999':
        dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
        if dlg.OK == False: win.close()  # user pressed cancel
    else:
        print "Subid entered is: %s"%(subid)
        expInfo['Participant ID']=subid
        expInfo['Visit ID']=visitid
        
    # Store info about the experiment session

    
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    # filename = _thisDir + os.sep + 'data/%s_%s_%s_%s' %(expInfo['Participant ID'], expInfo['Visit ID'], expName, expInfo['date'])

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
    win = visual.Window(size=[1366, 768], fullscr=FullScreenFlag, screen=0, allowGUI=True, allowStencil=False,
        monitor = ScreenToUse, color=[-1,-1,-1], colorSpace=u'rgb',
        blendMode=u'add', useFBO=True,
        units=u'norm')
    # store frame rate of monitor if we can measure it successfully
    expInfo['frameRate']=win.getActualFrameRate()
    if expInfo['frameRate']!=None:
        frameDur = 1.0/round(expInfo['frameRate'])
    else:
        frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

    # Initialize components for Routine "trial"
    trialClock = core.Clock()
    ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
    
    # THE AIM IS TO 
    TopUpperLine = visual.Line(win=win, name='TopUpperLine',units=u'norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace=u'rgb',
        fillColor=u'[1,1,-1]', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    UpperText = visual.TextStim(win=win, ori=0, name='UpperText',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,0.3], height=0.25, wrapWidth=SETwrapWidth, ## Changed from 1.5 because of 7 letters
        color=[0,0,0], colorSpace=u'rgb', opacity=1,
        depth=-2.0)
    UpperBrackets = visual.TextStim(win=win, ori=0, name='UpperBrackets',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,0.3], height=0.25, wrapWidth=SETwrapWidth,
        color=u'yellow', colorSpace=u'rgb', opacity=1,
        depth=-3.0)
    BotUpperLine = visual.Line(win=win, name='BotUpperLine',units=u'norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace=u'rgb',
        fillColor=u'yellow', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    TopLowerLine = visual.Line(win=win, name='TopLowerLine',units=u'norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor=u'cyan', lineColorSpace=u'rgb',
        fillColor=u'cyan', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    LowerText = visual.TextStim(win=win, ori=0, name='LowerText',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,-0.3], height=0.25, wrapWidth=2,
        color=[0,0,0], colorSpace=u'rgb', opacity=1,
        depth=-6.0)
    LowerBrackets = visual.TextStim(win=win, ori=0, name='LowerBrackets',
        text=u'+',    font=u'Lucida Console',
        units=u'norm', pos=[0,-0.3], height=0.25, wrapWidth=SETwrapWidth,
        color=u'cyan', colorSpace=u'rgb', opacity=1,
        depth=-7.0)
    BotLowerLine = visual.Line(win=win, name='BotLowerLine',units=u'norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor=u'cyan', lineColorSpace=u'rgb',
        fillColor=u'cyan', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    TrialCrossHair = visual.TextStim(win=win, ori=0, name='TrialCrossHair',
        text=u'+',    font=u'Lucida Console',
        units=u'norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color=u'green', colorSpace=u'rgb', opacity=1,
        depth=-9.0)
    RestCrossHair = visual.TextStim(win=win, ori=0, name='RestCrossHair',
        text=u'+',    font=u'Lucida Console',
        units=u'norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color=u'red', colorSpace=u'rgb', opacity=1,
        depth=-10.0)
    WaitForScanner = visual.TextStim(win=win, ori=0, name='RestCrossHair',
        text=u'Waiting for Scanner, press r to advance',    font=u'Lucida Console',
        units=u'norm', pos=[0, 0], height=0.1, wrapWidth=None,
        color=u'red', colorSpace=u'rgb', opacity=1,
        depth=-10.0)

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method=u'sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions(INPUTFILE),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)



    # PRESENT THE SCREEN TO WAIT FOR THE MRI TRIGGER
    #vol = launchScan(win, MR_settings,  mode='Scan')

    # ########################################################
    # There should be WAITING FOR SCANNER trial here
    # The test2 routine has these parts in it
    #------Prepare to start Routine "ScanWait"-------
    t = 0
    ScanWaitClock = core.Clock()
    ScanWaitClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    ScannerTrigger = event.BuilderKeyResponse()  # create an object of type KeyResponse
    ScannerTrigger.status = NOT_STARTED
    # keep track of which components have finished
    ScanWaitComponents = []
    ScanWaitComponents.append(WaitForScanner)
    ScanWaitComponents.append(ScannerTrigger)
    for thisComponent in ScanWaitComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "ScanWait"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = ScanWaitClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if t >= 0.0 and WaitForScanner.status == NOT_STARTED:
            # keep track of start time/frame for later
            WaitForScanner.tStart = t  # underestimates by a little under one frame
            WaitForScanner.frameNStart = frameN  # exact frame index
            WaitForScanner.setAutoDraw(True)
        
        # *key_resp_3* updates
        if t >= 0.0 and ScannerTrigger.status == NOT_STARTED:
            # keep track of start time/frame for later
            ScannerTrigger.tStart = t  # underestimates by a little under one frame
            ScannerTrigger.frameNStart = frameN  # exact frame index
            ScannerTrigger.status = STARTED
            # keyboard checking is just starting
            ScannerTrigger.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if ScannerTrigger.status == STARTED:
            theseKeys = event.getKeys(keyList=['r','equal'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                ScannerTrigger.keys = theseKeys[-1]  # just the last key pressed
                ScannerTrigger.rt = ScannerTrigger.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ScanWaitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
            
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()

    #-------Ending Routine "ScanWait"-------
    for thisComponent in ScanWaitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if ScannerTrigger.keys in ['', [], None]:  # No response was made
       ScannerTrigger.keys=None
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('ScannerTrigger.keys',ScannerTrigger.keys)
    if ScannerTrigger.keys != None:  # we had a response
        thisExp.addData('ScannerTrigger.rt', ScannerTrigger.rt)
    thisExp.nextEntry()
    # ########################################################

    # ########################################################
    # There should be an intro off trial here also

    # Write out when the experiment begins
    thisExp.addData('TrialStartTime', time.time())
    thisExp.nextEntry()
    #------Prepare to start Routine "intro"-------
    t = 0
    introClock = core.Clock()
    introClock.reset()  # clock 
    frameN = -1
    routineTimer.add(IntroTime)
    # update component parameters for each repeat
    # keep track of which components have finished
    introComponents = []
    introComponents.append(RestCrossHair)
    for thisComponent in introComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "intro"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = introClock.getTime()
        
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if t >= 0.0 and RestCrossHair.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair.tStart = t  # underestimates by a little under one frame
            RestCrossHair.frameNStart = frameN  # exact frame index
            RestCrossHair.setAutoDraw(True)
        elif RestCrossHair.status == STARTED and t >= (0.0 + (IntroTime-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "intro"-------
    for thisComponent in introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # ########################################################

    for thisTrial in trials:
        # Write to the file the time this trial starts
        trials.addData('TrialStartTime',time.time())
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        
        # ENCODING SET
        # Add spaces to between the letters of the stimulus set
        # Note use Lucida Console font because it is monspaced
        tempStimSet = StimSet
        # Letters for space - letter - space - letter ... - space
        StimSet=' '
        for i in tempStimSet:
            StimSet=StimSet+i+' '
        # Create the brackets
        # What bracket positions to use?
        # Find the first character of the bracket variable
        UpBrackText = ''
        if UpBrack > 0:
            BracketList = list(str(UpBrack))
            LeftBrackPos = int(BracketList[0])
            RightBrackPos = int(BracketList[-1])
            for i in range(0,SETletCycle,1):   ## Changed from 13 when using 7 letters
                UpBrackText = UpBrackText+' '
            s = list(UpBrackText)
            s[2*LeftBrackPos-1-1]='{'
            s[2*RightBrackPos-1+1]='}'
            UpBrackText = ''.join(s)
        
        # PROBE 
        # Add spaces to between the letters of the stimulus set
        # Note use Lucida Console font because it is monspaced
        tempProbeLet = ProbeLet
        # Letters for space - letter - space - letter ... - space
        ProbeLet=' '
        for i in tempProbeLet:
            ProbeLet = ProbeLet+i+' '
        # Create the brackets
        # What bracket positions to use?
        # Find the first character of the bracket variable
        BotBrackText = ''
        if BotBrack > 0:
            BracketList = list(str(BotBrack))
            LeftBrackPos = int(BracketList[0])
            RightBrackPos = int(BracketList[-1])
            for i in range(0,SETletCycle,1):   ## Changed from 13 when using 7 letters
                BotBrackText = BotBrackText+' '
            s = list(BotBrackText)
            s[2*LeftBrackPos-1-1]='{'
            s[2*RightBrackPos-1+1]='}'
            BotBrackText = ''.join(s)
            
        # update component parameters for each repeat
        UpperText.setText(StimSet)
        UpperBrackets.setText(UpBrackText)
        LowerText.setText(ProbeLet)
        LowerBrackets.setText(BotBrackText)
        
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
            elif TopUpperLine.status == STARTED and t >= (0 + (TrialITIDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                TopUpperLine.setAutoDraw(False)
            
            # *UpperText* updates
            if t >= 0 and UpperText.status == NOT_STARTED:
                # keep track of start time/frame for later
                UpperText.tStart = t  # underestimates by a little under one frame
                UpperText.frameNStart = frameN  # exact frame index
                UpperText.setAutoDraw(True)
            elif UpperText.status == STARTED and t >= (0 + (StimDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                UpperText.setAutoDraw(False)
            
            # *UpperBrackets* updates
            if t >= 0.0 and UpperBrackets.status == NOT_STARTED:
                # keep track of start time/frame for later
                UpperBrackets.tStart = t  # underestimates by a little under one frame
                UpperBrackets.frameNStart = frameN  # exact frame index
                UpperBrackets.setAutoDraw(True)
            elif UpperBrackets.status == STARTED and t >= (0.0 + (StimDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                UpperBrackets.setAutoDraw(False)
            
            # *BotUpperLine* updates
            if t >= 0.0 and BotUpperLine.status == NOT_STARTED:
                # keep track of start time/frame for later
                BotUpperLine.tStart = t  # underestimates by a little under one frame
                BotUpperLine.frameNStart = frameN  # exact frame index
                BotUpperLine.setAutoDraw(True)
            elif BotUpperLine.status == STARTED and t >= (0.0 + (TrialITIDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                BotUpperLine.setAutoDraw(False)
            
            # *TopLowerLine* updates
            if t >= 0.0 and TopLowerLine.status == NOT_STARTED:
                # keep track of start time/frame for later
                TopLowerLine.tStart = t  # underestimates by a little under one frame
                TopLowerLine.frameNStart = frameN  # exact frame index
                TopLowerLine.setAutoDraw(True)
            elif TopLowerLine.status == STARTED and t >= (0.0 + (TrialITIDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                TopLowerLine.setAutoDraw(False)
            
            # *LowerText* updates
            if t >= ProbeStart and LowerText.status == NOT_STARTED:
                # keep track of start time/frame for later
                LowerText.tStart = t  # underestimates by a little under one frame
                LowerText.frameNStart = frameN  # exact frame index
                LowerText.setAutoDraw(True)
            elif LowerText.status == STARTED and t >= (ProbeStart + (ProbeDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                LowerText.setAutoDraw(False)
            
            # *LowerBrackets* updates
            if t >= ProbeStart and LowerBrackets.status == NOT_STARTED:
                # keep track of start time/frame for later
                LowerBrackets.tStart = t  # underestimates by a little under one frame
                LowerBrackets.frameNStart = frameN  # exact frame index
                LowerBrackets.setAutoDraw(True)
            elif LowerBrackets.status == STARTED and t >= (ProbeStart + (ProbeDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                LowerBrackets.setAutoDraw(False)
            
            # *BotLowerLine* updates
            if t >= 0.0 and BotLowerLine.status == NOT_STARTED:
                # keep track of start time/frame for later
                BotLowerLine.tStart = t  # underestimates by a little under one frame
                BotLowerLine.frameNStart = frameN  # exact frame index
                BotLowerLine.setAutoDraw(True)
            elif BotLowerLine.status == STARTED and t >= (0.0 + (TrialITIDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                BotLowerLine.setAutoDraw(False)
            
            # *TrialCrossHair* updates
            if t >= 0 and TrialCrossHair.status == NOT_STARTED:
                # keep track of start time/frame for later
                TrialCrossHair.tStart = t  # underestimates by a little under one frame
                TrialCrossHair.frameNStart = frameN  # exact frame index
                TrialCrossHair.setAutoDraw(True)
            elif TrialCrossHair.status == STARTED and t >= (0 + (TrialDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                TrialCrossHair.setAutoDraw(False)
            
            # *RestCrossHair* updates
            if t >= TrialDur and RestCrossHair.status == NOT_STARTED:
                # keep track of start time/frame for later
                RestCrossHair.tStart = t  # underestimates by a little under one frame
                RestCrossHair.frameNStart = frameN  # exact frame index
                RestCrossHair.setAutoDraw(True)
            elif RestCrossHair.status == STARTED and t >= (TrialDur + (ITI-win.monitorFramePeriod*0.75)): #most of one frame period left
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
            elif KeyboardResp.status == STARTED and t >= (ProbeStart + (ProbeDurITI-win.monitorFramePeriod*0.75)): #most of one frame period left
                KeyboardResp.status = STOPPED
            if KeyboardResp.status == STARTED:
                theseKeys = event.getKeys(keyList=AllowedInputKeys)#['1', '2', '3', '4', '5', '6', '7', '8'])
                
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
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                win.close()
                sys.exit()

            
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
        thisExp.nextEntry()
        
    # ########################################################
    # There should be an intro off trial here also

    #------Prepare to start Routine "EndTime"-------
    thisExp.addData('TrialStartTime', time.time())
    thisExp.nextEntry()
    t = 0
    EndTimeClock = core.Clock()
    EndTimeClock.reset()  # clock 
    frameN = -1
    routineTimer.add(End)
    # update component parameters for each repeat
    # keep track of which components have finished
    EndTimeComponents = []
    EndTimeComponents.append(RestCrossHair)
    for thisComponent in EndTimeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "EndTime"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = EndTimeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *End* updates
        if t >= 0.0 and RestCrossHair.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair.tStart = t  # underestimates by a little under one frame
            RestCrossHair.frameNStart = frameN  # exact frame index
            RestCrossHair.setAutoDraw(True)
        if RestCrossHair.status == STARTED and t >= (0.0 + (End-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndTimeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
            #win.close()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "EndTime"-------
    thisExp.addData('TrialStartTime', time.time())
    thisExp.nextEntry()
    for thisComponent in EndTimeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # ########################################################
    thisExp.addData('TrialStartTime', time.time())
    thisExp.nextEntry()    
    # completed 1 repeats of 'trials'
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    win.close()
    #sys.exit()
    return filename

def PartialTrialFeedback(INPUTFILE,filename,subid=9999,visitid=9999):
    # filename is for the output file where the data gets written to
    expInfo = {u'Visit ID': u'001', u'Participant ID': u''}
    if subid == '9999':
        dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
        if dlg.OK == False: win.close()  # user pressed cancel
    else:
        print "Subid entered is: %s"%(subid)
        expInfo['Participant ID']=subid
        expInfo['Visit ID']=visitid
        
    # Store info about the experiment session

    
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    
    # The following line is commented out because now the output file is given as an input. 
    # This allows better control over what it is called.
    #filename = _thisDir + os.sep + 'data/%s_%s_%s_%s' %(expInfo['Participant ID'], expInfo['Visit ID'], expName, expInfo['date'])

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
    win = visual.Window(size=[800, 600], fullscr=FullScreenFlag, screen=0, allowGUI=True, allowStencil=False,
        monitor=u'testMonitor', color=[-1,-1,-1], colorSpace=u'rgb',
        blendMode=u'add', useFBO=True,
        units=u'use preferences')
    # store frame rate of monitor if we can measure it successfully
    expInfo['frameRate']=win.getActualFrameRate()
    if expInfo['frameRate']!=None:
        frameDur = 1.0/round(expInfo['frameRate'])
    else:
        frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

    # Initialize components for Routine "trial"
    trialClock = core.Clock()
    ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
    TopUpperLine = visual.Line(win=win, name='TopUpperLine',units=u'norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace=u'rgb',
        fillColor=u'[1,1,-1]', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    UpperText = visual.TextStim(win=win, ori=0, name='UpperText',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,0.3], height=0.25, wrapWidth=1.7,
        color=[0,0,0], colorSpace=u'rgb', opacity=1,
        depth=-2.0)
    UpperBrackets = visual.TextStim(win=win, ori=0, name='UpperBrackets',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,0.3], height=0.25, wrapWidth=1.7,
        color=u'yellow', colorSpace=u'rgb', opacity=1,
        depth=-3.0)
    BotUpperLine = visual.Line(win=win, name='BotUpperLine',units=u'norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace=u'rgb',
        fillColor=u'yellow', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    TopLowerLine = visual.Line(win=win, name='TopLowerLine',units=u'norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor=u'cyan', lineColorSpace=u'rgb',
        fillColor=u'cyan', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    LowerText = visual.TextStim(win=win, ori=0, name='LowerText',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,-0.3], height=0.25, wrapWidth=2,
        color=[0,0,0], colorSpace=u'rgb', opacity=1,
        depth=-6.0)
    LowerBrackets = visual.TextStim(win=win, ori=0, name='LowerBrackets',
        text=u'+',    font=u'Lucida Console',
        units=u'norm', pos=[0,-0.3], height=0.25, wrapWidth=1.5,
        color=u'cyan', colorSpace=u'rgb', opacity=1,
        depth=-7.0)
    BotLowerLine = visual.Line(win=win, name='BotLowerLine',units=u'norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor=u'cyan', lineColorSpace=u'rgb',
        fillColor=u'cyan', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    TrialCrossHair = visual.TextStim(win=win, ori=0, name='TrialCrossHair',
        text=u'+',    font=u'Lucida Console',
        units=u'norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color=u'green', colorSpace=u'rgb', opacity=1,
        depth=-9.0)
    RestCrossHair = visual.TextStim(win=win, ori=0, name='RestCrossHair',
        text=u'+',    font=u'Lucida Console',
        units=u'norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color=u'red', colorSpace=u'rgb', opacity=1,
        depth=-10.0)
    WaitForScanner = visual.TextStim(win=win, ori=0, name='RestCrossHair',
        text=u'Waiting for Scanner\n Or press r to advance',    font=u'Lucida Console',
        units=u'norm', pos=[0, 0], height=0.1, wrapWidth=None,
        color=u'red', colorSpace=u'rgb', opacity=1,
        depth=-10.0)
    ThankYou = visual.TextStim(win=win, ori=0, name='RestCrossHair',
        text=u'Merci\nThank you',    font=u'Lucida Console',
        units=u'norm', pos=[0, 0], height=0.1, wrapWidth=None,
        color=u'yellow', colorSpace=u'rgb', opacity=1,
        depth=-10.0)
    # Initialize components for Routine "Feedback"
    FeedbackClock = core.Clock()
    #msg variable just needs some value at start
    msg=''
    FeedbackMsg = visual.TextStim(win=win, ori=0, name='FeedbackMsg',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-1.0)

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method=u'sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions(INPUTFILE),#TrialListShort1#TrialList5Loads6Repeats
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)



    # PRESENT THE SCREEN TO WAIT FOR THE MRI TRIGGER
    #vol = launchScan(win, MR_settings,  mode='Scan')

    # ########################################################
    # There should be WAITING FOR SCANNER trial here
    # The test2 routine has these parts in it
    #------Prepare to start Routine "ScanWait"-------
    t = 0
    ScanWaitClock = core.Clock()
    ScanWaitClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    ScannerTrigger = event.BuilderKeyResponse()  # create an object of type KeyResponse
    ScannerTrigger.status = NOT_STARTED
    # keep track of which components have finished
    ScanWaitComponents = []
    ScanWaitComponents.append(WaitForScanner)
    ScanWaitComponents.append(ScannerTrigger)
    for thisComponent in ScanWaitComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "ScanWait"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = ScanWaitClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if t >= 0.0 and WaitForScanner.status == NOT_STARTED:
            # keep track of start time/frame for later
            WaitForScanner.tStart = t  # underestimates by a little under one frame
            WaitForScanner.frameNStart = frameN  # exact frame index
            WaitForScanner.setAutoDraw(True)
        
        # *key_resp_3* updates
        if t >= 0.0 and ScannerTrigger.status == NOT_STARTED:
            # keep track of start time/frame for later
            ScannerTrigger.tStart = t  # underestimates by a little under one frame
            ScannerTrigger.frameNStart = frameN  # exact frame index
            ScannerTrigger.status = STARTED
            # keyboard checking is just starting
            ScannerTrigger.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if ScannerTrigger.status == STARTED:
            theseKeys = event.getKeys(keyList=['5', 'r'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                ScannerTrigger.keys = theseKeys[-1]  # just the last key pressed
                ScannerTrigger.rt = ScannerTrigger.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ScanWaitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            #core.quit()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()

    #-------Ending Routine "ScanWait"-------
    for thisComponent in ScanWaitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if ScannerTrigger.keys in ['', [], None]:  # No response was made
       ScannerTrigger.keys=None
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('ScannerTrigger.keys',ScannerTrigger.keys)
    if ScannerTrigger.keys != None:  # we had a response
        thisExp.addData('ScannerTrigger.rt', ScannerTrigger.rt)
    thisExp.nextEntry()
    # ########################################################

    # ########################################################
    # There should be an intro off trial here also
    IntroTime = 5
    # Write out when the experiment begins
    thisExp.addData('TrialStartTime', time.time())
    thisExp.nextEntry()
    #------Prepare to start Routine "intro"-------
    t = 0
    introClock = core.Clock()
    introClock.reset()  # clock 
    frameN = -1
    routineTimer.add(IntroTime)
    # update component parameters for each repeat
    # keep track of which components have finished
    introComponents = []
    introComponents.append(RestCrossHair)
    for thisComponent in introComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "intro"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = introClock.getTime()
        
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if t >= 0.0 and RestCrossHair.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair.tStart = t  # underestimates by a little under one frame
            RestCrossHair.frameNStart = frameN  # exact frame index
            RestCrossHair.setAutoDraw(True)
        elif RestCrossHair.status == STARTED and t >= (0.0 + (IntroTime-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "intro"-------
    for thisComponent in introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # ########################################################

    for thisTrial in trials:
        # Write to the file the time this trial starts
        trials.addData('TrialStartTime',time.time())
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        
        # ENCODING SET
        # Add spaces to between the letters of the stimulus set
        # Note use Lucida Console font because it is monspaced
        tempStimSet = StimSet
        # Letters for space - letter - space - letter ... - space
        StimSet=' '
        for i in tempStimSet:
            StimSet=StimSet+i+' '
        # Create the brackets
        # What bracket positions to use?
        # Find the first character of the bracket variable
        UpBrackText = ''
        if UpBrack > 0:
            BracketList = list(str(UpBrack))
            LeftBrackPos = int(BracketList[0])
            RightBrackPos = int(BracketList[-1])
            for i in range(0,13,1):   ## Changed from 13 when using 7 letters
                UpBrackText = UpBrackText+' '
            s = list(UpBrackText)
            s[2*LeftBrackPos-1-1]='{'
            s[2*RightBrackPos-1+1]='}'
            UpBrackText = ''.join(s)
        
        # PROBE 
        # Add spaces to between the letters of the stimulus set
        # Note use Lucida Console font because it is monspaced
        tempProbeLet = ProbeLet
        print '%s'%(tempProbeLet)
        # Letters for space - letter - space - letter ... - space
        ProbeLet=' '
        for i in tempProbeLet:
            ProbeLet = ProbeLet+i+' '
        # Create the brackets
        # What bracket positions to use?
        # Find the first character of the bracket variable
        BotBrackText = ''
        if BotBrack > 0:
            BracketList = list(str(BotBrack))
            LeftBrackPos = int(BracketList[0])
            RightBrackPos = int(BracketList[-1])
            for i in range(0,13,1):   ## Changed from 13 when using 7 letters
                BotBrackText = BotBrackText+' '
            s = list(BotBrackText)
            s[2*LeftBrackPos-1-1]='{'
            s[2*RightBrackPos-1+1]='}'
            BotBrackText = ''.join(s)
            
        # update component parameters for each repeat
        UpperText.setText(StimSet)
        UpperBrackets.setText(UpBrackText)
        LowerText.setText(ProbeLet)
        LowerBrackets.setText(BotBrackText)
        
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
            elif TopUpperLine.status == STARTED and t >= (0 + (TrialITIDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                TopUpperLine.setAutoDraw(False)
            
            # *UpperText* updates
            if t >= 0 and UpperText.status == NOT_STARTED:
                # keep track of start time/frame for later
                UpperText.tStart = t  # underestimates by a little under one frame
                UpperText.frameNStart = frameN  # exact frame index
                UpperText.setAutoDraw(True)
            elif UpperText.status == STARTED and t >= (0 + (StimDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                UpperText.setAutoDraw(False)
            
            # *UpperBrackets* updates
            if t >= 0.0 and UpperBrackets.status == NOT_STARTED:
                # keep track of start time/frame for later
                UpperBrackets.tStart = t  # underestimates by a little under one frame
                UpperBrackets.frameNStart = frameN  # exact frame index
                UpperBrackets.setAutoDraw(True)
            elif UpperBrackets.status == STARTED and t >= (0.0 + (StimDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                UpperBrackets.setAutoDraw(False)
            
            # *BotUpperLine* updates
            if t >= 0.0 and BotUpperLine.status == NOT_STARTED:
                # keep track of start time/frame for later
                BotUpperLine.tStart = t  # underestimates by a little under one frame
                BotUpperLine.frameNStart = frameN  # exact frame index
                BotUpperLine.setAutoDraw(True)
            elif BotUpperLine.status == STARTED and t >= (0.0 + (TrialITIDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                BotUpperLine.setAutoDraw(False)
            
            # *TopLowerLine* updates
            if t >= 0.0 and TopLowerLine.status == NOT_STARTED:
                # keep track of start time/frame for later
                TopLowerLine.tStart = t  # underestimates by a little under one frame
                TopLowerLine.frameNStart = frameN  # exact frame index
                TopLowerLine.setAutoDraw(True)
            elif TopLowerLine.status == STARTED and t >= (0.0 + (TrialITIDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                TopLowerLine.setAutoDraw(False)
            
            # *LowerText* updates
            if t >= ProbeStart and LowerText.status == NOT_STARTED:
                # keep track of start time/frame for later
                LowerText.tStart = t  # underestimates by a little under one frame
                LowerText.frameNStart = frameN  # exact frame index
                LowerText.setAutoDraw(True)
            elif LowerText.status == STARTED and t >= (ProbeStart + (ProbeDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                LowerText.setAutoDraw(False)
            
            # *LowerBrackets* updates
            if t >= ProbeStart and LowerBrackets.status == NOT_STARTED:
                # keep track of start time/frame for later
                LowerBrackets.tStart = t  # underestimates by a little under one frame
                LowerBrackets.frameNStart = frameN  # exact frame index
                LowerBrackets.setAutoDraw(True)
            elif LowerBrackets.status == STARTED and t >= (ProbeStart + (ProbeDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                LowerBrackets.setAutoDraw(False)
            
            # *BotLowerLine* updates
            if t >= 0.0 and BotLowerLine.status == NOT_STARTED:
                # keep track of start time/frame for later
                BotLowerLine.tStart = t  # underestimates by a little under one frame
                BotLowerLine.frameNStart = frameN  # exact frame index
                BotLowerLine.setAutoDraw(True)
            elif BotLowerLine.status == STARTED and t >= (0.0 + (TrialITIDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                BotLowerLine.setAutoDraw(False)
            
            # *TrialCrossHair* updates
            if t >= 0 and TrialCrossHair.status == NOT_STARTED:
                # keep track of start time/frame for later
                TrialCrossHair.tStart = t  # underestimates by a little under one frame
                TrialCrossHair.frameNStart = frameN  # exact frame index
                TrialCrossHair.setAutoDraw(True)
            elif TrialCrossHair.status == STARTED and t >= (0 + (TrialDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                TrialCrossHair.setAutoDraw(False)
            
            # *RestCrossHair* updates
            if t >= TrialDur and RestCrossHair.status == NOT_STARTED:
                # keep track of start time/frame for later
                RestCrossHair.tStart = t  # underestimates by a little under one frame
                RestCrossHair.frameNStart = frameN  # exact frame index
                RestCrossHair.setAutoDraw(True)
            elif RestCrossHair.status == STARTED and t >= (TrialDur + (ITI-win.monitorFramePeriod*0.75)): #most of one frame period left
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
            elif KeyboardResp.status == STARTED and t >= (ProbeStart + (ProbeDurITI-win.monitorFramePeriod*0.75)): #most of one frame period left
                KeyboardResp.status = STOPPED
            if KeyboardResp.status == STARTED:
                theseKeys = event.getKeys(keyList=AllowedInputKeys)#['1', '2', '3', '4', '5', '6', '7', '8','down','right'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    #KeyboardResp.keys.extend(theseKeys)  # storing all keys
                    KeyboardResp.keys = theseKeys[-1]  # just the last key pressed
                    #KeyboardResp.rt.append(KeyboardResp.clock.getTime())
                    KeyboardResp.rt = KeyboardResp.clock.getTime()
                    # was this 'correct'?
                    # What if the participant responded whenthey were not supposed to?
                    if str(Correct).lower() == 'none':
                        KeyboardResp.corr = -10 # RESPONSE WHEN NONE WAS EXPECTED
                    else:
                        if (KeyboardResp.keys == str(Correct)) or (KeyboardResp.keys == Correct):
                            KeyboardResp.corr = 1 # CORRECT
                        else:
                            KeyboardResp.corr = 0 # INCORRECT
                    # was this 'correct'?
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
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                win.close()
                sys.exit()

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
        if KeyboardResp.keys in ['', [], None]:  # No response was made
           KeyboardResp.keys=None
           # was no response the correct answer?!
           if str(Correct).lower() == 'none': KeyboardResp.corr = 10  # correct non-response
           else: KeyboardResp.corr = -1  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('KeyboardResp.keys',KeyboardResp.keys)
        trials.addData('KeyboardResp.corr', KeyboardResp.corr)
        if KeyboardResp.keys != None:  # we had a response
            trials.addData('KeyboardResp.rt', KeyboardResp.rt)
        thisExp.nextEntry()
        
        
    # ########################################################    
        #------Prepare to start Routine "Feedback"-------
        FeedbackDur = 1.5
        t = 0
        FeedbackClock.reset()  # clock 
        frameN = -1
        routineTimer.add(FeedbackDur)
        # update component parameters for each repeat
        if KeyboardResp.corr == 1:#stored on last run routine
          msg="Correct! RT=%.3f" %(KeyboardResp.rt)
        elif KeyboardResp.corr == 0:
          msg="Oops! That was wrong"
        elif KeyboardResp.corr == -1:
          msg="No response...miss"
        elif KeyboardResp.corr == 10:
          msg="No response, good!"
        FeedbackMsg.setText(msg)
        # keep track of which components have finished
        FeedbackComponents = []
        FeedbackComponents.append(FeedbackMsg)
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Feedback"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *FeedbackMsg* updates
            if t >= 0.0 and FeedbackMsg.status == NOT_STARTED:
                # keep track of start time/frame for later
                FeedbackMsg.tStart = t  # underestimates by a little under one frame
                FeedbackMsg.frameNStart = frameN  # exact frame index
                FeedbackMsg.setAutoDraw(True)
            if FeedbackMsg.status == STARTED and t >= (0.0 + (FeedbackDur-win.monitorFramePeriod*0.75)): #most of one frame period left
                FeedbackMsg.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                win.close()
                sys.exit()
                
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Feedback"-------
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)


        #------Prepare to start Routine "REST"-------
        t = 0
        RESTClock = core.Clock()
        RESTClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        RESTComponents = []
        RESTComponents.append(RestCrossHair)
        for thisComponent in RESTComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "REST"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = RESTClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *RestCrossHair* updates
            if t >= 0.0 and RestCrossHair.status == NOT_STARTED:
                # keep track of start time/frame for later
                RestCrossHair.tStart = t  # underestimates by a little under one frame
                RestCrossHair.frameNStart = frameN  # exact frame index
                RestCrossHair.setAutoDraw(True)
            if RestCrossHair.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                RestCrossHair.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RESTComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                win.close()
                sys.exit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "REST"-------
        for thisComponent in RESTComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()


    win.flip()
    # ########################################################
    # There should be an intro off trial here also
    EndTime = 10
    #------Prepare to start Routine "EndTime"-------
    thisExp.addData('TrialStartTime', time.time())
    thisExp.nextEntry()
    t = 0
    EndTimeClock = core.Clock()
    EndTimeClock.reset()  # clock 
    frameN = -1
    routineTimer.add(EndTime)
    # update component parameters for each repeat
    # keep track of which components have finished
    EndTimeComponents = []
    EndTimeComponents.append(RestCrossHair)
    for thisComponent in EndTimeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "EndTime"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = EndTimeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *End* updates
        if t >= 0.0 and RestCrossHair.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair.tStart = t  # underestimates by a little under one frame
            RestCrossHair.frameNStart = frameN  # exact frame index
            RestCrossHair.setAutoDraw(True)
        if RestCrossHair.status == STARTED and t >= (0.0 + (EndTime-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndTimeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
            
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "EndTime"-------
    for thisComponent in EndTimeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            
    # ########################################################        
    # There should be an intro off trial here also
    ThankYouTime = 3
    #------Prepare to start Routine "EndTime"-------
    thisExp.addData('TrialStartTime', time.time())
    thisExp.nextEntry()
    t = 0
    ThankYouClock = core.Clock()
    ThankYouClock.reset()  # clock 
    frameN = -1
    routineTimer.add(ThankYouTime)
    # update component parameters for each repeat
    # keep track of which components have finished
    ThankYouComponents = []
    ThankYouComponents.append(ThankYou)
    for thisComponent in ThankYouComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "EndTime"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ThankYouClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *End* updates
        if t >= 0.0 and ThankYou.status == NOT_STARTED:
            # keep track of start time/frame for later
            ThankYou.tStart = t  # underestimates by a little under one frame
            ThankYou.frameNStart = frameN  # exact frame index
            ThankYou.setAutoDraw(True)
        if ThankYou.status == STARTED and t >= (0.0 + (ThankYouTime-win.monitorFramePeriod*0.75)): #most of one frame period left
            ThankYou.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ThankYouComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "Thank you"-------
    for thisComponent in ThankYouComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)       
    # ########################################################
    thisExp.addData('TrialStartTime', time.time())
    thisExp.nextEntry()    
    # completed 1 repeats of 'trials'
    win.close()
#    win.close()

def Instructions():
    # Store info about the experiment session
    expName = u'Instructions'  # from the Builder filename that created this script
    expInfo = {u'session': u'001', u'participant': u''}
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath=None,
        savePickle=True, saveWideText=False,
        dataFileName=filename)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

    endExpNow = False  # flag for 'escape' or other condition => quit the exp

    # Start Code - component code to be run before the window creation

    # Setup the Window
    win = visual.Window(size=[800, 600], fullscr=FullScreenFlag, screen=0, allowGUI=True, allowStencil=False,
        monitor=u'UbuntuMon', color=[-1,-1,-1], colorSpace=u'rgb',
        blendMode=u'add', useFBO=True,
        units=u'norm')

    # store frame rate of monitor if we can measure it successfully
    expInfo['frameRate']=win.getActualFrameRate()
    if expInfo['frameRate']!=None:
        frameDur = 1.0/round(expInfo['frameRate'])
    else:
        frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

    # Initialize components for Routine "ButtonPractice"
    ButtonPracticeClock = core.Clock()
    text_28 = visual.TextStim(win=win, ori=0, name='text_28',
        text="First ...\nLet's make sure the buttons work.\nPress the RIGHT INDEX Finger button.",    font='Lucida Console',
        pos=[0,0.3], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=0.0)
    ISI_14 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_14')
    TopUpperLine_14 = visual.Line(win=win, name='TopUpperLine_14',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='[1,1,-1]', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    UpperText_14 = visual.TextStim(win=win, ori=0, name='UpperText_14',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-3.0)
    UpperBrackets_14 = visual.TextStim(win=win, ori=0, name='UpperBrackets_14',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-4.0)
    BotUpperLine_14 = visual.Line(win=win, name='BotUpperLine_14',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='yellow', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TopLowerLine_14 = visual.Line(win=win, name='TopLowerLine_14',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    LowerText_14 = visual.TextStim(win=win, ori=0, name='LowerText_14',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=2,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-7.0)
    LowerBrackets_14 = visual.TextStim(win=win, ori=0, name='LowerBrackets_14',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=None,
        color='cyan', colorSpace='rgb', opacity=1,
        depth=-8.0)
    BotLowerLine_14 = visual.Line(win=win, name='BotLowerLine_14',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TrialCrossHair_14 = visual.TextStim(win=win, ori=0, name='TrialCrossHair_14',
        text='\n',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='green', colorSpace='rgb', opacity=1,
        depth=-10.0)
    RestCrossHair_14 = visual.TextStim(win=win, ori=0, name='RestCrossHair_14',
        text=None,    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='red', colorSpace='rgb', opacity=1,
        depth=-11.0)

    # Initialize components for Routine "Feedback"
    FeedbackClock = core.Clock()
    msg='?????'
    text_25 = visual.TextStim(win=win, ori=0, name='text_25',
        text='default text',    font='Lucida Console',
        pos=[0, 0], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-1.0)

    # Initialize components for Routine "ButtonPractice_MIDDLE"
    ButtonPractice_MIDDLEClock = core.Clock()
    text_29 = visual.TextStim(win=win, ori=0, name='text_29',
        text='Press the RIGHT MIDDLE Finger button.',    font='Lucida Console',
        pos=[0,0.3], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=0.0)
    ISI_15 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_15')
    TopUpperLine_15 = visual.Line(win=win, name='TopUpperLine_15',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='[1,1,-1]', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    UpperText_15 = visual.TextStim(win=win, ori=0, name='UpperText_15',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-3.0)
    UpperBrackets_15 = visual.TextStim(win=win, ori=0, name='UpperBrackets_15',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-4.0)
    BotUpperLine_15 = visual.Line(win=win, name='BotUpperLine_15',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='yellow', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TopLowerLine_15 = visual.Line(win=win, name='TopLowerLine_15',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    LowerText_15 = visual.TextStim(win=win, ori=0, name='LowerText_15',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=2,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-7.0)
    LowerBrackets_15 = visual.TextStim(win=win, ori=0, name='LowerBrackets_15',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=None,
        color='cyan', colorSpace='rgb', opacity=1,
        depth=-8.0)
    BotLowerLine_15 = visual.Line(win=win, name='BotLowerLine_15',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TrialCrossHair_15 = visual.TextStim(win=win, ori=0, name='TrialCrossHair_15',
        text='\n',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='green', colorSpace='rgb', opacity=1,
        depth=-10.0)
    RestCrossHair_15 = visual.TextStim(win=win, ori=0, name='RestCrossHair_15',
        text=None,    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='red', colorSpace='rgb', opacity=1,
        depth=-11.0)

    # Initialize components for Routine "Feedback_MIDDLE"
    Feedback_MIDDLEClock = core.Clock()
    msg='?????'
    text_26 = visual.TextStim(win=win, ori=0, name='text_26',
        text='default text',    font=u'Lucida Console',
        pos=[0, 0], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-1.0)

    # Initialize components for Routine "var_6Letters_2"
    var_6Letters_2Clock = core.Clock()
    text_13 = visual.TextStim(win=win, ori=0, name='text_13',
        text='This is the screen you will see for each trial',    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=0.0)
    text_16 = visual.TextStim(win=win, ori=0, name='text_16',
        text='With an UPPER Part',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.1, wrapWidth=1.25,
        color='white', colorSpace='rgb', opacity=1,
        depth=-1.0)
    text_18 = visual.TextStim(win=win, ori=0, name='text_18',
        text='And a LOWER part',    font='Lucida Console',
        pos=[0,-0.3], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-2.0)
    text_21 = visual.TextStim(win=win, ori=0, name='text_21',
        text=None,    font='Lucida Console',
        pos=[0, 0], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-3.0)
    ISI_13 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_13')
    TopUpperLine_13 = visual.Line(win=win, name='TopUpperLine_13',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='[1,1,-1]', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    UpperText_13 = visual.TextStim(win=win, ori=0, name='UpperText_13',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-6.0)
    UpperBrackets_13 = visual.TextStim(win=win, ori=0, name='UpperBrackets_13',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-7.0)
    BotUpperLine_13 = visual.Line(win=win, name='BotUpperLine_13',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='yellow', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TopLowerLine_13 = visual.Line(win=win, name='TopLowerLine_13',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    LowerText_13 = visual.TextStim(win=win, ori=0, name='LowerText_13',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=2,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-10.0)
    LowerBrackets_13 = visual.TextStim(win=win, ori=0, name='LowerBrackets_13',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=None,
        color='cyan', colorSpace='rgb', opacity=1,
        depth=-11.0)
    BotLowerLine_13 = visual.Line(win=win, name='BotLowerLine_13',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TrialCrossHair_13 = visual.TextStim(win=win, ori=0, name='TrialCrossHair_13',
        text='+',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='green', colorSpace='rgb', opacity=1,
        depth=-13.0)
    RestCrossHair_13 = visual.TextStim(win=win, ori=0, name='RestCrossHair_13',
        text='+',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='red', colorSpace='rgb', opacity=1,
        depth=-14.0)
    text_22 = visual.TextStim(win=win, ori=0, name='text_22',
        text='You will also see a cross hair on the screen',    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-15.0)
    text_23 = visual.TextStim(win=win, ori=0, name='text_23',
        text='Either Green',    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-16.0)
    text_24 = visual.TextStim(win=win, ori=0, name='text_24',
        text='Or RED',    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-17.0)

    # Initialize components for Routine "var_6Letters_0"
    var_6Letters_0Clock = core.Clock()
    text_2 = visual.TextStim(win=win, ori=0, name='text_2',
        text='For this experiment you will see letters at the top of the screen.',    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=1.1,
        color='white', colorSpace='rgb', opacity=1,
        depth=0.0)
    text = visual.TextStim(win=win, ori=0, name='text',
        text='Some of the letters will be enclosed by brackets.',    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-1.0)
    text_6 = visual.TextStim(win=win, ori=0, name='text_6',
        text=u'These are the letters to remember.',    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-2.0)
    text_4 = visual.TextStim(win=win, ori=0, name='text_4',
        text='The letters will be removed, focus on the green cross hair.',    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-3.0)
    ISI_11 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_11')
    TopUpperLine_11 = visual.Line(win=win, name='TopUpperLine_11',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='[1,1,-1]', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    UpperText_11 = visual.TextStim(win=win, ori=0, name='UpperText_11',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-6.0)
    UpperBrackets_11 = visual.TextStim(win=win, ori=0, name='UpperBrackets_11',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-7.0)
    BotUpperLine_11 = visual.Line(win=win, name='BotUpperLine_11',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='yellow', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TopLowerLine_11 = visual.Line(win=win, name='TopLowerLine_11',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    LowerText_11 = visual.TextStim(win=win, ori=0, name='LowerText_11',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=2,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-10.0)
    LowerBrackets_11 = visual.TextStim(win=win, ori=0, name='LowerBrackets_11',
        text='  { }        ',    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=None,
        color='cyan', colorSpace='rgb', opacity=1,
        depth=-11.0)
    BotLowerLine_11 = visual.Line(win=win, name='BotLowerLine_11',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TrialCrossHair_11 = visual.TextStim(win=win, ori=0, name='TrialCrossHair_11',
        text='+',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='green', colorSpace='rgb', opacity=1,
        depth=-13.0)
    RestCrossHair_11 = visual.TextStim(win=win, ori=0, name='RestCrossHair_11',
        text='+',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='red', colorSpace='rgb', opacity=1,
        depth=-14.0)
    text_5 = visual.TextStim(win=win, ori=0, name='text_5',
        text='You will then see letters at the bottom.',    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=1.1,
        color='white', colorSpace='rgb', opacity=1,
        depth=-16.0)
    text_7 = visual.TextStim(win=win, ori=0, name='text_7',
        text='Only one letter will be in brackets.',    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-17.0)
    text_8 = visual.TextStim(win=win, ori=0, name='text_8',
        text='You need to decide whether this letter was one that you had to remember.',    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=1.25,
        color='white', colorSpace='rgb', opacity=1,
        depth=-18.0)
    text_9 = visual.TextStim(win=win, ori=0, name='text_9',
        text='YES = INDEX finger button\nNO  = MIDDLE finger button',    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-19.0)
    text_10 = visual.TextStim(win=win, ori=0, name='text_10',
        text='The trial is then over and the cross hair turns RED.',    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-20.0)

    # Initialize components for Routine "var_6Letters_1"
    var_6Letters_1Clock = core.Clock()
    text_11 = visual.TextStim(win=win, ori=0, name='text_11',
        text=u"Let's Repeat",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=0.0)
    text_12 = visual.TextStim(win=win, ori=0, name='text_12',
        text='Remember the letters B and C',    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=1.25,
        color='white', colorSpace='rgb', opacity=1,
        depth=-1.0)
    text_14 = visual.TextStim(win=win, ori=0, name='text_14',
        text=u'Letters are removed',    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-2.0)
    ISI_12 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_12')
    TopUpperLine_12 = visual.Line(win=win, name='TopUpperLine_12',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='[1,1,-1]', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    UpperText_12 = visual.TextStim(win=win, ori=0, name='UpperText_12',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-5.0)
    UpperBrackets_12 = visual.TextStim(win=win, ori=0, name='UpperBrackets_12',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-6.0)
    BotUpperLine_12 = visual.Line(win=win, name='BotUpperLine_12',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='yellow', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TopLowerLine_12 = visual.Line(win=win, name='TopLowerLine_12',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    LowerText_12 = visual.TextStim(win=win, ori=0, name='LowerText_12',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,-0.3], height=0.2, wrapWidth=2,
        color=[0,0,0], colorSpace=u'rgb', opacity=1,
        depth=-9.0)
    LowerBrackets_12 = visual.TextStim(win=win, ori=0, name='LowerBrackets_12',
        text='  { }        ',    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=None,
        color='cyan', colorSpace='rgb', opacity=1,
        depth=-10.0)
    BotLowerLine_12 = visual.Line(win=win, name='BotLowerLine_12',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TrialCrossHair_12 = visual.TextStim(win=win, ori=0, name='TrialCrossHair_12',
        text='+',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='green', colorSpace='rgb', opacity=1,
        depth=-12.0)
    RestCrossHair_12 = visual.TextStim(win=win, ori=0, name='RestCrossHair_12',
        text='+',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='red', colorSpace='rgb', opacity=1,
        depth=-13.0)
    text_17 = visual.TextStim(win=win, ori=0, name='text_17',
        text=u'Are you trying to remember the letter b?',    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-15.0)
    text_19 = visual.TextStim(win=win, ori=0, name='text_19',
        text=u'Yes you are. You would press the INDEX finger button as quickly as possible.',    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-16.0)
    text_20 = visual.TextStim(win=win, ori=0, name='text_20',
        text=u'The trial is over and the cross hair turns RED.',    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-17.0)

    # Initialize components for Routine "DemoTrialRealTimes"
    DemoTrialRealTimesClock = core.Clock()
    text_44 = visual.TextStim(win=win, ori=0, name='text_44',
        text=u"Let's repeat at the true pace",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=0.0)
    text_45 = visual.TextStim(win=win, ori=0, name='text_45',
        text=u'Remember the letters B and C',    font=u'Lucida Console',
        units=u'norm', pos=[0, 0.8], height=0.1, wrapWidth=1.25,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-1.0)
    text_46 = visual.TextStim(win=win, ori=0, name='text_46',
        text=u'Letters are removed',    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-2.0)
    ISI_18 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_18')
    TopUpperLine_18 = visual.Line(win=win, name='TopUpperLine_18',units=u'norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace=u'rgb',
        fillColor=u'[1,1,-1]', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    UpperText_18 = visual.TextStim(win=win, ori=0, name='UpperText_18',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace=u'rgb', opacity=1,
        depth=-5.0)
    UpperBrackets_18 = visual.TextStim(win=win, ori=0, name='UpperBrackets_18',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=u'yellow', colorSpace=u'rgb', opacity=1,
        depth=-6.0)
    BotUpperLine_18 = visual.Line(win=win, name='BotUpperLine_18',units=u'norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace=u'rgb',
        fillColor=u'yellow', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    TopLowerLine_18 = visual.Line(win=win, name='TopLowerLine_18',units=u'norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor=u'cyan', lineColorSpace=u'rgb',
        fillColor=u'cyan', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    LowerText_17 = visual.TextStim(win=win, ori=0, name='LowerText_17',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,-0.3], height=0.2, wrapWidth=2,
        color=[0,0,0], colorSpace=u'rgb', opacity=1,
        depth=-9.0)
    LowerBrackets_17 = visual.TextStim(win=win, ori=0, name='LowerBrackets_17',
        text=u'  { }        ',    font=u'Lucida Console',
        units=u'norm', pos=[0,-0.3], height=0.2, wrapWidth=None,
        color=u'cyan', colorSpace=u'rgb', opacity=1,
        depth=-10.0)
    BotLowerLine_18 = visual.Line(win=win, name='BotLowerLine_18',units=u'norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor=u'cyan', lineColorSpace=u'rgb',
        fillColor=u'cyan', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    TrialCrossHair_18 = visual.TextStim(win=win, ori=0, name='TrialCrossHair_18',
        text=u'+',    font=u'Lucida Console',
        units=u'norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color=u'green', colorSpace=u'rgb', opacity=1,
        depth=-12.0)
    RestCrossHair_18 = visual.TextStim(win=win, ori=0, name='RestCrossHair_18',
        text=u'+',    font=u'Lucida Console',
        units=u'norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color=u'red', colorSpace=u'rgb', opacity=1,
        depth=-13.0)
    text_48 = visual.TextStim(win=win, ori=0, name='text_48',
        text=u'Respond as quickly as possible',    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-15.0)
    text_49 = visual.TextStim(win=win, ori=0, name='text_49',
        text=u'The trial is over and the cross hair turns RED.',    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-16.0)

    # Initialize components for Routine "NumLettersToRem"
    NumLettersToRemClock = core.Clock()
    text_15 = visual.TextStim(win=win, ori=0, name='text_15',
        text='The number of letters to remember',    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=0.0)
    text_33 = visual.TextStim(win=win, ori=0, name='text_33',
        text='Varies between 1 and 6',    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=1.25,
        color='white', colorSpace='rgb', opacity=1,
        depth=-1.0)
    text_34 = visual.TextStim(win=win, ori=0, name='text_34',
        text='There will always be six letters presented',    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-2.0)
    text_3 = visual.TextStim(win=win, ori=0, name='text_3',
        text='It is the brackets that indicate which letters to remember.',    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-3.0)
    text_35 = visual.TextStim(win=win, ori=0, name='text_35',
        text='Here are some examples',    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-4.0)
    UpBrack1 = visual.TextStim(win=win, ori=0, name='UpBrack1',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-5.0)
    ISI_17 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_17')
    TopUpperLine_17 = visual.Line(win=win, name='TopUpperLine_17',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='[1,1,-1]', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    UpperText_17 = visual.TextStim(win=win, ori=0, name='UpperText_17',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-8.0)
    UpperBrackets_17 = visual.TextStim(win=win, ori=0, name='UpperBrackets_17',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-9.0)
    BotUpperLine_17 = visual.Line(win=win, name='BotUpperLine_17',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='yellow', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TopLowerLine_17 = visual.Line(win=win, name='TopLowerLine_17',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    BotLowerLine_17 = visual.Line(win=win, name='BotLowerLine_17',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TrialCrossHair_17 = visual.TextStim(win=win, ori=0, name='TrialCrossHair_17',
        text='+',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='green', colorSpace='rgb', opacity=1,
        depth=-13.0)
    RestCrossHair_17 = visual.TextStim(win=win, ori=0, name='RestCrossHair_17',
        text=None,    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='red', colorSpace='rgb', opacity=1,
        depth=-14.0)
    UpBrack2 = visual.TextStim(win=win, ori=0, name='UpBrack2',
        text='{   }        ',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-15.0)
    UpBrack3 = visual.TextStim(win=win, ori=0, name='UpBrack3',
        text='      {     }',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='Yellow', colorSpace='rgb', opacity=1,
        depth=-16.0)
    UpBrack4 = visual.TextStim(win=win, ori=0, name='UpBrack4',
        text='  {       }  ',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-17.0)
    UpBrack5 = visual.TextStim(win=win, ori=0, name='UpBrack5',
        text='{         }  ',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-18.0)
    UpBrack6 = visual.TextStim(win=win, ori=0, name='UpBrack6',
        text=u'{           }',    font=u'Lucida Console',
        units=u'norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=u'yellow', colorSpace=u'rgb', opacity=1,
        depth=-19.0)
    text_38 = visual.TextStim(win=win, ori=0, name='text_38',
        text=u'One letter',    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-20.0)
    text_39 = visual.TextStim(win=win, ori=0, name='text_39',
        text=u'Two letters',    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-21.0)
    text_40 = visual.TextStim(win=win, ori=0, name='text_40',
        text=u'Three letters',    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-22.0)
    text_41 = visual.TextStim(win=win, ori=0, name='text_41',
        text=u'Four letters',    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-23.0)
    text_42 = visual.TextStim(win=win, ori=0, name='text_42',
        text=u'Five letters',    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-24.0)
    text_43 = visual.TextStim(win=win, ori=0, name='text_43',
        text=u'Six letters',    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-25.0)

    # Initialize components for Routine "TrialParts_1"
    TrialParts_1Clock = core.Clock()
    text_27 = visual.TextStim(win=win, ori=0, name='text_27',
        text=u'To help with the analysis of the brain data.\nSome trials are PARTIAL.',    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=0.0)
    text_30 = visual.TextStim(win=win, ori=0, name='text_30',
        text='All trials will have a set of letters to study.',    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=1.25,
        color='white', colorSpace='rgb', opacity=1,
        depth=-1.0)
    text_31 = visual.TextStim(win=win, ori=0, name='text_31',
        text='Some will not require a response',    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-2.0)
    text_32 = visual.TextStim(win=win, ori=0, name='text_32',
        text='Some will have no delay between the letters to study and the response.',    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=1.5,
        color='white', colorSpace='rgb', opacity=1,
        depth=-3.0)
    ISI_16 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_16')
    TopUpperLine_16 = visual.Line(win=win, name='TopUpperLine_16',units=u'norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace=u'rgb',
        fillColor=u'[1,1,-1]', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    UpperText_16 = visual.TextStim(win=win, ori=0, name='UpperText_16',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-6.0)
    UpperBrackets_16 = visual.TextStim(win=win, ori=0, name='UpperBrackets_16',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-7.0)
    BotUpperLine_16 = visual.Line(win=win, name='BotUpperLine_16',units=u'norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace=u'rgb',
        fillColor=u'yellow', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    TopLowerLine_16 = visual.Line(win=win, name='TopLowerLine_16',units=u'norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor=u'cyan', lineColorSpace=u'rgb',
        fillColor=u'cyan', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    LowerText_16 = visual.TextStim(win=win, ori=0, name='LowerText_16',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=2,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-10.0)
    LowerBrackets_16 = visual.TextStim(win=win, ori=0, name='LowerBrackets_16',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=None,
        color='cyan', colorSpace='rgb', opacity=1,
        depth=-11.0)
    BotLowerLine_16 = visual.Line(win=win, name='BotLowerLine_16',units=u'norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor=u'cyan', lineColorSpace=u'rgb',
        fillColor=u'cyan', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    TrialCrossHair_16 = visual.TextStim(win=win, ori=0, name='TrialCrossHair_16',
        text=None,    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='green', colorSpace='rgb', opacity=1,
        depth=-13.0)
    RestCrossHair_16 = visual.TextStim(win=win, ori=0, name='RestCrossHair_16',
        text=None,    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='red', colorSpace='rgb', opacity=1,
        depth=-14.0)
    text_36 = visual.TextStim(win=win, ori=0, name='text_36',
        text='What is important is that when the crosshair turns RED. The trial is over.',    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=1.5,
        color='white', colorSpace='rgb', opacity=1,
        depth=-15.0)
    text_37 = visual.TextStim(win=win, ori=0, name='text_37',
        text='Try to forget any of the studied letters and wait for the next trial',    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=1.5,
        color='white', colorSpace='rgb', opacity=1,
        depth=-16.0)
    text_50 = visual.TextStim(win=win, ori=0, name='text_50',
        text=u'Here is an example trial with feedback.\nRemember respond as quickly as possible.',    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-17.0)

    # Initialize components for Routine "trial5_2"
    trial5_2Clock = core.Clock()
    ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
    TopUpperLine = visual.Line(win=win, name='TopUpperLine',units=u'norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace=u'rgb',
        fillColor=u'[1,1,-1]', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    UpperText = visual.TextStim(win=win, ori=0, name='UpperText',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace=u'rgb', opacity=1,
        depth=-2.0)
    UpperBrackets = visual.TextStim(win=win, ori=0, name='UpperBrackets',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=u'yellow', colorSpace=u'rgb', opacity=1,
        depth=-3.0)
    BotUpperLine = visual.Line(win=win, name='BotUpperLine',units=u'norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace=u'rgb',
        fillColor=u'yellow', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    TopLowerLine = visual.Line(win=win, name='TopLowerLine',units=u'norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor=u'cyan', lineColorSpace=u'rgb',
        fillColor=u'cyan', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    LowerText = visual.TextStim(win=win, ori=0, name='LowerText',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,-0.3], height=0.2, wrapWidth=2,
        color=[0,0,0], colorSpace=u'rgb', opacity=1,
        depth=-6.0)
    LowerBrackets = visual.TextStim(win=win, ori=0, name='LowerBrackets',
        text=u'      { }    ',    font=u'Lucida Console',
        units=u'norm', pos=[0,-0.3], height=0.2, wrapWidth=None,
        color=u'cyan', colorSpace=u'rgb', opacity=1,
        depth=-7.0)
    BotLowerLine = visual.Line(win=win, name='BotLowerLine',units=u'norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor=u'cyan', lineColorSpace=u'rgb',
        fillColor=u'cyan', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    TrialCrossHair = visual.TextStim(win=win, ori=0, name='TrialCrossHair',
        text='+',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='green', colorSpace='rgb', opacity=1,
        depth=-9.0)
    RestCrossHair = visual.TextStim(win=win, ori=0, name='RestCrossHair',
        text=u'+',    font=u'Lucida Console',
        units=u'norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color=u'red', colorSpace=u'rgb', opacity=1,
        depth=-10.0)

    # Initialize components for Routine "TrialFeedBack"
    TrialFeedBackClock = core.Clock()
    #msg variable just needs some value at start
    msg=''
    text_47 = visual.TextStim(win=win, ori=0, name='text_47',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0, 0], height=0.1, wrapWidth=1.5,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-1.0)

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=10, method='sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=[None],
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
        
        #------Prepare to start Routine "ButtonPractice"-------
        t = 0
        ButtonPracticeClock.reset()  # clock 
        frameN = -1
        routineTimer.add(120.000000)
        # update component parameters for each repeat
        UpperText_14.setText('')
        UpperBrackets_14.setText('')
        LowerText_14.setText('')
        key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_2.status = NOT_STARTED
        # keep track of which components have finished
        ButtonPracticeComponents = []
        ButtonPracticeComponents.append(text_28)
        ButtonPracticeComponents.append(ISI_14)
        ButtonPracticeComponents.append(TopUpperLine_14)
        ButtonPracticeComponents.append(UpperText_14)
        ButtonPracticeComponents.append(UpperBrackets_14)
        ButtonPracticeComponents.append(BotUpperLine_14)
        ButtonPracticeComponents.append(TopLowerLine_14)
        ButtonPracticeComponents.append(LowerText_14)
        ButtonPracticeComponents.append(LowerBrackets_14)
        ButtonPracticeComponents.append(BotLowerLine_14)
        ButtonPracticeComponents.append(TrialCrossHair_14)
        ButtonPracticeComponents.append(RestCrossHair_14)
        ButtonPracticeComponents.append(key_resp_2)
        for thisComponent in ButtonPracticeComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "ButtonPractice"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ButtonPracticeClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_28* updates
            if t >= 0 and text_28.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_28.tStart = t  # underestimates by a little under one frame
                text_28.frameNStart = frameN  # exact frame index
                text_28.setAutoDraw(True)
            elif text_28.status == STARTED and t >= (0 + (60-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_28.setAutoDraw(False)
            
            # *TopUpperLine_14* updates
            if t >= 0 and TopUpperLine_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                TopUpperLine_14.tStart = t  # underestimates by a little under one frame
                TopUpperLine_14.frameNStart = frameN  # exact frame index
                TopUpperLine_14.setAutoDraw(True)
            elif TopUpperLine_14.status == STARTED and t >= (0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
                TopUpperLine_14.setAutoDraw(False)
            
            # *UpperText_14* updates
            if t >= 0 and UpperText_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                UpperText_14.tStart = t  # underestimates by a little under one frame
                UpperText_14.frameNStart = frameN  # exact frame index
                UpperText_14.setAutoDraw(True)
            elif UpperText_14.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                UpperText_14.setAutoDraw(False)
            
            # *UpperBrackets_14* updates
            if t >= 0 and UpperBrackets_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                UpperBrackets_14.tStart = t  # underestimates by a little under one frame
                UpperBrackets_14.frameNStart = frameN  # exact frame index
                UpperBrackets_14.setAutoDraw(True)
            elif UpperBrackets_14.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                UpperBrackets_14.setAutoDraw(False)
            
            # *BotUpperLine_14* updates
            if t >= 0.0 and BotUpperLine_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                BotUpperLine_14.tStart = t  # underestimates by a little under one frame
                BotUpperLine_14.frameNStart = frameN  # exact frame index
                BotUpperLine_14.setAutoDraw(True)
            elif BotUpperLine_14.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
                BotUpperLine_14.setAutoDraw(False)
            
            # *TopLowerLine_14* updates
            if t >= 0.0 and TopLowerLine_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                TopLowerLine_14.tStart = t  # underestimates by a little under one frame
                TopLowerLine_14.frameNStart = frameN  # exact frame index
                TopLowerLine_14.setAutoDraw(True)
            elif TopLowerLine_14.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
                TopLowerLine_14.setAutoDraw(False)
            
            # *LowerText_14* updates
            if t >= 0 and LowerText_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                LowerText_14.tStart = t  # underestimates by a little under one frame
                LowerText_14.frameNStart = frameN  # exact frame index
                LowerText_14.setAutoDraw(True)
            elif LowerText_14.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                LowerText_14.setAutoDraw(False)
            
            # *LowerBrackets_14* updates
            if t >= 0 and LowerBrackets_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                LowerBrackets_14.tStart = t  # underestimates by a little under one frame
                LowerBrackets_14.frameNStart = frameN  # exact frame index
                LowerBrackets_14.setAutoDraw(True)
            elif LowerBrackets_14.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                LowerBrackets_14.setAutoDraw(False)
            
            # *BotLowerLine_14* updates
            if t >= 0.0 and BotLowerLine_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                BotLowerLine_14.tStart = t  # underestimates by a little under one frame
                BotLowerLine_14.frameNStart = frameN  # exact frame index
                BotLowerLine_14.setAutoDraw(True)
            elif BotLowerLine_14.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
                BotLowerLine_14.setAutoDraw(False)
            
            # *TrialCrossHair_14* updates
            if t >= 0 and TrialCrossHair_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                TrialCrossHair_14.tStart = t  # underestimates by a little under one frame
                TrialCrossHair_14.frameNStart = frameN  # exact frame index
                TrialCrossHair_14.setAutoDraw(True)
            elif TrialCrossHair_14.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                TrialCrossHair_14.setAutoDraw(False)
            
            # *RestCrossHair_14* updates
            if t >= 0 and RestCrossHair_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                RestCrossHair_14.tStart = t  # underestimates by a little under one frame
                RestCrossHair_14.frameNStart = frameN  # exact frame index
                RestCrossHair_14.setAutoDraw(True)
            elif RestCrossHair_14.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                RestCrossHair_14.setAutoDraw(False)
            
            # *key_resp_2* updates
            if t >= 0.0 and key_resp_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_2.tStart = t  # underestimates by a little under one frame
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            elif key_resp_2.status == STARTED and t >= (0.0 + (60-win.monitorFramePeriod*0.75)): #most of one frame period left
                key_resp_2.status = STOPPED
            if key_resp_2.status == STARTED:
                theseKeys = event.getKeys(keyList=AllowedInputKeys)#['1', '2', '3', '4', '5', '6', '7', '8', '9','down','right'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_2.rt = key_resp_2.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_2.keys == str('6')) or (key_resp_2.keys == 'down'):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            # *ISI_14* period
            if t >= 0.0 and ISI_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI_14.tStart = t  # underestimates by a little under one frame
                ISI_14.frameNStart = frameN  # exact frame index
                ISI_14.start(1)
            elif ISI_14.status == STARTED: #one frame should pass before updating params and completing
                ISI_14.complete() #finish the static period
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ButtonPracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                win.close()
                sys.exit()
                #win.close()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "ButtonPractice"-------
        for thisComponent in ButtonPracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
           key_resp_2.keys=None
           # was no response the correct answer?!
           if str('6').lower() == 'none': key_resp_2.corr = 1  # correct non-response
           else: key_resp_2.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_resp_2.keys',key_resp_2.keys)
        trials.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trials.addData('key_resp_2.rt', key_resp_2.rt)
        
        #------Prepare to start Routine "Feedback"-------
        t = 0
        FeedbackClock.reset()  # clock 
        frameN = -1
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        if len(key_resp_2.keys)<1:
            msg="Please press the RIGHT INDEX Finger button"
            trials.finished = Falses
        elif key_resp_2.corr:#stored on last run routine
            msg="Correct! That button indicates a YES response." 
            trials.finished = True
        else:
            msg="Oops! Wrong button, please try again."
            trials.finished = False
        text_25.setText(msg)
        # keep track of which components have finished
        FeedbackComponents = []
        FeedbackComponents.append(text_25)
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Feedback"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_25* updates
            if t >= 0.0 and text_25.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_25.tStart = t  # underestimates by a little under one frame
                text_25.frameNStart = frameN  # exact frame index
                text_25.setAutoDraw(True)
            elif text_25.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_25.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                win.close()
                sys.exit()
                
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Feedback"-------
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed 10 repeats of 'trials'


    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=10, method='random', 
        extraInfo=expInfo, originPath=None,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)

    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2.keys():
                exec(paramName + '= thisTrial_2.' + paramName)
        
        #------Prepare to start Routine "ButtonPractice_MIDDLE"-------
        t = 0
        ButtonPractice_MIDDLEClock.reset()  # clock 
        frameN = -1
        routineTimer.add(20.000000)
        # update component parameters for each repeat
        UpperText_15.setText('')
        UpperBrackets_15.setText('')
        LowerText_15.setText('')
        key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_3.status = NOT_STARTED
        # keep track of which components have finished
        ButtonPractice_MIDDLEComponents = []
        ButtonPractice_MIDDLEComponents.append(text_29)
        ButtonPractice_MIDDLEComponents.append(ISI_15)
        ButtonPractice_MIDDLEComponents.append(TopUpperLine_15)
        ButtonPractice_MIDDLEComponents.append(UpperText_15)
        ButtonPractice_MIDDLEComponents.append(UpperBrackets_15)
        ButtonPractice_MIDDLEComponents.append(BotUpperLine_15)
        ButtonPractice_MIDDLEComponents.append(TopLowerLine_15)
        ButtonPractice_MIDDLEComponents.append(LowerText_15)
        ButtonPractice_MIDDLEComponents.append(LowerBrackets_15)
        ButtonPractice_MIDDLEComponents.append(BotLowerLine_15)
        ButtonPractice_MIDDLEComponents.append(TrialCrossHair_15)
        ButtonPractice_MIDDLEComponents.append(RestCrossHair_15)
        ButtonPractice_MIDDLEComponents.append(key_resp_3)
        for thisComponent in ButtonPractice_MIDDLEComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "ButtonPractice_MIDDLE"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ButtonPractice_MIDDLEClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_29* updates
            if t >= 0 and text_29.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_29.tStart = t  # underestimates by a little under one frame
                text_29.frameNStart = frameN  # exact frame index
                text_29.setAutoDraw(True)
            elif text_29.status == STARTED and t >= (0 + (10-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_29.setAutoDraw(False)
            
            # *TopUpperLine_15* updates
            if t >= 0 and TopUpperLine_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                TopUpperLine_15.tStart = t  # underestimates by a little under one frame
                TopUpperLine_15.frameNStart = frameN  # exact frame index
                TopUpperLine_15.setAutoDraw(True)
            elif TopUpperLine_15.status == STARTED and t >= (0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
                TopUpperLine_15.setAutoDraw(False)
            
            # *UpperText_15* updates
            if t >= 0 and UpperText_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                UpperText_15.tStart = t  # underestimates by a little under one frame
                UpperText_15.frameNStart = frameN  # exact frame index
                UpperText_15.setAutoDraw(True)
            elif UpperText_15.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                UpperText_15.setAutoDraw(False)
            
            # *UpperBrackets_15* updates
            if t >= 0 and UpperBrackets_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                UpperBrackets_15.tStart = t  # underestimates by a little under one frame
                UpperBrackets_15.frameNStart = frameN  # exact frame index
                UpperBrackets_15.setAutoDraw(True)
            elif UpperBrackets_15.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                UpperBrackets_15.setAutoDraw(False)
            
            # *BotUpperLine_15* updates
            if t >= 0.0 and BotUpperLine_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                BotUpperLine_15.tStart = t  # underestimates by a little under one frame
                BotUpperLine_15.frameNStart = frameN  # exact frame index
                BotUpperLine_15.setAutoDraw(True)
            elif BotUpperLine_15.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
                BotUpperLine_15.setAutoDraw(False)
            
            # *TopLowerLine_15* updates
            if t >= 0.0 and TopLowerLine_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                TopLowerLine_15.tStart = t  # underestimates by a little under one frame
                TopLowerLine_15.frameNStart = frameN  # exact frame index
                TopLowerLine_15.setAutoDraw(True)
            elif TopLowerLine_15.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
                TopLowerLine_15.setAutoDraw(False)
            
            # *LowerText_15* updates
            if t >= 0 and LowerText_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                LowerText_15.tStart = t  # underestimates by a little under one frame
                LowerText_15.frameNStart = frameN  # exact frame index
                LowerText_15.setAutoDraw(True)
            elif LowerText_15.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                LowerText_15.setAutoDraw(False)
            
            # *LowerBrackets_15* updates
            if t >= 0 and LowerBrackets_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                LowerBrackets_15.tStart = t  # underestimates by a little under one frame
                LowerBrackets_15.frameNStart = frameN  # exact frame index
                LowerBrackets_15.setAutoDraw(True)
            elif LowerBrackets_15.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                LowerBrackets_15.setAutoDraw(False)
            
            # *BotLowerLine_15* updates
            if t >= 0.0 and BotLowerLine_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                BotLowerLine_15.tStart = t  # underestimates by a little under one frame
                BotLowerLine_15.frameNStart = frameN  # exact frame index
                BotLowerLine_15.setAutoDraw(True)
            elif BotLowerLine_15.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
                BotLowerLine_15.setAutoDraw(False)
            
            # *TrialCrossHair_15* updates
            if t >= 0 and TrialCrossHair_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                TrialCrossHair_15.tStart = t  # underestimates by a little under one frame
                TrialCrossHair_15.frameNStart = frameN  # exact frame index
                TrialCrossHair_15.setAutoDraw(True)
            elif TrialCrossHair_15.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                TrialCrossHair_15.setAutoDraw(False)
            
            # *RestCrossHair_15* updates
            if t >= 0 and RestCrossHair_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                RestCrossHair_15.tStart = t  # underestimates by a little under one frame
                RestCrossHair_15.frameNStart = frameN  # exact frame index
                RestCrossHair_15.setAutoDraw(True)
            elif RestCrossHair_15.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                RestCrossHair_15.setAutoDraw(False)
            
            # *key_resp_3* updates
            if t >= 0.0 and key_resp_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_3.tStart = t  # underestimates by a little under one frame
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                key_resp_3.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            elif key_resp_3.status == STARTED and t >= (0.0 + (10-win.monitorFramePeriod*0.75)): #most of one frame period left
                key_resp_3.status = STOPPED
            if key_resp_3.status == STARTED:
                theseKeys = event.getKeys(keyList=AllowedInputKeys)#['1', '2', '3', '4', '5', '6', '7', '8', '9','down','right'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_3.rt = key_resp_3.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_3.keys == str('7')) or (key_resp_3.keys == 'right'):
                        key_resp_3.corr = 1
                    else:
                        key_resp_3.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            # *ISI_15* period
            if t >= 0.0 and ISI_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI_15.tStart = t  # underestimates by a little under one frame
                ISI_15.frameNStart = frameN  # exact frame index
                ISI_15.start(1)
            elif ISI_15.status == STARTED: #one frame should pass before updating params and completing
                ISI_15.complete() #finish the static period
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ButtonPractice_MIDDLEComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                win.close()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "ButtonPractice_MIDDLE"-------
        for thisComponent in ButtonPractice_MIDDLEComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
           key_resp_3.keys=None
           # was no response the correct answer?!
           if str('7').lower() == 'none': key_resp_3.corr = 1  # correct non-response
           else: key_resp_3.corr = 0  # failed to respond (incorrectly)
        # store data for trials_2 (TrialHandler)
        trials_2.addData('key_resp_3.keys',key_resp_3.keys)
        trials_2.addData('key_resp_3.corr', key_resp_3.corr)
        if key_resp_3.keys != None:  # we had a response
            trials_2.addData('key_resp_3.rt', key_resp_3.rt)
        
        #------Prepare to start Routine "Feedback_MIDDLE"-------
        t = 0
        Feedback_MIDDLEClock.reset()  # clock 
        frameN = -1
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        if len(key_resp_3.keys)<1:
            msg="Please press the RIGHT MIDDLE Finger button"
            trials_2.finished = Falses
        elif key_resp_3.corr:#stored on last run routine
            msg="Good! That button indicates a NO response." 
            trials_2.finished = True
        else:
            msg="Oops! Wrong button, please try again."
            trials_2.finished = False
        text_26.setText(msg)
        # keep track of which components have finished
        Feedback_MIDDLEComponents = []
        Feedback_MIDDLEComponents.append(text_26)
        for thisComponent in Feedback_MIDDLEComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Feedback_MIDDLE"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Feedback_MIDDLEClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_26* updates
            if t >= 0.0 and text_26.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_26.tStart = t  # underestimates by a little under one frame
                text_26.frameNStart = frameN  # exact frame index
                text_26.setAutoDraw(True)
            elif text_26.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_26.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Feedback_MIDDLEComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                win.close()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Feedback_MIDDLE"-------
        for thisComponent in Feedback_MIDDLEComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed 10 repeats of 'trials_2'


    #------Prepare to start Routine "var_6Letters_2"-------
    t = 0
    var_6Letters_2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    UpperText_13.setText('')
    UpperBrackets_13.setText('')
    LowerText_13.setText('')
    # keep track of which components have finished
    var_6Letters_2Components = []
    var_6Letters_2Components.append(text_13)
    var_6Letters_2Components.append(text_16)
    var_6Letters_2Components.append(text_18)
    var_6Letters_2Components.append(text_21)
    var_6Letters_2Components.append(ISI_13)
    var_6Letters_2Components.append(TopUpperLine_13)
    var_6Letters_2Components.append(UpperText_13)
    var_6Letters_2Components.append(UpperBrackets_13)
    var_6Letters_2Components.append(BotUpperLine_13)
    var_6Letters_2Components.append(TopLowerLine_13)
    var_6Letters_2Components.append(LowerText_13)
    var_6Letters_2Components.append(LowerBrackets_13)
    var_6Letters_2Components.append(BotLowerLine_13)
    var_6Letters_2Components.append(TrialCrossHair_13)
    var_6Letters_2Components.append(RestCrossHair_13)
    var_6Letters_2Components.append(text_22)
    var_6Letters_2Components.append(text_23)
    var_6Letters_2Components.append(text_24)
    for thisComponent in var_6Letters_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "var_6Letters_2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = var_6Letters_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_13* updates
        if t >= 0.0 and text_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_13.tStart = t  # underestimates by a little under one frame
            text_13.frameNStart = frameN  # exact frame index
            text_13.setAutoDraw(True)
        elif text_13.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_13.setAutoDraw(False)
        
        # *text_16* updates
        if t >= 3 and text_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_16.tStart = t  # underestimates by a little under one frame
            text_16.frameNStart = frameN  # exact frame index
            text_16.setAutoDraw(True)
        elif text_16.status == STARTED and t >= (3 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_16.setAutoDraw(False)
        
        # *text_18* updates
        if t >= 6 and text_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_18.tStart = t  # underestimates by a little under one frame
            text_18.frameNStart = frameN  # exact frame index
            text_18.setAutoDraw(True)
        elif text_18.status == STARTED and t >= (6 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_18.setAutoDraw(False)
        
        # *text_21* updates
        if t >= 0 and text_21.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_21.tStart = t  # underestimates by a little under one frame
            text_21.frameNStart = frameN  # exact frame index
            text_21.setAutoDraw(True)
        elif text_21.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_21.setAutoDraw(False)
        
        # *TopUpperLine_13* updates
        if t >= 0 and TopUpperLine_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopUpperLine_13.tStart = t  # underestimates by a little under one frame
            TopUpperLine_13.frameNStart = frameN  # exact frame index
            TopUpperLine_13.setAutoDraw(True)
        elif TopUpperLine_13.status == STARTED and t >= (0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopUpperLine_13.setAutoDraw(False)
        
        # *UpperText_13* updates
        if t >= 0 and UpperText_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperText_13.tStart = t  # underestimates by a little under one frame
            UpperText_13.frameNStart = frameN  # exact frame index
            UpperText_13.setAutoDraw(True)
        elif UpperText_13.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperText_13.setAutoDraw(False)
        
        # *UpperBrackets_13* updates
        if t >= 0 and UpperBrackets_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBrackets_13.tStart = t  # underestimates by a little under one frame
            UpperBrackets_13.frameNStart = frameN  # exact frame index
            UpperBrackets_13.setAutoDraw(True)
        elif UpperBrackets_13.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBrackets_13.setAutoDraw(False)
        
        # *BotUpperLine_13* updates
        if t >= 0.0 and BotUpperLine_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotUpperLine_13.tStart = t  # underestimates by a little under one frame
            BotUpperLine_13.frameNStart = frameN  # exact frame index
            BotUpperLine_13.setAutoDraw(True)
        elif BotUpperLine_13.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotUpperLine_13.setAutoDraw(False)
        
        # *TopLowerLine_13* updates
        if t >= 0.0 and TopLowerLine_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopLowerLine_13.tStart = t  # underestimates by a little under one frame
            TopLowerLine_13.frameNStart = frameN  # exact frame index
            TopLowerLine_13.setAutoDraw(True)
        elif TopLowerLine_13.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopLowerLine_13.setAutoDraw(False)
        
        # *LowerText_13* updates
        if t >= 0 and LowerText_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerText_13.tStart = t  # underestimates by a little under one frame
            LowerText_13.frameNStart = frameN  # exact frame index
            LowerText_13.setAutoDraw(True)
        elif LowerText_13.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerText_13.setAutoDraw(False)
        
        # *LowerBrackets_13* updates
        if t >= 0 and LowerBrackets_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerBrackets_13.tStart = t  # underestimates by a little under one frame
            LowerBrackets_13.frameNStart = frameN  # exact frame index
            LowerBrackets_13.setAutoDraw(True)
        elif LowerBrackets_13.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerBrackets_13.setAutoDraw(False)
        
        # *BotLowerLine_13* updates
        if t >= 0.0 and BotLowerLine_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotLowerLine_13.tStart = t  # underestimates by a little under one frame
            BotLowerLine_13.frameNStart = frameN  # exact frame index
            BotLowerLine_13.setAutoDraw(True)
        elif BotLowerLine_13.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotLowerLine_13.setAutoDraw(False)
        
        # *TrialCrossHair_13* updates
        if t >= 12 and TrialCrossHair_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialCrossHair_13.tStart = t  # underestimates by a little under one frame
            TrialCrossHair_13.frameNStart = frameN  # exact frame index
            TrialCrossHair_13.setAutoDraw(True)
        elif TrialCrossHair_13.status == STARTED and t >= (12 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            TrialCrossHair_13.setAutoDraw(False)
        
        # *RestCrossHair_13* updates
        if t >= 15 and RestCrossHair_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair_13.tStart = t  # underestimates by a little under one frame
            RestCrossHair_13.frameNStart = frameN  # exact frame index
            RestCrossHair_13.setAutoDraw(True)
        elif RestCrossHair_13.status == STARTED and t >= (15 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair_13.setAutoDraw(False)
        
        # *text_22* updates
        if t >= 9 and text_22.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_22.tStart = t  # underestimates by a little under one frame
            text_22.frameNStart = frameN  # exact frame index
            text_22.setAutoDraw(True)
        elif text_22.status == STARTED and t >= (9 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_22.setAutoDraw(False)
        
        # *text_23* updates
        if t >= 12 and text_23.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_23.tStart = t  # underestimates by a little under one frame
            text_23.frameNStart = frameN  # exact frame index
            text_23.setAutoDraw(True)
        elif text_23.status == STARTED and t >= (12 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_23.setAutoDraw(False)
        
        # *text_24* updates
        if t >= 15 and text_24.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_24.tStart = t  # underestimates by a little under one frame
            text_24.frameNStart = frameN  # exact frame index
            text_24.setAutoDraw(True)
        elif text_24.status == STARTED and t >= (15 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_24.setAutoDraw(False)
        # *ISI_13* period
        if t >= 0.0 and ISI_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_13.tStart = t  # underestimates by a little under one frame
            ISI_13.frameNStart = frameN  # exact frame index
            ISI_13.start(1)
        elif ISI_13.status == STARTED: #one frame should pass before updating params and completing
            ISI_13.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in var_6Letters_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "var_6Letters_2"-------
    for thisComponent in var_6Letters_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #------Prepare to start Routine "var_6Letters_0"-------
    t = 0
    var_6Letters_0Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(30.000000)
    # update component parameters for each repeat
    UpperText_11.setText(' A B C D E F ')
    UpperBrackets_11.setText('  {   }      ')
    LowerText_11.setText(' a b c d e f ')
    KeyboardResp_11 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyboardResp_11.status = NOT_STARTED
    # keep track of which components have finished
    var_6Letters_0Components = []
    var_6Letters_0Components.append(text_2)
    var_6Letters_0Components.append(text)
    var_6Letters_0Components.append(text_6)
    var_6Letters_0Components.append(text_4)
    var_6Letters_0Components.append(ISI_11)
    var_6Letters_0Components.append(TopUpperLine_11)
    var_6Letters_0Components.append(UpperText_11)
    var_6Letters_0Components.append(UpperBrackets_11)
    var_6Letters_0Components.append(BotUpperLine_11)
    var_6Letters_0Components.append(TopLowerLine_11)
    var_6Letters_0Components.append(LowerText_11)
    var_6Letters_0Components.append(LowerBrackets_11)
    var_6Letters_0Components.append(BotLowerLine_11)
    var_6Letters_0Components.append(TrialCrossHair_11)
    var_6Letters_0Components.append(RestCrossHair_11)
    var_6Letters_0Components.append(KeyboardResp_11)
    var_6Letters_0Components.append(text_5)
    var_6Letters_0Components.append(text_7)
    var_6Letters_0Components.append(text_8)
    var_6Letters_0Components.append(text_9)
    var_6Letters_0Components.append(text_10)
    for thisComponent in var_6Letters_0Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "var_6Letters_0"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = var_6Letters_0Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        elif text_2.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_2.setAutoDraw(False)
        
        # *text* updates
        if t >= 3 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # underestimates by a little under one frame
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        elif text.status == STARTED and t >= (3 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text.setAutoDraw(False)
        
        # *text_6* updates
        if t >= 6 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t  # underestimates by a little under one frame
            text_6.frameNStart = frameN  # exact frame index
            text_6.setAutoDraw(True)
        elif text_6.status == STARTED and t >= (6 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_6.setAutoDraw(False)
        
        # *text_4* updates
        if t >= 9 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t  # underestimates by a little under one frame
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        elif text_4.status == STARTED and t >= (9 + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_4.setAutoDraw(False)
        
        # *TopUpperLine_11* updates
        if t >= 0 and TopUpperLine_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopUpperLine_11.tStart = t  # underestimates by a little under one frame
            TopUpperLine_11.frameNStart = frameN  # exact frame index
            TopUpperLine_11.setAutoDraw(True)
        elif TopUpperLine_11.status == STARTED and t >= (0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopUpperLine_11.setAutoDraw(False)
        
        # *UpperText_11* updates
        if t >= 0 and UpperText_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperText_11.tStart = t  # underestimates by a little under one frame
            UpperText_11.frameNStart = frameN  # exact frame index
            UpperText_11.setAutoDraw(True)
        elif UpperText_11.status == STARTED and t >= (0 + (9-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperText_11.setAutoDraw(False)
        
        # *UpperBrackets_11* updates
        if t >= 3 and UpperBrackets_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBrackets_11.tStart = t  # underestimates by a little under one frame
            UpperBrackets_11.frameNStart = frameN  # exact frame index
            UpperBrackets_11.setAutoDraw(True)
        elif UpperBrackets_11.status == STARTED and t >= (3 + (6-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBrackets_11.setAutoDraw(False)
        
        # *BotUpperLine_11* updates
        if t >= 0.0 and BotUpperLine_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotUpperLine_11.tStart = t  # underestimates by a little under one frame
            BotUpperLine_11.frameNStart = frameN  # exact frame index
            BotUpperLine_11.setAutoDraw(True)
        elif BotUpperLine_11.status == STARTED and t >= (0.0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotUpperLine_11.setAutoDraw(False)
        
        # *TopLowerLine_11* updates
        if t >= 0.0 and TopLowerLine_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopLowerLine_11.tStart = t  # underestimates by a little under one frame
            TopLowerLine_11.frameNStart = frameN  # exact frame index
            TopLowerLine_11.setAutoDraw(True)
        elif TopLowerLine_11.status == STARTED and t >= (0.0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopLowerLine_11.setAutoDraw(False)
        
        # *LowerText_11* updates
        if t >= 14 and LowerText_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerText_11.tStart = t  # underestimates by a little under one frame
            LowerText_11.frameNStart = frameN  # exact frame index
            LowerText_11.setAutoDraw(True)
        elif LowerText_11.status == STARTED and t >= (14 + (9-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerText_11.setAutoDraw(False)
        
        # *LowerBrackets_11* updates
        if t >= 17 and LowerBrackets_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerBrackets_11.tStart = t  # underestimates by a little under one frame
            LowerBrackets_11.frameNStart = frameN  # exact frame index
            LowerBrackets_11.setAutoDraw(True)
        elif LowerBrackets_11.status == STARTED and t >= (17 + (6-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerBrackets_11.setAutoDraw(False)
        
        # *BotLowerLine_11* updates
        if t >= 0.0 and BotLowerLine_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotLowerLine_11.tStart = t  # underestimates by a little under one frame
            BotLowerLine_11.frameNStart = frameN  # exact frame index
            BotLowerLine_11.setAutoDraw(True)
        elif BotLowerLine_11.status == STARTED and t >= (0.0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotLowerLine_11.setAutoDraw(False)
        
        # *TrialCrossHair_11* updates
        if t >= 0 and TrialCrossHair_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialCrossHair_11.tStart = t  # underestimates by a little under one frame
            TrialCrossHair_11.frameNStart = frameN  # exact frame index
            TrialCrossHair_11.setAutoDraw(True)
        elif TrialCrossHair_11.status == STARTED and t >= (0 + (26-win.monitorFramePeriod*0.75)): #most of one frame period left
            TrialCrossHair_11.setAutoDraw(False)
        
        # *RestCrossHair_11* updates
        if t >= 26 and RestCrossHair_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair_11.tStart = t  # underestimates by a little under one frame
            RestCrossHair_11.frameNStart = frameN  # exact frame index
            RestCrossHair_11.setAutoDraw(True)
        elif RestCrossHair_11.status == STARTED and t >= (26 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair_11.setAutoDraw(False)
        
        # *KeyboardResp_11* updates
        if t >= 0 and KeyboardResp_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyboardResp_11.tStart = t  # underestimates by a little under one frame
            KeyboardResp_11.frameNStart = frameN  # exact frame index
            KeyboardResp_11.status = STARTED
            # keyboard checking is just starting
            KeyboardResp_11.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif KeyboardResp_11.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyboardResp_11.status = STOPPED
        if KeyboardResp_11.status == STARTED:
            theseKeys = event.getKeys(keyList=AllowedInputKeys)#['1', '2', '3', '4', '5', '6', '7', '8','down','right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                KeyboardResp_11.keys.extend(theseKeys)  # storing all keys
                KeyboardResp_11.rt.append(KeyboardResp_11.clock.getTime())
        
        # *text_5* updates
        if t >= 14 and text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_5.tStart = t  # underestimates by a little under one frame
            text_5.frameNStart = frameN  # exact frame index
            text_5.setAutoDraw(True)
        elif text_5.status == STARTED and t >= (14 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_5.setAutoDraw(False)
        
        # *text_7* updates
        if t >= 17 and text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_7.tStart = t  # underestimates by a little under one frame
            text_7.frameNStart = frameN  # exact frame index
            text_7.setAutoDraw(True)
        elif text_7.status == STARTED and t >= (17 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_7.setAutoDraw(False)
        
        # *text_8* updates
        if t >= 20 and text_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_8.tStart = t  # underestimates by a little under one frame
            text_8.frameNStart = frameN  # exact frame index
            text_8.setAutoDraw(True)
        elif text_8.status == STARTED and t >= (20 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_8.setAutoDraw(False)
        
        # *text_9* updates
        if t >= 23 and text_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_9.tStart = t  # underestimates by a little under one frame
            text_9.frameNStart = frameN  # exact frame index
            text_9.setAutoDraw(True)
        elif text_9.status == STARTED and t >= (23 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_9.setAutoDraw(False)
        
        # *text_10* updates
        if t >= 26 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t  # underestimates by a little under one frame
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        elif text_10.status == STARTED and t >= (26 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_10.setAutoDraw(False)
        # *ISI_11* period
        if t >= 0.0 and ISI_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_11.tStart = t  # underestimates by a little under one frame
            ISI_11.frameNStart = frameN  # exact frame index
            ISI_11.start(1)
        elif ISI_11.status == STARTED: #one frame should pass before updating params and completing
            ISI_11.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in var_6Letters_0Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "var_6Letters_0"-------
    for thisComponent in var_6Letters_0Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyboardResp_11.keys in ['', [], None]:  # No response was made
       KeyboardResp_11.keys=None
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('KeyboardResp_11.keys',KeyboardResp_11.keys)
    if KeyboardResp_11.keys != None:  # we had a response
        thisExp.addData('KeyboardResp_11.rt', KeyboardResp_11.rt)
    thisExp.nextEntry()

    #------Prepare to start Routine "var_6Letters_1"-------
    t = 0
    var_6Letters_1Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(22.000000)
    # update component parameters for each repeat
    UpperText_12.setText(' A B C D E F ')
    UpperBrackets_12.setText('  {   }      ')
    LowerText_12.setText(u' a b c d e f ')
    KeyboardResp_12 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyboardResp_12.status = NOT_STARTED
    # keep track of which components have finished
    var_6Letters_1Components = []
    var_6Letters_1Components.append(text_11)
    var_6Letters_1Components.append(text_12)
    var_6Letters_1Components.append(text_14)
    var_6Letters_1Components.append(ISI_12)
    var_6Letters_1Components.append(TopUpperLine_12)
    var_6Letters_1Components.append(UpperText_12)
    var_6Letters_1Components.append(UpperBrackets_12)
    var_6Letters_1Components.append(BotUpperLine_12)
    var_6Letters_1Components.append(TopLowerLine_12)
    var_6Letters_1Components.append(LowerText_12)
    var_6Letters_1Components.append(LowerBrackets_12)
    var_6Letters_1Components.append(BotLowerLine_12)
    var_6Letters_1Components.append(TrialCrossHair_12)
    var_6Letters_1Components.append(RestCrossHair_12)
    var_6Letters_1Components.append(KeyboardResp_12)
    var_6Letters_1Components.append(text_17)
    var_6Letters_1Components.append(text_19)
    var_6Letters_1Components.append(text_20)
    for thisComponent in var_6Letters_1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "var_6Letters_1"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = var_6Letters_1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_11* updates
        if t >= 0.0 and text_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_11.tStart = t  # underestimates by a little under one frame
            text_11.frameNStart = frameN  # exact frame index
            text_11.setAutoDraw(True)
        elif text_11.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_11.setAutoDraw(False)
        
        # *text_12* updates
        if t >= 3 and text_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_12.tStart = t  # underestimates by a little under one frame
            text_12.frameNStart = frameN  # exact frame index
            text_12.setAutoDraw(True)
        elif text_12.status == STARTED and t >= (3 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_12.setAutoDraw(False)
        
        # *text_14* updates
        if t >= 6 and text_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_14.tStart = t  # underestimates by a little under one frame
            text_14.frameNStart = frameN  # exact frame index
            text_14.setAutoDraw(True)
        elif text_14.status == STARTED and t >= (6 + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_14.setAutoDraw(False)
        
        # *TopUpperLine_12* updates
        if t >= 0 and TopUpperLine_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopUpperLine_12.tStart = t  # underestimates by a little under one frame
            TopUpperLine_12.frameNStart = frameN  # exact frame index
            TopUpperLine_12.setAutoDraw(True)
        elif TopUpperLine_12.status == STARTED and t >= (0 + (22-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopUpperLine_12.setAutoDraw(False)
        
        # *UpperText_12* updates
        if t >= 0 and UpperText_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperText_12.tStart = t  # underestimates by a little under one frame
            UpperText_12.frameNStart = frameN  # exact frame index
            UpperText_12.setAutoDraw(True)
        elif UpperText_12.status == STARTED and t >= (0 + (6-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperText_12.setAutoDraw(False)
        
        # *UpperBrackets_12* updates
        if t >= 3 and UpperBrackets_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBrackets_12.tStart = t  # underestimates by a little under one frame
            UpperBrackets_12.frameNStart = frameN  # exact frame index
            UpperBrackets_12.setAutoDraw(True)
        elif UpperBrackets_12.status == STARTED and t >= (3 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBrackets_12.setAutoDraw(False)
        
        # *BotUpperLine_12* updates
        if t >= 0.0 and BotUpperLine_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotUpperLine_12.tStart = t  # underestimates by a little under one frame
            BotUpperLine_12.frameNStart = frameN  # exact frame index
            BotUpperLine_12.setAutoDraw(True)
        elif BotUpperLine_12.status == STARTED and t >= (0.0 + (22-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotUpperLine_12.setAutoDraw(False)
        
        # *TopLowerLine_12* updates
        if t >= 0.0 and TopLowerLine_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopLowerLine_12.tStart = t  # underestimates by a little under one frame
            TopLowerLine_12.frameNStart = frameN  # exact frame index
            TopLowerLine_12.setAutoDraw(True)
        elif TopLowerLine_12.status == STARTED and t >= (0.0 + (22-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopLowerLine_12.setAutoDraw(False)
        
        # *LowerText_12* updates
        if t >= 11 and LowerText_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerText_12.tStart = t  # underestimates by a little under one frame
            LowerText_12.frameNStart = frameN  # exact frame index
            LowerText_12.setAutoDraw(True)
        elif LowerText_12.status == STARTED and t >= (11 + (6-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerText_12.setAutoDraw(False)
        
        # *LowerBrackets_12* updates
        if t >= 11 and LowerBrackets_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerBrackets_12.tStart = t  # underestimates by a little under one frame
            LowerBrackets_12.frameNStart = frameN  # exact frame index
            LowerBrackets_12.setAutoDraw(True)
        elif LowerBrackets_12.status == STARTED and t >= (11 + (6-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerBrackets_12.setAutoDraw(False)
        
        # *BotLowerLine_12* updates
        if t >= 0.0 and BotLowerLine_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotLowerLine_12.tStart = t  # underestimates by a little under one frame
            BotLowerLine_12.frameNStart = frameN  # exact frame index
            BotLowerLine_12.setAutoDraw(True)
        elif BotLowerLine_12.status == STARTED and t >= (0.0 + (22-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotLowerLine_12.setAutoDraw(False)
        
        # *TrialCrossHair_12* updates
        if t >= 0 and TrialCrossHair_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialCrossHair_12.tStart = t  # underestimates by a little under one frame
            TrialCrossHair_12.frameNStart = frameN  # exact frame index
            TrialCrossHair_12.setAutoDraw(True)
        elif TrialCrossHair_12.status == STARTED and t >= (0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
            TrialCrossHair_12.setAutoDraw(False)
        
        # *RestCrossHair_12* updates
        if t >= 17 and RestCrossHair_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair_12.tStart = t  # underestimates by a little under one frame
            RestCrossHair_12.frameNStart = frameN  # exact frame index
            RestCrossHair_12.setAutoDraw(True)
        elif RestCrossHair_12.status == STARTED and t >= (17 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair_12.setAutoDraw(False)
        
        # *KeyboardResp_12* updates
        if t >= 0 and KeyboardResp_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyboardResp_12.tStart = t  # underestimates by a little under one frame
            KeyboardResp_12.frameNStart = frameN  # exact frame index
            KeyboardResp_12.status = STARTED
            # keyboard checking is just starting
            KeyboardResp_12.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif KeyboardResp_12.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyboardResp_12.status = STOPPED
        if KeyboardResp_12.status == STARTED:
            theseKeys = event.getKeys(keyList=AllowedInputKeys)#['1', '2', '3', '4', '5', '6', '7', '8','down','right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                KeyboardResp_12.keys.extend(theseKeys)  # storing all keys
                KeyboardResp_12.rt.append(KeyboardResp_12.clock.getTime())
        
        # *text_17* updates
        if t >= 11 and text_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_17.tStart = t  # underestimates by a little under one frame
            text_17.frameNStart = frameN  # exact frame index
            text_17.setAutoDraw(True)
        elif text_17.status == STARTED and t >= (11 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_17.setAutoDraw(False)
        
        # *text_19* updates
        if t >= 14 and text_19.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_19.tStart = t  # underestimates by a little under one frame
            text_19.frameNStart = frameN  # exact frame index
            text_19.setAutoDraw(True)
        elif text_19.status == STARTED and t >= (14 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_19.setAutoDraw(False)
        
        # *text_20* updates
        if t >= 17 and text_20.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_20.tStart = t  # underestimates by a little under one frame
            text_20.frameNStart = frameN  # exact frame index
            text_20.setAutoDraw(True)
        elif text_20.status == STARTED and t >= (17 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_20.setAutoDraw(False)
        # *ISI_12* period
        if t >= 0.0 and ISI_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_12.tStart = t  # underestimates by a little under one frame
            ISI_12.frameNStart = frameN  # exact frame index
            ISI_12.start(1)
        elif ISI_12.status == STARTED: #one frame should pass before updating params and completing
            ISI_12.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in var_6Letters_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "var_6Letters_1"-------
    for thisComponent in var_6Letters_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyboardResp_12.keys in ['', [], None]:  # No response was made
       KeyboardResp_12.keys=None
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('KeyboardResp_12.keys',KeyboardResp_12.keys)
    if KeyboardResp_12.keys != None:  # we had a response
        thisExp.addData('KeyboardResp_12.rt', KeyboardResp_12.rt)
    thisExp.nextEntry()

    #------Prepare to start Routine "DemoTrialRealTimes"-------
    t = 0
    DemoTrialRealTimesClock.reset()  # clock 
    frameN = -1
    routineTimer.add(17.000000)
    # update component parameters for each repeat
    UpperText_18.setText(u' A B C D E F ')
    UpperBrackets_18.setText(u'  {   }      ')
    LowerText_17.setText(u' a b c d e f ')
    KeyboardResp_13 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyboardResp_13.status = NOT_STARTED
    # keep track of which components have finished
    DemoTrialRealTimesComponents = []
    DemoTrialRealTimesComponents.append(text_44)
    DemoTrialRealTimesComponents.append(text_45)
    DemoTrialRealTimesComponents.append(text_46)
    DemoTrialRealTimesComponents.append(ISI_18)
    DemoTrialRealTimesComponents.append(TopUpperLine_18)
    DemoTrialRealTimesComponents.append(UpperText_18)
    DemoTrialRealTimesComponents.append(UpperBrackets_18)
    DemoTrialRealTimesComponents.append(BotUpperLine_18)
    DemoTrialRealTimesComponents.append(TopLowerLine_18)
    DemoTrialRealTimesComponents.append(LowerText_17)
    DemoTrialRealTimesComponents.append(LowerBrackets_17)
    DemoTrialRealTimesComponents.append(BotLowerLine_18)
    DemoTrialRealTimesComponents.append(TrialCrossHair_18)
    DemoTrialRealTimesComponents.append(RestCrossHair_18)
    DemoTrialRealTimesComponents.append(KeyboardResp_13)
    DemoTrialRealTimesComponents.append(text_48)
    DemoTrialRealTimesComponents.append(text_49)
    for thisComponent in DemoTrialRealTimesComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "DemoTrialRealTimes"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = DemoTrialRealTimesClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_44* updates
        if t >= 0.0 and text_44.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_44.tStart = t  # underestimates by a little under one frame
            text_44.frameNStart = frameN  # exact frame index
            text_44.setAutoDraw(True)
        elif text_44.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_44.setAutoDraw(False)
        
        # *text_45* updates
        if t >= 3 and text_45.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_45.tStart = t  # underestimates by a little under one frame
            text_45.frameNStart = frameN  # exact frame index
            text_45.setAutoDraw(True)
        elif text_45.status == STARTED and t >= (3 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_45.setAutoDraw(False)
        
        # *text_46* updates
        if t >= 5 and text_46.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_46.tStart = t  # underestimates by a little under one frame
            text_46.frameNStart = frameN  # exact frame index
            text_46.setAutoDraw(True)
        elif text_46.status == STARTED and t >= (5 + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_46.setAutoDraw(False)
        
        # *TopUpperLine_18* updates
        if t >= 0 and TopUpperLine_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopUpperLine_18.tStart = t  # underestimates by a little under one frame
            TopUpperLine_18.frameNStart = frameN  # exact frame index
            TopUpperLine_18.setAutoDraw(True)
        elif TopUpperLine_18.status == STARTED and t >= (0 + (17-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopUpperLine_18.setAutoDraw(False)
        
        # *UpperText_18* updates
        if t >= 3 and UpperText_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperText_18.tStart = t  # underestimates by a little under one frame
            UpperText_18.frameNStart = frameN  # exact frame index
            UpperText_18.setAutoDraw(True)
        elif UpperText_18.status == STARTED and t >= (3 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperText_18.setAutoDraw(False)
        
        # *UpperBrackets_18* updates
        if t >= 3 and UpperBrackets_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBrackets_18.tStart = t  # underestimates by a little under one frame
            UpperBrackets_18.frameNStart = frameN  # exact frame index
            UpperBrackets_18.setAutoDraw(True)
        elif UpperBrackets_18.status == STARTED and t >= (3 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBrackets_18.setAutoDraw(False)
        
        # *BotUpperLine_18* updates
        if t >= 0.0 and BotUpperLine_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotUpperLine_18.tStart = t  # underestimates by a little under one frame
            BotUpperLine_18.frameNStart = frameN  # exact frame index
            BotUpperLine_18.setAutoDraw(True)
        elif BotUpperLine_18.status == STARTED and t >= (0.0 + (17-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotUpperLine_18.setAutoDraw(False)
        
        # *TopLowerLine_18* updates
        if t >= 0.0 and TopLowerLine_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopLowerLine_18.tStart = t  # underestimates by a little under one frame
            TopLowerLine_18.frameNStart = frameN  # exact frame index
            TopLowerLine_18.setAutoDraw(True)
        elif TopLowerLine_18.status == STARTED and t >= (0.0 + (17-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopLowerLine_18.setAutoDraw(False)
        
        # *LowerText_17* updates
        if t >= 10 and LowerText_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerText_17.tStart = t  # underestimates by a little under one frame
            LowerText_17.frameNStart = frameN  # exact frame index
            LowerText_17.setAutoDraw(True)
        elif LowerText_17.status == STARTED and t >= (10 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerText_17.setAutoDraw(False)
        
        # *LowerBrackets_17* updates
        if t >= 10 and LowerBrackets_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerBrackets_17.tStart = t  # underestimates by a little under one frame
            LowerBrackets_17.frameNStart = frameN  # exact frame index
            LowerBrackets_17.setAutoDraw(True)
        elif LowerBrackets_17.status == STARTED and t >= (10 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerBrackets_17.setAutoDraw(False)
        
        # *BotLowerLine_18* updates
        if t >= 0.0 and BotLowerLine_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotLowerLine_18.tStart = t  # underestimates by a little under one frame
            BotLowerLine_18.frameNStart = frameN  # exact frame index
            BotLowerLine_18.setAutoDraw(True)
        elif BotLowerLine_18.status == STARTED and t >= (0.0 + (17-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotLowerLine_18.setAutoDraw(False)
        
        # *TrialCrossHair_18* updates
        if t >= 0 and TrialCrossHair_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialCrossHair_18.tStart = t  # underestimates by a little under one frame
            TrialCrossHair_18.frameNStart = frameN  # exact frame index
            TrialCrossHair_18.setAutoDraw(True)
        elif TrialCrossHair_18.status == STARTED and t >= (0 + (12-win.monitorFramePeriod*0.75)): #most of one frame period left
            TrialCrossHair_18.setAutoDraw(False)
        
        # *RestCrossHair_18* updates
        if t >= 12 and RestCrossHair_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair_18.tStart = t  # underestimates by a little under one frame
            RestCrossHair_18.frameNStart = frameN  # exact frame index
            RestCrossHair_18.setAutoDraw(True)
        elif RestCrossHair_18.status == STARTED and t >= (12 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair_18.setAutoDraw(False)
        
        # *KeyboardResp_13* updates
        if t >= 0 and KeyboardResp_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyboardResp_13.tStart = t  # underestimates by a little under one frame
            KeyboardResp_13.frameNStart = frameN  # exact frame index
            KeyboardResp_13.status = STARTED
            # keyboard checking is just starting
            KeyboardResp_13.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif KeyboardResp_13.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyboardResp_13.status = STOPPED
        if KeyboardResp_13.status == STARTED:
            theseKeys = event.getKeys(keyList=AllowedInputKeys)#['1', '2', '3', '4', '5', '6', '7', '8'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                KeyboardResp_13.keys.extend(theseKeys)  # storing all keys
                KeyboardResp_13.rt.append(KeyboardResp_13.clock.getTime())
        
        # *text_48* updates
        if t >= 10 and text_48.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_48.tStart = t  # underestimates by a little under one frame
            text_48.frameNStart = frameN  # exact frame index
            text_48.setAutoDraw(True)
        elif text_48.status == STARTED and t >= (10 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_48.setAutoDraw(False)
        
        # *text_49* updates
        if t >= 12 and text_49.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_49.tStart = t  # underestimates by a little under one frame
            text_49.frameNStart = frameN  # exact frame index
            text_49.setAutoDraw(True)
        elif text_49.status == STARTED and t >= (12 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_49.setAutoDraw(False)
        # *ISI_18* period
        if t >= 0.0 and ISI_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_18.tStart = t  # underestimates by a little under one frame
            ISI_18.frameNStart = frameN  # exact frame index
            ISI_18.start(1)
        elif ISI_18.status == STARTED: #one frame should pass before updating params and completing
            ISI_18.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DemoTrialRealTimesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "DemoTrialRealTimes"-------
    for thisComponent in DemoTrialRealTimesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyboardResp_13.keys in ['', [], None]:  # No response was made
       KeyboardResp_13.keys=None
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('KeyboardResp_13.keys',KeyboardResp_13.keys)
    if KeyboardResp_13.keys != None:  # we had a response
        thisExp.addData('KeyboardResp_13.rt', KeyboardResp_13.rt)
    thisExp.nextEntry()

    #------Prepare to start Routine "NumLettersToRem"-------
    t = 0
    NumLettersToRemClock.reset()  # clock 
    frameN = -1
    routineTimer.add(30.000000)
    # update component parameters for each repeat
    UpBrack1.setText('        { }  ')
    UpperText_17.setText(' A B C D E F ')
    UpperBrackets_17.setText('')
    # keep track of which components have finished
    NumLettersToRemComponents = []
    NumLettersToRemComponents.append(text_15)
    NumLettersToRemComponents.append(text_33)
    NumLettersToRemComponents.append(text_34)
    NumLettersToRemComponents.append(text_3)
    NumLettersToRemComponents.append(text_35)
    NumLettersToRemComponents.append(UpBrack1)
    NumLettersToRemComponents.append(ISI_17)
    NumLettersToRemComponents.append(TopUpperLine_17)
    NumLettersToRemComponents.append(UpperText_17)
    NumLettersToRemComponents.append(UpperBrackets_17)
    NumLettersToRemComponents.append(BotUpperLine_17)
    NumLettersToRemComponents.append(TopLowerLine_17)
    NumLettersToRemComponents.append(BotLowerLine_17)
    NumLettersToRemComponents.append(TrialCrossHair_17)
    NumLettersToRemComponents.append(RestCrossHair_17)
    NumLettersToRemComponents.append(UpBrack2)
    NumLettersToRemComponents.append(UpBrack3)
    NumLettersToRemComponents.append(UpBrack4)
    NumLettersToRemComponents.append(UpBrack5)
    NumLettersToRemComponents.append(UpBrack6)
    NumLettersToRemComponents.append(text_38)
    NumLettersToRemComponents.append(text_39)
    NumLettersToRemComponents.append(text_40)
    NumLettersToRemComponents.append(text_41)
    NumLettersToRemComponents.append(text_42)
    NumLettersToRemComponents.append(text_43)
    for thisComponent in NumLettersToRemComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "NumLettersToRem"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = NumLettersToRemClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_15* updates
        if t >= 0.0 and text_15.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_15.tStart = t  # underestimates by a little under one frame
            text_15.frameNStart = frameN  # exact frame index
            text_15.setAutoDraw(True)
        elif text_15.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_15.setAutoDraw(False)
        
        # *text_33* updates
        if t >= 3 and text_33.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_33.tStart = t  # underestimates by a little under one frame
            text_33.frameNStart = frameN  # exact frame index
            text_33.setAutoDraw(True)
        elif text_33.status == STARTED and t >= (3 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_33.setAutoDraw(False)
        
        # *text_34* updates
        if t >= 6 and text_34.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_34.tStart = t  # underestimates by a little under one frame
            text_34.frameNStart = frameN  # exact frame index
            text_34.setAutoDraw(True)
        elif text_34.status == STARTED and t >= (6 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_34.setAutoDraw(False)
        
        # *text_3* updates
        if t >= 9 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        elif text_3.status == STARTED and t >= (9 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_3.setAutoDraw(False)
        
        # *text_35* updates
        if t >= 12 and text_35.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_35.tStart = t  # underestimates by a little under one frame
            text_35.frameNStart = frameN  # exact frame index
            text_35.setAutoDraw(True)
        elif text_35.status == STARTED and t >= (12 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_35.setAutoDraw(False)
        
        # *UpBrack1* updates
        if t >= 15 and UpBrack1.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpBrack1.tStart = t  # underestimates by a little under one frame
            UpBrack1.frameNStart = frameN  # exact frame index
            UpBrack1.setAutoDraw(True)
        elif UpBrack1.status == STARTED and t >= (15 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpBrack1.setAutoDraw(False)
        
        # *TopUpperLine_17* updates
        if t >= 0 and TopUpperLine_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopUpperLine_17.tStart = t  # underestimates by a little under one frame
            TopUpperLine_17.frameNStart = frameN  # exact frame index
            TopUpperLine_17.setAutoDraw(True)
        elif TopUpperLine_17.status == STARTED and t >= (0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopUpperLine_17.setAutoDraw(False)
        
        # *UpperText_17* updates
        if t >= 0 and UpperText_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperText_17.tStart = t  # underestimates by a little under one frame
            UpperText_17.frameNStart = frameN  # exact frame index
            UpperText_17.setAutoDraw(True)
        elif UpperText_17.status == STARTED and t >= (0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperText_17.setAutoDraw(False)
        
        # *UpperBrackets_17* updates
        if t >= 0.0 and UpperBrackets_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBrackets_17.tStart = t  # underestimates by a little under one frame
            UpperBrackets_17.frameNStart = frameN  # exact frame index
            UpperBrackets_17.setAutoDraw(True)
        elif UpperBrackets_17.status == STARTED and t >= (0.0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBrackets_17.setAutoDraw(False)
        
        # *BotUpperLine_17* updates
        if t >= 0.0 and BotUpperLine_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotUpperLine_17.tStart = t  # underestimates by a little under one frame
            BotUpperLine_17.frameNStart = frameN  # exact frame index
            BotUpperLine_17.setAutoDraw(True)
        elif BotUpperLine_17.status == STARTED and t >= (0.0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotUpperLine_17.setAutoDraw(False)
        
        # *TopLowerLine_17* updates
        if t >= 0.0 and TopLowerLine_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopLowerLine_17.tStart = t  # underestimates by a little under one frame
            TopLowerLine_17.frameNStart = frameN  # exact frame index
            TopLowerLine_17.setAutoDraw(True)
        elif TopLowerLine_17.status == STARTED and t >= (0.0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopLowerLine_17.setAutoDraw(False)
        
        # *BotLowerLine_17* updates
        if t >= 0.0 and BotLowerLine_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotLowerLine_17.tStart = t  # underestimates by a little under one frame
            BotLowerLine_17.frameNStart = frameN  # exact frame index
            BotLowerLine_17.setAutoDraw(True)
        elif BotLowerLine_17.status == STARTED and t >= (0.0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotLowerLine_17.setAutoDraw(False)
        
        # *TrialCrossHair_17* updates
        if t >= 0 and TrialCrossHair_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialCrossHair_17.tStart = t  # underestimates by a little under one frame
            TrialCrossHair_17.frameNStart = frameN  # exact frame index
            TrialCrossHair_17.setAutoDraw(True)
        elif TrialCrossHair_17.status == STARTED and t >= (0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            TrialCrossHair_17.setAutoDraw(False)
        
        # *RestCrossHair_17* updates
        if t >= 0.0 and RestCrossHair_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair_17.tStart = t  # underestimates by a little under one frame
            RestCrossHair_17.frameNStart = frameN  # exact frame index
            RestCrossHair_17.setAutoDraw(True)
        elif RestCrossHair_17.status == STARTED and t >= (0.0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair_17.setAutoDraw(False)
        
        # *UpBrack2* updates
        if t >= 18 and UpBrack2.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpBrack2.tStart = t  # underestimates by a little under one frame
            UpBrack2.frameNStart = frameN  # exact frame index
            UpBrack2.setAutoDraw(True)
        elif UpBrack2.status == STARTED and t >= (18 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpBrack2.setAutoDraw(False)
        
        # *UpBrack3* updates
        if t >= 20 and UpBrack3.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpBrack3.tStart = t  # underestimates by a little under one frame
            UpBrack3.frameNStart = frameN  # exact frame index
            UpBrack3.setAutoDraw(True)
        elif UpBrack3.status == STARTED and t >= (20 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpBrack3.setAutoDraw(False)
        
        # *UpBrack4* updates
        if t >= 22 and UpBrack4.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpBrack4.tStart = t  # underestimates by a little under one frame
            UpBrack4.frameNStart = frameN  # exact frame index
            UpBrack4.setAutoDraw(True)
        elif UpBrack4.status == STARTED and t >= (22 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpBrack4.setAutoDraw(False)
        
        # *UpBrack5* updates
        if t >= 24 and UpBrack5.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpBrack5.tStart = t  # underestimates by a little under one frame
            UpBrack5.frameNStart = frameN  # exact frame index
            UpBrack5.setAutoDraw(True)
        elif UpBrack5.status == STARTED and t >= (24 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpBrack5.setAutoDraw(False)
        
        # *UpBrack6* updates
        if t >= 26 and UpBrack6.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpBrack6.tStart = t  # underestimates by a little under one frame
            UpBrack6.frameNStart = frameN  # exact frame index
            UpBrack6.setAutoDraw(True)
        elif UpBrack6.status == STARTED and t >= (26 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpBrack6.setAutoDraw(False)
        
        # *text_38* updates
        if t >= 15 and text_38.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_38.tStart = t  # underestimates by a little under one frame
            text_38.frameNStart = frameN  # exact frame index
            text_38.setAutoDraw(True)
        elif text_38.status == STARTED and t >= (15 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_38.setAutoDraw(False)
        
        # *text_39* updates
        if t >= 18 and text_39.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_39.tStart = t  # underestimates by a little under one frame
            text_39.frameNStart = frameN  # exact frame index
            text_39.setAutoDraw(True)
        elif text_39.status == STARTED and t >= (18 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_39.setAutoDraw(False)
        
        # *text_40* updates
        if t >= 20 and text_40.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_40.tStart = t  # underestimates by a little under one frame
            text_40.frameNStart = frameN  # exact frame index
            text_40.setAutoDraw(True)
        elif text_40.status == STARTED and t >= (20 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_40.setAutoDraw(False)
        
        # *text_41* updates
        if t >= 22 and text_41.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_41.tStart = t  # underestimates by a little under one frame
            text_41.frameNStart = frameN  # exact frame index
            text_41.setAutoDraw(True)
        elif text_41.status == STARTED and t >= (22 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_41.setAutoDraw(False)
        
        # *text_42* updates
        if t >= 24 and text_42.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_42.tStart = t  # underestimates by a little under one frame
            text_42.frameNStart = frameN  # exact frame index
            text_42.setAutoDraw(True)
        elif text_42.status == STARTED and t >= (24 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_42.setAutoDraw(False)
        
        # *text_43* updates
        if t >= 26 and text_43.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_43.tStart = t  # underestimates by a little under one frame
            text_43.frameNStart = frameN  # exact frame index
            text_43.setAutoDraw(True)
        elif text_43.status == STARTED and t >= (26 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_43.setAutoDraw(False)
        # *ISI_17* period
        if t >= 0.0 and ISI_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_17.tStart = t  # underestimates by a little under one frame
            ISI_17.frameNStart = frameN  # exact frame index
            ISI_17.start(1)
        elif ISI_17.status == STARTED: #one frame should pass before updating params and completing
            ISI_17.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NumLettersToRemComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "NumLettersToRem"-------
    for thisComponent in NumLettersToRemComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #------Prepare to start Routine "TrialParts_1"-------
    t = 0
    TrialParts_1Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(25.000000)
    # update component parameters for each repeat
    UpperText_16.setText('')
    UpperBrackets_16.setText('')
    LowerText_16.setText('')
    # keep track of which components have finished
    TrialParts_1Components = []
    TrialParts_1Components.append(text_27)
    TrialParts_1Components.append(text_30)
    TrialParts_1Components.append(text_31)
    TrialParts_1Components.append(text_32)
    TrialParts_1Components.append(ISI_16)
    TrialParts_1Components.append(TopUpperLine_16)
    TrialParts_1Components.append(UpperText_16)
    TrialParts_1Components.append(UpperBrackets_16)
    TrialParts_1Components.append(BotUpperLine_16)
    TrialParts_1Components.append(TopLowerLine_16)
    TrialParts_1Components.append(LowerText_16)
    TrialParts_1Components.append(LowerBrackets_16)
    TrialParts_1Components.append(BotLowerLine_16)
    TrialParts_1Components.append(TrialCrossHair_16)
    TrialParts_1Components.append(RestCrossHair_16)
    TrialParts_1Components.append(text_36)
    TrialParts_1Components.append(text_37)
    TrialParts_1Components.append(text_50)
    for thisComponent in TrialParts_1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "TrialParts_1"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TrialParts_1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_27* updates
        if t >= 0.0 and text_27.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_27.tStart = t  # underestimates by a little under one frame
            text_27.frameNStart = frameN  # exact frame index
            text_27.setAutoDraw(True)
        elif text_27.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_27.setAutoDraw(False)
        
        # *text_30* updates
        if t >= 3 and text_30.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_30.tStart = t  # underestimates by a little under one frame
            text_30.frameNStart = frameN  # exact frame index
            text_30.setAutoDraw(True)
        elif text_30.status == STARTED and t >= (3 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_30.setAutoDraw(False)
        
        # *text_31* updates
        if t >= 6 and text_31.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_31.tStart = t  # underestimates by a little under one frame
            text_31.frameNStart = frameN  # exact frame index
            text_31.setAutoDraw(True)
        elif text_31.status == STARTED and t >= (6 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_31.setAutoDraw(False)
        
        # *text_32* updates
        if t >= 9 and text_32.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_32.tStart = t  # underestimates by a little under one frame
            text_32.frameNStart = frameN  # exact frame index
            text_32.setAutoDraw(True)
        elif text_32.status == STARTED and t >= (9 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_32.setAutoDraw(False)
        
        # *TopUpperLine_16* updates
        if t >= 0 and TopUpperLine_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopUpperLine_16.tStart = t  # underestimates by a little under one frame
            TopUpperLine_16.frameNStart = frameN  # exact frame index
            TopUpperLine_16.setAutoDraw(True)
        elif TopUpperLine_16.status == STARTED and t >= (0 + (25-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopUpperLine_16.setAutoDraw(False)
        
        # *UpperText_16* updates
        if t >= 0 and UpperText_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperText_16.tStart = t  # underestimates by a little under one frame
            UpperText_16.frameNStart = frameN  # exact frame index
            UpperText_16.setAutoDraw(True)
        elif UpperText_16.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperText_16.setAutoDraw(False)
        
        # *UpperBrackets_16* updates
        if t >= 0 and UpperBrackets_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBrackets_16.tStart = t  # underestimates by a little under one frame
            UpperBrackets_16.frameNStart = frameN  # exact frame index
            UpperBrackets_16.setAutoDraw(True)
        elif UpperBrackets_16.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBrackets_16.setAutoDraw(False)
        
        # *BotUpperLine_16* updates
        if t >= 0.0 and BotUpperLine_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotUpperLine_16.tStart = t  # underestimates by a little under one frame
            BotUpperLine_16.frameNStart = frameN  # exact frame index
            BotUpperLine_16.setAutoDraw(True)
        elif BotUpperLine_16.status == STARTED and t >= (0.0 + (25-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotUpperLine_16.setAutoDraw(False)
        
        # *TopLowerLine_16* updates
        if t >= 0.0 and TopLowerLine_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopLowerLine_16.tStart = t  # underestimates by a little under one frame
            TopLowerLine_16.frameNStart = frameN  # exact frame index
            TopLowerLine_16.setAutoDraw(True)
        elif TopLowerLine_16.status == STARTED and t >= (0.0 + (25-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopLowerLine_16.setAutoDraw(False)
        
        # *LowerText_16* updates
        if t >= 0 and LowerText_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerText_16.tStart = t  # underestimates by a little under one frame
            LowerText_16.frameNStart = frameN  # exact frame index
            LowerText_16.setAutoDraw(True)
        elif LowerText_16.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerText_16.setAutoDraw(False)
        
        # *LowerBrackets_16* updates
        if t >= 0 and LowerBrackets_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerBrackets_16.tStart = t  # underestimates by a little under one frame
            LowerBrackets_16.frameNStart = frameN  # exact frame index
            LowerBrackets_16.setAutoDraw(True)
        elif LowerBrackets_16.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerBrackets_16.setAutoDraw(False)
        
        # *BotLowerLine_16* updates
        if t >= 0.0 and BotLowerLine_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotLowerLine_16.tStart = t  # underestimates by a little under one frame
            BotLowerLine_16.frameNStart = frameN  # exact frame index
            BotLowerLine_16.setAutoDraw(True)
        elif BotLowerLine_16.status == STARTED and t >= (0.0 + (25-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotLowerLine_16.setAutoDraw(False)
        
        # *TrialCrossHair_16* updates
        if t >= 0 and TrialCrossHair_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialCrossHair_16.tStart = t  # underestimates by a little under one frame
            TrialCrossHair_16.frameNStart = frameN  # exact frame index
            TrialCrossHair_16.setAutoDraw(True)
        elif TrialCrossHair_16.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            TrialCrossHair_16.setAutoDraw(False)
        
        # *RestCrossHair_16* updates
        if t >= 0 and RestCrossHair_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair_16.tStart = t  # underestimates by a little under one frame
            RestCrossHair_16.frameNStart = frameN  # exact frame index
            RestCrossHair_16.setAutoDraw(True)
        elif RestCrossHair_16.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair_16.setAutoDraw(False)
        
        # *text_36* updates
        if t >= 12 and text_36.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_36.tStart = t  # underestimates by a little under one frame
            text_36.frameNStart = frameN  # exact frame index
            text_36.setAutoDraw(True)
        elif text_36.status == STARTED and t >= (12 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_36.setAutoDraw(False)
        
        # *text_37* updates
        if t >= 15 and text_37.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_37.tStart = t  # underestimates by a little under one frame
            text_37.frameNStart = frameN  # exact frame index
            text_37.setAutoDraw(True)
        elif text_37.status == STARTED and t >= (15 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_37.setAutoDraw(False)
        
        # *text_50* updates
        if t >= 20 and text_50.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_50.tStart = t  # underestimates by a little under one frame
            text_50.frameNStart = frameN  # exact frame index
            text_50.setAutoDraw(True)
        elif text_50.status == STARTED and t >= (20 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_50.setAutoDraw(False)
        # *ISI_16* period
        if t >= 0.0 and ISI_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_16.tStart = t  # underestimates by a little under one frame
            ISI_16.frameNStart = frameN  # exact frame index
            ISI_16.start(1)
        elif ISI_16.status == STARTED: #one frame should pass before updating params and completing
            ISI_16.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialParts_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "TrialParts_1"-------
    for thisComponent in TrialParts_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #------Prepare to start Routine "trial5_2"-------
    t = 0
    trial5_2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(11.000000)
    # update component parameters for each repeat
    UpperText.setText(u' L K R G M X ')
    UpperBrackets.setText(u'  {         }')
    LowerText.setText(u' b t y g q j ')
    resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    resp.status = NOT_STARTED
    # keep track of which components have finished
    trial5_2Components = []
    trial5_2Components.append(ISI)
    trial5_2Components.append(TopUpperLine)
    trial5_2Components.append(UpperText)
    trial5_2Components.append(UpperBrackets)
    trial5_2Components.append(BotUpperLine)
    trial5_2Components.append(TopLowerLine)
    trial5_2Components.append(LowerText)
    trial5_2Components.append(LowerBrackets)
    trial5_2Components.append(BotLowerLine)
    trial5_2Components.append(TrialCrossHair)
    trial5_2Components.append(RestCrossHair)
    trial5_2Components.append(resp)
    for thisComponent in trial5_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "trial5_2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial5_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TopUpperLine* updates
        if t >= 0 and TopUpperLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopUpperLine.tStart = t  # underestimates by a little under one frame
            TopUpperLine.frameNStart = frameN  # exact frame index
            TopUpperLine.setAutoDraw(True)
        elif TopUpperLine.status == STARTED and t >= (0 + (11-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopUpperLine.setAutoDraw(False)
        
        # *UpperText* updates
        if t >= 0 and UpperText.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperText.tStart = t  # underestimates by a little under one frame
            UpperText.frameNStart = frameN  # exact frame index
            UpperText.setAutoDraw(True)
        elif UpperText.status == STARTED and t >= (0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperText.setAutoDraw(False)
        
        # *UpperBrackets* updates
        if t >= 0.0 and UpperBrackets.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBrackets.tStart = t  # underestimates by a little under one frame
            UpperBrackets.frameNStart = frameN  # exact frame index
            UpperBrackets.setAutoDraw(True)
        elif UpperBrackets.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBrackets.setAutoDraw(False)
        
        # *BotUpperLine* updates
        if t >= 0.0 and BotUpperLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotUpperLine.tStart = t  # underestimates by a little under one frame
            BotUpperLine.frameNStart = frameN  # exact frame index
            BotUpperLine.setAutoDraw(True)
        elif BotUpperLine.status == STARTED and t >= (0.0 + (11-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotUpperLine.setAutoDraw(False)
        
        # *TopLowerLine* updates
        if t >= 0.0 and TopLowerLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopLowerLine.tStart = t  # underestimates by a little under one frame
            TopLowerLine.frameNStart = frameN  # exact frame index
            TopLowerLine.setAutoDraw(True)
        elif TopLowerLine.status == STARTED and t >= (0.0 + (11-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopLowerLine.setAutoDraw(False)
        
        # *LowerText* updates
        if t >= 7 and LowerText.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerText.tStart = t  # underestimates by a little under one frame
            LowerText.frameNStart = frameN  # exact frame index
            LowerText.setAutoDraw(True)
        elif LowerText.status == STARTED and t >= (7 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerText.setAutoDraw(False)
        
        # *LowerBrackets* updates
        if t >= 7 and LowerBrackets.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerBrackets.tStart = t  # underestimates by a little under one frame
            LowerBrackets.frameNStart = frameN  # exact frame index
            LowerBrackets.setAutoDraw(True)
        elif LowerBrackets.status == STARTED and t >= (7 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerBrackets.setAutoDraw(False)
        
        # *BotLowerLine* updates
        if t >= 0.0 and BotLowerLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotLowerLine.tStart = t  # underestimates by a little under one frame
            BotLowerLine.frameNStart = frameN  # exact frame index
            BotLowerLine.setAutoDraw(True)
        elif BotLowerLine.status == STARTED and t >= (0.0 + (11-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotLowerLine.setAutoDraw(False)
        
        # *TrialCrossHair* updates
        if t >= 0 and TrialCrossHair.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialCrossHair.tStart = t  # underestimates by a little under one frame
            TrialCrossHair.frameNStart = frameN  # exact frame index
            TrialCrossHair.setAutoDraw(True)
        elif TrialCrossHair.status == STARTED and t >= (0 + (9-win.monitorFramePeriod*0.75)): #most of one frame period left
            TrialCrossHair.setAutoDraw(False)
        
        # *RestCrossHair* updates
        if t >= 9 and RestCrossHair.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair.tStart = t  # underestimates by a little under one frame
            RestCrossHair.frameNStart = frameN  # exact frame index
            RestCrossHair.setAutoDraw(True)
        elif RestCrossHair.status == STARTED and t >= (9 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair.setAutoDraw(False)
        
        # *resp* updates
        if t >= 7 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t  # underestimates by a little under one frame
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            resp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif resp.status == STARTED and t >= (7 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            resp.status = STOPPED
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=AllowedInputKeys)#['1', '2', '3', '4', '5', '6', '7', '8'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp.keys = theseKeys[-1]  # just the last key pressed
                resp.rt = resp.clock.getTime()
                # was this 'correct'?
                if (resp.keys == str(u'6')) or (resp.keys == u'6'):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
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
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial5_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "trial5_2"-------
    for thisComponent in trial5_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
       resp.keys=None
       # was no response the correct answer?!
       if str(u'6').lower() == 'none': resp.corr = 1  # correct non-response
       else: resp.corr = 0  # failed to respond (incorrectly)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('resp.keys',resp.keys)
    thisExp.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        thisExp.addData('resp.rt', resp.rt)
    thisExp.nextEntry()

    #------Prepare to start Routine "TrialFeedBack"-------
    t = 0
    TrialFeedBackClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    if ((resp.corr) & (resp.rt < 2.0)):#stored on last run routine
      msg="Correct and on time! RT=%.3f" %(resp.rt)
    elif ((resp.corr) & (resp.rt > 2.0)):#stored on last run routine
      msg="Correct, but too slow!\n RT=%.3f\nResponse time should be less than two seconds." %(resp.rt)
    else:
      if resp.rt < 2.0:
        msg="Oops! That was incorrect, but on time!"
      else: 
        msg="Oops! That was incorrect and too slow!"
    text_47.setText(msg)
    # keep track of which components have finished
    TrialFeedBackComponents = []
    TrialFeedBackComponents.append(text_47)
    for thisComponent in TrialFeedBackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "TrialFeedBack"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TrialFeedBackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_47* updates
        if t >= 0.0 and text_47.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_47.tStart = t  # underestimates by a little under one frame
            text_47.frameNStart = frameN  # exact frame index
            text_47.setAutoDraw(True)
        elif text_47.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_47.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialFeedBackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "TrialFeedBack"-------
    for thisComponent in TrialFeedBackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    msg='Ended'
    win.close()
#    win.close()

def Test(subid,visitid):
    expInfo = {u'Visit ID': u'9999', u'Participant ID': u'1'}
    print 'subid is %s'%(subid)
    if subid == '9999':
        dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    else:
        expInfo['Participant ID']=subid
        expInfo['Visit ID']=visitid    
    # Store info about the experiment session

    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + 'data/%s_%s_%s_%s' %(expInfo['Participant ID'], expInfo['Visit ID'],expName, expInfo['date'])

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath=None,
        savePickle=True, saveWideText=False,
        dataFileName=filename)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

    endExpNow = False  # flag for 'escape' or other condition => quit the exp

    # Start Code - component code to be run before the window creation

    # Setup the Window
    win = visual.Window(size=[800, 600], fullscr=FullScreenFlag, screen=0, allowGUI=True, allowStencil=False,
        monitor=ScreenToUse, color=[-1,-1,-1], colorSpace='rgb',
        blendMode='average', useFBO=True,
        units='cm')
    # store frame rate of monitor if we can measure it successfully
    expInfo['frameRate']=win.getActualFrameRate()
    if expInfo['frameRate']!=None:
        frameDur = 1.0/round(expInfo['frameRate'])
    else:
        frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

    # Initialize components for Routine "trial_2"
    trial_2Clock = core.Clock()
    ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
    TopUpperLine = visual.Line(win=win, name='TopUpperLine',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='[1,1,-1]', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    UpperText = visual.TextStim(win=win, ori=0, name='UpperText',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0, 0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-2.0)
    UpperBrackets = visual.TextStim(win=win, ori=0, name='UpperBrackets',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0, 0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-3.0)
    BotUpperLine = visual.Line(win=win, name='BotUpperLine',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='yellow', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TopLowerLine = visual.Line(win=win, name='TopLowerLine',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    LowerText = visual.TextStim(win=win, ori=0, name='LowerText',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=2,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-6.0)
    LowerBrackets = visual.TextStim(win=win, ori=0, name='LowerBrackets',
        text='      { }    ',    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=None,
        color='cyan', colorSpace='rgb', opacity=1,
        depth=-7.0)
    BotLowerLine = visual.Line(win=win, name='BotLowerLine',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TrialCrossHair = visual.TextStim(win=win, ori=0, name='TrialCrossHair',
        text='+',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='green', colorSpace='rgb', opacity=1,
        depth=-9.0)
    RestCrossHair = visual.TextStim(win=win, ori=0, name='RestCrossHair',
        text='+',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='red', colorSpace='rgb', opacity=1,
        depth=-10.0)

    # Initialize components for Routine "TrialFeedBack"
    TrialFeedBackClock = core.Clock()
    #msg variable just needs some value at start
    msg=''
    text = visual.TextStim(win=win, ori=0, name='text',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.1, wrapWidth=1.5,
        color='white', colorSpace='rgb', opacity=1,
        depth=-1.0)

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

    #------Prepare to start Routine "trial_2"-------
    t = 0
    trial_2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(11.000000)
    # update component parameters for each repeat
    UpperText.setText(' A B C D E F ')
    UpperBrackets.setText('  {         }')
    LowerText.setText(' a b c d e f ')
    resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    resp.status = NOT_STARTED
    # keep track of which components have finished
    trial_2Components = []
    trial_2Components.append(ISI)
    trial_2Components.append(TopUpperLine)
    trial_2Components.append(UpperText)
    trial_2Components.append(UpperBrackets)
    trial_2Components.append(BotUpperLine)
    trial_2Components.append(TopLowerLine)
    trial_2Components.append(LowerText)
    trial_2Components.append(LowerBrackets)
    trial_2Components.append(BotLowerLine)
    trial_2Components.append(TrialCrossHair)
    trial_2Components.append(RestCrossHair)
    trial_2Components.append(resp)
    for thisComponent in trial_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "trial_2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TopUpperLine* updates
        if t >= 0 and TopUpperLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopUpperLine.tStart = t  # underestimates by a little under one frame
            TopUpperLine.frameNStart = frameN  # exact frame index
            TopUpperLine.setAutoDraw(True)
        elif TopUpperLine.status == STARTED and t >= (0 + (11-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopUpperLine.setAutoDraw(False)
        
        # *UpperText* updates
        if t >= 0 and UpperText.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperText.tStart = t  # underestimates by a little under one frame
            UpperText.frameNStart = frameN  # exact frame index
            UpperText.setAutoDraw(True)
        elif UpperText.status == STARTED and t >= (0 + (11-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperText.setAutoDraw(False)
        
        # *UpperBrackets* updates
        if t >= 0.0 and UpperBrackets.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBrackets.tStart = t  # underestimates by a little under one frame
            UpperBrackets.frameNStart = frameN  # exact frame index
            UpperBrackets.setAutoDraw(True)
        elif UpperBrackets.status == STARTED and t >= (0.0 + (11-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBrackets.setAutoDraw(False)
        
        # *BotUpperLine* updates
        if t >= 0.0 and BotUpperLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotUpperLine.tStart = t  # underestimates by a little under one frame
            BotUpperLine.frameNStart = frameN  # exact frame index
            BotUpperLine.setAutoDraw(True)
        elif BotUpperLine.status == STARTED and t >= (0.0 + (11-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotUpperLine.setAutoDraw(False)
        
        # *TopLowerLine* updates
        if t >= 0.0 and TopLowerLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopLowerLine.tStart = t  # underestimates by a little under one frame
            TopLowerLine.frameNStart = frameN  # exact frame index
            TopLowerLine.setAutoDraw(True)
        elif TopLowerLine.status == STARTED and t >= (0.0 + (11-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopLowerLine.setAutoDraw(False)
        
        # *LowerText* updates
        if t >= 7 and LowerText.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerText.tStart = t  # underestimates by a little under one frame
            LowerText.frameNStart = frameN  # exact frame index
            LowerText.setAutoDraw(True)
        elif LowerText.status == STARTED and t >= (0 + (11-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerText.setAutoDraw(False)
        
        # *LowerBrackets* updates
        if t >= 7 and LowerBrackets.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerBrackets.tStart = t  # underestimates by a little under one frame
            LowerBrackets.frameNStart = frameN  # exact frame index
            LowerBrackets.setAutoDraw(True)
        elif LowerBrackets.status == STARTED and t >= (0 + (11-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerBrackets.setAutoDraw(False)
        
        # *BotLowerLine* updates
        if t >= 0.0 and BotLowerLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotLowerLine.tStart = t  # underestimates by a little under one frame
            BotLowerLine.frameNStart = frameN  # exact frame index
            BotLowerLine.setAutoDraw(True)
        elif BotLowerLine.status == STARTED and t >= (0.0 + (11-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotLowerLine.setAutoDraw(False)
        
        # *TrialCrossHair* updates
        if t >= 0 and TrialCrossHair.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialCrossHair.tStart = t  # underestimates by a little under one frame
            TrialCrossHair.frameNStart = frameN  # exact frame index
            TrialCrossHair.setAutoDraw(True)
        elif TrialCrossHair.status == STARTED and t >= (0 + (9-win.monitorFramePeriod*0.75)): #most of one frame period left
            TrialCrossHair.setAutoDraw(False)
        
        # *RestCrossHair* updates
        if t >= 9 and RestCrossHair.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair.tStart = t  # underestimates by a little under one frame
            RestCrossHair.frameNStart = frameN  # exact frame index
            RestCrossHair.setAutoDraw(True)
        elif RestCrossHair.status == STARTED and t >= (9 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair.setAutoDraw(False)
        
        # *resp* updates
        if t >= 7 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t  # underestimates by a little under one frame
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            resp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif resp.status == STARTED and t >= (7 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            resp.status = STOPPED
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=AllowedInputKeys)#['1', '2', '3', '4', '5', '6', '7', '8'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp.keys = theseKeys[-1]  # just the last key pressed
                resp.rt = resp.clock.getTime()
                # was this 'correct'?
                if (resp.keys == str(u'6')) or (resp.keys == u'6'):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
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
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "trial_2"-------
    for thisComponent in trial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
       resp.keys=None
       # was no response the correct answer?!
       if str(u'6').lower() == 'none': resp.corr = 1  # correct non-response
       else: resp.corr = 0  # failed to respond (incorrectly)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('resp.keys',resp.keys)
    thisExp.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        thisExp.addData('resp.rt', resp.rt)
    thisExp.nextEntry()

    #------Prepare to start Routine "TrialFeedBack"-------
    t = 0
    TrialFeedBackClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    if ((resp.corr) & (resp.rt < 2.0)):#stored on last run routine
      msg="Correct and on time! RT=%.3f" %(resp.rt)
    elif ((resp.corr) & (resp.rt > 2.0)):#stored on last run routine
      msg="Correct, but too slow!\n RT=%.3f\nResponse time should be less than two seconds." %(resp.rt)
    else:
      if resp.rt < 2.0:
        msg="Oops! That was incorrect, but on time!"
      else: 
        msg="Oops! That was incorrect and too slow!"
    text.setText(msg)
    # keep track of which components have finished
    TrialFeedBackComponents = []
    TrialFeedBackComponents.append(text)
    for thisComponent in TrialFeedBackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "TrialFeedBack"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TrialFeedBackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # underestimates by a little under one frame
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        elif text.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialFeedBackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "TrialFeedBack"-------
    for thisComponent in TrialFeedBackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    msg='Ended'

    win.close()



# -*- coding: utf-8 -*-
def InstructionsFR():
    # Store info about the experiment session
    expName = u'InstructionsFR'  # from the Builder filename that created this script
    expInfo = {u'session': u'001', u'participant': u''}
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath=None,
        savePickle=True, saveWideText=False,
        dataFileName=filename)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

    endExpNow = False  # flag for 'escape' or other condition => quit the exp

    # Start Code - component code to be run before the window creation

    # Setup the Window
    win = visual.Window(size=[800, 600], fullscr=FullScreenFlag, screen=0, allowGUI=True, allowStencil=False,
        monitor=u'UbuntuMon', color=[-1,-1,-1], colorSpace=u'rgb',
        blendMode=u'add', useFBO=True,
        units=u'norm')

    # store frame rate of monitor if we can measure it successfully
    expInfo['frameRate']=win.getActualFrameRate()
    if expInfo['frameRate']!=None:
        frameDur = 1.0/round(expInfo['frameRate'])
    else:
        frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

    # Initialize components for Routine "ButtonPractice"
    ButtonPracticeClock = core.Clock()
    text_28 = visual.TextStim(win=win, ori=0, name='text_28',
        text=u"Tout d'abord, assurons-nous que les boutons fonctionnent. \n Appuyez sur le bouton de l'INDEX DROIT.",    font='Lucida Console',
        pos=[0,0.3], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=0.0)
    ISI_14 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_14')
    TopUpperLine_14 = visual.Line(win=win, name='TopUpperLine_14',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='[1,1,-1]', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    UpperText_14 = visual.TextStim(win=win, ori=0, name='UpperText_14',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-3.0)
    UpperBrackets_14 = visual.TextStim(win=win, ori=0, name='UpperBrackets_14',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-4.0)
    BotUpperLine_14 = visual.Line(win=win, name='BotUpperLine_14',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='yellow', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TopLowerLine_14 = visual.Line(win=win, name='TopLowerLine_14',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    LowerText_14 = visual.TextStim(win=win, ori=0, name='LowerText_14',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=2,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-7.0)
    LowerBrackets_14 = visual.TextStim(win=win, ori=0, name='LowerBrackets_14',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=None,
        color='cyan', colorSpace='rgb', opacity=1,
        depth=-8.0)
    BotLowerLine_14 = visual.Line(win=win, name='BotLowerLine_14',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TrialCrossHair_14 = visual.TextStim(win=win, ori=0, name='TrialCrossHair_14',
        text='\n',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='green', colorSpace='rgb', opacity=1,
        depth=-10.0)
    RestCrossHair_14 = visual.TextStim(win=win, ori=0, name='RestCrossHair_14',
        text=None,    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='red', colorSpace='rgb', opacity=1,
        depth=-11.0)

    # Initialize components for Routine "Feedback"
    FeedbackClock = core.Clock()
    msg='?????'
    text_25 = visual.TextStim(win=win, ori=0, name='text_25',
        text='default text',    font='Lucida Console',
        pos=[0, 0], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-1.0)

    # Initialize components for Routine "ButtonPractice_MIDDLE"
    ButtonPractice_MIDDLEClock = core.Clock()
    text_29 = visual.TextStim(win=win, ori=0, name='text_29',
        text=u"Appuyez sur le bouton du MAJEUR DROIT.",    font='Lucida Console',
        pos=[0,0.3], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=0.0)
    ISI_15 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_15')
    TopUpperLine_15 = visual.Line(win=win, name='TopUpperLine_15',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='[1,1,-1]', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    UpperText_15 = visual.TextStim(win=win, ori=0, name='UpperText_15',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-3.0)
    UpperBrackets_15 = visual.TextStim(win=win, ori=0, name='UpperBrackets_15',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-4.0)
    BotUpperLine_15 = visual.Line(win=win, name='BotUpperLine_15',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='yellow', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TopLowerLine_15 = visual.Line(win=win, name='TopLowerLine_15',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    LowerText_15 = visual.TextStim(win=win, ori=0, name='LowerText_15',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=2,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-7.0)
    LowerBrackets_15 = visual.TextStim(win=win, ori=0, name='LowerBrackets_15',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=None,
        color='cyan', colorSpace='rgb', opacity=1,
        depth=-8.0)
    BotLowerLine_15 = visual.Line(win=win, name='BotLowerLine_15',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TrialCrossHair_15 = visual.TextStim(win=win, ori=0, name='TrialCrossHair_15',
        text='\n',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='green', colorSpace='rgb', opacity=1,
        depth=-10.0)
    RestCrossHair_15 = visual.TextStim(win=win, ori=0, name='RestCrossHair_15',
        text=None,    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='red', colorSpace='rgb', opacity=1,
        depth=-11.0)

    # Initialize components for Routine "Feedback_MIDDLE"
    Feedback_MIDDLEClock = core.Clock()
    msg='?????'
    text_26 = visual.TextStim(win=win, ori=0, name='text_26',
        text='default text',    font=u'Lucida Console',
        pos=[0, 0], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-1.0)

    # Initialize components for Routine "var_6Letters_2"
    var_6Letters_2Clock = core.Clock()
    text_13 = visual.TextStim(win=win, ori=0, name='text_13',
        text=u"Voici l'écran que vous verrez lors de chaque essai",    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=0.0)
    text_16 = visual.TextStim(win=win, ori=0, name='text_16',
        text=u"avec une partie SUPÉRIEURE",    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.1, wrapWidth=1.25,
        color='white', colorSpace='rgb', opacity=1,
        depth=-1.0)
    text_18 = visual.TextStim(win=win, ori=0, name='text_18',
        text=u"et une partie INFÉRIEURE",    font='Lucida Console',
        pos=[0,-0.3], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-2.0)
    text_21 = visual.TextStim(win=win, ori=0, name='text_21',
        text=None,    font='Lucida Console',
        pos=[0, 0], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-3.0)
    ISI_13 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_13')
    TopUpperLine_13 = visual.Line(win=win, name='TopUpperLine_13',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='[1,1,-1]', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    UpperText_13 = visual.TextStim(win=win, ori=0, name='UpperText_13',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-6.0)
    UpperBrackets_13 = visual.TextStim(win=win, ori=0, name='UpperBrackets_13',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-7.0)
    BotUpperLine_13 = visual.Line(win=win, name='BotUpperLine_13',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='yellow', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TopLowerLine_13 = visual.Line(win=win, name='TopLowerLine_13',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    LowerText_13 = visual.TextStim(win=win, ori=0, name='LowerText_13',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=2,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-10.0)
    LowerBrackets_13 = visual.TextStim(win=win, ori=0, name='LowerBrackets_13',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=None,
        color='cyan', colorSpace='rgb', opacity=1,
        depth=-11.0)
    BotLowerLine_13 = visual.Line(win=win, name='BotLowerLine_13',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TrialCrossHair_13 = visual.TextStim(win=win, ori=0, name='TrialCrossHair_13',
        text='+',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='green', colorSpace='rgb', opacity=1,
        depth=-13.0)
    RestCrossHair_13 = visual.TextStim(win=win, ori=0, name='RestCrossHair_13',
        text='+',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='red', colorSpace='rgb', opacity=1,
        depth=-14.0)
    text_22 = visual.TextStim(win=win, ori=0, name='text_22',
        text=u"Vous verrez aussi une croix sur l'écran",    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-15.0)
    text_23 = visual.TextStim(win=win, ori=0, name='text_23',
        text=u"soit VERTE",    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-16.0)
    text_24 = visual.TextStim(win=win, ori=0, name='text_24',
        text=u"soit ROUGE",    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-17.0)

    # Initialize components for Routine "var_6Letters_0"
    var_6Letters_0Clock = core.Clock()
    text_2 = visual.TextStim(win=win, ori=0, name='text_2',
        text=u"Pour cette expérience vous allez voir des lettres en haut de l'écran.",    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=1.1,
        color='white', colorSpace='rgb', opacity=1,
        depth=0.0)
    text = visual.TextStim(win=win, ori=0, name='text',
        text=u"Certaines lettres seront entre parenthèses.",    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-1.0)
    text_6 = visual.TextStim(win=win, ori=0, name='text_6',
        text=u"Ce sont les lettres dont vous devez vous souvenir.",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-2.0)
    text_4 = visual.TextStim(win=win, ori=0, name='text_4',
        text=u"Les lettres vont disparaitre, concentrez-vous sur la croix verte.",    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-3.0)
    ISI_11 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_11')
    TopUpperLine_11 = visual.Line(win=win, name='TopUpperLine_11',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='[1,1,-1]', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    UpperText_11 = visual.TextStim(win=win, ori=0, name='UpperText_11',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-6.0)
    UpperBrackets_11 = visual.TextStim(win=win, ori=0, name='UpperBrackets_11',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-7.0)
    BotUpperLine_11 = visual.Line(win=win, name='BotUpperLine_11',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='yellow', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TopLowerLine_11 = visual.Line(win=win, name='TopLowerLine_11',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    LowerText_11 = visual.TextStim(win=win, ori=0, name='LowerText_11',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=2,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-10.0)
    LowerBrackets_11 = visual.TextStim(win=win, ori=0, name='LowerBrackets_11',
        text='  { }        ',    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=None,
        color='cyan', colorSpace='rgb', opacity=1,
        depth=-11.0)
    BotLowerLine_11 = visual.Line(win=win, name='BotLowerLine_11',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TrialCrossHair_11 = visual.TextStim(win=win, ori=0, name='TrialCrossHair_11',
        text='+',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='green', colorSpace='rgb', opacity=1,
        depth=-13.0)
    RestCrossHair_11 = visual.TextStim(win=win, ori=0, name='RestCrossHair_11',
        text='+',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='red', colorSpace='rgb', opacity=1,
        depth=-14.0)
    text_5 = visual.TextStim(win=win, ori=0, name='text_5',
        text=u"Vous allez ensuite voir des lettres au bas de l'écran.",    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=1.1,
        color='white', colorSpace='rgb', opacity=1,
        depth=-16.0)
    text_7 = visual.TextStim(win=win, ori=0, name='text_7',
        text=u"Seulement une lettre sera entre parenthèses.",    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-17.0)
    text_8 = visual.TextStim(win=win, ori=0, name='text_8',
        text=u"Vous devez décider si c'est une des lettre dont vous devez vous souvenir.",    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=1.25,
        color='white', colorSpace='rgb', opacity=1,
        depth=-18.0)
    text_9 = visual.TextStim(win=win, ori=0, name='text_9',
        text=u"OUI = bouton INDEX  \n NON = bouton MAJEUR",    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-19.0)
    text_10 = visual.TextStim(win=win, ori=0, name='text_10',
        text=u"L'essai se termine alors et la croix devient ROUGE.",    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-20.0)

    # Initialize components for Routine "var_6Letters_1"
    var_6Letters_1Clock = core.Clock()
    text_11 = visual.TextStim(win=win, ori=0, name='text_11',
        text=u"Répétons",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=0.0)
    text_12 = visual.TextStim(win=win, ori=0, name='text_12',
        text=u"Souvenez-vous des lettres B et C",    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=1.25,
        color='white', colorSpace='rgb', opacity=1,
        depth=-1.0)
    text_14 = visual.TextStim(win=win, ori=0, name='text_14',
        text=u"Les lettres vont disparaitre",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-2.0)
    ISI_12 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_12')
    TopUpperLine_12 = visual.Line(win=win, name='TopUpperLine_12',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='[1,1,-1]', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    UpperText_12 = visual.TextStim(win=win, ori=0, name='UpperText_12',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-5.0)
    UpperBrackets_12 = visual.TextStim(win=win, ori=0, name='UpperBrackets_12',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-6.0)
    BotUpperLine_12 = visual.Line(win=win, name='BotUpperLine_12',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='yellow', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TopLowerLine_12 = visual.Line(win=win, name='TopLowerLine_12',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    LowerText_12 = visual.TextStim(win=win, ori=0, name='LowerText_12',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,-0.3], height=0.2, wrapWidth=2,
        color=[0,0,0], colorSpace=u'rgb', opacity=1,
        depth=-9.0)
    LowerBrackets_12 = visual.TextStim(win=win, ori=0, name='LowerBrackets_12',
        text='  { }        ',    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=None,
        color='cyan', colorSpace='rgb', opacity=1,
        depth=-10.0)
    BotLowerLine_12 = visual.Line(win=win, name='BotLowerLine_12',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TrialCrossHair_12 = visual.TextStim(win=win, ori=0, name='TrialCrossHair_12',
        text='+',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='green', colorSpace='rgb', opacity=1,
        depth=-12.0)
    RestCrossHair_12 = visual.TextStim(win=win, ori=0, name='RestCrossHair_12',
        text='+',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='red', colorSpace='rgb', opacity=1,
        depth=-13.0)
    text_17 = visual.TextStim(win=win, ori=0, name='text_17',
        text=u"Est-ce que vous essayez de vous souvenir de la lettre b?",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-15.0)
    text_19 = visual.TextStim(win=win, ori=0, name='text_19',
        text=u"Oui. Vous devez appuyer sur le bouton avec l'INDEX aussi rapidement que possible.",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-16.0)
    text_20 = visual.TextStim(win=win, ori=0, name='text_20',
        text=u"L'essai est terminé et la croix devient ROUGE.",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-17.0)

    # Initialize components for Routine "DemoTrialRealTimes"
    DemoTrialRealTimesClock = core.Clock()
    text_44 = visual.TextStim(win=win, ori=0, name='text_44',
        text=u"Répétons à vitesse normale.",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=0.0)
    text_45 = visual.TextStim(win=win, ori=0, name='text_45',
        text=u"Souvenez-vous des lettres B et C",    font=u'Lucida Console',
        units=u'norm', pos=[0, 0.8], height=0.1, wrapWidth=1.25,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-1.0)
    text_46 = visual.TextStim(win=win, ori=0, name='text_46',
        text=u"Les lettres disparaissent",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-2.0)
    ISI_18 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_18')
    TopUpperLine_18 = visual.Line(win=win, name='TopUpperLine_18',units=u'norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace=u'rgb',
        fillColor=u'[1,1,-1]', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    UpperText_18 = visual.TextStim(win=win, ori=0, name='UpperText_18',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace=u'rgb', opacity=1,
        depth=-5.0)
    UpperBrackets_18 = visual.TextStim(win=win, ori=0, name='UpperBrackets_18',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=u'yellow', colorSpace=u'rgb', opacity=1,
        depth=-6.0)
    BotUpperLine_18 = visual.Line(win=win, name='BotUpperLine_18',units=u'norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace=u'rgb',
        fillColor=u'yellow', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    TopLowerLine_18 = visual.Line(win=win, name='TopLowerLine_18',units=u'norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor=u'cyan', lineColorSpace=u'rgb',
        fillColor=u'cyan', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    LowerText_17 = visual.TextStim(win=win, ori=0, name='LowerText_17',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,-0.3], height=0.2, wrapWidth=2,
        color=[0,0,0], colorSpace=u'rgb', opacity=1,
        depth=-9.0)
    LowerBrackets_17 = visual.TextStim(win=win, ori=0, name='LowerBrackets_17',
        text=u'  { }        ',    font=u'Lucida Console',
        units=u'norm', pos=[0,-0.3], height=0.2, wrapWidth=None,
        color=u'cyan', colorSpace=u'rgb', opacity=1,
        depth=-10.0)
    BotLowerLine_18 = visual.Line(win=win, name='BotLowerLine_18',units=u'norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor=u'cyan', lineColorSpace=u'rgb',
        fillColor=u'cyan', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    TrialCrossHair_18 = visual.TextStim(win=win, ori=0, name='TrialCrossHair_18',
        text=u'+',    font=u'Lucida Console',
        units=u'norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color=u'green', colorSpace=u'rgb', opacity=1,
        depth=-12.0)
    RestCrossHair_18 = visual.TextStim(win=win, ori=0, name='RestCrossHair_18',
        text=u'+',    font=u'Lucida Console',
        units=u'norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color=u'red', colorSpace=u'rgb', opacity=1,
        depth=-13.0)
    text_48 = visual.TextStim(win=win, ori=0, name='text_48',
        text=u"Répondez aussi rapidement que possible",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-15.0)
    text_49 = visual.TextStim(win=win, ori=0, name='text_49',
        text=u"L'essai est terminé et la croix devient ROUGE.",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-16.0)

    # Initialize components for Routine "NumLettersToRem"
    NumLettersToRemClock = core.Clock()
    text_15 = visual.TextStim(win=win, ori=0, name='text_15',
        text=u"Le nombre de lettres à se rappeler",    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=0.0)
    text_33 = visual.TextStim(win=win, ori=0, name='text_33',
        text=u"varie entre 1 et 6",    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=1.25,
        color='white', colorSpace='rgb', opacity=1,
        depth=-1.0)
    text_34 = visual.TextStim(win=win, ori=0, name='text_34',
        text=u"Il y aura toujours 6 lettres présentées",    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-2.0)
    text_3 = visual.TextStim(win=win, ori=0, name='text_3',
        text=u"Ce sont les parenthèses qui indiquent les lettres à mémoriser.",    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-3.0)
    text_35 = visual.TextStim(win=win, ori=0, name='text_35',
        text=u"Voici des exemples",    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-4.0)
    UpBrack1 = visual.TextStim(win=win, ori=0, name='UpBrack1',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-5.0)
    ISI_17 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_17')
    TopUpperLine_17 = visual.Line(win=win, name='TopUpperLine_17',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='[1,1,-1]', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    UpperText_17 = visual.TextStim(win=win, ori=0, name='UpperText_17',
        text='default text',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-8.0)
    UpperBrackets_17 = visual.TextStim(win=win, ori=0, name='UpperBrackets_17',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-9.0)
    BotUpperLine_17 = visual.Line(win=win, name='BotUpperLine_17',units='norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace='rgb',
        fillColor='yellow', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TopLowerLine_17 = visual.Line(win=win, name='TopLowerLine_17',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    BotLowerLine_17 = visual.Line(win=win, name='BotLowerLine_17',units='norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor='cyan', lineColorSpace='rgb',
        fillColor='cyan', fillColorSpace='rgb',
        opacity=1,interpolate=True)
    TrialCrossHair_17 = visual.TextStim(win=win, ori=0, name='TrialCrossHair_17',
        text='+',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='green', colorSpace='rgb', opacity=1,
        depth=-13.0)
    RestCrossHair_17 = visual.TextStim(win=win, ori=0, name='RestCrossHair_17',
        text=None,    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='red', colorSpace='rgb', opacity=1,
        depth=-14.0)
    UpBrack2 = visual.TextStim(win=win, ori=0, name='UpBrack2',
        text='{   }        ',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-15.0)
    UpBrack3 = visual.TextStim(win=win, ori=0, name='UpBrack3',
        text='      {     }',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='Yellow', colorSpace='rgb', opacity=1,
        depth=-16.0)
    UpBrack4 = visual.TextStim(win=win, ori=0, name='UpBrack4',
        text='  {       }  ',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-17.0)
    UpBrack5 = visual.TextStim(win=win, ori=0, name='UpBrack5',
        text='{         }  ',    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-18.0)
    UpBrack6 = visual.TextStim(win=win, ori=0, name='UpBrack6',
        text=u'{           }',    font=u'Lucida Console',
        units=u'norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=u'yellow', colorSpace=u'rgb', opacity=1,
        depth=-19.0)
    text_38 = visual.TextStim(win=win, ori=0, name='text_38',
        text=u"Une lettre",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-20.0)
    text_39 = visual.TextStim(win=win, ori=0, name='text_39',
        text=u"Deux lettres",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-21.0)
    text_40 = visual.TextStim(win=win, ori=0, name='text_40',
        text=u"Trois lettres",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-22.0)
    text_41 = visual.TextStim(win=win, ori=0, name='text_41',
        text=u"Quatre lettres",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-23.0)
    text_42 = visual.TextStim(win=win, ori=0, name='text_42',
        text=u"Cinq lettres",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-24.0)
    text_43 = visual.TextStim(win=win, ori=0, name='text_43',
        text=u"Six lettres",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-25.0)

    # Initialize components for Routine "TrialParts_1"
    TrialParts_1Clock = core.Clock()
    text_27 = visual.TextStim(win=win, ori=0, name='text_27',
        text=u"Pour aider avec les analyses des données du cerveau. Certains essais sont PARTIELS.",font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=1.5,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=0.0)
    text_30 = visual.TextStim(win=win, ori=0, name='text_30',
        text=u"Tous les essais ont une série de lettres à étudier.",    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=1.25,
        color='white', colorSpace='rgb', opacity=1,
        depth=-1.0)
    text_31 = visual.TextStim(win=win, ori=0, name='text_31',
        text=u"Certains ne demandent pas de réponse",    font='Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=-2.0)
    text_32 = visual.TextStim(win=win, ori=0, name='text_32',
        text=u"D'autres n'auront pas de délai entre les lettres à étudier et la réponse.",    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=1.5,
        color='white', colorSpace='rgb', opacity=1,
        depth=-3.0)
    ISI_16 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_16')
    TopUpperLine_16 = visual.Line(win=win, name='TopUpperLine_16',units=u'norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace=u'rgb',
        fillColor=u'[1,1,-1]', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    UpperText_16 = visual.TextStim(win=win, ori=0, name='UpperText_16',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-6.0)
    UpperBrackets_16 = visual.TextStim(win=win, ori=0, name='UpperBrackets_16',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color='yellow', colorSpace='rgb', opacity=1,
        depth=-7.0)
    BotUpperLine_16 = visual.Line(win=win, name='BotUpperLine_16',units=u'norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace=u'rgb',
        fillColor=u'yellow', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    TopLowerLine_16 = visual.Line(win=win, name='TopLowerLine_16',units=u'norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor=u'cyan', lineColorSpace=u'rgb',
        fillColor=u'cyan', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    LowerText_16 = visual.TextStim(win=win, ori=0, name='LowerText_16',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=2,
        color=[0,0,0], colorSpace='rgb', opacity=1,
        depth=-10.0)
    LowerBrackets_16 = visual.TextStim(win=win, ori=0, name='LowerBrackets_16',
        text=None,    font='Lucida Console',
        units='norm', pos=[0,-0.3], height=0.2, wrapWidth=None,
        color='cyan', colorSpace='rgb', opacity=1,
        depth=-11.0)
    BotLowerLine_16 = visual.Line(win=win, name='BotLowerLine_16',units=u'norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor=u'cyan', lineColorSpace=u'rgb',
        fillColor=u'cyan', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    TrialCrossHair_16 = visual.TextStim(win=win, ori=0, name='TrialCrossHair_16',
        text=None,    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='green', colorSpace='rgb', opacity=1,
        depth=-13.0)
    RestCrossHair_16 = visual.TextStim(win=win, ori=0, name='RestCrossHair_16',
        text=None,    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='red', colorSpace='rgb', opacity=1,
        depth=-14.0)
    text_36 = visual.TextStim(win=win, ori=0, name='text_36',
        text=u"Ce qui est important c'est quand la croix devient ROUGE. L'essai est terminé.",    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=1.5,
        color='white', colorSpace='rgb', opacity=1,
        depth=-15.0)
    text_37 = visual.TextStim(win=win, ori=0, name='text_37',
        text=u"Essayez d'oublier les lettres étudiées et attendez le nouvel essai",    font='Lucida Console',
        units='norm', pos=[0, 0.8], height=0.1, wrapWidth=1.5,
        color='white', colorSpace='rgb', opacity=1,
        depth=-16.0)
    text_50 = visual.TextStim(win=win, ori=0, name='text_50',
        text=u"Essayez d'oublier les lettres étudiées et attendez le nouvel essai",    font=u'Lucida Console',
        pos=[0, 0.8], height=0.1, wrapWidth=None,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-17.0)

    # Initialize components for Routine "trial5_2"
    trial5_2Clock = core.Clock()
    ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
    TopUpperLine = visual.Line(win=win, name='TopUpperLine',units=u'norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0,0.45],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace=u'rgb',
        fillColor=u'[1,1,-1]', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    UpperText = visual.TextStim(win=win, ori=0, name='UpperText',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=[0,0,0], colorSpace=u'rgb', opacity=1,
        depth=-2.0)
    UpperBrackets = visual.TextStim(win=win, ori=0, name='UpperBrackets',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,0.3], height=0.2, wrapWidth=1.5,
        color=u'yellow', colorSpace=u'rgb', opacity=1,
        depth=-3.0)
    BotUpperLine = visual.Line(win=win, name='BotUpperLine',units=u'norm', 
        start=(-[2, 0.95][0]/2.0, 0), end=(+[2, 0.95][0]/2.0, 0),
        ori=0, pos=[0, 0.15],
        lineWidth=2, lineColor=[1,1,-1], lineColorSpace=u'rgb',
        fillColor=u'yellow', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    TopLowerLine = visual.Line(win=win, name='TopLowerLine',units=u'norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0, -0.15],
        lineWidth=2, lineColor=u'cyan', lineColorSpace=u'rgb',
        fillColor=u'cyan', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    LowerText = visual.TextStim(win=win, ori=0, name='LowerText',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0,-0.3], height=0.2, wrapWidth=2,
        color=[0,0,0], colorSpace=u'rgb', opacity=1,
        depth=-6.0)
    LowerBrackets = visual.TextStim(win=win, ori=0, name='LowerBrackets',
        text=u'      { }    ',    font=u'Lucida Console',
        units=u'norm', pos=[0,-0.3], height=0.2, wrapWidth=None,
        color=u'cyan', colorSpace=u'rgb', opacity=1,
        depth=-7.0)
    BotLowerLine = visual.Line(win=win, name='BotLowerLine',units=u'norm', 
        start=(-[2, 0.5][0]/2.0, 0), end=(+[2, 0.5][0]/2.0, 0),
        ori=0, pos=[0,-0.45],
        lineWidth=2, lineColor=u'cyan', lineColorSpace=u'rgb',
        fillColor=u'cyan', fillColorSpace=u'rgb',
        opacity=1,interpolate=True)
    TrialCrossHair = visual.TextStim(win=win, ori=0, name='TrialCrossHair',
        text='+',    font='Lucida Console',
        units='norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color='green', colorSpace='rgb', opacity=1,
        depth=-9.0)
    RestCrossHair = visual.TextStim(win=win, ori=0, name='RestCrossHair',
        text=u'+',    font=u'Lucida Console',
        units=u'norm', pos=[0, 0], height=0.2, wrapWidth=None,
        color=u'red', colorSpace=u'rgb', opacity=1,
        depth=-10.0)

    # Initialize components for Routine "TrialFeedBack"
    TrialFeedBackClock = core.Clock()
    #msg variable just needs some value at start
    msg=''
    text_47 = visual.TextStim(win=win, ori=0, name='text_47',
        text='default text',    font=u'Lucida Console',
        units=u'norm', pos=[0, 0], height=0.1, wrapWidth=1.5,
        color=u'white', colorSpace=u'rgb', opacity=1,
        depth=-1.0)

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=10, method='sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=[None],
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
        
        #------Prepare to start Routine "ButtonPractice"-------
        t = 0
        ButtonPracticeClock.reset()  # clock 
        frameN = -1
        routineTimer.add(120.000000)
        # update component parameters for each repeat
        UpperText_14.setText('')
        UpperBrackets_14.setText('')
        LowerText_14.setText('')
        key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_2.status = NOT_STARTED
        # keep track of which components have finished
        ButtonPracticeComponents = []
        ButtonPracticeComponents.append(text_28)
        ButtonPracticeComponents.append(ISI_14)
        ButtonPracticeComponents.append(TopUpperLine_14)
        ButtonPracticeComponents.append(UpperText_14)
        ButtonPracticeComponents.append(UpperBrackets_14)
        ButtonPracticeComponents.append(BotUpperLine_14)
        ButtonPracticeComponents.append(TopLowerLine_14)
        ButtonPracticeComponents.append(LowerText_14)
        ButtonPracticeComponents.append(LowerBrackets_14)
        ButtonPracticeComponents.append(BotLowerLine_14)
        ButtonPracticeComponents.append(TrialCrossHair_14)
        ButtonPracticeComponents.append(RestCrossHair_14)
        ButtonPracticeComponents.append(key_resp_2)
        for thisComponent in ButtonPracticeComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "ButtonPractice"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ButtonPracticeClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_28* updates
            if t >= 0 and text_28.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_28.tStart = t  # underestimates by a little under one frame
                text_28.frameNStart = frameN  # exact frame index
                text_28.setAutoDraw(True)
            elif text_28.status == STARTED and t >= (0 + (60-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_28.setAutoDraw(False)
            
            # *TopUpperLine_14* updates
            if t >= 0 and TopUpperLine_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                TopUpperLine_14.tStart = t  # underestimates by a little under one frame
                TopUpperLine_14.frameNStart = frameN  # exact frame index
                TopUpperLine_14.setAutoDraw(True)
            elif TopUpperLine_14.status == STARTED and t >= (0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
                TopUpperLine_14.setAutoDraw(False)
            
            # *UpperText_14* updates
            if t >= 0 and UpperText_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                UpperText_14.tStart = t  # underestimates by a little under one frame
                UpperText_14.frameNStart = frameN  # exact frame index
                UpperText_14.setAutoDraw(True)
            elif UpperText_14.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                UpperText_14.setAutoDraw(False)
            
            # *UpperBrackets_14* updates
            if t >= 0 and UpperBrackets_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                UpperBrackets_14.tStart = t  # underestimates by a little under one frame
                UpperBrackets_14.frameNStart = frameN  # exact frame index
                UpperBrackets_14.setAutoDraw(True)
            elif UpperBrackets_14.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                UpperBrackets_14.setAutoDraw(False)
            
            # *BotUpperLine_14* updates
            if t >= 0.0 and BotUpperLine_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                BotUpperLine_14.tStart = t  # underestimates by a little under one frame
                BotUpperLine_14.frameNStart = frameN  # exact frame index
                BotUpperLine_14.setAutoDraw(True)
            elif BotUpperLine_14.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
                BotUpperLine_14.setAutoDraw(False)
            
            # *TopLowerLine_14* updates
            if t >= 0.0 and TopLowerLine_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                TopLowerLine_14.tStart = t  # underestimates by a little under one frame
                TopLowerLine_14.frameNStart = frameN  # exact frame index
                TopLowerLine_14.setAutoDraw(True)
            elif TopLowerLine_14.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
                TopLowerLine_14.setAutoDraw(False)
            
            # *LowerText_14* updates
            if t >= 0 and LowerText_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                LowerText_14.tStart = t  # underestimates by a little under one frame
                LowerText_14.frameNStart = frameN  # exact frame index
                LowerText_14.setAutoDraw(True)
            elif LowerText_14.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                LowerText_14.setAutoDraw(False)
            
            # *LowerBrackets_14* updates
            if t >= 0 and LowerBrackets_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                LowerBrackets_14.tStart = t  # underestimates by a little under one frame
                LowerBrackets_14.frameNStart = frameN  # exact frame index
                LowerBrackets_14.setAutoDraw(True)
            elif LowerBrackets_14.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                LowerBrackets_14.setAutoDraw(False)
            
            # *BotLowerLine_14* updates
            if t >= 0.0 and BotLowerLine_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                BotLowerLine_14.tStart = t  # underestimates by a little under one frame
                BotLowerLine_14.frameNStart = frameN  # exact frame index
                BotLowerLine_14.setAutoDraw(True)
            elif BotLowerLine_14.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
                BotLowerLine_14.setAutoDraw(False)
            
            # *TrialCrossHair_14* updates
            if t >= 0 and TrialCrossHair_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                TrialCrossHair_14.tStart = t  # underestimates by a little under one frame
                TrialCrossHair_14.frameNStart = frameN  # exact frame index
                TrialCrossHair_14.setAutoDraw(True)
            elif TrialCrossHair_14.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                TrialCrossHair_14.setAutoDraw(False)
            
            # *RestCrossHair_14* updates
            if t >= 0 and RestCrossHair_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                RestCrossHair_14.tStart = t  # underestimates by a little under one frame
                RestCrossHair_14.frameNStart = frameN  # exact frame index
                RestCrossHair_14.setAutoDraw(True)
            elif RestCrossHair_14.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                RestCrossHair_14.setAutoDraw(False)
            
            # *key_resp_2* updates
            if t >= 0.0 and key_resp_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_2.tStart = t  # underestimates by a little under one frame
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            elif key_resp_2.status == STARTED and t >= (0.0 + (60-win.monitorFramePeriod*0.75)): #most of one frame period left
                key_resp_2.status = STOPPED
            if key_resp_2.status == STARTED:
                theseKeys = event.getKeys(keyList=AllowedInputKeys)#['1', '2', '3', '4', '5', '6', '7', '8', '9','down','right'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_2.rt = key_resp_2.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_2.keys == str('6')) or (key_resp_2.keys == 'down'):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            # *ISI_14* period
            if t >= 0.0 and ISI_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI_14.tStart = t  # underestimates by a little under one frame
                ISI_14.frameNStart = frameN  # exact frame index
                ISI_14.start(1)
            elif ISI_14.status == STARTED: #one frame should pass before updating params and completing
                ISI_14.complete() #finish the static period
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ButtonPracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                win.close()
                sys.exit()
                #win.close()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "ButtonPractice"-------
        for thisComponent in ButtonPracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
           key_resp_2.keys=None
           # was no response the correct answer?!
           if str('6').lower() == 'none': key_resp_2.corr = 1  # correct non-response
           else: key_resp_2.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_resp_2.keys',key_resp_2.keys)
        trials.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trials.addData('key_resp_2.rt', key_resp_2.rt)
        
        #------Prepare to start Routine "Feedback"-------
        t = 0
        FeedbackClock.reset()  # clock 
        frameN = -1
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        if len(key_resp_2.keys)<1:
            msg=u"S'il vous plaît appuyez sur le bouton de l'INDEX DROIT"
            trials.finished = Falses
        elif key_resp_2.corr:#stored on last run routine
            msg=u"Correct! Ce bouton indique la réponse OUI." 
            trials.finished = True
        else:
            msg=u"Oups! Mauvais bouton, s'il vous plaît essayez encore."
            trials.finished = False
        text_25.setText(msg)
        # keep track of which components have finished
        FeedbackComponents = []
        FeedbackComponents.append(text_25)
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Feedback"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_25* updates
            if t >= 0.0 and text_25.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_25.tStart = t  # underestimates by a little under one frame
                text_25.frameNStart = frameN  # exact frame index
                text_25.setAutoDraw(True)
            elif text_25.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_25.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                win.close()
                sys.exit()
                
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Feedback"-------
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed 10 repeats of 'trials'


    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=10, method='random', 
        extraInfo=expInfo, originPath=None,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)

    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2.keys():
                exec(paramName + '= thisTrial_2.' + paramName)
        
        #------Prepare to start Routine "ButtonPractice_MIDDLE"-------
        t = 0
        ButtonPractice_MIDDLEClock.reset()  # clock 
        frameN = -1
        routineTimer.add(20.000000)
        # update component parameters for each repeat
        UpperText_15.setText('')
        UpperBrackets_15.setText('')
        LowerText_15.setText('')
        key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_3.status = NOT_STARTED
        # keep track of which components have finished
        ButtonPractice_MIDDLEComponents = []
        ButtonPractice_MIDDLEComponents.append(text_29)
        ButtonPractice_MIDDLEComponents.append(ISI_15)
        ButtonPractice_MIDDLEComponents.append(TopUpperLine_15)
        ButtonPractice_MIDDLEComponents.append(UpperText_15)
        ButtonPractice_MIDDLEComponents.append(UpperBrackets_15)
        ButtonPractice_MIDDLEComponents.append(BotUpperLine_15)
        ButtonPractice_MIDDLEComponents.append(TopLowerLine_15)
        ButtonPractice_MIDDLEComponents.append(LowerText_15)
        ButtonPractice_MIDDLEComponents.append(LowerBrackets_15)
        ButtonPractice_MIDDLEComponents.append(BotLowerLine_15)
        ButtonPractice_MIDDLEComponents.append(TrialCrossHair_15)
        ButtonPractice_MIDDLEComponents.append(RestCrossHair_15)
        ButtonPractice_MIDDLEComponents.append(key_resp_3)
        for thisComponent in ButtonPractice_MIDDLEComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "ButtonPractice_MIDDLE"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ButtonPractice_MIDDLEClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_29* updates
            if t >= 0 and text_29.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_29.tStart = t  # underestimates by a little under one frame
                text_29.frameNStart = frameN  # exact frame index
                text_29.setAutoDraw(True)
            elif text_29.status == STARTED and t >= (0 + (10-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_29.setAutoDraw(False)
            
            # *TopUpperLine_15* updates
            if t >= 0 and TopUpperLine_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                TopUpperLine_15.tStart = t  # underestimates by a little under one frame
                TopUpperLine_15.frameNStart = frameN  # exact frame index
                TopUpperLine_15.setAutoDraw(True)
            elif TopUpperLine_15.status == STARTED and t >= (0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
                TopUpperLine_15.setAutoDraw(False)
            
            # *UpperText_15* updates
            if t >= 0 and UpperText_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                UpperText_15.tStart = t  # underestimates by a little under one frame
                UpperText_15.frameNStart = frameN  # exact frame index
                UpperText_15.setAutoDraw(True)
            elif UpperText_15.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                UpperText_15.setAutoDraw(False)
            
            # *UpperBrackets_15* updates
            if t >= 0 and UpperBrackets_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                UpperBrackets_15.tStart = t  # underestimates by a little under one frame
                UpperBrackets_15.frameNStart = frameN  # exact frame index
                UpperBrackets_15.setAutoDraw(True)
            elif UpperBrackets_15.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                UpperBrackets_15.setAutoDraw(False)
            
            # *BotUpperLine_15* updates
            if t >= 0.0 and BotUpperLine_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                BotUpperLine_15.tStart = t  # underestimates by a little under one frame
                BotUpperLine_15.frameNStart = frameN  # exact frame index
                BotUpperLine_15.setAutoDraw(True)
            elif BotUpperLine_15.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
                BotUpperLine_15.setAutoDraw(False)
            
            # *TopLowerLine_15* updates
            if t >= 0.0 and TopLowerLine_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                TopLowerLine_15.tStart = t  # underestimates by a little under one frame
                TopLowerLine_15.frameNStart = frameN  # exact frame index
                TopLowerLine_15.setAutoDraw(True)
            elif TopLowerLine_15.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
                TopLowerLine_15.setAutoDraw(False)
            
            # *LowerText_15* updates
            if t >= 0 and LowerText_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                LowerText_15.tStart = t  # underestimates by a little under one frame
                LowerText_15.frameNStart = frameN  # exact frame index
                LowerText_15.setAutoDraw(True)
            elif LowerText_15.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                LowerText_15.setAutoDraw(False)
            
            # *LowerBrackets_15* updates
            if t >= 0 and LowerBrackets_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                LowerBrackets_15.tStart = t  # underestimates by a little under one frame
                LowerBrackets_15.frameNStart = frameN  # exact frame index
                LowerBrackets_15.setAutoDraw(True)
            elif LowerBrackets_15.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                LowerBrackets_15.setAutoDraw(False)
            
            # *BotLowerLine_15* updates
            if t >= 0.0 and BotLowerLine_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                BotLowerLine_15.tStart = t  # underestimates by a little under one frame
                BotLowerLine_15.frameNStart = frameN  # exact frame index
                BotLowerLine_15.setAutoDraw(True)
            elif BotLowerLine_15.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
                BotLowerLine_15.setAutoDraw(False)
            
            # *TrialCrossHair_15* updates
            if t >= 0 and TrialCrossHair_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                TrialCrossHair_15.tStart = t  # underestimates by a little under one frame
                TrialCrossHair_15.frameNStart = frameN  # exact frame index
                TrialCrossHair_15.setAutoDraw(True)
            elif TrialCrossHair_15.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                TrialCrossHair_15.setAutoDraw(False)
            
            # *RestCrossHair_15* updates
            if t >= 0 and RestCrossHair_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                RestCrossHair_15.tStart = t  # underestimates by a little under one frame
                RestCrossHair_15.frameNStart = frameN  # exact frame index
                RestCrossHair_15.setAutoDraw(True)
            elif RestCrossHair_15.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
                RestCrossHair_15.setAutoDraw(False)
            
            # *key_resp_3* updates
            if t >= 0.0 and key_resp_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_3.tStart = t  # underestimates by a little under one frame
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                key_resp_3.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            elif key_resp_3.status == STARTED and t >= (0.0 + (10-win.monitorFramePeriod*0.75)): #most of one frame period left
                key_resp_3.status = STOPPED
            if key_resp_3.status == STARTED:
                theseKeys = event.getKeys(keyList=AllowedInputKeys)#['1', '2', '3', '4', '5', '6', '7', '8', '9','down','right'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_3.rt = key_resp_3.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_3.keys == str('7')) or (key_resp_3.keys == 'right'):
                        key_resp_3.corr = 1
                    else:
                        key_resp_3.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            # *ISI_15* period
            if t >= 0.0 and ISI_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI_15.tStart = t  # underestimates by a little under one frame
                ISI_15.frameNStart = frameN  # exact frame index
                ISI_15.start(1)
            elif ISI_15.status == STARTED: #one frame should pass before updating params and completing
                ISI_15.complete() #finish the static period
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ButtonPractice_MIDDLEComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                win.close()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "ButtonPractice_MIDDLE"-------
        for thisComponent in ButtonPractice_MIDDLEComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
           key_resp_3.keys=None
           # was no response the correct answer?!
           if str('7').lower() == 'none': key_resp_3.corr = 1  # correct non-response
           else: key_resp_3.corr = 0  # failed to respond (incorrectly)
        # store data for trials_2 (TrialHandler)
        trials_2.addData('key_resp_3.keys',key_resp_3.keys)
        trials_2.addData('key_resp_3.corr', key_resp_3.corr)
        if key_resp_3.keys != None:  # we had a response
            trials_2.addData('key_resp_3.rt', key_resp_3.rt)
        
        #------Prepare to start Routine "Feedback_MIDDLE"-------
        t = 0
        Feedback_MIDDLEClock.reset()  # clock 
        frameN = -1
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        if len(key_resp_3.keys)<1:
            msg=u"S'il vous plaît appuyez sur le bouton du MAJEUR DROIT"
            trials_2.finished = Falses
        elif key_resp_3.corr:#stored on last run routine
            msg=u"Bien! Ce bouton indique la réponse NON." 
            trials_2.finished = True
        else:
            msg=u"Oups! Mauvais bouton, s'il vous plaît essayez à nouveau."
            trials_2.finished = False
        text_26.setText(msg)
        # keep track of which components have finished
        Feedback_MIDDLEComponents = []
        Feedback_MIDDLEComponents.append(text_26)
        for thisComponent in Feedback_MIDDLEComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Feedback_MIDDLE"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Feedback_MIDDLEClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_26* updates
            if t >= 0.0 and text_26.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_26.tStart = t  # underestimates by a little under one frame
                text_26.frameNStart = frameN  # exact frame index
                text_26.setAutoDraw(True)
            elif text_26.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_26.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Feedback_MIDDLEComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                win.close()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Feedback_MIDDLE"-------
        for thisComponent in Feedback_MIDDLEComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed 10 repeats of 'trials_2'


    #------Prepare to start Routine "var_6Letters_2"-------
    t = 0
    var_6Letters_2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    UpperText_13.setText('')
    UpperBrackets_13.setText('')
    LowerText_13.setText('')
    # keep track of which components have finished
    var_6Letters_2Components = []
    var_6Letters_2Components.append(text_13)
    var_6Letters_2Components.append(text_16)
    var_6Letters_2Components.append(text_18)
    var_6Letters_2Components.append(text_21)
    var_6Letters_2Components.append(ISI_13)
    var_6Letters_2Components.append(TopUpperLine_13)
    var_6Letters_2Components.append(UpperText_13)
    var_6Letters_2Components.append(UpperBrackets_13)
    var_6Letters_2Components.append(BotUpperLine_13)
    var_6Letters_2Components.append(TopLowerLine_13)
    var_6Letters_2Components.append(LowerText_13)
    var_6Letters_2Components.append(LowerBrackets_13)
    var_6Letters_2Components.append(BotLowerLine_13)
    var_6Letters_2Components.append(TrialCrossHair_13)
    var_6Letters_2Components.append(RestCrossHair_13)
    var_6Letters_2Components.append(text_22)
    var_6Letters_2Components.append(text_23)
    var_6Letters_2Components.append(text_24)
    for thisComponent in var_6Letters_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "var_6Letters_2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = var_6Letters_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_13* updates
        if t >= 0.0 and text_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_13.tStart = t  # underestimates by a little under one frame
            text_13.frameNStart = frameN  # exact frame index
            text_13.setAutoDraw(True)
        elif text_13.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_13.setAutoDraw(False)
        
        # *text_16* updates
        if t >= 3 and text_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_16.tStart = t  # underestimates by a little under one frame
            text_16.frameNStart = frameN  # exact frame index
            text_16.setAutoDraw(True)
        elif text_16.status == STARTED and t >= (3 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_16.setAutoDraw(False)
        
        # *text_18* updates
        if t >= 6 and text_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_18.tStart = t  # underestimates by a little under one frame
            text_18.frameNStart = frameN  # exact frame index
            text_18.setAutoDraw(True)
        elif text_18.status == STARTED and t >= (6 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_18.setAutoDraw(False)
        
        # *text_21* updates
        if t >= 0 and text_21.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_21.tStart = t  # underestimates by a little under one frame
            text_21.frameNStart = frameN  # exact frame index
            text_21.setAutoDraw(True)
        elif text_21.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_21.setAutoDraw(False)
        
        # *TopUpperLine_13* updates
        if t >= 0 and TopUpperLine_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopUpperLine_13.tStart = t  # underestimates by a little under one frame
            TopUpperLine_13.frameNStart = frameN  # exact frame index
            TopUpperLine_13.setAutoDraw(True)
        elif TopUpperLine_13.status == STARTED and t >= (0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopUpperLine_13.setAutoDraw(False)
        
        # *UpperText_13* updates
        if t >= 0 and UpperText_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperText_13.tStart = t  # underestimates by a little under one frame
            UpperText_13.frameNStart = frameN  # exact frame index
            UpperText_13.setAutoDraw(True)
        elif UpperText_13.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperText_13.setAutoDraw(False)
        
        # *UpperBrackets_13* updates
        if t >= 0 and UpperBrackets_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBrackets_13.tStart = t  # underestimates by a little under one frame
            UpperBrackets_13.frameNStart = frameN  # exact frame index
            UpperBrackets_13.setAutoDraw(True)
        elif UpperBrackets_13.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBrackets_13.setAutoDraw(False)
        
        # *BotUpperLine_13* updates
        if t >= 0.0 and BotUpperLine_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotUpperLine_13.tStart = t  # underestimates by a little under one frame
            BotUpperLine_13.frameNStart = frameN  # exact frame index
            BotUpperLine_13.setAutoDraw(True)
        elif BotUpperLine_13.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotUpperLine_13.setAutoDraw(False)
        
        # *TopLowerLine_13* updates
        if t >= 0.0 and TopLowerLine_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopLowerLine_13.tStart = t  # underestimates by a little under one frame
            TopLowerLine_13.frameNStart = frameN  # exact frame index
            TopLowerLine_13.setAutoDraw(True)
        elif TopLowerLine_13.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopLowerLine_13.setAutoDraw(False)
        
        # *LowerText_13* updates
        if t >= 0 and LowerText_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerText_13.tStart = t  # underestimates by a little under one frame
            LowerText_13.frameNStart = frameN  # exact frame index
            LowerText_13.setAutoDraw(True)
        elif LowerText_13.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerText_13.setAutoDraw(False)
        
        # *LowerBrackets_13* updates
        if t >= 0 and LowerBrackets_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerBrackets_13.tStart = t  # underestimates by a little under one frame
            LowerBrackets_13.frameNStart = frameN  # exact frame index
            LowerBrackets_13.setAutoDraw(True)
        elif LowerBrackets_13.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerBrackets_13.setAutoDraw(False)
        
        # *BotLowerLine_13* updates
        if t >= 0.0 and BotLowerLine_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotLowerLine_13.tStart = t  # underestimates by a little under one frame
            BotLowerLine_13.frameNStart = frameN  # exact frame index
            BotLowerLine_13.setAutoDraw(True)
        elif BotLowerLine_13.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotLowerLine_13.setAutoDraw(False)
        
        # *TrialCrossHair_13* updates
        if t >= 12 and TrialCrossHair_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialCrossHair_13.tStart = t  # underestimates by a little under one frame
            TrialCrossHair_13.frameNStart = frameN  # exact frame index
            TrialCrossHair_13.setAutoDraw(True)
        elif TrialCrossHair_13.status == STARTED and t >= (12 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            TrialCrossHair_13.setAutoDraw(False)
        
        # *RestCrossHair_13* updates
        if t >= 15 and RestCrossHair_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair_13.tStart = t  # underestimates by a little under one frame
            RestCrossHair_13.frameNStart = frameN  # exact frame index
            RestCrossHair_13.setAutoDraw(True)
        elif RestCrossHair_13.status == STARTED and t >= (15 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair_13.setAutoDraw(False)
        
        # *text_22* updates
        if t >= 9 and text_22.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_22.tStart = t  # underestimates by a little under one frame
            text_22.frameNStart = frameN  # exact frame index
            text_22.setAutoDraw(True)
        elif text_22.status == STARTED and t >= (9 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_22.setAutoDraw(False)
        
        # *text_23* updates
        if t >= 12 and text_23.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_23.tStart = t  # underestimates by a little under one frame
            text_23.frameNStart = frameN  # exact frame index
            text_23.setAutoDraw(True)
        elif text_23.status == STARTED and t >= (12 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_23.setAutoDraw(False)
        
        # *text_24* updates
        if t >= 15 and text_24.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_24.tStart = t  # underestimates by a little under one frame
            text_24.frameNStart = frameN  # exact frame index
            text_24.setAutoDraw(True)
        elif text_24.status == STARTED and t >= (15 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_24.setAutoDraw(False)
        # *ISI_13* period
        if t >= 0.0 and ISI_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_13.tStart = t  # underestimates by a little under one frame
            ISI_13.frameNStart = frameN  # exact frame index
            ISI_13.start(1)
        elif ISI_13.status == STARTED: #one frame should pass before updating params and completing
            ISI_13.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in var_6Letters_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "var_6Letters_2"-------
    for thisComponent in var_6Letters_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #------Prepare to start Routine "var_6Letters_0"-------
    t = 0
    var_6Letters_0Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(30.000000)
    # update component parameters for each repeat
    UpperText_11.setText(' A B C D E F ')
    UpperBrackets_11.setText('  {   }      ')
    LowerText_11.setText(' a b c d e f ')
    KeyboardResp_11 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyboardResp_11.status = NOT_STARTED
    # keep track of which components have finished
    var_6Letters_0Components = []
    var_6Letters_0Components.append(text_2)
    var_6Letters_0Components.append(text)
    var_6Letters_0Components.append(text_6)
    var_6Letters_0Components.append(text_4)
    var_6Letters_0Components.append(ISI_11)
    var_6Letters_0Components.append(TopUpperLine_11)
    var_6Letters_0Components.append(UpperText_11)
    var_6Letters_0Components.append(UpperBrackets_11)
    var_6Letters_0Components.append(BotUpperLine_11)
    var_6Letters_0Components.append(TopLowerLine_11)
    var_6Letters_0Components.append(LowerText_11)
    var_6Letters_0Components.append(LowerBrackets_11)
    var_6Letters_0Components.append(BotLowerLine_11)
    var_6Letters_0Components.append(TrialCrossHair_11)
    var_6Letters_0Components.append(RestCrossHair_11)
    var_6Letters_0Components.append(KeyboardResp_11)
    var_6Letters_0Components.append(text_5)
    var_6Letters_0Components.append(text_7)
    var_6Letters_0Components.append(text_8)
    var_6Letters_0Components.append(text_9)
    var_6Letters_0Components.append(text_10)
    for thisComponent in var_6Letters_0Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "var_6Letters_0"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = var_6Letters_0Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        elif text_2.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_2.setAutoDraw(False)
        
        # *text* updates
        if t >= 3 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # underestimates by a little under one frame
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        elif text.status == STARTED and t >= (3 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text.setAutoDraw(False)
        
        # *text_6* updates
        if t >= 6 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t  # underestimates by a little under one frame
            text_6.frameNStart = frameN  # exact frame index
            text_6.setAutoDraw(True)
        elif text_6.status == STARTED and t >= (6 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_6.setAutoDraw(False)
        
        # *text_4* updates
        if t >= 9 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t  # underestimates by a little under one frame
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        elif text_4.status == STARTED and t >= (9 + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_4.setAutoDraw(False)
        
        # *TopUpperLine_11* updates
        if t >= 0 and TopUpperLine_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopUpperLine_11.tStart = t  # underestimates by a little under one frame
            TopUpperLine_11.frameNStart = frameN  # exact frame index
            TopUpperLine_11.setAutoDraw(True)
        elif TopUpperLine_11.status == STARTED and t >= (0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopUpperLine_11.setAutoDraw(False)
        
        # *UpperText_11* updates
        if t >= 0 and UpperText_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperText_11.tStart = t  # underestimates by a little under one frame
            UpperText_11.frameNStart = frameN  # exact frame index
            UpperText_11.setAutoDraw(True)
        elif UpperText_11.status == STARTED and t >= (0 + (9-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperText_11.setAutoDraw(False)
        
        # *UpperBrackets_11* updates
        if t >= 3 and UpperBrackets_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBrackets_11.tStart = t  # underestimates by a little under one frame
            UpperBrackets_11.frameNStart = frameN  # exact frame index
            UpperBrackets_11.setAutoDraw(True)
        elif UpperBrackets_11.status == STARTED and t >= (3 + (6-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBrackets_11.setAutoDraw(False)
        
        # *BotUpperLine_11* updates
        if t >= 0.0 and BotUpperLine_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotUpperLine_11.tStart = t  # underestimates by a little under one frame
            BotUpperLine_11.frameNStart = frameN  # exact frame index
            BotUpperLine_11.setAutoDraw(True)
        elif BotUpperLine_11.status == STARTED and t >= (0.0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotUpperLine_11.setAutoDraw(False)
        
        # *TopLowerLine_11* updates
        if t >= 0.0 and TopLowerLine_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopLowerLine_11.tStart = t  # underestimates by a little under one frame
            TopLowerLine_11.frameNStart = frameN  # exact frame index
            TopLowerLine_11.setAutoDraw(True)
        elif TopLowerLine_11.status == STARTED and t >= (0.0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopLowerLine_11.setAutoDraw(False)
        
        # *LowerText_11* updates
        if t >= 14 and LowerText_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerText_11.tStart = t  # underestimates by a little under one frame
            LowerText_11.frameNStart = frameN  # exact frame index
            LowerText_11.setAutoDraw(True)
        elif LowerText_11.status == STARTED and t >= (14 + (9-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerText_11.setAutoDraw(False)
        
        # *LowerBrackets_11* updates
        if t >= 17 and LowerBrackets_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerBrackets_11.tStart = t  # underestimates by a little under one frame
            LowerBrackets_11.frameNStart = frameN  # exact frame index
            LowerBrackets_11.setAutoDraw(True)
        elif LowerBrackets_11.status == STARTED and t >= (17 + (6-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerBrackets_11.setAutoDraw(False)
        
        # *BotLowerLine_11* updates
        if t >= 0.0 and BotLowerLine_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotLowerLine_11.tStart = t  # underestimates by a little under one frame
            BotLowerLine_11.frameNStart = frameN  # exact frame index
            BotLowerLine_11.setAutoDraw(True)
        elif BotLowerLine_11.status == STARTED and t >= (0.0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotLowerLine_11.setAutoDraw(False)
        
        # *TrialCrossHair_11* updates
        if t >= 0 and TrialCrossHair_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialCrossHair_11.tStart = t  # underestimates by a little under one frame
            TrialCrossHair_11.frameNStart = frameN  # exact frame index
            TrialCrossHair_11.setAutoDraw(True)
        elif TrialCrossHair_11.status == STARTED and t >= (0 + (26-win.monitorFramePeriod*0.75)): #most of one frame period left
            TrialCrossHair_11.setAutoDraw(False)
        
        # *RestCrossHair_11* updates
        if t >= 26 and RestCrossHair_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair_11.tStart = t  # underestimates by a little under one frame
            RestCrossHair_11.frameNStart = frameN  # exact frame index
            RestCrossHair_11.setAutoDraw(True)
        elif RestCrossHair_11.status == STARTED and t >= (26 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair_11.setAutoDraw(False)
        
        # *KeyboardResp_11* updates
        if t >= 0 and KeyboardResp_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyboardResp_11.tStart = t  # underestimates by a little under one frame
            KeyboardResp_11.frameNStart = frameN  # exact frame index
            KeyboardResp_11.status = STARTED
            # keyboard checking is just starting
            KeyboardResp_11.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif KeyboardResp_11.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyboardResp_11.status = STOPPED
        if KeyboardResp_11.status == STARTED:
            theseKeys = event.getKeys(keyList=AllowedInputKeys)#['1', '2', '3', '4', '5', '6', '7', '8','down','right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                KeyboardResp_11.keys.extend(theseKeys)  # storing all keys
                KeyboardResp_11.rt.append(KeyboardResp_11.clock.getTime())
        
        # *text_5* updates
        if t >= 14 and text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_5.tStart = t  # underestimates by a little under one frame
            text_5.frameNStart = frameN  # exact frame index
            text_5.setAutoDraw(True)
        elif text_5.status == STARTED and t >= (14 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_5.setAutoDraw(False)
        
        # *text_7* updates
        if t >= 17 and text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_7.tStart = t  # underestimates by a little under one frame
            text_7.frameNStart = frameN  # exact frame index
            text_7.setAutoDraw(True)
        elif text_7.status == STARTED and t >= (17 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_7.setAutoDraw(False)
        
        # *text_8* updates
        if t >= 20 and text_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_8.tStart = t  # underestimates by a little under one frame
            text_8.frameNStart = frameN  # exact frame index
            text_8.setAutoDraw(True)
        elif text_8.status == STARTED and t >= (20 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_8.setAutoDraw(False)
        
        # *text_9* updates
        if t >= 23 and text_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_9.tStart = t  # underestimates by a little under one frame
            text_9.frameNStart = frameN  # exact frame index
            text_9.setAutoDraw(True)
        elif text_9.status == STARTED and t >= (23 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_9.setAutoDraw(False)
        
        # *text_10* updates
        if t >= 26 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t  # underestimates by a little under one frame
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        elif text_10.status == STARTED and t >= (26 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_10.setAutoDraw(False)
        # *ISI_11* period
        if t >= 0.0 and ISI_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_11.tStart = t  # underestimates by a little under one frame
            ISI_11.frameNStart = frameN  # exact frame index
            ISI_11.start(1)
        elif ISI_11.status == STARTED: #one frame should pass before updating params and completing
            ISI_11.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in var_6Letters_0Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "var_6Letters_0"-------
    for thisComponent in var_6Letters_0Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyboardResp_11.keys in ['', [], None]:  # No response was made
       KeyboardResp_11.keys=None
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('KeyboardResp_11.keys',KeyboardResp_11.keys)
    if KeyboardResp_11.keys != None:  # we had a response
        thisExp.addData('KeyboardResp_11.rt', KeyboardResp_11.rt)
    thisExp.nextEntry()

    #------Prepare to start Routine "var_6Letters_1"-------
    t = 0
    var_6Letters_1Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(22.000000)
    # update component parameters for each repeat
    UpperText_12.setText(' A B C D E F ')
    UpperBrackets_12.setText('  {   }      ')
    LowerText_12.setText(u' a b c d e f ')
    KeyboardResp_12 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyboardResp_12.status = NOT_STARTED
    # keep track of which components have finished
    var_6Letters_1Components = []
    var_6Letters_1Components.append(text_11)
    var_6Letters_1Components.append(text_12)
    var_6Letters_1Components.append(text_14)
    var_6Letters_1Components.append(ISI_12)
    var_6Letters_1Components.append(TopUpperLine_12)
    var_6Letters_1Components.append(UpperText_12)
    var_6Letters_1Components.append(UpperBrackets_12)
    var_6Letters_1Components.append(BotUpperLine_12)
    var_6Letters_1Components.append(TopLowerLine_12)
    var_6Letters_1Components.append(LowerText_12)
    var_6Letters_1Components.append(LowerBrackets_12)
    var_6Letters_1Components.append(BotLowerLine_12)
    var_6Letters_1Components.append(TrialCrossHair_12)
    var_6Letters_1Components.append(RestCrossHair_12)
    var_6Letters_1Components.append(KeyboardResp_12)
    var_6Letters_1Components.append(text_17)
    var_6Letters_1Components.append(text_19)
    var_6Letters_1Components.append(text_20)
    for thisComponent in var_6Letters_1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "var_6Letters_1"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = var_6Letters_1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_11* updates
        if t >= 0.0 and text_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_11.tStart = t  # underestimates by a little under one frame
            text_11.frameNStart = frameN  # exact frame index
            text_11.setAutoDraw(True)
        elif text_11.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_11.setAutoDraw(False)
        
        # *text_12* updates
        if t >= 3 and text_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_12.tStart = t  # underestimates by a little under one frame
            text_12.frameNStart = frameN  # exact frame index
            text_12.setAutoDraw(True)
        elif text_12.status == STARTED and t >= (3 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_12.setAutoDraw(False)
        
        # *text_14* updates
        if t >= 6 and text_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_14.tStart = t  # underestimates by a little under one frame
            text_14.frameNStart = frameN  # exact frame index
            text_14.setAutoDraw(True)
        elif text_14.status == STARTED and t >= (6 + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_14.setAutoDraw(False)
        
        # *TopUpperLine_12* updates
        if t >= 0 and TopUpperLine_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopUpperLine_12.tStart = t  # underestimates by a little under one frame
            TopUpperLine_12.frameNStart = frameN  # exact frame index
            TopUpperLine_12.setAutoDraw(True)
        elif TopUpperLine_12.status == STARTED and t >= (0 + (22-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopUpperLine_12.setAutoDraw(False)
        
        # *UpperText_12* updates
        if t >= 0 and UpperText_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperText_12.tStart = t  # underestimates by a little under one frame
            UpperText_12.frameNStart = frameN  # exact frame index
            UpperText_12.setAutoDraw(True)
        elif UpperText_12.status == STARTED and t >= (0 + (6-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperText_12.setAutoDraw(False)
        
        # *UpperBrackets_12* updates
        if t >= 3 and UpperBrackets_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBrackets_12.tStart = t  # underestimates by a little under one frame
            UpperBrackets_12.frameNStart = frameN  # exact frame index
            UpperBrackets_12.setAutoDraw(True)
        elif UpperBrackets_12.status == STARTED and t >= (3 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBrackets_12.setAutoDraw(False)
        
        # *BotUpperLine_12* updates
        if t >= 0.0 and BotUpperLine_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotUpperLine_12.tStart = t  # underestimates by a little under one frame
            BotUpperLine_12.frameNStart = frameN  # exact frame index
            BotUpperLine_12.setAutoDraw(True)
        elif BotUpperLine_12.status == STARTED and t >= (0.0 + (22-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotUpperLine_12.setAutoDraw(False)
        
        # *TopLowerLine_12* updates
        if t >= 0.0 and TopLowerLine_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopLowerLine_12.tStart = t  # underestimates by a little under one frame
            TopLowerLine_12.frameNStart = frameN  # exact frame index
            TopLowerLine_12.setAutoDraw(True)
        elif TopLowerLine_12.status == STARTED and t >= (0.0 + (22-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopLowerLine_12.setAutoDraw(False)
        
        # *LowerText_12* updates
        if t >= 11 and LowerText_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerText_12.tStart = t  # underestimates by a little under one frame
            LowerText_12.frameNStart = frameN  # exact frame index
            LowerText_12.setAutoDraw(True)
        elif LowerText_12.status == STARTED and t >= (11 + (6-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerText_12.setAutoDraw(False)
        
        # *LowerBrackets_12* updates
        if t >= 11 and LowerBrackets_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerBrackets_12.tStart = t  # underestimates by a little under one frame
            LowerBrackets_12.frameNStart = frameN  # exact frame index
            LowerBrackets_12.setAutoDraw(True)
        elif LowerBrackets_12.status == STARTED and t >= (11 + (6-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerBrackets_12.setAutoDraw(False)
        
        # *BotLowerLine_12* updates
        if t >= 0.0 and BotLowerLine_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotLowerLine_12.tStart = t  # underestimates by a little under one frame
            BotLowerLine_12.frameNStart = frameN  # exact frame index
            BotLowerLine_12.setAutoDraw(True)
        elif BotLowerLine_12.status == STARTED and t >= (0.0 + (22-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotLowerLine_12.setAutoDraw(False)
        
        # *TrialCrossHair_12* updates
        if t >= 0 and TrialCrossHair_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialCrossHair_12.tStart = t  # underestimates by a little under one frame
            TrialCrossHair_12.frameNStart = frameN  # exact frame index
            TrialCrossHair_12.setAutoDraw(True)
        elif TrialCrossHair_12.status == STARTED and t >= (0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
            TrialCrossHair_12.setAutoDraw(False)
        
        # *RestCrossHair_12* updates
        if t >= 17 and RestCrossHair_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair_12.tStart = t  # underestimates by a little under one frame
            RestCrossHair_12.frameNStart = frameN  # exact frame index
            RestCrossHair_12.setAutoDraw(True)
        elif RestCrossHair_12.status == STARTED and t >= (17 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair_12.setAutoDraw(False)
        
        # *KeyboardResp_12* updates
        if t >= 0 and KeyboardResp_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyboardResp_12.tStart = t  # underestimates by a little under one frame
            KeyboardResp_12.frameNStart = frameN  # exact frame index
            KeyboardResp_12.status = STARTED
            # keyboard checking is just starting
            KeyboardResp_12.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif KeyboardResp_12.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyboardResp_12.status = STOPPED
        if KeyboardResp_12.status == STARTED:
            theseKeys = event.getKeys(keyList=AllowedInputKeys)#['1', '2', '3', '4', '5', '6', '7', '8','down','right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                KeyboardResp_12.keys.extend(theseKeys)  # storing all keys
                KeyboardResp_12.rt.append(KeyboardResp_12.clock.getTime())
        
        # *text_17* updates
        if t >= 11 and text_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_17.tStart = t  # underestimates by a little under one frame
            text_17.frameNStart = frameN  # exact frame index
            text_17.setAutoDraw(True)
        elif text_17.status == STARTED and t >= (11 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_17.setAutoDraw(False)
        
        # *text_19* updates
        if t >= 14 and text_19.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_19.tStart = t  # underestimates by a little under one frame
            text_19.frameNStart = frameN  # exact frame index
            text_19.setAutoDraw(True)
        elif text_19.status == STARTED and t >= (14 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_19.setAutoDraw(False)
        
        # *text_20* updates
        if t >= 17 and text_20.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_20.tStart = t  # underestimates by a little under one frame
            text_20.frameNStart = frameN  # exact frame index
            text_20.setAutoDraw(True)
        elif text_20.status == STARTED and t >= (17 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_20.setAutoDraw(False)
        # *ISI_12* period
        if t >= 0.0 and ISI_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_12.tStart = t  # underestimates by a little under one frame
            ISI_12.frameNStart = frameN  # exact frame index
            ISI_12.start(1)
        elif ISI_12.status == STARTED: #one frame should pass before updating params and completing
            ISI_12.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in var_6Letters_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "var_6Letters_1"-------
    for thisComponent in var_6Letters_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyboardResp_12.keys in ['', [], None]:  # No response was made
       KeyboardResp_12.keys=None
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('KeyboardResp_12.keys',KeyboardResp_12.keys)
    if KeyboardResp_12.keys != None:  # we had a response
        thisExp.addData('KeyboardResp_12.rt', KeyboardResp_12.rt)
    thisExp.nextEntry()

    #------Prepare to start Routine "DemoTrialRealTimes"-------
    t = 0
    DemoTrialRealTimesClock.reset()  # clock 
    frameN = -1
    routineTimer.add(17.000000)
    # update component parameters for each repeat
    UpperText_18.setText(u' A B C D E F ')
    UpperBrackets_18.setText(u'  {   }      ')
    LowerText_17.setText(u' a b c d e f ')
    KeyboardResp_13 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    KeyboardResp_13.status = NOT_STARTED
    # keep track of which components have finished
    DemoTrialRealTimesComponents = []
    DemoTrialRealTimesComponents.append(text_44)
    DemoTrialRealTimesComponents.append(text_45)
    DemoTrialRealTimesComponents.append(text_46)
    DemoTrialRealTimesComponents.append(ISI_18)
    DemoTrialRealTimesComponents.append(TopUpperLine_18)
    DemoTrialRealTimesComponents.append(UpperText_18)
    DemoTrialRealTimesComponents.append(UpperBrackets_18)
    DemoTrialRealTimesComponents.append(BotUpperLine_18)
    DemoTrialRealTimesComponents.append(TopLowerLine_18)
    DemoTrialRealTimesComponents.append(LowerText_17)
    DemoTrialRealTimesComponents.append(LowerBrackets_17)
    DemoTrialRealTimesComponents.append(BotLowerLine_18)
    DemoTrialRealTimesComponents.append(TrialCrossHair_18)
    DemoTrialRealTimesComponents.append(RestCrossHair_18)
    DemoTrialRealTimesComponents.append(KeyboardResp_13)
    DemoTrialRealTimesComponents.append(text_48)
    DemoTrialRealTimesComponents.append(text_49)
    for thisComponent in DemoTrialRealTimesComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "DemoTrialRealTimes"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = DemoTrialRealTimesClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_44* updates
        if t >= 0.0 and text_44.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_44.tStart = t  # underestimates by a little under one frame
            text_44.frameNStart = frameN  # exact frame index
            text_44.setAutoDraw(True)
        elif text_44.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_44.setAutoDraw(False)
        
        # *text_45* updates
        if t >= 3 and text_45.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_45.tStart = t  # underestimates by a little under one frame
            text_45.frameNStart = frameN  # exact frame index
            text_45.setAutoDraw(True)
        elif text_45.status == STARTED and t >= (3 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_45.setAutoDraw(False)
        
        # *text_46* updates
        if t >= 5 and text_46.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_46.tStart = t  # underestimates by a little under one frame
            text_46.frameNStart = frameN  # exact frame index
            text_46.setAutoDraw(True)
        elif text_46.status == STARTED and t >= (5 + (5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_46.setAutoDraw(False)
        
        # *TopUpperLine_18* updates
        if t >= 0 and TopUpperLine_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopUpperLine_18.tStart = t  # underestimates by a little under one frame
            TopUpperLine_18.frameNStart = frameN  # exact frame index
            TopUpperLine_18.setAutoDraw(True)
        elif TopUpperLine_18.status == STARTED and t >= (0 + (17-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopUpperLine_18.setAutoDraw(False)
        
        # *UpperText_18* updates
        if t >= 3 and UpperText_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperText_18.tStart = t  # underestimates by a little under one frame
            UpperText_18.frameNStart = frameN  # exact frame index
            UpperText_18.setAutoDraw(True)
        elif UpperText_18.status == STARTED and t >= (3 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperText_18.setAutoDraw(False)
        
        # *UpperBrackets_18* updates
        if t >= 3 and UpperBrackets_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBrackets_18.tStart = t  # underestimates by a little under one frame
            UpperBrackets_18.frameNStart = frameN  # exact frame index
            UpperBrackets_18.setAutoDraw(True)
        elif UpperBrackets_18.status == STARTED and t >= (3 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBrackets_18.setAutoDraw(False)
        
        # *BotUpperLine_18* updates
        if t >= 0.0 and BotUpperLine_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotUpperLine_18.tStart = t  # underestimates by a little under one frame
            BotUpperLine_18.frameNStart = frameN  # exact frame index
            BotUpperLine_18.setAutoDraw(True)
        elif BotUpperLine_18.status == STARTED and t >= (0.0 + (17-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotUpperLine_18.setAutoDraw(False)
        
        # *TopLowerLine_18* updates
        if t >= 0.0 and TopLowerLine_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopLowerLine_18.tStart = t  # underestimates by a little under one frame
            TopLowerLine_18.frameNStart = frameN  # exact frame index
            TopLowerLine_18.setAutoDraw(True)
        elif TopLowerLine_18.status == STARTED and t >= (0.0 + (17-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopLowerLine_18.setAutoDraw(False)
        
        # *LowerText_17* updates
        if t >= 10 and LowerText_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerText_17.tStart = t  # underestimates by a little under one frame
            LowerText_17.frameNStart = frameN  # exact frame index
            LowerText_17.setAutoDraw(True)
        elif LowerText_17.status == STARTED and t >= (10 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerText_17.setAutoDraw(False)
        
        # *LowerBrackets_17* updates
        if t >= 10 and LowerBrackets_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerBrackets_17.tStart = t  # underestimates by a little under one frame
            LowerBrackets_17.frameNStart = frameN  # exact frame index
            LowerBrackets_17.setAutoDraw(True)
        elif LowerBrackets_17.status == STARTED and t >= (10 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerBrackets_17.setAutoDraw(False)
        
        # *BotLowerLine_18* updates
        if t >= 0.0 and BotLowerLine_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotLowerLine_18.tStart = t  # underestimates by a little under one frame
            BotLowerLine_18.frameNStart = frameN  # exact frame index
            BotLowerLine_18.setAutoDraw(True)
        elif BotLowerLine_18.status == STARTED and t >= (0.0 + (17-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotLowerLine_18.setAutoDraw(False)
        
        # *TrialCrossHair_18* updates
        if t >= 0 and TrialCrossHair_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialCrossHair_18.tStart = t  # underestimates by a little under one frame
            TrialCrossHair_18.frameNStart = frameN  # exact frame index
            TrialCrossHair_18.setAutoDraw(True)
        elif TrialCrossHair_18.status == STARTED and t >= (0 + (12-win.monitorFramePeriod*0.75)): #most of one frame period left
            TrialCrossHair_18.setAutoDraw(False)
        
        # *RestCrossHair_18* updates
        if t >= 12 and RestCrossHair_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair_18.tStart = t  # underestimates by a little under one frame
            RestCrossHair_18.frameNStart = frameN  # exact frame index
            RestCrossHair_18.setAutoDraw(True)
        elif RestCrossHair_18.status == STARTED and t >= (12 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair_18.setAutoDraw(False)
        
        # *KeyboardResp_13* updates
        if t >= 0 and KeyboardResp_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            KeyboardResp_13.tStart = t  # underestimates by a little under one frame
            KeyboardResp_13.frameNStart = frameN  # exact frame index
            KeyboardResp_13.status = STARTED
            # keyboard checking is just starting
            KeyboardResp_13.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif KeyboardResp_13.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            KeyboardResp_13.status = STOPPED
        if KeyboardResp_13.status == STARTED:
            theseKeys = event.getKeys(keyList=AllowedInputKeys)#['1', '2', '3', '4', '5', '6', '7', '8'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                KeyboardResp_13.keys.extend(theseKeys)  # storing all keys
                KeyboardResp_13.rt.append(KeyboardResp_13.clock.getTime())
        
        # *text_48* updates
        if t >= 10 and text_48.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_48.tStart = t  # underestimates by a little under one frame
            text_48.frameNStart = frameN  # exact frame index
            text_48.setAutoDraw(True)
        elif text_48.status == STARTED and t >= (10 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_48.setAutoDraw(False)
        
        # *text_49* updates
        if t >= 12 and text_49.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_49.tStart = t  # underestimates by a little under one frame
            text_49.frameNStart = frameN  # exact frame index
            text_49.setAutoDraw(True)
        elif text_49.status == STARTED and t >= (12 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_49.setAutoDraw(False)
        # *ISI_18* period
        if t >= 0.0 and ISI_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_18.tStart = t  # underestimates by a little under one frame
            ISI_18.frameNStart = frameN  # exact frame index
            ISI_18.start(1)
        elif ISI_18.status == STARTED: #one frame should pass before updating params and completing
            ISI_18.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DemoTrialRealTimesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "DemoTrialRealTimes"-------
    for thisComponent in DemoTrialRealTimesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if KeyboardResp_13.keys in ['', [], None]:  # No response was made
       KeyboardResp_13.keys=None
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('KeyboardResp_13.keys',KeyboardResp_13.keys)
    if KeyboardResp_13.keys != None:  # we had a response
        thisExp.addData('KeyboardResp_13.rt', KeyboardResp_13.rt)
    thisExp.nextEntry()

    #------Prepare to start Routine "NumLettersToRem"-------
    t = 0
    NumLettersToRemClock.reset()  # clock 
    frameN = -1
    routineTimer.add(30.000000)
    # update component parameters for each repeat
    UpBrack1.setText('        { }  ')
    UpperText_17.setText(' A B C D E F ')
    UpperBrackets_17.setText('')
    # keep track of which components have finished
    NumLettersToRemComponents = []
    NumLettersToRemComponents.append(text_15)
    NumLettersToRemComponents.append(text_33)
    NumLettersToRemComponents.append(text_34)
    NumLettersToRemComponents.append(text_3)
    NumLettersToRemComponents.append(text_35)
    NumLettersToRemComponents.append(UpBrack1)
    NumLettersToRemComponents.append(ISI_17)
    NumLettersToRemComponents.append(TopUpperLine_17)
    NumLettersToRemComponents.append(UpperText_17)
    NumLettersToRemComponents.append(UpperBrackets_17)
    NumLettersToRemComponents.append(BotUpperLine_17)
    NumLettersToRemComponents.append(TopLowerLine_17)
    NumLettersToRemComponents.append(BotLowerLine_17)
    NumLettersToRemComponents.append(TrialCrossHair_17)
    NumLettersToRemComponents.append(RestCrossHair_17)
    NumLettersToRemComponents.append(UpBrack2)
    NumLettersToRemComponents.append(UpBrack3)
    NumLettersToRemComponents.append(UpBrack4)
    NumLettersToRemComponents.append(UpBrack5)
    NumLettersToRemComponents.append(UpBrack6)
    NumLettersToRemComponents.append(text_38)
    NumLettersToRemComponents.append(text_39)
    NumLettersToRemComponents.append(text_40)
    NumLettersToRemComponents.append(text_41)
    NumLettersToRemComponents.append(text_42)
    NumLettersToRemComponents.append(text_43)
    for thisComponent in NumLettersToRemComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "NumLettersToRem"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = NumLettersToRemClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_15* updates
        if t >= 0.0 and text_15.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_15.tStart = t  # underestimates by a little under one frame
            text_15.frameNStart = frameN  # exact frame index
            text_15.setAutoDraw(True)
        elif text_15.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_15.setAutoDraw(False)
        
        # *text_33* updates
        if t >= 3 and text_33.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_33.tStart = t  # underestimates by a little under one frame
            text_33.frameNStart = frameN  # exact frame index
            text_33.setAutoDraw(True)
        elif text_33.status == STARTED and t >= (3 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_33.setAutoDraw(False)
        
        # *text_34* updates
        if t >= 6 and text_34.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_34.tStart = t  # underestimates by a little under one frame
            text_34.frameNStart = frameN  # exact frame index
            text_34.setAutoDraw(True)
        elif text_34.status == STARTED and t >= (6 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_34.setAutoDraw(False)
        
        # *text_3* updates
        if t >= 9 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        elif text_3.status == STARTED and t >= (9 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_3.setAutoDraw(False)
        
        # *text_35* updates
        if t >= 12 and text_35.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_35.tStart = t  # underestimates by a little under one frame
            text_35.frameNStart = frameN  # exact frame index
            text_35.setAutoDraw(True)
        elif text_35.status == STARTED and t >= (12 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_35.setAutoDraw(False)
        
        # *UpBrack1* updates
        if t >= 15 and UpBrack1.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpBrack1.tStart = t  # underestimates by a little under one frame
            UpBrack1.frameNStart = frameN  # exact frame index
            UpBrack1.setAutoDraw(True)
        elif UpBrack1.status == STARTED and t >= (15 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpBrack1.setAutoDraw(False)
        
        # *TopUpperLine_17* updates
        if t >= 0 and TopUpperLine_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopUpperLine_17.tStart = t  # underestimates by a little under one frame
            TopUpperLine_17.frameNStart = frameN  # exact frame index
            TopUpperLine_17.setAutoDraw(True)
        elif TopUpperLine_17.status == STARTED and t >= (0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopUpperLine_17.setAutoDraw(False)
        
        # *UpperText_17* updates
        if t >= 0 and UpperText_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperText_17.tStart = t  # underestimates by a little under one frame
            UpperText_17.frameNStart = frameN  # exact frame index
            UpperText_17.setAutoDraw(True)
        elif UpperText_17.status == STARTED and t >= (0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperText_17.setAutoDraw(False)
        
        # *UpperBrackets_17* updates
        if t >= 0.0 and UpperBrackets_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBrackets_17.tStart = t  # underestimates by a little under one frame
            UpperBrackets_17.frameNStart = frameN  # exact frame index
            UpperBrackets_17.setAutoDraw(True)
        elif UpperBrackets_17.status == STARTED and t >= (0.0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBrackets_17.setAutoDraw(False)
        
        # *BotUpperLine_17* updates
        if t >= 0.0 and BotUpperLine_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotUpperLine_17.tStart = t  # underestimates by a little under one frame
            BotUpperLine_17.frameNStart = frameN  # exact frame index
            BotUpperLine_17.setAutoDraw(True)
        elif BotUpperLine_17.status == STARTED and t >= (0.0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotUpperLine_17.setAutoDraw(False)
        
        # *TopLowerLine_17* updates
        if t >= 0.0 and TopLowerLine_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopLowerLine_17.tStart = t  # underestimates by a little under one frame
            TopLowerLine_17.frameNStart = frameN  # exact frame index
            TopLowerLine_17.setAutoDraw(True)
        elif TopLowerLine_17.status == STARTED and t >= (0.0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopLowerLine_17.setAutoDraw(False)
        
        # *BotLowerLine_17* updates
        if t >= 0.0 and BotLowerLine_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotLowerLine_17.tStart = t  # underestimates by a little under one frame
            BotLowerLine_17.frameNStart = frameN  # exact frame index
            BotLowerLine_17.setAutoDraw(True)
        elif BotLowerLine_17.status == STARTED and t >= (0.0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotLowerLine_17.setAutoDraw(False)
        
        # *TrialCrossHair_17* updates
        if t >= 0 and TrialCrossHair_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialCrossHair_17.tStart = t  # underestimates by a little under one frame
            TrialCrossHair_17.frameNStart = frameN  # exact frame index
            TrialCrossHair_17.setAutoDraw(True)
        elif TrialCrossHair_17.status == STARTED and t >= (0 + (30-win.monitorFramePeriod*0.75)): #most of one frame period left
            TrialCrossHair_17.setAutoDraw(False)
        
        # *RestCrossHair_17* updates
        if t >= 0.0 and RestCrossHair_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair_17.tStart = t  # underestimates by a little under one frame
            RestCrossHair_17.frameNStart = frameN  # exact frame index
            RestCrossHair_17.setAutoDraw(True)
        elif RestCrossHair_17.status == STARTED and t >= (0.0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair_17.setAutoDraw(False)
        
        # *UpBrack2* updates
        if t >= 18 and UpBrack2.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpBrack2.tStart = t  # underestimates by a little under one frame
            UpBrack2.frameNStart = frameN  # exact frame index
            UpBrack2.setAutoDraw(True)
        elif UpBrack2.status == STARTED and t >= (18 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpBrack2.setAutoDraw(False)
        
        # *UpBrack3* updates
        if t >= 20 and UpBrack3.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpBrack3.tStart = t  # underestimates by a little under one frame
            UpBrack3.frameNStart = frameN  # exact frame index
            UpBrack3.setAutoDraw(True)
        elif UpBrack3.status == STARTED and t >= (20 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpBrack3.setAutoDraw(False)
        
        # *UpBrack4* updates
        if t >= 22 and UpBrack4.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpBrack4.tStart = t  # underestimates by a little under one frame
            UpBrack4.frameNStart = frameN  # exact frame index
            UpBrack4.setAutoDraw(True)
        elif UpBrack4.status == STARTED and t >= (22 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpBrack4.setAutoDraw(False)
        
        # *UpBrack5* updates
        if t >= 24 and UpBrack5.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpBrack5.tStart = t  # underestimates by a little under one frame
            UpBrack5.frameNStart = frameN  # exact frame index
            UpBrack5.setAutoDraw(True)
        elif UpBrack5.status == STARTED and t >= (24 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpBrack5.setAutoDraw(False)
        
        # *UpBrack6* updates
        if t >= 26 and UpBrack6.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpBrack6.tStart = t  # underestimates by a little under one frame
            UpBrack6.frameNStart = frameN  # exact frame index
            UpBrack6.setAutoDraw(True)
        elif UpBrack6.status == STARTED and t >= (26 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpBrack6.setAutoDraw(False)
        
        # *text_38* updates
        if t >= 15 and text_38.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_38.tStart = t  # underestimates by a little under one frame
            text_38.frameNStart = frameN  # exact frame index
            text_38.setAutoDraw(True)
        elif text_38.status == STARTED and t >= (15 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_38.setAutoDraw(False)
        
        # *text_39* updates
        if t >= 18 and text_39.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_39.tStart = t  # underestimates by a little under one frame
            text_39.frameNStart = frameN  # exact frame index
            text_39.setAutoDraw(True)
        elif text_39.status == STARTED and t >= (18 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_39.setAutoDraw(False)
        
        # *text_40* updates
        if t >= 20 and text_40.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_40.tStart = t  # underestimates by a little under one frame
            text_40.frameNStart = frameN  # exact frame index
            text_40.setAutoDraw(True)
        elif text_40.status == STARTED and t >= (20 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_40.setAutoDraw(False)
        
        # *text_41* updates
        if t >= 22 and text_41.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_41.tStart = t  # underestimates by a little under one frame
            text_41.frameNStart = frameN  # exact frame index
            text_41.setAutoDraw(True)
        elif text_41.status == STARTED and t >= (22 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_41.setAutoDraw(False)
        
        # *text_42* updates
        if t >= 24 and text_42.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_42.tStart = t  # underestimates by a little under one frame
            text_42.frameNStart = frameN  # exact frame index
            text_42.setAutoDraw(True)
        elif text_42.status == STARTED and t >= (24 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_42.setAutoDraw(False)
        
        # *text_43* updates
        if t >= 26 and text_43.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_43.tStart = t  # underestimates by a little under one frame
            text_43.frameNStart = frameN  # exact frame index
            text_43.setAutoDraw(True)
        elif text_43.status == STARTED and t >= (26 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_43.setAutoDraw(False)
        # *ISI_17* period
        if t >= 0.0 and ISI_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_17.tStart = t  # underestimates by a little under one frame
            ISI_17.frameNStart = frameN  # exact frame index
            ISI_17.start(1)
        elif ISI_17.status == STARTED: #one frame should pass before updating params and completing
            ISI_17.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NumLettersToRemComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "NumLettersToRem"-------
    for thisComponent in NumLettersToRemComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #------Prepare to start Routine "TrialParts_1"-------
    t = 0
    TrialParts_1Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(25.000000)
    # update component parameters for each repeat
    UpperText_16.setText('')
    UpperBrackets_16.setText('')
    LowerText_16.setText('')
    # keep track of which components have finished
    TrialParts_1Components = []
    TrialParts_1Components.append(text_27)
    TrialParts_1Components.append(text_30)
    TrialParts_1Components.append(text_31)
    TrialParts_1Components.append(text_32)
    TrialParts_1Components.append(ISI_16)
    TrialParts_1Components.append(TopUpperLine_16)
    TrialParts_1Components.append(UpperText_16)
    TrialParts_1Components.append(UpperBrackets_16)
    TrialParts_1Components.append(BotUpperLine_16)
    TrialParts_1Components.append(TopLowerLine_16)
    TrialParts_1Components.append(LowerText_16)
    TrialParts_1Components.append(LowerBrackets_16)
    TrialParts_1Components.append(BotLowerLine_16)
    TrialParts_1Components.append(TrialCrossHair_16)
    TrialParts_1Components.append(RestCrossHair_16)
    TrialParts_1Components.append(text_36)
    TrialParts_1Components.append(text_37)
    TrialParts_1Components.append(text_50)
    for thisComponent in TrialParts_1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "TrialParts_1"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TrialParts_1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_27* updates
        if t >= 0.0 and text_27.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_27.tStart = t  # underestimates by a little under one frame
            text_27.frameNStart = frameN  # exact frame index
            text_27.setAutoDraw(True)
        elif text_27.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_27.setAutoDraw(False)
        
        # *text_30* updates
        if t >= 3 and text_30.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_30.tStart = t  # underestimates by a little under one frame
            text_30.frameNStart = frameN  # exact frame index
            text_30.setAutoDraw(True)
        elif text_30.status == STARTED and t >= (3 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_30.setAutoDraw(False)
        
        # *text_31* updates
        if t >= 6 and text_31.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_31.tStart = t  # underestimates by a little under one frame
            text_31.frameNStart = frameN  # exact frame index
            text_31.setAutoDraw(True)
        elif text_31.status == STARTED and t >= (6 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_31.setAutoDraw(False)
        
        # *text_32* updates
        if t >= 9 and text_32.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_32.tStart = t  # underestimates by a little under one frame
            text_32.frameNStart = frameN  # exact frame index
            text_32.setAutoDraw(True)
        elif text_32.status == STARTED and t >= (9 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_32.setAutoDraw(False)
        
        # *TopUpperLine_16* updates
        if t >= 0 and TopUpperLine_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopUpperLine_16.tStart = t  # underestimates by a little under one frame
            TopUpperLine_16.frameNStart = frameN  # exact frame index
            TopUpperLine_16.setAutoDraw(True)
        elif TopUpperLine_16.status == STARTED and t >= (0 + (25-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopUpperLine_16.setAutoDraw(False)
        
        # *UpperText_16* updates
        if t >= 0 and UpperText_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperText_16.tStart = t  # underestimates by a little under one frame
            UpperText_16.frameNStart = frameN  # exact frame index
            UpperText_16.setAutoDraw(True)
        elif UpperText_16.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperText_16.setAutoDraw(False)
        
        # *UpperBrackets_16* updates
        if t >= 0 and UpperBrackets_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBrackets_16.tStart = t  # underestimates by a little under one frame
            UpperBrackets_16.frameNStart = frameN  # exact frame index
            UpperBrackets_16.setAutoDraw(True)
        elif UpperBrackets_16.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBrackets_16.setAutoDraw(False)
        
        # *BotUpperLine_16* updates
        if t >= 0.0 and BotUpperLine_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotUpperLine_16.tStart = t  # underestimates by a little under one frame
            BotUpperLine_16.frameNStart = frameN  # exact frame index
            BotUpperLine_16.setAutoDraw(True)
        elif BotUpperLine_16.status == STARTED and t >= (0.0 + (25-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotUpperLine_16.setAutoDraw(False)
        
        # *TopLowerLine_16* updates
        if t >= 0.0 and TopLowerLine_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopLowerLine_16.tStart = t  # underestimates by a little under one frame
            TopLowerLine_16.frameNStart = frameN  # exact frame index
            TopLowerLine_16.setAutoDraw(True)
        elif TopLowerLine_16.status == STARTED and t >= (0.0 + (25-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopLowerLine_16.setAutoDraw(False)
        
        # *LowerText_16* updates
        if t >= 0 and LowerText_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerText_16.tStart = t  # underestimates by a little under one frame
            LowerText_16.frameNStart = frameN  # exact frame index
            LowerText_16.setAutoDraw(True)
        elif LowerText_16.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerText_16.setAutoDraw(False)
        
        # *LowerBrackets_16* updates
        if t >= 0 and LowerBrackets_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerBrackets_16.tStart = t  # underestimates by a little under one frame
            LowerBrackets_16.frameNStart = frameN  # exact frame index
            LowerBrackets_16.setAutoDraw(True)
        elif LowerBrackets_16.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerBrackets_16.setAutoDraw(False)
        
        # *BotLowerLine_16* updates
        if t >= 0.0 and BotLowerLine_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotLowerLine_16.tStart = t  # underestimates by a little under one frame
            BotLowerLine_16.frameNStart = frameN  # exact frame index
            BotLowerLine_16.setAutoDraw(True)
        elif BotLowerLine_16.status == STARTED and t >= (0.0 + (25-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotLowerLine_16.setAutoDraw(False)
        
        # *TrialCrossHair_16* updates
        if t >= 0 and TrialCrossHair_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialCrossHair_16.tStart = t  # underestimates by a little under one frame
            TrialCrossHair_16.frameNStart = frameN  # exact frame index
            TrialCrossHair_16.setAutoDraw(True)
        elif TrialCrossHair_16.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            TrialCrossHair_16.setAutoDraw(False)
        
        # *RestCrossHair_16* updates
        if t >= 0 and RestCrossHair_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair_16.tStart = t  # underestimates by a little under one frame
            RestCrossHair_16.frameNStart = frameN  # exact frame index
            RestCrossHair_16.setAutoDraw(True)
        elif RestCrossHair_16.status == STARTED and t >= (0 + (0-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair_16.setAutoDraw(False)
        
        # *text_36* updates
        if t >= 12 and text_36.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_36.tStart = t  # underestimates by a little under one frame
            text_36.frameNStart = frameN  # exact frame index
            text_36.setAutoDraw(True)
        elif text_36.status == STARTED and t >= (12 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_36.setAutoDraw(False)
        
        # *text_37* updates
        if t >= 15 and text_37.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_37.tStart = t  # underestimates by a little under one frame
            text_37.frameNStart = frameN  # exact frame index
            text_37.setAutoDraw(True)
        elif text_37.status == STARTED and t >= (15 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_37.setAutoDraw(False)
        
        # *text_50* updates
        if t >= 20 and text_50.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_50.tStart = t  # underestimates by a little under one frame
            text_50.frameNStart = frameN  # exact frame index
            text_50.setAutoDraw(True)
        elif text_50.status == STARTED and t >= (20 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_50.setAutoDraw(False)
        # *ISI_16* period
        if t >= 0.0 and ISI_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_16.tStart = t  # underestimates by a little under one frame
            ISI_16.frameNStart = frameN  # exact frame index
            ISI_16.start(1)
        elif ISI_16.status == STARTED: #one frame should pass before updating params and completing
            ISI_16.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialParts_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "TrialParts_1"-------
    for thisComponent in TrialParts_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    #------Prepare to start Routine "trial5_2"-------
    t = 0
    trial5_2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(11.000000)
    # update component parameters for each repeat
    UpperText.setText(u' L K R G M X ')
    UpperBrackets.setText(u'  {         }')
    LowerText.setText(u' b t y g q j ')
    resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    resp.status = NOT_STARTED
    # keep track of which components have finished
    trial5_2Components = []
    trial5_2Components.append(ISI)
    trial5_2Components.append(TopUpperLine)
    trial5_2Components.append(UpperText)
    trial5_2Components.append(UpperBrackets)
    trial5_2Components.append(BotUpperLine)
    trial5_2Components.append(TopLowerLine)
    trial5_2Components.append(LowerText)
    trial5_2Components.append(LowerBrackets)
    trial5_2Components.append(BotLowerLine)
    trial5_2Components.append(TrialCrossHair)
    trial5_2Components.append(RestCrossHair)
    trial5_2Components.append(resp)
    for thisComponent in trial5_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "trial5_2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial5_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TopUpperLine* updates
        if t >= 0 and TopUpperLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopUpperLine.tStart = t  # underestimates by a little under one frame
            TopUpperLine.frameNStart = frameN  # exact frame index
            TopUpperLine.setAutoDraw(True)
        elif TopUpperLine.status == STARTED and t >= (0 + (11-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopUpperLine.setAutoDraw(False)
        
        # *UpperText* updates
        if t >= 0 and UpperText.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperText.tStart = t  # underestimates by a little under one frame
            UpperText.frameNStart = frameN  # exact frame index
            UpperText.setAutoDraw(True)
        elif UpperText.status == STARTED and t >= (0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperText.setAutoDraw(False)
        
        # *UpperBrackets* updates
        if t >= 0.0 and UpperBrackets.status == NOT_STARTED:
            # keep track of start time/frame for later
            UpperBrackets.tStart = t  # underestimates by a little under one frame
            UpperBrackets.frameNStart = frameN  # exact frame index
            UpperBrackets.setAutoDraw(True)
        elif UpperBrackets.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            UpperBrackets.setAutoDraw(False)
        
        # *BotUpperLine* updates
        if t >= 0.0 and BotUpperLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotUpperLine.tStart = t  # underestimates by a little under one frame
            BotUpperLine.frameNStart = frameN  # exact frame index
            BotUpperLine.setAutoDraw(True)
        elif BotUpperLine.status == STARTED and t >= (0.0 + (11-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotUpperLine.setAutoDraw(False)
        
        # *TopLowerLine* updates
        if t >= 0.0 and TopLowerLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            TopLowerLine.tStart = t  # underestimates by a little under one frame
            TopLowerLine.frameNStart = frameN  # exact frame index
            TopLowerLine.setAutoDraw(True)
        elif TopLowerLine.status == STARTED and t >= (0.0 + (11-win.monitorFramePeriod*0.75)): #most of one frame period left
            TopLowerLine.setAutoDraw(False)
        
        # *LowerText* updates
        if t >= 7 and LowerText.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerText.tStart = t  # underestimates by a little under one frame
            LowerText.frameNStart = frameN  # exact frame index
            LowerText.setAutoDraw(True)
        elif LowerText.status == STARTED and t >= (7 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerText.setAutoDraw(False)
        
        # *LowerBrackets* updates
        if t >= 7 and LowerBrackets.status == NOT_STARTED:
            # keep track of start time/frame for later
            LowerBrackets.tStart = t  # underestimates by a little under one frame
            LowerBrackets.frameNStart = frameN  # exact frame index
            LowerBrackets.setAutoDraw(True)
        elif LowerBrackets.status == STARTED and t >= (7 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            LowerBrackets.setAutoDraw(False)
        
        # *BotLowerLine* updates
        if t >= 0.0 and BotLowerLine.status == NOT_STARTED:
            # keep track of start time/frame for later
            BotLowerLine.tStart = t  # underestimates by a little under one frame
            BotLowerLine.frameNStart = frameN  # exact frame index
            BotLowerLine.setAutoDraw(True)
        elif BotLowerLine.status == STARTED and t >= (0.0 + (11-win.monitorFramePeriod*0.75)): #most of one frame period left
            BotLowerLine.setAutoDraw(False)
        
        # *TrialCrossHair* updates
        if t >= 0 and TrialCrossHair.status == NOT_STARTED:
            # keep track of start time/frame for later
            TrialCrossHair.tStart = t  # underestimates by a little under one frame
            TrialCrossHair.frameNStart = frameN  # exact frame index
            TrialCrossHair.setAutoDraw(True)
        elif TrialCrossHair.status == STARTED and t >= (0 + (9-win.monitorFramePeriod*0.75)): #most of one frame period left
            TrialCrossHair.setAutoDraw(False)
        
        # *RestCrossHair* updates
        if t >= 9 and RestCrossHair.status == NOT_STARTED:
            # keep track of start time/frame for later
            RestCrossHair.tStart = t  # underestimates by a little under one frame
            RestCrossHair.frameNStart = frameN  # exact frame index
            RestCrossHair.setAutoDraw(True)
        elif RestCrossHair.status == STARTED and t >= (9 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            RestCrossHair.setAutoDraw(False)
        
        # *resp* updates
        if t >= 7 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t  # underestimates by a little under one frame
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            resp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif resp.status == STARTED and t >= (7 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
            resp.status = STOPPED
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=AllowedInputKeys)#['1', '2', '3', '4', '5', '6', '7', '8'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp.keys = theseKeys[-1]  # just the last key pressed
                resp.rt = resp.clock.getTime()
                # was this 'correct'?
                if (resp.keys == str(u'6')) or (resp.keys == u'6'):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
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
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial5_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "trial5_2"-------
    for thisComponent in trial5_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
       resp.keys=None
       # was no response the correct answer?!
       if str(u'6').lower() == 'none': resp.corr = 1  # correct non-response
       else: resp.corr = 0  # failed to respond (incorrectly)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('resp.keys',resp.keys)
    thisExp.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        thisExp.addData('resp.rt', resp.rt)
    thisExp.nextEntry()

    #------Prepare to start Routine "TrialFeedBack"-------
    t = 0
    TrialFeedBackClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    if ((resp.corr) & (resp.rt < 2.0)):#stored on last run routine
      msg=u"Correct et dans les temps! TR=%.3f" %(resp.rt)
    elif ((resp.corr) & (resp.rt > 2.0)):#stored on last run routine
      msg=u"Correct, mais trop long!\n RT=%.3f\nLe temps pour répondre doit être moins de deux secondes." %(resp.rt)
    else:
      if resp.rt < 2.0:
        msg=u"Oups! C'était incorrect, mais dans les temps!"
      else: 
        msg=u"Oups! C'était incorrect et trop long!"
    text_47.setText(msg)
    # keep track of which components have finished
    TrialFeedBackComponents = []
    TrialFeedBackComponents.append(text_47)
    for thisComponent in TrialFeedBackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "TrialFeedBack"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TrialFeedBackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_47* updates
        if t >= 0.0 and text_47.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_47.tStart = t  # underestimates by a little under one frame
            text_47.frameNStart = frameN  # exact frame index
            text_47.setAutoDraw(True)
        elif text_47.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_47.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialFeedBackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            win.close()
            sys.exit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    #-------Ending Routine "TrialFeedBack"-------
    for thisComponent in TrialFeedBackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    msg='Ended'
    win.close()
#    win.close()
