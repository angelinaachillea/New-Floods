from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
import datetime

stations= build_station_list()
update_water_levels(stations)
dt=2
p=4

highest_current_stations= stations_highest_rel_level(stations, 5)

dates = []
levels = []

for station in highest_current_stations:
    results = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    dates.append(results[0])
    levels.append(results[1])
    plot_water_level_with_fit(station,dates,levels,p)
