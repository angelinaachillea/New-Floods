#print the second function from geo stations_within_radius, giving a value for r as 10
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
def run():    
    stations = build_station_list()
    centre=(52.2053,0.1218)
    radial_distances = stations_within_radius(stations,centre,10)
    print("stations in radius of 10km from Cambridge city centre")
    x=(sorted_by_key(radial_distances, 0))
    print(x)

if __name__== "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()