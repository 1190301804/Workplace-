import os
from cmath import atan, tan, sin, cos, acos
from math import radians
from geopy.distance import distance

import folium
from IPython.display import display

import webbrowser


class Map:
    def __init__(self, center, zoom_start):
        self.center = center
        self.zoom_start = zoom_start
        self.my_map = folium.Map(location=self.center, zoom_start=self.zoom_start)

    def showMap(self):
        # Create the map
        # Display the map
        self.my_map.save("map.html")
        webbrowser.open("map.html")

    def Mark(self,mark_place,mark_place_name):
        folium.Marker(location=mark_place,popup=mark_place_name , icon=folium.Icon(color='red')).add_to(self.my_map)

    # 输入 A的维度，A的经度 ，B的纬度，B的经度
    # 返回单位：km
    def getDistance(self,LocationA,LocationB):
        km = distance(LocationA, LocationB)
        folium.PolyLine([LocationA, LocationB],popup=str(km),color="red", weight=5, opacity=60).add_to(self.my_map)
        return km



def draw_map(marked_place):
    import folium
    # PuertoRico_map =folium.Map(location=[18.24914, -66.62804],zoom_start=10)
    # display world map
    location = [18.24914, -66.62804]
    PuertoRico_map = Map(center=location,zoom_start= 10)

    for x in marked_place:
        PuertoRico_map.Mark(marked_place.get(x),x)

    return  PuertoRico_map



# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # marked_place = {
    #     "Caribbean Medical Center": [18.33, -65.65], "Hospital HIMA": [18.22, -66.03],
    #     "Hospital Pavia Santurce": [18.44, -66.07], "Puerto Rico Children's Hospital": [18.40, -66.16],
    #     "Hospital Pavia Arecibo": [18.47, -66.73]}

    marked_place = {
        "A": [18.33, -65.65], "B": [18.22, -66.03],
        "C": [18.44, -66.07], "D": [18.40, -66.16],
        "E": [18.47, -66.73]}

    map= draw_map(marked_place)

    X = map.getDistance(marked_place.get("A"),marked_place.get("B"))
    print(X)
    X = map.getDistance(marked_place.get("B"),marked_place.get("C"))
    print(X)
    X = map.getDistance(marked_place.get("C"),marked_place.get("D"))
    print(X)
    X = map.getDistance(marked_place.get("D"),marked_place.get("E"))
    print(X)
    X = map.getDistance(marked_place.get("E"),marked_place.get("A"))
    print(X)

    map.showMap()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
