class Music:
    songs = []

    def __init__(self, name, artist, length):
        self.name = name
        self.artist = artist
        self.length = length
        Music.songs.append(self)

    def __str__(self):
        return f'Song: {self.name} - Artist: {self.artist} - {self.length} seconds'
    
    def listing_songs():
        for song in Music.songs:
            print(f'Song: {song.name} - Artist: {song.artist} - {song.length} seconds')

music_the_astronaut = Music('The astronaut', 'Jin', 443)
music_come_back_to_me = Music('Come back to me', 'RM', 629)
music_apt = Music('APT.', 'Rosé and Bruno Mars', 254)


Music.listing_songs()
print(music_the_astronaut)