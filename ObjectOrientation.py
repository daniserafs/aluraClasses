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

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False


restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

restaurante_dandadan = Restaurante()

restaurantes = [restaurante_praca, restaurante_dandadan]

print(restaurante_praca.ativo)

if(restaurante_praca.ativo == False):
    print(f'O Restaurante {restaurante_praca.nome} está inativo')
else:
    print(f'O Restaurante {restaurante_praca.nome} está ativo')