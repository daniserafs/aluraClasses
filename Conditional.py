# odd number?
def odd_number(x):
    if(x % 2) == 0: 
        print(f'{x} is even')
    else: print(f'{x} is odd')

# don't forget to convert to int when getting the input
number = int(input('Enter a number: '))
is_odd = odd_number(number)

# age classification
def age_class(x):
    if(x < 12):
        print('Criança: 0 a 12 anos.')
    elif(x < 18):
        print('Adolescente 13 a 18 anos.')
    else:
        print('Adulto: acima de 18 anos.')
age = int(input('Enter your age: '))
age_class(age)

# user check

USER_NAME = 'Danidinha'
PASSWORD = '123'

def user_check(user, password):
    if(user != USER_NAME or password != PASSWORD):
        print('User or password incorrect!')
    else:
        print('You may enter!')

user = input('Enter your username: ')
password = input('Enter your password: ')
user_check(user, password)