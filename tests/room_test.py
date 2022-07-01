import unittest
from src.guest import Guest
# from src.karaoke_bar import KaraokeBar
from src.room import Room
# from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(4, 12)
        self.room2 = Room(6, 8)
        self.room3 = Room(10, 16)
        self.guest1 = Guest("Bob", 10, "Enter Sandman")
        self.guest2 = Guest("Sandra", 40, "Hotel California")
        self.guest3 = Guest("Kevin", 20, "Don't Let Me Down")

    def test_check_room_has_number(self):
        self.assertEqual(4, self.room1.room_num)
        self.assertEqual(6, self.room2.room_num)
        self.assertEqual(10, self.room3.room_num)

    def test_check_capacity_of_room(self):
        self.assertEqual(12, self.room1.capacity)
        self.assertEqual(8, self.room2.capacity)
        self.assertEqual(16, self.room3.capacity)


    def test_check_guests(self):
        self.assertEqual(0, len(self.room1.list_of_guests))

    def test_check_guest_in(self):
        self.room1.check_guest_in(self.guest1)
        self.assertEqual(1, len(self.room1.list_of_guests))

    def test_check_guest_out(self):
        self.room1.check_guest_in(self.guest1)
        self.assertEqual(1, len(self.room1.list_of_guests))
        self.room1.check_guest_out(self.guest1)
        self.assertEqual(0, len(self.room1.list_of_guests))







