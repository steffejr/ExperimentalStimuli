""" 
Create a window and display the letters in the format similar to what Rypma does.
Letters at the top of the screen, line, cross-hair, line, single letter towards bottom.
"""
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Setup the Window
win = visual.Window(size=[800,600], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
    
LetterStimulus = visual.TextStim(win=win, ori=0, name='LetterStimulus',
    text='defult text',    font='Arial',
    pos=[0, 0.6], height=0.2, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
# This is a line extending almost across the screen
UpperLineStim = visual.Line(win, start=(-0.95, 0.5), end=(0.95, 0.5))  
LowerLineStim = visual.Line(win, start=(-0.95, -0.5), end=(0.95, -0.5))  
# Make a series of craoshairs
RedCrossHair = visual.TextStim(win=win,ori = 0, name='ResCrossHair',
    text = '+', height = 0.2, color = 'red', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Prepare what will be drawn to the screen
LetterStimulus.draw()
UpperLineStim.draw()
LowerLineStim.draw()
RedCrossHair.draw()
# display what is prepared 
win.flip()
# remove what is shown
win.flip()

trialComponents = []
trialComponents.append(LetterStimulus)