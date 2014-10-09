#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.03), Sat Sep 20 20:39:42 2014
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0

#from psychopy import gui

from psychopy import visual, gui

win1 = visual.Window(size=(400, 200), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace=u'rgb',
    blendMode=u'avg', useFBO=True,
    )

win2 = visual.Window(size=(400, 200), fullscr=False, screen=1, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace=u'rgb',
    blendMode=u'avg', useFBO=True,
    )

Test1 = visual.TextStim(win=win1, ori=0, name='text',
    text=u'ONE',    font=u'Arial',
    pos=[0, 0], height=0.7, wrapWidth=None,
    color=u'red', colorSpace=u'rgb', opacity=1,
    depth=0.0)

Test2 = visual.TextStim(win=win2, ori=0, name='text',
    text=u'TWO',    font=u'Arial',
    pos=[0, 0], height=0.7, wrapWidth=None,
    color=u'red', colorSpace=u'rgb', opacity=1,
    depth=0.0)




Test1.draw()
win1.flip()

Test2.draw()
win2.flip()

        
infoDlg = gui.Dlg(title='Pick the screen to use')
infoDlg.addField('Screen',choices=["One","Two"])
infoDlg.show()