from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
from floodsystem.station import inconsistent_typical_range_stations
#def run():
stations=build_station_list()
inconsistent_data= inconsistent_typical_range_stations(stations)
print(sorted_by_key(inconsistent_data,0))

#if __name__ == "__main__":
   # print("*** Task 1F: CUED Part IA Flood Warning System ***")
   # run()