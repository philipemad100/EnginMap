from decimal import Decimal
import matplotlib.pyplot as pt
import numpy as np
def taskCalculations():
    with open("Vehicle Data.txt",'w')as f:
        f.write("")
    Pmax=int(input("Enter Max. Power (in KW): "))
    NeMax=int(input("Enter RPM at max Power: ")) 
    Ne=[1000,2000,3000,4000,5000,6000]   #EngineTurns(rpm)
    Te=[]                                #EngineTorque
    Pe=[]                                #EnginePower
    for i in range(len(Ne)):                 #TorqueCalculations
        Pe.insert(i,round(Pmax*((Ne[i]/NeMax)+
                                ((Ne[i]/NeMax)**2)-
                                ((Ne[i]/NeMax)**3)),2))
        Te.insert(i,(round(((9550*Pe[i])/Ne[i]),2)))
        
    GVW=float(input("Enter Gross Vehicle Weight OR Curb weight if available(N)"))#GVW= GrossVehicleWeight
    Cd =float(input("Enter Drag Coefficient (Cd): ")) #Cd= DragCoefficient
    Af =float(input("Enter Air resistance: ")) #Af= AirResistance
    z=float(input("Enter Efficiency of the Engine: ")) #z= EfficiencyOfEngine
    rw=float(input("Enter Radius of the Tire (in meters): ")) #rw= RadiusWheel
    Nig=input("Enter Number of Transmission Gears: ")
    blabla=["First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eightth","Ninth","Tenth","Eleventh"]
    ig=[]       #ig=GearboxReductionRatio
    for i in range(int(Nig)):
        IG=float(input("Enter "+blabla[i]+" Gear ratio: "))
        ig.insert(i,IG)
    iF=float(input("Enter Diffrential Reduction Ratio: ")) #iF= DiffrentialReductionRatio
    p=1.225 #p= DensityOfAir
    fr=0.014; FR=fr*GVW;  
    #fr= RollingCoefficient #FR= RollingResistance 
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
taskCalculations()
