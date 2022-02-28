import matplotlib
import numpy as np
import matplotlib.pyplot as plt
def polyfit(dates , levels, p):
    
    time_shift=1
    date_num=matplotlib.dates.date2num(dates)
    y=levels
    d0=2
    shifted_dates = date_num-date_num[0]
    
    p_coeff=np.polyfit(shifted_dates,y,p)
    poly=np.poly1d(p_coeff)
    
    return(poly, time_shift)
