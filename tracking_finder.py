import pandas as pd
import numpy as np
import pvlib
azimuth = pd.read_csv("Azimuth.csv")
azimuth["Azimuth"] = [0.001 if a_ > 180 else a_ for a_ in azimuth["Azimuth"]]
zenith = pd.read_csv("solar2.csv")
Plib = pvlib.tracking.SingleAxisTracker()
data = Plib.singleaxis(apparent_zenith=zenith['SolarZenithAngle'],apparent_azimuth=azimuth['Azimuth'])
data2 = pvlib.tracking.singleaxis(apparent_zenith=zenith['SolarZenithAngle'],apparent_azimuth=azimuth['Azimuth'])
print(data,data2)
np.savetxt("tracking_data.csv", data, delimiter=",")
#np.savetxt("aaaatracking_data.csv", data2, delimiter=",")