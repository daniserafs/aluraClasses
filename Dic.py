 
def first_dictionary():
    
    name = input('Digite o nome da pessoa: ')
    age = int(input('Digite a idade da pessoa: '))
    city = input('Digite a cidade da pessoa: ')
    dados_da_pessoa = {'name': name, 'age' : age, 'city' : city}

    people = dados_da_pessoa

    print(people)
    return people

def update_dictionary(people):

    # person = input('Informe a pessoa para atualizar a idade')
    new_age = int(input('Digite a nova idade: '))
    people['age'] = new_age
    #print(people)
    return people

def add_profession(people):
    profession = input('Digite a profissão dela: ')
    people['profession'] = profession
    
def delete_item(people):
    del people['city']

def power_to():
    power = {'1 x 1' : 1 * 1, '2 x 2' : 2 * 2, "3 x 3": 3 * 3, "4 x 4" : 4 * 4, '5 x 5' : 5 * 5}
    print(power)

power_to()
people = first_dictionary()
new_people= update_dictionary(people)
add_profession(new_people)
print(people)
delete_item(people)
print(people)


