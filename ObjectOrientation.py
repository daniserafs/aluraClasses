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

print(f'Song: {music_the_astronaut.name} - Artist: {music_the_astronaut.artist} - {music_the_astronaut.length} seconds')

class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False


restaurante_praca = Restaurante('Praça', 'Gourmet')
#restaurante_praca.nome = 'Praça'
#restaurante_praca.categoria = 'Italiana'

restaurante_dandadan = Restaurante('Pizza Express', 'Italiana')

restaurantes = [restaurante_praca, restaurante_dandadan]

print(restaurante_praca.ativo)

if(restaurante_praca.ativo == False):
    print(f'O Restaurante {restaurante_praca.nome} está inativo')
else:
    print(f'O Restaurante {restaurante_praca.nome} está ativo')

categoria = Restaurante.categoria
restaurante_praca.nome = "Bistrô"

restaurante_pizza = Restaurante()

restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
print(f'A categoria do restaurante {restaurante_pizza.nome} é {restaurante_pizza.categoria}')
restaurante_pizza.ativo = True
print(f'O Restaurante {restaurante_praca.nome} tem a categoria: {restaurante_praca.categoria}')