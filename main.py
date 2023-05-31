from solara import *
import leafmap
import os


# NOW I CREATE ZOOM VALUE AND CENTER CONRDINATE
zoom = reactive(2)
center = reactive((30,10))

class Map(leafmap.Map):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		# NOW I WILL CHANGE TILE THEME WITH OWN TILE
		self.add_tile_layer(
			url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
			name="Google Satellite",
			attribution="Google"
			)
		# AND NOW I will create MARKER FROM GEOJSON
		# AND NOW I WILL CREATE geojson FILE
		# NOW LOAD YOU FILE GEOJSON HERE
		url = "my.geojson"
		self.add_point_layer(url,popup=["name","country"],layer_name="US Cities")
		




@solara.component
def Page():
	with Column(margin=10):
		Text(f"zoom : {zoom.value}")
		Text(f"center : {center.value}")
		# NOW I CREATE MAPS
		Map.element(
			zoom=zoom.value,
			on_zoom=zoom.set,
			center=center.value,
			on_center=center.set,
			scroll_wheel_zoom=True,
			toolbar_ctrl=False,
			data_ctrl=False

			)
