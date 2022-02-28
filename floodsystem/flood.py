from secrets import token_urlsafe
from floodsystem.utils import sorted_by_key, gt_with_none 


def stations_level_over_threshold(stations, tol):
    #for station in stations:
       # if gt_with_none(station.relative_water_level(), tol) and station.name != "Letcombe Bassett"], 1, True)
    #return sorted_by_key(stations, station.relative_water_level())
    stations_levels_list = []
    for station in stations:
        if gt_with_none(station.relative_water_level(), tol) and station.name != "Letcombe Bassett":
            stations_levels_list.append((station, station.relative_water_level()))
    return sorted_by_key(stations_levels_list, 1, True) #1 means sort by second item of tuple, True means reverse list

'''
def stations_highest_rel_level(stations, N):
    for station in stations:
        x= sorted_by_key(stations,station.latest_level,True)
        At_risk_stations=x[:N]
    return At_risk_stations
'''
def stations_highest_rel_level(stations, N):
    #for i in range(N):
        #return stations_level_over_threshold(stations,-9999.9)[i]
    stations_list = []
    for station in stations_level_over_threshold(stations, -9999)[0:N]:
        stations_list.append(station[0])
    return stations_list
    #for x in stations_level_over_threshold(stations, -9999.9)[0:N]:
        #return [x[0]]


