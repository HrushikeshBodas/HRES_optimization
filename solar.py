'''
import pandas as pd
import numpy
import math
import datetime
sun_dat = pd.read_csv("solar2.csv")
def calculateI(df):
    hour = float(df["Hour"])
    minu = float(df["Minute"])
    hA=0
    if hour > 12 :
        hA = (hour - 12)*15+(minu/60.0)*15
        hA = -hA
    elif hour<12 :
        hA = (12 - hour)*15 - (minu/60.0)*15
    else:
        hA=0.0
    year = int(df["Year"])
    month = int(df["Month"])
    day = int(df["Day"])
    date1 = datetime.date(year, month, day)
    epoch = "2014-01-01"
    year1, month1, day1 = map(int, epoch.split('-'))
    date0  = datetime.date(year1, month1, day1)
    n = (date1-date0).days+1
    dc = 23.45*sin(360.0*(284+n)/365.0)
    #az=
    theta = acos(ctheta(19.1197, dc, m, hA, az))
    
    # calculating beam radiation now ...
    rb = ctheta(lat, dc, m, hA, az)/ctheta(lat, dc, 0, hA, az)
    rd = (1+cos(m))*0.5
    rr = 0.2*(1-cos(m))*0.5
    It = Ib*rb+Id*rd+Ir*rr
    return It*1.0/1000


data = np.genfromtxt("solar2.csv", dtype=float, delimiter=',', names=True)
wind_dat = pd.read_csv("wind copy.csv")
sun_dat = pd.read_csv("solar2.csv")
def solar_gen(eff,A,Ibn,theta,phi):
    #I_t = Ib_t + Id_t + Ir_t
    rho = 1.225
    #I_t = Ibn*(math.cos(theta)+C*math.cos(phi/2)*math.cos(phi/2)+rho*(math.cos(chi)+C)*math.sin(phi/2)*math.sin(phi/2))
import sys, datetime, math, csv

def sin(var):
    return math.sin((1.0/360.0)*2*3.1415*var)
def cos(var):
    return math.cos((1.0/360.0)*2*3.1415*var)
def asin(var):
    return math.asin(var)*360/(2*3.1415)    
def acos(var):
    return math.acos(var)*360/(2*3.1415)    

def ctheta(lat, dc, m, hA, az):
    ctheta = sin(lat)*(sin(dc)*cos(m)+cos(dc)*cos(az)*cos(hA)*sin(m))+cos(lat)*(cos(dc)*cos(hA)*cos(m)-sin(dc)*cos(az)*sin(m))+cos(dc)*sin(az)*sin(hA)*sin(m)
    return ctheta

def calculateI(datetime1, Ib,Id,Ir,lat, lon, m, az):
    hour = float(datetime1[9:11])
    minu = float(datetime1[12:14])
    hA=0
    if hour > 12 :
        hA = (hour - 12)*15+(minu/60.0)*15
        hA = -hA
    elif hour<12 :
        hA = (12 - hour)*15 - (minu/60.0)*15
    else:
        hA=0.0
    year = int(datetime1[0:4] )
    month = int(datetime1[4:6])
    day = int(datetime1[6:8])
    date1 = datetime.date(year, month, day)
    epoch = "2019-01-01"
    year1, month1, day1 = map(int, epoch.split('-'))
    date0  = datetime.date(year1, month1, day1)
    n = (date1-date0).days+1
    dc = 23.45*sin(360.0*(284+n)/365.0)
    theta = acos(ctheta(lat, dc, m, hA, az))
    
    # calculating beam radiation now ...
    rb = ctheta(lat, dc, m, hA, az)/ctheta(lat, dc, 0, hA, az)
    rd = (1+cos(m))*0.5
    rr = 0.2*(1-cos(m))*0.5
    It = Ib*rb+Id*rd+Ir*rr
    return It*1.0/1000



def driver():
    with open('./data.csv','rt')as f:
        data = csv.reader(f)
        for row in data:
            datetime1 = row[0]
            Ib=float(row[1])
            Id=float(row[2])
            Ir=float(row[3])
            az=90.0-float(row[4])
            lat = 19.130
            lon = 72.910
            m = 0
            print(datetime1," ",calculateI(datetime1, Ib,Id,Ir,lat, lon, m, az),"\n")

if __name__ == "__main__":
    driver()
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
'''