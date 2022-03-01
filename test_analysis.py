
import matplotlib
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import numpy as np
import datetime

def test_polyfit():
    stations= build_station_list()
    update_water_levels(stations)
    station= stations[0] # pick a station randomly
    results= fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=2)) #take data from 2 days back
    poly, d0 = polyfit(results[0],results[1],4) #results[0]=dates, results[1]= levels, 4 is the degree for the least squares fit
    assert type(poly) == type(np.poly1d([1])) #the function from the analysis section has its own type
    assert d0 == matplotlib.dates.date2num(results[0])[0]

