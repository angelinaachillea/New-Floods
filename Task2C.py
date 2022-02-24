#test to seee if working
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


stations=build_station_list
update_water_levels(stations)
N=10
for station_tuple in stations_highest_rel_level(stations,N):
    print(station_tuple[0].name + " "+str(station_tuple[1]))
    

