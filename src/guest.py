class Guest:
    def __init__(self, _name, _money, _fav_song):
        self.name = _name
        self.money = _money
        self.fav_song = _fav_song
    
    def check_afford_ticket(self):
        ticket_price = 5 
        if self.money >= ticket_price:
            return "You may enter!"
        else:
            return "Unlucky!"

    


        
