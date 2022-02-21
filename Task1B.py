#use the function created in the geo section station_by_distance
#print a list of the first 10 values 
#print a list of the last 10 values
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
def run(): 
    stations = build_station_list()
    p=(52.2053,0.1218)
    distances = stations_by_distance(stations, p)
    print("10 closest stations")
    for x in range(10):
        print(distances[x][0].name,distances[x][0].town,distances[x][1])
    print("10 furthest away stations")
    for x in range(len(distances)-10, len(distances)):    
        print(distances[x][0].name,distances[x][0].town,distances[x][1])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()