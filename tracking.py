import pandas as pd
import numpy as np
import pvlib
'''
azimuth = pd.read_csv("Azimuth.csv")
azimuth["Azimuth"] = [0.001 if a_ > 180 else a_ for a_ in azimuth["Azimuth"]]
track = pd.read_csv("tracking_data.csv")
Plib = pvlib.tracking.SingleAxisTracker()
data = Plib.get_irradiance(track["surface_tilt"],track["surface_azimuth"])
data2 = pvlib.tracking.get_irra(apparent_zenith=zenith['SolarZenithAngle'],apparent_azimuth=azimuth['Azimuth'])
print(data,data2)
np.savetxt("tracking_data.csv", data, delimiter=",")
'''
#np.savetxt("aaaatracking_data.csv", data2, delimiter=",")
demand_ = pd.read_excel("iitb_demand.xlsx")
demand_.to_csv("./iitbdemand.csv",sep=',')