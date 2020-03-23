# This file generates the required azimuth values.
import pandas as pd
import numpy as np
from pysolar.solar import get_azimuth_fast
import pytz
import datetime
epoch = datetime.datetime(year=2014,month=1,day=1,hour=0,minute=0, tzinfo=pytz.timezone('Asia/Kolkata'))
sol = pd.read_csv("solar2.csv")
sol2 = pd.read_csv("Idata_solar.csv")
tzinf = pytz.timezone('Asia/Kolkata')
d_aware=tzinf.localize(datetime.datetime.now())

def calcAZ():
    angles=[]
    print("Started computing azimuth Angles",datetime.datetime.now())
    dd = pd.date_range(start="2014-01-01 00:30",end="2014-12-31 23:30",freq='H',tz='Asia/Kolkata')
    for x in dd:
        angles.append(get_azimuth_fast(19.11,72.9052,x.to_pydatetime()))
    return(angles)

angles = calcAZ()
np.savetxt("Azimuth.csv", angles, delimiter=",")