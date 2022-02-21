from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list
def run():
    stations = build_station_list()

    print("{} stations. First 10 - {}".format(len(rivers_with_station(stations)), sorted(rivers_with_station(stations))[:10]))

    dictionary = stations_by_river(stations)
    river_aire = dictionary['River Aire']
    print(sorted(river_aire))

    river_cam = dictionary['River Cam']
    print(sorted(river_cam))

    river_Thames = dictionary['River Thames']
    print(sorted(river_Thames))

if __name__=="__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()