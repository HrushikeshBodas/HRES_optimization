import sys, datetime, math, csv
import numpy as np
import pandas as pd
sol = pd.read_csv("solar2.csv")
from pysolar.solar import get_altitude

def sin(var):
    return np.sin((1.0/360.0)*2*3.1415*var)
def cos(var):
    return np.cos((1.0/360.0)*2*3.1415*var)
def asin(var):
    return np.arcsin(var)*360/(2*3.1415)    
def acos(var):
    return np.arccos(var)*360/(2*3.1415)    

def ctheta(lat, dc, m, hA, az):
    ctheta = np.sin(lat)*(np.sin(dc)*np.cos(m)+np.cos(dc)*np.cos(az)*np.cos(hA)*np.sin(m))+np.cos(lat)*(np.cos(dc)*np.cos(hA)*np.cos(m)-np.sin(dc)*np.cos(az)*np.sin(m))+np.cos(dc)*np.sin(az)*np.sin(hA)*np.sin(m)
    return ctheta

def calcHA(df):
    hA=0
    hour = df["Hour"]
    minu = df["Minute"]
    if hour > 12 :
        hA = (hour - 12)*15+(minu/60.0)*15
        hA = -hA
    elif hour<12 :
        hA = (12 - hour)*15 - (minu/60.0)*15
    else:
        hA=0.0

def calcAZ(df):
    ddd = pd.date_range(start='2014-01-01 00:30',end='2014-12-31 23:30',freq='H',tz ='Asia/Calcutta') 
    angles=[]
    for x in ddd:
        angles.append(get_altitude(19.11,72.9052,x))
    return(angles)

def calculateI(df):
    sol['HA']=sol.apply(calcHA,axis=1)
    year = df["Year"]
    month = df["Month"]
    day = df["Day"]
    date1 = pd.to_datetime((year*1000+month*100+day).apply(str),format='%Y%m%d')
    epoch = "2014-01-01"
    year1, month1, day1 = map(int, epoch.split('-'))
    date0  = datetime.date(year1, month1, day1)
    n = (date1-date0).days+1
    dc = 23.45*np.sin(360.0*(284+n)/365.0)
    sol['AZ']=sol.apply(calcAZ,axis=1)       
    #theta = np.arccos(ctheta(19.1197, dc, 19.1197, sol['HA'], sol['AZ']))
    Idata = pd.read_csv("Idata_solar.csv")
    # calculating beam radiation now ...
    rb = ctheta(19.1197, dc, 19.1197, sol['HA'], sol['AZ'])/ctheta(19.1197, dc, 0, sol['HA'], sol['AZ'])
    rd = (1+cos(19.1197))*0.5
    rr = 0.2*(1-cos(19.1197))*0.5
    It = Idata[1]*rb+Idata[2]*rd+Idata[3]*rr
    return It*1.0/1000


print(calculateI(sol))

"""
datetime1 = input('Enter a date in YYYY-MM-DD format: ')
time_entry = input('Enter a time (LAT) in HHMM format: ')
DNI = float(input('Enter Direct Normal Irradiance : '))
lat = float(input('Enter latitude: '))
lon = float(input('Enter longitude: '))
m = float(input('Enter slope/tilt: '))
az =float(input('Enter azimuth: '))
Id = float(input('Enter Id: '))
Ig = float(input('Enter Ig: '))
calculateI(datetime1, time_entry, DNI, lat, lon, m, az, Id, Ig)
import pvlib
import pandas as pd
import numpy
from pysolar.solar import *
import datetime
sun_dat = pd.read_csv("solar2.csv")
lat = 19.130
lon = 72.910
#didx = pd.DatetimeIndex(start ='2014-01-01 00:30', freq ='H', periods = 24*365, tz ='Asia/Calcutta') 
#print(ddd)
for x in ddd:
    print(x)
    angles = get_altitude(lat,lon,datetime.datetime.now(tz=""))
    print(angles)
    break
#a = pvlib.tracking.singleaxis(sun_dat["SolarZenithAngle"],angles.azimuth)
#print(a)

"""