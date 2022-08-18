import folium

mapa = folium.Map(
    location=[-15.651695, -56.173604],
    tiles='Stamen Terrain',
    zoom_start=13
)
folium.Marker(
    [-15.651695, -56.173604],
    popup='<i>Casa</i>',
    tooltip='Click aqui',
    icon=folium.Icon(icon="cloud"),
).add_to(mapa)

folium.CircleMarker(
    location=[-15.651695, -56.173604],
    radius=50,
    popup="Laurelhurst Park",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(mapa)

mapa.save('mmeumapa.html')

print('Salvou o Mapa')
