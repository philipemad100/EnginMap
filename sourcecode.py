from decimal import Decimal
import matplotlib.pyplot as pt
import numpy as np
import re
from tkinter import *
def taskCalculations():
    with open("Vehicle Data.txt",'w')as f:
        f.write("")
    Pmax=int(PmaxEntry.get())
    NeMax=int(NeMaxEntry.get()) 
    Ne=[1000,2000,3000,4000,5000,6000]   #EngineTurns(rpm)
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

    blabla=["First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eightth","Ninth","Tenth","Eleventh"]
    ig=[]       #ig=GearboxReductionRatio
    for i in range(int(Nig)):
        IG=float(input("Enter "+blabla[i]+" Gear ratio: "))
        ig.insert(i,IG)

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
    
Pmax=Label(root,text="Pmax: ")
Pmax.grid(row=0,column=0)
PmaxEntry=Entry(root)
PmaxEntry.grid(row=0, column=1)
NeMax=Label(root,text="NeMax: ")
NeMax.grid(row=0,column=2)
NeMaxEntry=Entry(root)
NeMaxEntry.grid(row=0,column=3)

GVW=Label(root,text="GVW: ")
GVW.grid(row=1,column=0)
GVWEntry=Entry(root)
GVWEntry.grid(row=1, column=1)
Cd=Label(root,text="Drag Coefficient: ")
Cd.grid(row=1,column=2)
CdEntry=Entry(root)
CdEntry.grid(row=1,column=3)

Af=Label(root,text="Af: ")
Af.grid(row=2,column=0)
AfEntry=Entry(root)
AfEntry.grid(row=2,column=1)
z=Label(root,text="Eng. Efficiency: ")
z.grid(row=2,column=2)
zEntry=Entry(root)
zEntry.grid(row=2,column=3)

rw=Label(root,text="Radius of wheel: ")
rw.grid(row=3,column=0)
rwEntry=Entry(root)
rwEntry.grid(row=3,column=1)
iF=Label(root,text="Differential Reduction: ")
iF.grid(row=3,column=2)
iFEntry=Entry(root)
iFEntry.grid(row=3,column=3)

Nig=Label(root,text="Number of Gears")
Nig.grid(row=4,column=0)
NigEntry=Entry(root)
NigEntry.grid(row=4,column=1)
p=Label(root,text="Density of Air")
p.grid(row=4,column=2)
pEntry=Entry(root)
pEntry.grid(row=4,column=3)

fr=Label(root,text="Rolling Coefficient")
fr.grid(row=5,column=0)
frEntry=Entry(root)
frEntry.grid(row=5,column=1)
Butt=Button(root,text="Enter Data",command=taskCalculations)
Butt.grid(row=5,column=2)

root.mainloop()

