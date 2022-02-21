# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""


from ssl import SSL_ERROR_WANT_X509_LOOKUP
from floodsystem.station import MonitoringStation
from .utils import sorted_by_key  # noqa
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers.
    return c * r



def stations_by_distance(stations,p):
    distance=[]
    for station in stations:
        distance.append((station, haversine(p[0],p[1],station.coord[0],station.coord[1])))
    x=sorted_by_key(distance,1)
    
    return x



def rivers_with_station(stations):
    rivers = set() 
    for station in stations:
        rivers.add(station.river)
    return rivers 

def stations_by_river(stations):
    dictionary = {}
    for river in rivers_with_station(stations):
        listOfStations = []
        for station in stations:
            if station.river == river:
                listOfStations.append(station.name)    
        dictionary[river] = listOfStations      
    return dictionary 

def rivers_by_station_number(stations, N):
    listOfTuples = []
    for river in stations_by_river(stations).keys():
        numberTuple = (river,len(stations_by_river(stations)[river]))
        listOfTuples.append(numberTuple)
    listOfTuples.sort(key=lambda y: y[1], reverse = True)
    nth_value = listOfTuples[N - 1][1]    
    rivers_output = []
    for river in listOfTuples:
        if river[1] < nth_value:
            break
        rivers_output.append(river)
    return rivers_output

def stations_within_radius(stations,centre,r):
    distances=[]
    for station in stations:
        lengths= haversine(station.coord[0],station.coord[1],centre[0],centre[1])
        if lengths < r :
            distances.append(station.name)
    
    return distances


