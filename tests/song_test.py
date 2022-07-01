import unittest
# from src.guest import Guest
# from src.karaoke_bar import KaraokeBar
# from src.room import Room
from src.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Enter Sandman", "Metallica", 3.5)
        self.song2 = Song("Hotel California", "The Eagles", 4.00)
        self.song3 = Song("Don't Let Me Down", "The Beatles", 3.20)
        self.song4 = Song("Dance Wiv Me", "Dizzee Rascal", 2.60)
        self.song5 = Song("All Night Long", "Lionel Ritchie", 4.18)
        self.song6 = Song("Karma Chameleon", "Culture Club", 4.10)

 
    def test_song_has_name(self):
        self.assertEqual("Enter Sandman", self.song1.name)
        self.assertEqual("Hotel California", self.song2.name)
        self.assertEqual("Don't Let Me Down", self.song3.name)
        self.assertEqual("Dance Wiv Me", self.song4.name)
        self.assertEqual("All Night Long", self.song5.name)
        self.assertEqual("Karma Chameleon", self.song6.name)
    

    def test_check_song_has_artist(self):
        self.assertEqual("Metallica", self.song1.artist)
        self.assertEqual("The Eagles", self.song2.artist)
        self.assertEqual("The Beatles", self.song3.artist)
        self.assertEqual("Dizzee Rascal", self.song4.artist)
        self.assertEqual("Lionel Ritchie", self.song5.artist)
        self.assertEqual("Culture Club", self.song6.artist)

   
        



