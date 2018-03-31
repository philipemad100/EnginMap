from decimal import Decimal
import matplotlib.pyplot as pt
import numpy as np
def taskCalculations():
    Pe=[23.2,49.8,76.75,100.9,119.1,129] #EnginePower
    Ne=[1000,2000,3000,4000,5000,6000]   #EngineTurns(rpm)
    Te=[]                                #EngineTorque
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
    
    ig=[3.359,2.095,1.485,1.056,0.754,0.556] 
    for i in range(len(Pe)): #TorquePower
        Te.insert(i,(round(((9550*Pe[i])/Ne[i]),2)))
    for i in range(len(Ne)): #First gear
        V1.insert(i,(round((0.377*Ne[i]*rw)/(ig[0]*iF),2)))
        FA1.insert(i,(round((0.5*p*Cd*Af*((5/18)*V1[i])**2),2)))
        TE1.insert(i,(round((Te[i]*z*ig[0]*iF)/rw,2)))
        DF1.insert(i,(round((TE1[i]-FA1[i])/GVW,3)))
        a1.insert(i,round(TE1[i]/(GVW/9.8),2))
    print(V1);print(FA1);print(TE1);print(DF1)
    print("-------------------")
    for i in range(len(Ne)): #Second gear
        V2.insert(i,(round((0.377*Ne[i]*rw)/(ig[1]*iF),2)))
        FA2.insert(i,(round((0.5*p*Cd*Af*((5/18)*V2[i])**2),2)))
        TE2.insert(i,(round((Te[i]*z*ig[1]*iF)/rw,2)))
        DF2.insert(i,(round((TE2[i]-FA2[i])/GVW,3)))
        a2.insert(i,round(TE2[i]/(GVW/9.8),2))
    print(V2);print(FA2);print(TE2);print(DF2)
    print("---------------------")
    for i in range(len(Ne)): #Third gear
        V3.insert(i,(round((0.377*Ne[i]*rw)/(ig[2]*iF),2)))
        FA3.insert(i,(round((0.5*p*Cd*Af*((5/18)*V3[i])**2),2)))
        TE3.insert(i,(round((Te[i]*z*ig[2]*iF)/rw,2)))
        DF3.insert(i,(round((TE3[i]-FA3[i])/GVW,3)))
        a3.insert(i,round(TE3[i]/(GVW/9.8),2))
    print(V3);print(FA3);print(TE3);print(DF3)
    print("---------------------")
    for i in range(len(Ne)): #Fourth gear
        V4.insert(i,(round((0.377*Ne[i]*rw)/(ig[3]*iF),2)))
        FA4.insert(i,(round((0.5*p*Cd*Af*((5/18)*V4[i])**2),2)))
        TE4.insert(i,(round((Te[i]*z*ig[3]*iF)/rw,2)))
        DF4.insert(i,(round((TE4[i]-FA4[i])/GVW,3)))
        a4.insert(i,round(TE4[i]/(GVW/9.8),2))
    print(V4);print(FA4);print(TE4);print(DF4)
    print("---------------------")
    for i in range(len(Ne)): #fifth gear
        V5.insert(i,(round((0.377*Ne[i]*rw)/(ig[4]*iF),2)))
        FA5.insert(i,(round((0.5*p*Cd*Af*((5/18)*V5[i])**2),2)))
        TE5.insert(i,(round((Te[i]*z*ig[4]*iF)/rw,2)))
        DF5.insert(i,(round((TE5[i]-FA5[i])/GVW,3)))
        a5.insert(i,round(TE5[i]/(GVW/9.8),2))
    print(V5);print(FA5);print(TE5);print(DF5)
    print("---------------------")
    for i in range(len(Ne)): #sixth gear
        V6.insert(i,(round((0.377*Ne[i]*rw)/(ig[5]*iF),2)))
        FA6.insert(i,(round((0.5*p*Cd*Af*((5/18)*V6[i])**2),2)))
        TE6.insert(i,(round((Te[i]*z*ig[5]*iF)/rw,2)))
        DF6.insert(i,(round((TE6[i]-FA6[i])/GVW,3)))
        a6.insert(i,round(TE6[i]/(GVW/9.8),2))
    print(V6);print(FA6);print(TE6);print(DF6)



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
