class Car:
    cars = []
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
        Car.cars.append(self)

    def __str__(self):
        return f'{self.model} | {self.color} | {self.year}'
    
    def listing_cars():
        for car in Car.cars:
            print(f'Model: {car.model} - Color: {car.color} - Year: {car.year}')


honda_cr_v = Car('Honda CR-V', 'Silver', '2023')
corolla = Car('Corolla', 'Red', '2019')
sentra = Car('Nissan Sentra', 'Red', '2020')
camry = Car('Toyota Camry', 'Silver', '2021')

Car.listing_cars()

class Restaurant:
    restaurants = []
    def __init__(self, name, category, openHours, numberOfEmployees):
        
        self.name = name
        self.category = category
        self.active = False
        self.openHours = openHours
        self.numberOfEmployees = numberOfEmployees
        Restaurant.restaurants.append(self)
        

    def __str__(self):
        return f'{self.name} | {self.category} | {self.openHours} | {self.numberOfEmployees}'
    
    def listing_restaurants():
        for restaurant in Restaurant.restaurants:
            print(f'Restaurant: {restaurant.name} - Category: {restaurant.category} - Active: {restaurant.active} - Open Hours: {restaurant.openHours} - Number of employees: {restaurant.numberOfEmployees}')

restaurant_square = Restaurant('Praça', 'Gourmet', '19h00 - 00h00', 10)
restaurant_dandadan = Restaurant('Pizza Express', 'Italiana', '18h30 - 01h00', 5)

#restaurantes = [restaurante_praca, restaurante_dandadan]

Restaurant.listing_restaurants()

class Client:
    clients = []
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
        self.active = False
        Client.clients.append(self)

    def listing_clients():
        for client in Client.clients:
            print(f'{client.name} | {client.age} | {client.id}')

client1 = Client('danidinha', '12300', '28')

Client.listing_clients()

class Book():
    def __init__(self, title='', author='', pages=0):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author} - {self.pages} pages'
    
    @property
    def author_title(self):
        return f'{self.title} by {self.author}'

    def increase_pages(self, amount):
        self.pages += amount


class Person():
    people=[]
    def __init__(self, name = '', age= 0, profession = ''):
        self.name = name
        self.age = age
        self.profession = profession
        Person.people.append(self)

    def __str__(self):
        return f'My name is {self.name}. I am {self.age} years old. I am a {self.profession}'
    
    @property
    def greetings(self):
        if self.profession:
            return f'Hello, I am {self.name}! I am a {self.profession} and I like computers a lot'
        else:
            return f'Hello, I am {self.name}'

    def happy_birthday(self):
        self.age += 1

    def listing_people():
        for person in Person.people:
            print(f'{person.name} | {person.age} | {person.profession}')

person1 = Person('danidinha', 28, 'Computer Scientist')
person2 = Person('Kim Namjoon',30, 'Singer' )
person3 = Person('Jimin', 29, 'Singer' )
print(person1)
person1.happy_birthday()
print(person1)
Person.listing_people()
person2.happy_birthday()
person3.happy_birthday()
Person.listing_people()