class Music:
    name = ''
    artist = ''
    length = int


music_the_astronaut = Music()
music_the_astronaut.name = 'The Astronaut'
music_the_astronaut.artist = 'Jin'
music_the_astronaut.length = 443

music_come_back_to_me = Music()
music_come_back_to_me.name = 'Come back to me'
music_come_back_to_me.artist = 'RM'
music_come_back_to_me.length = 629

music_apt = Music()
music_apt.name = 'APT.'
music_apt.artist = 'ROSÉ and Bruno Mars'
music_apt.length = 254

print(f'Song: {music_the_astronaut.name} - Artist: {music_the_astronaut.artist} - {music_the_astronaut.length} segundos')