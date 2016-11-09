win = visual.Window(size=[800,600], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )

Let = '[ABCDE]F'
LetStim = visual.TextStim(win=win, ori=0, name='LetStim',
    text = '',    font='Arial',
    pos=[0, 0.6], height=0.2, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

LetWidth = 0.8
LetLen = 6
Positions = np.arange(-0.8,0.81,1.6/(LetLen-1))

LetCount = 0
win.flip()
for i in range(0,LetLen+2,1):
    if (Let[i] != '[') & (Let[i] != ']'):
        LetStim.setColor('white')
        LetStim.setText(Let[i])
        LetStim.setPos([Positions[LetCount],0.9])
        LetStim.draw()        
        LetCount = LetCount + 1
    elif (Let[i] == '['):
        LetStim.setText(Let[i])
        LetStim.setColor('yellow')
        LetStim.setPos([Positions[LetCount]-0.1,0.9])
        LetStim.draw()  
    elif (Let[i] == ']'):
        LetStim.setText(Let[i])
        LetStim.setColor('yellow')
        LetStim.setPos([Positions[LetCount-1]+0.1,0.9])
        LetStim.draw()  
    print i
win.flip()

