class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def center(self):
        center_x = self.x + self.width // 2
        center_y = self.y + self.height // 2
        return center_x, center_y

    def intersects(self, other):
        return not (self.x > other.x + other.width or
                    self.x + self.width < other.x or
                    self.y > other.y + other.height or
                    self.y + self.height < other.y)
