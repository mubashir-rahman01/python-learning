# class can have it's own method which are shared in all instances
class Point:
    def __init__(self, a, b): # it will be invoke by default
        self.a = a
        self.b = b
        
    def __str__(self): # customizes the human-readable string representation of the object
        return f"{self.a} and {self.b}"
    
    def __add__(self, other):
        return f"The sum: {
        Point(
            self.a + other.a,
            self.b + other.b
        )}"
        
    # similar to this there are other magic methods __sub()__, __mul()__, __eq()__, __ne()__ __lt()__
          
    def display(self):
        print(f" The points are: {self.a} and {self.b}")
    
    @classmethod    
    def zero(cls):
        return (0,0)
    
point = Point(3,4)
another = Point(5,6);

print(point + another);

#point.display();

#print(Point.zero())

# the class method will be shared by every instance
# print("instance values: ", point.zero())


# create a class song to implement add, remove and print all songs
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
        
    def add_song(self, song):
        self.songs.append(song)
        print(f"Song {song} added")
        
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Song {song} removed")
            
    def show_songs(self):
        print(f"Playlist '{self.name}':")
        for song in self.songs:
            print(f"- {song}")     
    
    
my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()