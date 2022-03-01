
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold

def test_stations_level_over_threshold():
    
    stations = build_station_list()
    update_water_levels(stations)
    stations_above_threshold = stations_level_over_threshold(stations, 0.9)
    for i in range(len(stations_above_threshold) - 1):
        assert stations_above_threshold[i][1] >= stations_above_threshold[i + 1][1] #make sure stations are sorted by flow rate
        assert stations_above_threshold[i][1] >= 0.9 #make sure stations flow rate are all above 0.9 (threshold), you can vary values for different climates etc


def test_stations_highest_rel_level():

    stations = build_station_list()
    update_water_levels(stations)

    highest_flowers = stations_highest_rel_level(stations, 10)
    assert len(highest_flowers) == 10

    #test values are sorted in decreasing order
    for i in range(len(highest_flowers) - 1):
        assert highest_flowers[i].relative_water_level() > highest_flowers[i + 1].relative_water_level()