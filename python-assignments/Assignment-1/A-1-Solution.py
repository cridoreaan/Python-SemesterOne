
### YOUR CODE FOR calculateArea() FUNCTION GOES HERE ###
def calculateArea(width, length):
    return width * length
#### End OF MARKER



____________________________________________________________________________________________________________________________________________

### YOUR CODE FOR checkTilesFit() FUNCTION GOES HERE ###
def checkTilesFit(plot_width, plot_length, tile_width, tile_length):
    if plot_width % tile_width == 0 and plot_length % tile_length == 0 or tile_width % plot_width == 0 and tile_length % plot_length == 0 or plot_length % tile_length == 0 and tile_width % plot_width == 0:
        return True
    else:
        return False

#### End OF MARKER

### YOUR CODE FOR calculateTiles() FUNCTION GOES HERE ###
def calculateTiles(plot_width, plot_length, tile_width, tile_length):
    if type(plot_width) == str or type(plot_length) == str or type(tile_width) == str or type(tile_length) == str:
        return "Invalid Input"
    if plot_width == 0 or plot_length == 0 or tile_width == 0 or tile_length == 0:
        return None
    P_A = plot_width * plot_length
    T_A = tile_width * tile_length
    n_o_tiles = P_A//T_A
    if checkTilesFit(plot_width, plot_length, tile_width, tile_length) == True:
        return n_o_tiles
    else:
        return "Not Possible"

#### End OF MARKER
