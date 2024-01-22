from init_data import data
from tile import *
from color import Color




color_data = data['board']['colors']
for k, v in color_data.items():
    print(k, v)

print(Color)
color_objects = { k: Color(k, *v) for k, v in color_data.items()}

go_tile = GoTile("Go")

# Access the 'tiles' key in the dictionary and create instances of the corresponding classes
tiles_data = data['board']['tiles']

head_tile = go_tile
for tile_data in tiles_data:
    tile_type = tile_data['type']
    if tile_type == 'StreetTile':
        tile_obj = StreetTile( tile_data.get('title'), color_objects[tile_data.get('color')], int(tile_data.get('price')), int(tile_data.get('constructionCost')), list(map(int, tile_data.get('rents'))))
    elif tile_type == 'TrainStationTile':
        tile_obj = TrainStationTile( tile_data.get('title'), int(tile_data.get('price')))
    elif tile_type == 'UtilityTile':
        tile_obj = UtilityTile( tile_data.get('title'), int(tile_data.get('price')))
    else:
        print(tile_type)
        raise TypeError("Unkown tile type")

    # print(str(tile_obj))
    head_tile = head_tile.insertHead(tile_obj)



go_tile.dispAll()

str_colors = [print(str(c)) for c in color_objects.values()]

print(color_objects)
# print(str_colors)



Monopoly(go_tile, color_objects.values()).run()


