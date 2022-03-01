
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
    results= fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=2))
    poly, d0 = polyfit(results[0],results[1],4)
    assert type(poly) == type(np.poly1d([1]))
    assert d0 == matplotlib.dates.date2num(results[0])[0]

