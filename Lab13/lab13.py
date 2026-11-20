#1
class fly:
    def method(fly):
        print("fly high")
class swim:
    def method(swim):
        print("Swim fast")
class duck(fly, swim):
    def method(duck):
        fly.method(duck)
        swim.method(duck)
d1 = duck()
d1.method()

#2
class music_player:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        return f"Music player initialized with playlist: {self.playlist_name}"
class GPS:
    def __init__(self, location):
        self.location = location
        return f"GPS initialized at location: {self.location}"
class smartcar(music_player, GPS):
    def __init__(self, playlist_name, location, car_model):
        music_player.__init__(self, playlist_name)
        GPS.__init__(self, location)
        self.car_model = car_model
    def display_info(self):
        return f"Smart Car Model: {self.car_model}, Playlist: {self.playlist_name}, Location: {self.location}"  
car1 = smartcar("Top Hits", "New York", "Tesla Model S")
print(car1.display_info())

#3
class dog:
    def method(speaks):
        print("WOOOF")
class cat:
    def method(speaks):
        print("MEOWWWW")
class Confused(dog, cat):
    def method(animal):
        dog.method(animal)
        cat.method(animal)
a1 = Confused()
a1.method()
 

