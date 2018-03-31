import matplotlib.pyplot as pt
import numpy as np
from tkinter import *
import tkinter as tk
from tkinter import font  as tkfont #for customizing Font

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        global container
        container = tk.Frame(self)
        container.pack(side="left", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=10)
        container.grid_columnconfigure(0, weight=10)

        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container,
                      controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        
    def get_page(self, page_class):
        return self.frames[page_class]


class StartPage(tk.Frame):
    
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Engine's Data", font=controller.title_font)
        label.grid(row=0,column=2)
        
        global PmaxEntry
        Pmax=Label(self,text="Pmax: ")
        Pmax.grid(row=1,column=0)
        PmaxEntry=Entry(self)
        PmaxEntry.grid(row=1, column=1)
        global NeMaxEntry
        NeMax=Label(self,text="NeMax: ")
        NeMax.grid(row=1,column=2)
        NeMaxEntry=Entry(self)
        NeMaxEntry.grid(row=1,column=3)
        global GVWEntry
        GVW=Label(self,text="GVW: ")
        GVW.grid(row=1,column=4)
        GVWEntry=Entry(self)
        GVWEntry.grid(row=1, column=5)
        global CdEntry
        Cd=Label(self,text="Drag Coefficient: ")
        Cd.grid(row=2,column=0)
        CdEntry=Entry(self)
        CdEntry.grid(row=2,column=1)
        global AfEntry
        Af=Label(self,text="Af: ") 
        Af.grid(row=2,column=2)
        AfEntry=Entry(self)
        AfEntry.grid(row=2,column=3)
        global zEntry
        z=Label(self,text="Eng. Efficiency: ") 
        z.grid(row=2,column=4)
        zEntry=Entry(self)
        zEntry.grid(row=2,column=5)
        global rwEntry
        rw=Label(self,text="Radius of wheel: ") 
        rw.grid(row=3,column=0)
        rwEntry=Entry(self)
        rwEntry.grid(row=3,column=1)
        global iFEntry
        iF=Label(self,text="Differential Reduction: ")
        iF.grid(row=3,column=2)
        iFEntry=Entry(self)
        iFEntry.grid(row=3,column=3)
        global frEntry
        fr=Label(self,text="Rolling Coefficient")
        fr.grid(row=3,column=4)       
        frEntry=Entry(self)
        frEntry.grid(row=3,column=5)
        global pEntry
        p=Label(self,text="Density of Air")
        p.grid(row=4,column=0)
        pEntry=Entry(self)
        pEntry.grid(row=4,column=1)
        global NigEntry
        Nig=Label(self,text="Number of Gears")
        Nig.grid(row=4,column=4)
        NigEntry=Entry(self)
        NigEntry.grid(row=4,column=5)        
        Butt=Button(self,text="Transmission Ratios",
                    command=lambda: controller.show_frame("PageOne"))
        Butt.grid(row=5,column=2)
        copr=tk.Label(self,text="© 2018 Philip Emad")
        copr.grid(row=5, column=3)
        
class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Transmission Ratios", font=controller.title_font)
        label.pack()        
        nutt=Button(self,text="Enter Transmission Ratios",command=Calculations.transmission)
        nutt.pack()
        Butt=Button(self,text="Calculate",command=Calculations.taskCalculations)
        Butt.pack()
        copr=tk.Label(self,text="© 2018 Philip Emad")
        copr.pack()
        
class Calculations():

    def transmission(): #For "PageOne" Frame  
        GearNames=["First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eightth","Ninth","Tenth","Eleventh"]
        global ig
        global iG
        iG={}
        for i in range (int(NigEntry.get())):
            ig=[]
            iG['ig{}'.format(i)] =(ig)
            IG=Label(container,text="Enter "+GearNames[i]+" Gear ratio: ")
            IG.grid(row=i+1,column=0)
            (iG['ig' +str(i)])=Entry(container)
            (iG['ig' +str(i)]).grid(row=i+1,column=1)
    def taskCalculations():
        with open("Vehicle Data.txt",'w')as f:
            f.write("")
        Pmax=float(PmaxEntry.get()) #Pmax= MaximumPower
        NeMax=int(NeMaxEntry.get()) #NeMax= Maximum Rpm 
        Ne=[1000,2000,3000,4000,5000,6000,7000]   #EngineTurns(rpm)
        Te=[]                                #EngineTorque
        Pe=[]                                #EnginePower
        for i in range(len(Ne)):                 #TorqueCalculations
            Pe.insert(i,round(Pmax*((Ne[i]/NeMax)+
                                    ((Ne[i]/NeMax)**2)-
                                    ((Ne[i]/NeMax)**3)),2))
            Te.insert(i,(round(((9550*Pe[i])/Ne[i]),2)))
            
        GVW=float(GVWEntry.get())#GVW=  rossVehicleMass
        Cd= float(CdEntry.get()) #Cd= DragCoefficient
        Af= float(AfEntry.get()) #Af= AirResistance
        z=  float(zEntry.get())  #z= EfficiencyOfEngine
        rw= float(rwEntry.get()) #rw= RadiusWheel
        iF= float(iFEntry.get()) #iF= DiffrentialReductionRatio
        Nig=int(NigEntry.get())  #Nig=NumberOfTransmissionGears
        p=  float(pEntry.get())  #p= DensityOfAir
        fr= float(frEntry.get()) #fr= RollingCoefficient

        for i in range (int(NigEntry.get())): #Inserting Gear Ratios From Their Entries
            ig.insert(i,float((iG['ig' +str(i)]).get()))

        FR=fr*GVW;
        #FR= RollingResistance 
        EngData={}
        for i in range(len(ig)):#Calculations + Plotting
            V=[]                #V=Velocity
            FA=[]               #AirResistance
            TE=[]               #TE=TractiveEffort
            DF=[]               #DF=DynamicFactor
            FT=[]               #FT=TotalResistance
            ACC=[]              #ACC=Accleration
            for j in range(len(Ne)):
                V.insert(j,(round((0.377*Ne[j]*rw)/(ig[i]*iF),2)))
                FA.insert(j,(round((0.5*p*Cd*Af*((5/18)*V[j])**2),2)))
                TE.insert(j,(round((Te[j]*z*ig[i]*iF)/rw,2)))
                DF.insert(j,(round((TE[j]-FA[j])/GVW,3)))
                FT.insert(j,(round(FA[j]+FR,2)))
                ACC.insert(j,(round((DF[j]-fr)/(GVW/9800),2)))
            EngData['V{}'.format(i)] =(V) ; EngData['FA{}'.format(i)]=(FA)
            EngData['TE{}'.format(i)]=(TE); EngData['DF{}'.format(i)]=(DF)
            EngData['FT{}'.format(i)]=(FT); EngData['ACC{}'.format(i)]=(ACC)
            a=("V"   +str(i+1)+"="+ str(EngData['V'  +str(i)])); b=("FA"  +str(i+1)+"="+ str(EngData['FA' +str(i)]))
            c=("TE"  +str(i+1)+"="+ str(EngData['TE' +str(i)])); d=("DF"  +str(i+1)+"="+ str(EngData['DF' +str(i)]))
            e=("FT"  +str(i+1)+"="+ str(EngData['FT' +str(i)])); f=("Acc"+str(i+1)+"="+ str(EngData['ACC'+str(i)]))
            print("---------------------")
            print(a) ;print(b) ;print(c) ;print(d); print(e);print(f)
            with open("Vehicle Data.txt",'a')as f:     #Saving Data into a Text File
                f.write(str(a)+"\n"+str(b)+"\n"+
                        str(c)+"\n"+str(d)+"\n"+
                        str(e)+"\n"+str(f)+"\n"+
                        "----------------------------------------------"+"\n")


        fig=pt.figure()
        fig.patch.set_facecolor("grey")
        
        TEV=fig.add_subplot(2,2,1)      #TractiveEffortGraph
        TEV.set_xlabel('V (Km/hr)')
        TEV.set_ylabel("Tractive Effort")
        pt.ylim([0,max(EngData['TE'+str(0)])+200])
        pt.grid(linewidth=1)

        DFV=fig.add_subplot(2,2,3)      #DynamicFactorGraph
        DFV.set_xlabel('V (Km/hr)')
        DFV.set_ylabel("Dynamic Factor")
        pt.ylim([0,max(EngData['DF'+str(0)])+0.01])
        pt.xlim([0,250])
        pt.grid(linewidth=1)

        FTV=DFV.twinx()                 #TotalResistanceGraph
        FTV.set_ylabel("Total Resistance")

        TorqueGraph=fig.add_subplot(1,2,2)          #TorquePowerGraph
        TorqueGraph.plot(Ne,Te,"black",label="Torque")
        TorqueGraph.set_xlabel('rpm')
        TorqueGraph.set_ylabel("Torque")
        pt.grid(linewidth=1)
        pt.legend()

        PowerGraph=TorqueGraph.twinx()              #TorquePowerGraph
        PowerGraph.plot(Ne,Pe,"red",label="Power")
        PowerGraph.set_ylabel("Power")
        pt.legend()

        for i in range(len(ig)):
            TEV.plot(EngData['V'+str(i)],EngData['TE'+str(i)])
            DFV.plot(EngData['V'+str(i)],EngData['DF'+str(i)])
            FTV.plot(EngData['V'+str(i)],EngData['FT'+str(i)],"black")
        pt.show()
    
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
