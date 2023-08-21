import folium

import pandas as pd


# Make a data frame with dots to show on the map
data = pd.DataFrame({
   'lat':[53.55416445, 53.57416000, 53.600833, 53.3575300, 53.249950, 52.520008, 52.966667, 47.374444],
   'lon':[9.9583295, 9.95679000, 9.476389, 10.2128200, 10.408870, 13.404954, 11.15, 8.541111],
   'name':['Hamburg St. Pauli', 'Hamburg Eimsbüttel', 'Stade', 'Winsen', 'Lüneburg', 'Berlin', 'Lüchow', 'Zürich'],
}, dtype=str)


#   'scenario': ['A: Hamburg St. Pauli -> Lüchow', 'B: Hamburg Eimsbüttel -> Berlin', 'C: Lüneburg -> Zürich', 'D: Winsen -> Stade'],


# Make map
base_map = folium.Map(location=[53.551086, 9.993682], control_scale=True, zoom_start=10)

# 'A: Hamburg St. Pauli -> Lüchow'
points_a = [
    (53.55416445, 9.9583295),
    (52.966667, 11.15)
]
# 'B: Hamburg Eimsbüttel -> Berlin'
points_b = [
    (53.57416000, 9.95679000),
    (52.520008, 13.404954)
]
# 'C: Lüneburg -> Zürich'
points_c = [
    (53.249950, 10.408870),
    (47.374444, 8.541111)
]
# 'D: Winsen -> Stade'
points_d = [
    (53.3575300, 10.2128200),
    (53.600833, 9.476389)
]

# Create feature groups for each line
line_a = folium.FeatureGroup(name='A: Hamburg St. Pauli -> Lüchow').add_to(base_map)
line_b = folium.FeatureGroup(name='B: Hamburg Eimsbüttel -> Berlin').add_to(base_map)
line_c = folium.FeatureGroup(name='C: Lüneburg -> Zürich').add_to(base_map)
line_d = folium.FeatureGroup(name='D: Winsen -> Stade').add_to(base_map)

# add lines
line_a.add_child(folium.PolyLine(locations=points_a, weight=3, color='yellow'))
line_b.add_child(folium.PolyLine(locations=points_b, weight=3, color='yellow'))
line_c.add_child(folium.PolyLine(locations=points_c, weight=3, color='yellow'))
line_d.add_child(folium.PolyLine(locations=points_d, weight=3, color='yellow'))

# Define the icons
icons = {
    'car': folium.Icon(color='white', icon='car', icon_color='red', prefix='fa'),
    'plane': folium.Icon(color='white', icon='plane', icon_color='green', prefix='fa'),
    'train': folium.Icon(color='white', icon='train', icon_color='blue', prefix='fa')
}

# add marker one by one on the map
for i in range(0,len(data)):
   folium.Marker(
      location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
      popup=data.iloc[i]['name'],
   ).add_to(base_map)


folium.LayerControl().add_to(base_map)

# Save the map as an HTML file
base_map.save("transporation.html")

print("Map generation completed.")
