import matplotlib
import matplotlib.pyplot as plt 
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit

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
    stations = station
    length = len(stations)
    for i in range(length):
        plt.plot(dates[i], levels[i])
        x = matplotlib.dates.date2num(dates[i])
        poly, shift = polyfit(dates[i], levels[i], 4)
        if not poly == None:
            plt.plot(x, poly(x - shift))
        if show_typical_range:
            plt.plot(x, [stations[i].typical_range[0]] * len(x), 'g--')
            plt.plot(x, [stations[i].typical_range[1]] * len(x), 'g--')
        plt.xlabel("Dates")
        plt.ylabel("Water Level (m)")
        plt.xticks(rotation=45);
        plt.title(stations[i].name)

        # Display plot
        plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()
