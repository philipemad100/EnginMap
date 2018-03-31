from decimal import Decimal
import matplotlib.pyplot as pt
import numpy as np
def taskCalculations():
    with open("Vehicle Data.txt",'w')as f:
        f.write("")
    Pmax=129 ;NeMax=6000 
    Ne=[1000,2000,3000,4000,5000,6000]   #EngineTurns(rpm)
    Te=[]                                #EngineTorque
    Pe=[]                                #EnginePower
    for i in range(len(Ne)):                 #TorqueCalculations
        Pe.insert(i,round(Pmax*((Ne[i]/NeMax)+
                                ((Ne[i]/NeMax)**2)-
                                ((Ne[i]/NeMax)**3)),2))
        Te.insert(i,(round(((9550*Pe[i])/Ne[i]),2)))
    V1=[];FA1=[];TE1=[];DF1=[];a1=[]     #V=Velocity
    V2=[];FA2=[];TE2=[];DF2=[];a2=[]     #TE=TractiveEffort
    V3=[];FA3=[];TE3=[];DF3=[];a3=[]     #DF=DynamicFactor
    V4=[];FA4=[];TE4=[];DF4=[];a4=[]     #a=Accleration
    V5=[];FA5=[];TE5=[];DF5=[];a5=[]
    V6=[];FA6=[];TE6=[];DF6=[];a6=[]
    
    GVW=24000; Cd=0.38
    #GVW=  rossVehicleMass; Cd= DragCoefficient
    Af=2.936; iF=4.25
    #Af= AirResistance; iF= DiffrentialReductionRatio
    rw=0.36865; p=1.225; z=0.95
    #rw= RadiusWheel; p= DensityOfAir; z= EfficiencyOfEngine
    fr=0.014; FR=fr*GVW;  
    #fr= RollingCoefficient #FR= RollingResistance
    ig=[3.359,2.095,1.485,1.056,0.754,0.556] 
    for i in range(len(Ne)): #First gear
        V1.insert(i,(round((0.377*Ne[i]*rw)/(ig[0]*iF),2)))
        FA1.insert(i,(round((0.5*p*Cd*Af*((5/18)*V1[i])**2),2)))
        TE1.insert(i,(round((Te[i]*z*ig[0]*iF)/rw,2)))
        DF1.insert(i,(round((TE1[i]-FA1[i])/GVW,3)))
        a1.insert(i,round(TE1[i]/(GVW/9.8),2))
    FT1=list(np.asarray(FA1)+FR) #FT= TotalResistance
    print("V1="+str(V1));print("FA1="+str(FA1));
    print("TE1="+str(TE1));print("DF1="+str(DF1));
    print("FT1="+str(FT1));print("Acc1="+str(a1))
    print("-------------------")
    for i in range(len(Ne)): #Second gear
        V2.insert(i,(round((0.377*Ne[i]*rw)/(ig[1]*iF),2)))
        FA2.insert(i,(round((0.5*p*Cd*Af*((5/18)*V2[i])**2),2)))
        TE2.insert(i,(round((Te[i]*z*ig[1]*iF)/rw,2)))
        DF2.insert(i,(round((TE2[i]-FA2[i])/GVW,3)))
        a2.insert(i,round(TE2[i]/(GVW/9.8),2))
    FT2=list(np.asarray(FA2)+FR)
    print("V2="+str(V2));print("FA2="+str(FA2));
    print("TE2="+str(TE2));print("DF2="+str(DF2));
    print("FT2="+str(FT2));print("Acc2="+str(a2))
    print("---------------------")
    for i in range(len(Ne)): #Third gear
        V3.insert(i,(round((0.377*Ne[i]*rw)/(ig[2]*iF),2)))
        FA3.insert(i,(round((0.5*p*Cd*Af*((5/18)*V3[i])**2),2)))
        TE3.insert(i,(round((Te[i]*z*ig[2]*iF)/rw,2)))
        DF3.insert(i,(round((TE3[i]-FA3[i])/GVW,3)))
        a3.insert(i,round(TE3[i]/(GVW/9.8),2))
    FT3=list(np.asarray(FA3)+FR)
    print("V3="+str(V3));print("FA3="+str(FA3));
    print("TE3="+str(TE3));print("DF3="+str(DF3));
    print("FT3="+str(FT3));print("Acc3="+str(a3))
    print("---------------------")
    for i in range(len(Ne)): #Fourth gear
        V4.insert(i,(round((0.377*Ne[i]*rw)/(ig[3]*iF),2)))
        FA4.insert(i,(round((0.5*p*Cd*Af*((5/18)*V4[i])**2),2)))
        TE4.insert(i,(round((Te[i]*z*ig[3]*iF)/rw,2)))
        DF4.insert(i,(round((TE4[i]-FA4[i])/GVW,3)))
        a4.insert(i,round(TE4[i]/(GVW/9.8),2))
    FT4=list(np.asarray(FA4)+FR)
    print("V4="+str(V4));print("FA4="+str(FA4));
    print("TE4="+str(TE4));print("DF4="+str(DF4));
    print("FT4="+str(FT4));print("Acc4="+str(a4))
    print("---------------------")
    for i in range(len(Ne)): #fifth gear
        V5.insert(i,(round((0.377*Ne[i]*rw)/(ig[4]*iF),2)))
        FA5.insert(i,(round((0.5*p*Cd*Af*((5/18)*V5[i])**2),2)))
        TE5.insert(i,(round((Te[i]*z*ig[4]*iF)/rw,2)))
        DF5.insert(i,(round((TE5[i]-FA5[i])/GVW,3)))
        a5.insert(i,round(TE5[i]/(GVW/9.8),2))
    FT5=list(np.asarray(FA5)+FR)
    print("V5="+str(V5));print("FA5="+str(FA5));
    print("TE5="+str(TE5));print("DF5="+str(DF5));
    print("FT5="+str(FT5));print("Acc5="+str(a5))
    print("---------------------")
    for i in range(len(Ne)): #sixth gear
        V6.insert(i,(round((0.377*Ne[i]*rw)/(ig[5]*iF),2)))
        FA6.insert(i,(round((0.5*p*Cd*Af*((5/18)*V6[i])**2),2)))
        TE6.insert(i,(round((Te[i]*z*ig[5]*iF)/rw,2)))
        DF6.insert(i,(round((TE6[i]-FA6[i])/GVW,3)))
        a6.insert(i,round(TE6[i]/(GVW/9.8),2))
    FT6=list(np.asarray(FA6)+FR)
    print("V6="+str(V6));print("FA6="+str(FA6));
    print("TE6="+str(TE6));print("DF6="+str(DF6));
    print("FT6="+str(FT6));print("Acc6="+str(a6))

    with open("Vehicle Data.txt",'a+')as f:                              #Saving Data into a Text File
        f.write("V1= "+str(V1)+"\n"+"FA1="+str(FA1)+"\n"+"TE1="+str(TE1)+"\n"+"DF1="+str(DF1)+"\n"+
                "----------------------------------------------"+"\n")
        f.write("V2= "+str(V2)+"\n"+"FA2="+str(FA2)+"\n"+"TE2="+str(TE2)+"\n"+"DF2="+str(DF2)+"\n"+
                "----------------------------------------------"+"\n")
        f.write("V3= "+str(V3)+"\n"+"FA3="+str(FA3)+"\n"+"TE3="+str(TE3)+"\n"+"DF3="+str(DF3)+"\n"+
                "----------------------------------------------"+"\n")
        f.write("V4= "+str(V4)+"\n"+"FA4="+str(FA4)+"\n"+"TE4="+str(TE4)+"\n"+"DF4="+str(DF4)+"\n"+
                "----------------------------------------------"+"\n")
        f.write("V5= "+str(V5)+"\n"+"FA5="+str(FA5)+"\n"+"TE5="+str(TE5)+"\n"+"DF5="+str(DF5)+"\n"+
                "----------------------------------------------"+"\n")
        f.write("V6= "+str(V6)+"\n"+"FA6="+str(FA6)+"\n"+"TE6="+str(TE6)+"\n"+"DF6="+str(DF6)+"\n"+"\n")

    fig=pt.figure()
    fig.patch.set_facecolor("grey")
    
    TEV=fig.add_subplot(2,2,1)                  #Tractive Effort Graph
    TEV.plot(V1,TE1,"black",label="First Gear") #First Gear
    TEV.plot(V2,TE2,"red",label="Second Gear")  #Second Gear
    TEV.plot(V3,TE3,"blue",label="Third Gear")  #Third Gear
    TEV.plot(V4,TE4,"green",label="Fourth Gear")#Fourth Gear
    TEV.plot(V5,TE5,"orange",label="Fifth Gear")#Fifth Gear
    TEV.plot(V6,TE6,"magenta",label="Sixth Gear")#Sixth Gear
    TEV.set_xlabel('V (Km/hr)')
    TEV.set_ylabel("Tractive Effort")
    pt.grid(linewidth=1)
    pt.ylim([0,9100])
    pt.legend()

    DFV=fig.add_subplot(2,2,3)                  #Dynamic Factor Graph
    DFV.plot(V1,DF1,"black",label="First Gear") #First Gear
    DFV.plot(V2,DF2,"red",label="Second Gear")  #Second Gear
    DFV.plot(V3,DF3,"blue",label="Third Gear")  #Third Gear
    DFV.plot(V4,DF4,"green",label="Fourth Gear")#Fourth Gear
    DFV.plot(V5,DF5,"orange",label="Fifth Gear")#Fifth Gear
    DFV.plot(V6,DF6,"magenta",label="Sixth Gear")#Sixth Gear
    DFV.set_xlabel('V (Km/hr)')
    DFV.set_ylabel("Dynamic Factor")
    pt.ylim([0,0.4])
    pt.xlim([0,200])
    pt.grid(linewidth=1)
    pt.legend()

    FTV=DFV.twinx()
    FTV.plot(V1,FT1,"black")
    FTV.plot(V2,FT2,"black")
    FTV.plot(V3,FT3,"black")
    FTV.plot(V4,FT4,"black")
    FTV.plot(V5,FT5,"black")
    FTV.plot(V6,FT6,"black")
    FTV.set_ylabel("Total Resistance")
    pt.grid(linewidth=1)

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
    pt.show()
taskCalculations()
