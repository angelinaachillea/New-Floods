import matplotlib.pyplot as plt 
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from datetime import datetime, timedelta

def plot_water_levels(station, dates, levels):
    if len(station) >= 5:
        station= station [0:5]
        length = 5 
    else:
        station = station 
        length = len(station)
    for i in range(length):
        plt.plot(dates[i],levels[i])
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45);
        plt.title(station[i].name)
        plt.tight_layout()
plt.show()
