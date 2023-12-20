floor_width = float(input("Enter the width of the floor: "))
floor_length = float(input("Enter the length of the floor: "))
tile_width = float(input("Enter the width of a tile: "))
tile_length = float(input("Enter the length of a tile: "))
tile_cost = float(input("Enter the cost of a tile: "))
num_tiles_width = floor_width / tile_width
num_tiles_length = floor_length / tile_length
total_tiles = num_tiles_width * num_tiles_length
total_cost = total_tiles * tile_cost
print("The total cost to cover the floor plan is:", total_cost)
