from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
from psychopy.hardware.emulator import launchScan


trialClock = core.Clock()
continueRoutine = True
while continueRoutine and not 'escape' in event.getKeys():
    # get current time
    t1 = trialClock.getTime()

    t2 = globalClock.getTime()
    print 'Trial time is: %0.6f'%(t1)
    print 'Global time is: %0.6f'%(t2)
    if t1 > 0.1:
        continueRoutine = False