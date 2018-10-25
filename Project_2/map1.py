import folium

map = folium.Map(location=[40.757,-111.894], zoom_start=12)

fg = folium.FeatureGroup(name="SaltyLake")
fg.add_child(folium.Marker(location=[40.773, -111.891], popup ='Salty Lake Temple', icon=folium.Icon(color='blue')))
map.add_child(fg)

map.save("SaltyLake.html")
