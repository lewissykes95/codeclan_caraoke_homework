class Room:
    def __init__(self, _room_num, _capacity):
        self.room_num = _room_num
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

    
    def check_capacity(self, room):
        if room.capacity == 12:
            return True
        else: 
            return False

    def check_limit(self, guest, room):
        self.list_of_guests.append(guest)
        if len(self.list_of_guests) <= room.capacity:
            return True
        else: 
            return False 


    






    

   



    





   



        
    
        



        

    
    
    



  

    


