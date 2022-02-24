import matplotlib
import numpy as np
import matplotlib.pyplot as plt
def polyfit(dates , levels, p):
    
    x=matplotlib.dates.date2num(dates)
    y=levels
    d0=-2
    
    p_coeff=np.polyfit(x-x[0],y,p)
    poly=np.poly1d(p_coeff)
    plt.plot(x,y,p)
    
    x1=np.linspace(x[0],x[-1],d0)
    plt.plot(x1,poly(x1))
    
    plt.show()
