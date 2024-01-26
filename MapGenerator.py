import random
import mapElement as mE
from Room import Room


class MapGenerator:
    def __init__(self, width, height, num_rooms):
        self.width = width
        self.height = height
        self.num_rooms = num_rooms
        self.map_layout = [[mE.Wall() for _ in range(width)] for _ in range(height)]
        self.rooms = []

    def generate_map(self):
        self.create_rooms()
        self.connect_rooms()
        self.remove_dead_ends()
        return self.map_layout

    def create_rooms(self):
        for _ in range(self.num_rooms):
            room_width = random.randint(5, 12)
            room_height = random.randint(5, 12)

            while True:
                x = random.randint(1, self.width - room_width - 1)
                y = random.randint(1, self.height - room_height - 1)

                new_room = self.create_room(x, y, room_width, room_height)

                if not any(new_room.intersects(existing_room) for existing_room in self.rooms):
                    self.rooms.append(new_room)
                    self.place_room(new_room)
                    break
                else:
                    room_width = max(4, room_width - 1)
                    room_height = max(4, room_height - 1)

    def create_room(self, x, y, width, height):
        return Room(x, y, width, height)

    def place_room(self, room):
        for i in range(room.x, room.x + room.width):
            for j in range(room.y, room.y + room.height):
                self.map_layout[j][i] = mE.Floor()

    def connect_rooms(self):
        for i in range(len(self.rooms) - 1):
            room1 = self.rooms[i]
            room2 = self.rooms[i + 1]
            self.connect_two_rooms(room1, room2)

    def connect_two_rooms(self, room1, room2):
        x1, y1 = room1.center()
        x2, y2 = room2.center()

        while x1 != x2 or y1 != y2:
            if x1 != x2:
                self.map_layout[y1][x1] = mE.Floor()
                x1 += (x2 - x1) // abs(x2 - x1)
            if y1 != y2:
                self.map_layout[y1][x1] = mE.Floor()
                y1 += (y2 - y1) // abs(y2 - y1)

    def remove_dead_ends(self):
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                if (
                    self.map_layout[i][j] == mE.Floor() and
                    sum(1 for neighbor in [
                        self.map_layout[i - 1][j],
                        self.map_layout[i + 1][j],
                        self.map_layout[i][j - 1],
                        self.map_layout[i][j + 1]
                    ] if neighbor == mE.Wall()) >= 3
                ):
                    self.map_layout[i][j] = mE.Wall()
