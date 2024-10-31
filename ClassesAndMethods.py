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
        