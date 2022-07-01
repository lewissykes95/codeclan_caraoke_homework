import unittest
from src.guest import Guest
from src.karaoke_bar import KaraokeBar
# from src.room import Room
# from src.song import Song


class TestKaraokeBar(unittest.TestCase):
    def setUp(self):
        self.karaoke_bar = KaraokeBar("Po Karaoke", 10, 500.00)

    def test_check_karaoke_bar_has_name(self):
        self.assertEqual("Po Karaoke", self.karaoke_bar.name)

    def test_check_number_of_rooms(self):
        self.assertEqual(10, self.karaoke_bar.rooms)

    def test_check_karaoke_bar_has_money_in_till(self):
        self.assertEqual(500.00, self.karaoke_bar.till)

    



    
        


    