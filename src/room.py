class Room:
    def __init__(self, _room_num, _capacity):
        self.room_num = _room_num
        # self.song = _song
        # self.guest = _guest
        self.capacity = _capacity
        self.till = 0
        self.list_of_songs = {}
        self.list_of_guests = []

    def check_guest_in(self, guest):
        self.list_of_guests.append(guest)

    def check_guest_out(self, guest):
        self.list_of_guests.remove(guest)

    def add_song(self, song):
        self.list_of_songs[song.name] = song 
    
    def remove_song(self, song):
        del self.list_of_songs[song.name]



  

    


