import folium
my_map4 = folium.Map(location = [24.224850, 83.026140],
                                        zoom_start=12)
folium.Marker([28.834330, 77.581400],
            popup='Delhi').add_to(my_map4)
folium.Marker([24.224850, 83.026140],
            popup='Python.Hub').add_to(my_map4)
folium.PolyLine(locations=[(28.834330, 77.581400), (24.224850, 83.026140) ],
                line_opacity = 1).add_to(my_map4)

my_map4.save("my_map4.html")
my_map4

