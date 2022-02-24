import matplotlib.pyplot as plt 
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from datetime import datetime, timedelta
from analysis import polyfit

def plot_water_levels(stations, dates, levels):
    stations = stations 
    length = len(stations)
    for i in range(length):
        plt.plot(dates[i],levels[i])
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45);
        plt.title(stations[i].name)
        plt.tight_layout()plt.plot(dates[i], [stations[i].typical_range[0]] * len(dates[i]), 'g--')
        plt.plot(dates[i], [stations[i].typical_range[1]] * len(dates[i]), 'g--')
        plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()

def plot_water_level_with_fit(station,dates,levels,p):
#copy and paste the polyfit and plot water levels code? or somehow integrate the function into this one
