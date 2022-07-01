import unittest
from src.guest import Guest
from src.karaoke_bar import KaraokeBar
# from src.room import Room
# from src.song import Song


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Bob", 10, "Enter Sandman")
        self.guest2 = Guest("Sandra", 40, "Hotel California")
        self.guest3 = Guest("Kevin", 20, "Don't Let Me Down")
 
    def test_check_guest_has_name(self):
        self.assertEqual("Bob", self.guest1.name)
        self.assertEqual("Sandra", self.guest2.name)
        self.assertEqual("Kevin", self.guest3.name)

    def test_check_guest_has_money(self):
        self.assertEqual(10, self.guest1.money)
        self.assertEqual(40, self.guest2.money)
        self.assertEqual(20, self.guest3.money)
    
    def test_check_guest_favourite_song(self):
        self.assertEqual("Enter Sandman", self.guest1.fav_song)
        self.assertEqual("Hotel California", self.guest2.fav_song)
        self.assertEqual("Don't Let Me Down", self.guest3.fav_song)
        
