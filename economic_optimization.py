'''
Objective function to be minimised is 
F = C_one_time + C_o&m
C_one_time = C_pv + C_store + C_wind + C_backup
C_o&m = C_o&m_pv + C_o&m_wind + C_o&m_store + C_o&m_backup
minimise 
delta P = P_gen - P_demand
Pgen = sigma(wind,solar)
Pdem = from load data
storage = max(deltaP) - min delta P
N_bat = storage/capac
charging
battery(t) = battery(t-1) + (P_pv(t)*eta_dc_dc + Pwind*eta_ac_dc-Pload/eta_inverter)*eta_cha_*delat_T
discharging
cbat = cbat-1 + 


DE(t) = (P_load-P_tot)*delta T
P_tot = (P_pv + P_wg + Cbat_t-1 - Cbat_min)*eta_inv
https://www.waaree.com/documents/Super_400_Mono_PERC.pdf
'''
import numpy as np
import pandas as pd
import pyswarm


def LCOE(x):
    solar_ = pd.read_csv("It.csv")
    wind_ = pd.read_csv("Wind_gen.csv")
    solar = np.absolute(solar_)
    panels = x[0]
    panel_cost = 1000
    wt = x[1]
    wt_cost = 100000
    panel_life = 20
    wt_life = 20
    battery_rating = x[2]
    battery_per_cost = x[3]
    CRF = 0.1*(1.1)**20/(1.1**20-1)
    p_gen = panels*2.0160315*0.19*solar*365*24+365*24*wt*wind_
    demand_ = pd.read_csv("Demand_data_IIT Bombay.xslx")
    battery_rating = np.max(np.max(p_gen - demand_)*60*60 ,np.max(demand_ - p_gen))//0.8
    LCOE = (panels*panel_cost + wt*wt_cost + battery_rating*battery_per_cost)*CRF + 0.2*(panels*panel_cost + wt*wt_cost + battery_rating*battery_per_cost)
    LCOE = LCOE/(np.sum(panels*2.0160315*0.19*solar*365*24+365*24*wt*wind_))
    return ((panels*panel_cost + wt*wt_cost + battery_rating*battery_per_cost)*CRF + 0.2*(panels*panel_cost + wt*wt_cost + battery_rating*battery_per_cost))/(np.sum(panels*2.0160315*0.19*solar*365*24+365*24*wt*wind_))

def lpsp(x):
    panels = x[0]
    wt = x[1]
    solar_ = pd.read_csv("It.csv")
    wind_ = pd.read_csv("Wind_gen.csv")
    demand_ = pd.read_csv("iitb_data.csv")
    solar = np.absolute(solar_)
    '''
    LPSP = (SIGMA LPS(t))/(SIGMA LOAD(t))
    LPS(t) = Eload(t) - Egen(t)
    
    p_gen = panels*2.0160315*0.19*solar*365*24+365*24*wt*wind_
    p_demand = demand_ 
    '''