"""
Ce fichier génère une carte interactive avec Folium.
"""

# %%
import folium
from folium.plugins import MarkerCluster
import json

coordinates = json.load(open('coordinates.json'))

snippets = json.load(open('tome1.json', encoding='utf-8'))

# construction de la carte
# inspiré par https://medium.com/@saidakbarp/interactive-map-visualization-with-folium-in-python-2e95544d8d9b


def make_snippet(snippets, location):
    """Makes a colored html snippet."""
    output = "<br>".join(sentence.replace(
        location, f'<i style="background-color: yellow;">{location}</i>') for sentence in snippets)
    return output


map = folium.Map(location=[48.853, 2.348], zoom_start=5,
                 tiles='Stamen Watercolor', attr="Stamen attribution")
marker_cluster = MarkerCluster().add_to(map)  # create marker clusters
for location in coordinates:
    coords = coordinates[location]
    if location in snippets:
        popup = make_snippet(snippets[location], location)
        popup = folium.Popup(popup, parse_html=False, max_width=400)
    else:
        popup = f"Lieu : {location}<br>"
    tooltip = f"{location}"
    folium.Marker(coords,  # adding more details to the popup screen using HTML
                  popup=popup,
                  tooltip=tooltip).add_to(marker_cluster)

map

map.save('tome1.html')

print('Lieux manquants dans les coordonnées :', [
      key for key in snippets if key not in coordinates])


# %%
