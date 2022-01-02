import os
from cmath import atan, tan, sin, cos, acos
from math import radians

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
    # 返回单位：m
    def getDistance(self,latA, lonA, latB, lonB):

        ra = 6378140  # radius of equator: meter
        rb = 6356755  # radius of polar: meter
        flatten = (ra - rb) / ra  # Partial rate of the earth
        # change angle to radians
        radLatA = radians(latA)
        radLonA = radians(lonA)
        radLatB = radians(latB)
        radLonB = radians(lonB)

        pA = atan(rb / ra * tan(radLatA))
        pB = atan(rb / ra * tan(radLatB))
        x = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(radLonA - radLonB))
        c1 = (sin(x) - x) * (sin(pA) + sin(pB)) ** 2 / cos(x / 2) ** 2
        c2 = (sin(x) + x) * (sin(pA) - sin(pB)) ** 2 / sin(x / 2) ** 2
        dr = flatten / 8 * (c1 - c2)
        distance = ra * (x + dr)
        return distance

def draw_map():
    import folium
    # PuertoRico_map =folium.Map(location=[18.24914, -66.62804],zoom_start=10)
    # display world map
    location = [18.24914, -66.62804]
    PuertoRico_map = Map(center=location,zoom_start= 10)

    marked_place = {
        "Caribbean Medical Center":[18.33 ,-65.65],"Hospital HIMA":[18.22 ,-66.03],
        "Hospital Pavia Santurce":[18.44 ,-66.07],"Puerto Rico Children's Hospital":[18.40 ,-66.16],
        "Hospital Pavia Arecibo":[18.47 ,-66.73]}


    for x in marked_place:
        PuertoRico_map.Mark(marked_place.get(x),x)
    PuertoRico_map.showMap()

    return  PuertoRico_map



def getDistance(map,A,B):

    print(map.getDistance(A[0],A[1],B[0],B[1]))
    return map.getDistance(A[0],A[1],B[0],B[1])



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    map= draw_map()

    A= [18.33 ,-65.65]
    B =[18.22 ,-66.03]
    getDistance(map,A,B)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
