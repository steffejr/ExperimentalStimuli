#!/usr/bin/env python2
#rotate flashing wedge
from psychopy import visual, event, core

globalClock = core.Clock()
win = visual.Window([800,800])
#make two wedges (in opposite contrast) and alternate them for flashing
wedge1 = visual.RadialStim(win, tex='sqrXsqr', color=1,size=1,
    visibleWedge=[0, 45], radialCycles=4, angularCycles=8, interpolate=False,
    autoLog=False)#this stim changes too much for autologging to be useful
wedge2 = visual.RadialStim(win,tex='sqrXsqr', color=-1,size=1,
    visibleWedge=[0, 45], radialCycles=4, angularCycles=8, interpolate=False,
    autoLog=False)#this stim changes too much for autologging to be useful
grating1 = visual.GratingStim(win=win, name='grating',
    tex=u'sqrXsqr', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5], sf=5, phase=0.0,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)
grating2 = visual.GratingStim(win=win, name='grating_2',
    tex=u'sqrXsqr', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5], sf=5, phase=0.0,
    color=[-1,-1,-1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=-2.0)
t=0
rotationRate = 0.01 #revs per sec
flashRate = 5.0 # Hertz
flashPeriod = 1/flashRate #seconds for one B-W cycle (ie 1/Hz)
while t<5:#for 5 secs
    t=globalClock.getTime()
    if (t%flashPeriod) < (flashPeriod/2.0):# (NB more accurate to use number of frames)
        stim = grating1
    else:
        stim=grating2
        
    #stim.setOri(t*rotationRate*360.0)
    stim.draw()
    win.flip()
    
win.close()
