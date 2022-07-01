import unittest
from src.guest import Guest
from src.karaoke_bar import KaraokeBar
# from src.room import Room
# from src.song import Song


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Bob", 10, "Enter Sandman")

    
    def test_check_guest_has_name(self):
        self.assertEqual("Bob", self.guest.name)

    def test_check_guest_has_money(self):
        self.assertEqual(10, self.guest.money)
    
    def test_check_guest_favourite_song(self):
        self.assertEqual("Enter Sandman", self.guest.fav_song)
        
