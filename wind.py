import pandas as pd
import math
wind_dat = pd.read_csv("wind copy.csv")
sun_dat = pd.read_csv("solar2.csv")
#print(data["ClearskyDHI"][10])
#print(data['DHI'][10])
def daily_en(dd,mm,yy):
    wind_day = wind_dat
    #print(wind_day.head)
    #wind_day.loc[:,'Power']=0.0
    wind_day['Power']=wind_day.apply(wind_gen,axis=1)
    print(wind_day["speed","Power"])
    

def wind_gen(df):
    #print(df)
    Vrated=11
    Vcutin=3
    Vcutoff=25
    Prated=25000
    rho=1.225
    pow = 0
    cp = {3:0.130,3.5:0.3,4:0.39,4.5:0.430,5:0.450,6:0.47,7:0.48,8:0.47,9:0.43,10:0.35,11:0.27,12:0.21,13:0.17,14:0.13,15:0.11,16:0.09,17:0.07,18:0.06,19:0.05,20:0.05}
    if(df["speed"]<Vcutin):
        #print("off")
        pow = 0
    elif(df["speed"]>Vcutin and df["speed"]< Vrated):
        cpi=cp[math.floor(df["speed"]) if df["speed"]>5 else math.floor(2*df["speed"])/2]
        pow = 0.5*cpi*rho*11307*df["speed"]*df["speed"]*df["speed"]
    elif(df["speed"]>Vrated and df["speed"]< Vcutoff):
        pow = Prated
    else:
        pow =  0
    return pow

daily_en(2014,1,1)
'''
Year,Month,Day,Hour,Minute,DHI,DNI,GHI,Clearsky DHI,Clearsky DNI,Clearsky GHI,Dew Point,Temperature,Pressure,Relative Humidity,Solar Zenith Angle,Precipitable Water,Snow Depth,Wind Direction,Wind Speed,Fill Flag
Power from solar is given by
P = eta * Area * I(tilted)
eta = eta_r * eta_pc * (1-beta*(T_c - T_cref))
T_c = T_a + (NOCT-20)/800*I(tilted)


Wind Model :
2.5 Mw 
cut in 3
cut off 25
dia 120 
hub height 110/139 m

'''