import matplotlib
import numpy as np
import matplotlib.pyplot as plt
def polyfit(dates , levels, p):
    
    time_shift=1
    date_num=matplotlib.dates.date2num(dates)
    y=levels
    d0=2
    
    p_coeff=np.polyfit(date_num-date_num[time_shift-1],y,p)
    poly=np.poly1d(p_coeff)
    
    return(poly, time_shift)
