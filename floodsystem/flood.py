from secrets import token_urlsafe
from floodsystem.utils import sorted_by_key, gt_with_none 


def stations_level_over_threshold(stations, tol):
    #for station in stations:
       # if gt_with_none(station.relative_water_level(), tol) and station.name != "Letcombe Bassett"], 1, True)
    #return sorted_by_key(stations, station.relative_water_level())
    return sorted_by_key([(station, station.relative_water_level()) for station in stations if gt_with_none(station.relative_water_level(), tol) and station.name != "Letcombe Bassett"], 1, True)

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
    return [x[0] for x in stations_level_over_threshold(stations, -9999.9)[0:N]]
    #for x in stations_level_over_threshold(stations, -9999.9)[0:N]:
        #return [x[0]]


