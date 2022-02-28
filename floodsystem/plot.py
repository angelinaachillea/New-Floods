import matplotlib
import matplotlib.pyplot as plt 
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit
import numpy as np

def plot_water_levels(station, dates, levels):
    stations = station 
    length = len(stations)
    for i in range(length):
        plt.plot(dates[i],levels[i])
        plt.subplot(int(length / 3) + 1, (int(length / 2) > 0) + int(length / 5) + 1, i + 1)
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45);
        plt.title(stations[i].name)
        plt.plot(dates[i], [stations[i].typical_range[0]] * len(dates[i]), 'g--')
        plt.plot(dates[i], [stations[i].typical_range[1]] * len(dates[i]), 'g--')
        plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p, show_typical_range = True):
    """Plot water levels for a station with polyfit.
    Also accepts lists as input, showing up to the first 6 stations."""
    poly, d0 = polyfit(dates, levels, p)
    dates_num = matplotlib.dates.date2num(dates)
    
    typical_min = station.typical_range[0]
    typical_max = station.typical_range[1]
    typical_min_list = np.full(len(dates), typical_min)
    typical_max_list = np.full(len(dates), typical_max)
    
    plt.plot(dates, levels, label = "Real data")
    plt.plot(dates, poly(dates_num - dates_num[d0 - 1]), label = "Least-squares polynomial fit")
    plt.plot(dates, typical_min_list, label = "Typical minimum level")
    plt.plot(dates, typical_max_list, label = "Typical maximum level")
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.legend()
    plt.tight_layout()  
    plt.show()