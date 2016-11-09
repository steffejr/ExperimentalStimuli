#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
import PartialTrialFunction
#import ProcessAFile

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        #self.entryVariable1 = Tkinter.StringVar()
        self.subIDVar = Tkinter.StringVar()
        self.entry1 = Tkinter.Entry(textvariable=self.subIDVar)
        self.subIDVar.set(9999)
        
        self.visIDVar = Tkinter.StringVar()
        self.entry2 = Tkinter.Entry(textvariable=self.visIDVar)
        self.visIDVar.set(0001)
        
        self.entry1.grid(column=0,row=1,sticky='EW')
        self.entry2.grid(column=0,row=3,sticky='EW')
        
        
        #self.entry.bind("<Return>", self.OnPressEnter)
        
        #self.entryVariable1.set(u"9999")
        labelSubid = Tkinter.Label(self,text='Participant ID')
        labelSubid.grid(column=0,row=0)
        
        #self.entryVariable2 = Tkinter.StringVar()
        #self.entry2 = Tkinter.Entry(self,textvariable=self.entryVariable2)
        
        #self.entry2.grid(column=0,row=3,sticky='EW')
        #self.entry2.bind("<Return>", self.OnPressEnter)
        
        #self.entryVariable2.set(u"0001")
        labelVisitid = Tkinter.Label(self,text='Visit ID')
        labelVisitid.grid(column=0,row=2)
        
# Make the buttons
        button1 = Tkinter.Button(self,text=u"Training in order with FB",
                                command=self.OnButtonClickTrainOrderFB,width = 25)
        button4 = Tkinter.Button(self,text=u"Training with FB",
                                command=self.OnButtonClickTrainFB,width = 25)
        button5 = Tkinter.Button(self,text=u"Training NO FB",
                                command=self.OnButtonClickTrainNoFB,width = 25)
        button2 = Tkinter.Button(self,text=u"Run 1",
                                command=self.OnButtonClickRun1,width = 25)

        button3 = Tkinter.Button(self,text=u"Run 2",
                                command=self.OnButtonClickRun2,width = 25)

        button14 = Tkinter.Button(self,text=u"optional Run 3",
                                command=self.OnButtonClickRun3,width = 25)
                                
        button6 = Tkinter.Button(self,text=u"Instructions",
                                command=self.OnButtonClickInstructions,width = 25)                                

        button11 = Tkinter.Button(self,text=u"Test One Trial",
                                command=self.TestOneTrial,width = 25)    
        button12 = Tkinter.Button(self,text=u"Test Button",
                                command=self.TestButton,width = 25)    
        # Checkbox for the completion of training
        self.CB1Var = Tkinter.IntVar()
        self.CB1Var.set(0)
        self.Check1 = Tkinter.Checkbutton(self,text="Complete",variable = self.CB1Var,state='disabled',disabledforeground='blue')
        
        self.CB2Var = Tkinter.IntVar()
        self.CB2Var.set(0)
        self.Check2 = Tkinter.Checkbutton(self,text="Complete",variable = self.CB2Var,state='disabled',disabledforeground='blue')
        
        self.CB3Var = Tkinter.BooleanVar()
        self.Check3 = Tkinter.Checkbutton(self,text="Complete",variable = self.CB3Var,state='disabled',disabledforeground='blue')
        
        button6.grid(column=1,row=0)        
        button1.grid(column=1,row=1)        
        button4.grid(column=1,row=2)                        
        button5.grid(column=1,row=3)        
        button2.grid(column=1,row=4)        
        button3.grid(column=1,row=5)        
        button14.grid(column=1,row=8)        

        button11.grid(column = 3,row = 1)
        button12.grid(column = 3,row = 2)
        
        self.Check1.grid(column=2,row=10)
        self.Check2.grid(column=2,row=11)
        self.Check3.grid(column=2,row=12)
        
        CloseButton = Tkinter.Button(text = "Good-bye.", command = self.close_window)
        CloseButton.grid(column=3,row = 13)
#        label = Tkinter.Label(self,textvariable=self.labelVariable,
#                              anchor="w",fg="white",bg="blue")
        
        #label.grid(column=0,row=3,columnspan=2,sticky='EW')


        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())       
        self.entry1.focus_set()
        self.entry1.selection_range(0, Tkinter.END)
    def close_window(self):
        app.destroy()
        
    def OnButtonClickInstructions(self):
#        self.labelVariable.set( self.entryVariable.get()+" (Train 1)" )
#        self.entry.focus_set()
#        self.entry.selection_range(0, Tkinter.END)
        PartialTrialFunction.Instructions()
        # Every time the button is pressed the check box alternates
        if self.CB1Var.get() == 1:
            self.Check1.deselect()
            self.CB1Var.set(0)
        else:
            self.Check1.select()
            self.CB1Var.set(1)

    def TestOneTrial(self):
#        self.labelVariable.set( self.entryVariable.get()+" (Train 1)" )
#        self.entry.focus_set()
#        self.entry.selection_range(0, Tkinter.END)
        OutFile = PartialTrialFunction.PartialTrial('../../ExperimentalTrials/OneTrial.csv')
       # ProcessAFile.ProcessAFile(OutFile+'.csv','1111','TestTag')
        print OutFile
        # Every time the button is pressed the check box alternates
        if self.CB1Var.get() == 1:
            self.Check1.deselect()
            self.CB1Var.set(0)
        else:
            self.Check1.select()
            self.CB1Var.set(1)
            
    def TestButton(self):
#        self.labelVariable.set( self.entryVariable.get()+" (Train 1)" )
#        self.entry1.focus_set()
#        self.entry1.selection_range(0, Tkinter.END)
        #PartialTrialFunction.TestSomething(self.subIDVar.get(),self.visIDVar.get())
        PartialTrialFunctionV2.Test(self.subIDVar.get(),self.visIDVar.get())
        #PartialTrialFunction.PartialTrial('TwoTrials.csv',self.subIDVar.get(),self.visIDVar.get())
        
    def OnButtonClickTrainOrderFB(self):
#        self.labelVariable.set( self.entryVariable.get()+" (Train 1)" )
#        self.entry1.focus_set()
#        self.entry1.selection_range(0, Tkinter.END)
        PartialTrialFunction.PartialTrialFeedback('../../ExperimentalTrials/Training30TrialsInOrder.csv',self.subIDVar.get(),self.visIDVar.get())
        # Every time the button is pressed the check box alternates
        if self.CB1Var.get() == 1:
            self.Check1.deselect()
            self.CB1Var.set(0)
        else:
            self.Check1.select()
            self.CB1Var.set(1)
            
    def OnButtonClickTrainFB(self):
#        self.labelVariable.set( self.entryVariable.get()+" (Train 1)" )
#        self.entry.focus_set()
#        self.entry.selection_range(0, Tkinter.END)
        PartialTrialFunction.PartialTrialFeedback('../../ExperimentalTrials/Practice30Trials6LoadsVer1.csv',self.subIDVar.get(),self.visIDVar.get())
        # Every time the button is pressed the check box alternates
        if self.CB1Var.get() == 1:
            self.Check1.deselect()
            self.CB1Var.set(0)
        else:
            self.Check1.select()
            self.CB1Var.set(1)
            
    def OnButtonClickTrainNoFB(self):
#        self.labelVariable.set( self.entryVariable.get()+" (Train 1)" )
#        self.entry.focus_set()
#        self.entry.selection_range(0, Tkinter.END)
        PartialTrialFunction.PartialTrial('../../ExperimentalTrials/Practice30Trials6LoadsVer2.csv',self.subIDVar.get(),self.visIDVar.get())
        # Every time the button is pressed the check box alternates
        if self.CB1Var.get() == 1:
            self.Check1.deselect()
            self.CB1Var.set(0)
        else:
            self.Check1.select()
            self.CB1Var.set(1)


    def OnButtonClickRun1(self):
#        self.labelVariable.set( self.entryVariable.get()+" (Run 1)" )
#        self.entry.focus_set()
#        self.entry.selection_range(0, Tkinter.END)
        PartialTrialFunction.PartialTrial('../../ExperimentalTrials/Optimized72Trials_6LoadsVer1.csv',self.subIDVar.get(),self.visIDVar.get())
        # Every time the button is pressed the check box alternates
        print self.CB2Var.get()
        if self.CB2Var.get() == 1:
            self.Check2.deselect()
            self.CB2Var.set(0)
        else:
            self.Check2.select()
            self.CB2Var.set(1)


    def OnButtonClickRun2(self):
#        self.labelVariable.set( self.entryVariable.get()+" (Run 2)" )
#        self.entry.focus_set()
        PartialTrialFunction.PartialTrial('../../ExperimentalTrials/Optimized72Trials_6LoadsVer2.csv',self.subIDVar.get(),self.visIDVar.get())
        #Test1.Test()
        self.entry.selection_range(0, Tkinter.END)
        # Every time the button is pressed the check box alternates
        if self.CB3Var.get() == 1:
            self.Check3.deselect()
            self.CB3Var.set(0)
        else:
            self.Check3.select()
            self.CB3Var.set(1)

    def OnButtonClickRun3(self):
#        self.labelVariable.set( self.entryVariable.get()+" (Run 2)" )
#        self.entry.focus_set()
        PartialTrialFunction.PartialTrial('../../ExperimentalTrials/Optimized72Trials_6LoadsVer3.csv',self.subIDVar.get(),self.visIDVar.get())
        #Test1.Test()
        self.entry.selection_range(0, Tkinter.END)
        # Every time the button is pressed the check box alternates
        if self.CB3Var.get() == 1:
            self.Check3.deselect()
            self.CB3Var.set(0)
        else:
            self.Check3.select()
            self.CB3Var.set(1)        
#    def OnPressEnter(self,event):
#        self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )
#        self.entry.focus_set()
#        self.entry.selection_range(0, Tkinter.END)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Partial Trial DIR Experiment')
    app.mainloop()