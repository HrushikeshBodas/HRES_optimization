import pandas as pd
import numpy as np
np.set_printoptions(threshold=np.inf)
from pysolar.solar import get_azimuth_fast
import pytz
import datetime
import sys
epoch = datetime.datetime(year=2014,month=1,day=1,hour=0,minute=0, tzinfo=pytz.timezone('Asia/Kolkata'))
sol = pd.read_csv("solar2.csv")
sol2 = pd.read_csv("Idata_solar.csv")
azimuth_angles=pd.read_csv("Azimuth.csv")
tzinf = pytz.timezone('Asia/Kolkata')
d_aware=tzinf.localize(datetime.datetime.now())
# P = it A eta
# It = Ir*rr + Ib*rb + Id*rd
'''
rb = ctheta(lat, dc, m, hA, az)/ctheta(lat, dc, 0, hA, az)
rd = (1+cos(m))*0.5
rr = 0.2*(1-cos(m))*0.5
It = Ib*rb+Id*rd+Ir*rr
   
'''
# get a set of dates
dd = pd.date_range(start="2014-01-01 00:30",end="2014-12-31 23:30",freq='H',tz='Asia/Kolkata')
# costheta function to get a numpy implementation of the formula given in sukhatme book
def ctheta(lat, dc, m, hA, az):
    ctheta = np.sin(1.0*lat)*np.multiply(np.cos(1.0*m),np.sin(1.0*dc))+np.sin(1.0*lat)*np.multiply(np.multiply(np.cos(1.0*dc),np.cos(1.0*az)),np.multiply(np.cos(1.0*hA),np.sin(1.0*m)))+np.cos(1.0*m)*np.cos(1.0*lat)*np.multiply(np.cos(1.0*dc),np.cos(1.0*hA))-np.sin(1.0*m)*np.cos(1.0*lat)*np.multiply(np.sin(1.0*dc),np.cos(1.0*az))+np.sin(1.0*m)*np.multiply(np.cos(1.0*dc),np.multiply(np.sin(1.0*az),np.sin(1.0*hA)))
    return ctheta

# function to calculate the hour angles.
def calcHA(df):
    hA=0
    if df['Hour'] > 12 :
        hA = (df['Hour'] - 12)*15+(df["Minute"]/60.0)*15
        hA = -hA
    elif df["Hour"]<12 :
        hA = (12 - df['Hour'])*15 - (df["Minute"]/60.0)*15
    else:
        hA=0.0
    return hA
# caclulates the coefficient rb
def calcrb(sol):
    return ctheta(19.1197, sol['dc'], 19.1197, sol['HA'], sol['AZ'])/ctheta(19.1197, sol['dc'], 0, sol['HA'], sol['AZ'])

#calculate input radiation to the solar panel per meter square at various time intervals
def calculateI(df):
   
    sol['HA']=sol.apply(calcHA,axis=1)
    #print(sol['HA'])
    n = (dd-epoch).days+1
   
    df['dc'] = -23.45*np.cos(1.0*2*np.pi*(10+n)/365.0)
    #print(df['dc'])
    sol['AZ'] = azimuth_angles['Azimuth']
    #print('Computed Az Angles')
    #theta = np.arccos(ctheta(19.1197, dc, 19.1197, sol['HA'], sol['AZ']))
    Idata = pd.read_csv("Idata_solar.csv")
    #print(Idata.head)
    # calculating beam radiation now ...
    sol['rb']=sol.apply(calcrb,axis=1)
    rd = (1+np.cos(1.0*19.1197))*0.5
    rr = 0.2*(1-np.cos(1.0*19.1197))*0.5
    It = np.multiply(Idata["Bi"],sol['rb'])+Idata["Di"]*rd+Idata["Ri"]*rr
    '''
    np.savetxt("BeamCompoent.csv", np.multiply(Idata['Bi'],sol['rb']), delimiter=",")
    np.savetxt("rb.csv", sol['rb'], delimiter=",")
    np.savetxt("Di.csv", Idata['Di'], delimiter=",")
    np.savetxt("Ri.csv", Idata['Ri'], delimiter=",")
    '''
    return It*1.0/1000

aaaa = calculateI(sol)
np.savetxt("It.csv", aaaa, delimiter=",")