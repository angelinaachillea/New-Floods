from secrets import token_urlsafe
from .utils import sorted_by_key, gt_with_none


def stations_level_over_threshold(stations, tol):
    for station in stations:
        tol= tol
        if station.relative_water_level() > tol:
    return sorted_by_key(stations, station.relative_water_level())
    
def stations_highest_rel_level(stations, N):
    for station in stations:
        x= sorted_by_key(stations,station.latest_level,True)
        At_risk_stations=x[:N]
    return At_risk_stations
