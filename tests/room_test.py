import unittest
# from src.guest import Guest
# from src.karaoke_bar import KaraokeBar
from src.room import Room
# from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(4, 12)
        self.room1 = Room(6, 8)
        # self.guest = Guest("Bob", 10, "Enter Sandman")

    def test_check_room_has_number(self):
        self.assertEqual(4, self.room.room_num)
        self.assertEqual(6, self.room1.room_num)

    def test_check_capacity_of_room(self):
        self.assertEqual(12, self.room.capacity)
        self.assertEqual(8, self.room1.capacity)







