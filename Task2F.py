from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from datetime import datetime, timedelta

stations= build_station_list()
update_water_levels(stations)
dt=2
p=4

highest_current_stations= stations_highest_rel_level(stations, 5)

dates = []
levels = []

for stations in highest_current_stations:
    results = fetch_measure_levels(stations.measure_id, dt=datetime.timedelta(days=dt))
    dates.append(results[0])
    levels.append(results[1])
print(plot_water_level_with_fit(highest_current_stations,dates,levels,p))
