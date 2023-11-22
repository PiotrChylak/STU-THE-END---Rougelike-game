import mapElement as mE


class Map:
    def __init__(self, x, y, layout):
        self.x = x
        self.y = y
        self.mapLayout = layout

    def check(self, x1, y1):
        print(self.mapLayout[x1][y1].description)
