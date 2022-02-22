from secrets import token_urlsafe
from .utils import sorted_by_key, gt_with_none


def stations_level_over_threshold(stations, tol):
    for station in stations:
        tol= tol
        if station.relative_water_level() > tol
    return sorted_by_key(stations, station.relative_water_level())
    
def stations_highest_rel_level(stations, N):
    for i in stations_level_over_threshold(stations, tol):
        return [i[0] 