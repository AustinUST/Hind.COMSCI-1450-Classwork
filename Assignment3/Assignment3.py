
#1
class Playlist:
    def __init__(self, title):
        self.title = title
        self.songs = []

    def add_song(self, song_name):
        self.songs.append(song_name)

    def remove_song(self, song_name):
        if song_name in self.songs:
            self.songs.remove(song_name)
        else:
            print("Song not found.")

    def get_summary(self):
        return f"{self.title}: {len(self.songs)} song(s)"


road_trip = Playlist("Road Trip")
road_trip.add_song("Song One")
road_trip.add_song("Song Two")
road_trip.add_song("Song Three")
road_trip.remove_song("Song Two")

print(road_trip.get_summary())

#2
class GiftCard:
    def __init__(self, owner):
        self.__owner = owner
        self.__balance = 0.0

    def get_balance(self):
        return self.__balance

    def reload(self, amount):
        if amount > 0:
            self.__balance += amount

    def spend(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient gift card balance!")


card = GiftCard("Jordan")
card.reload(50)
card.spend(75)
card.spend(20)
print(card.get_balance())

try:
    print(card.__balance)
except AttributeError:
    print("Private __balance cannot be accessed directly")

#3

class MediaItem:
    def __init__(self, title, minutes):
        self.title = title
        self.minutes = minutes

    def play(self):
        return f"Playing {self.title} ({self.minutes} mins)"


class PodcastEpisode(MediaItem):
    def __init__(self, title, minutes, host):
        super().__init__(title, minutes)
        self.host = host

    def play(self):
        return f"{super().play()} - Hosted by {self.host}"


episode = PodcastEpisode("Tech Talk", 45, "Alex")
print(episode.play())

#4
class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage.")


class ArmoredKnight(Character):
    def __init__(self, name, health, armor):
        super().__init__(name, health)
        self.armor = armor

    def take_damage(self, amount):
        print(f"Armor blocks {self.armor} damage!")
        reduced_damage = max(0, amount - self.armor)
        super().take_damage(reduced_damage)


arthur = ArmoredKnight("Arthur", 100, 15)
arthur.take_damage(40)
print(arthur.health)

