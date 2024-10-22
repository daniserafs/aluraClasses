# odd number?
def odd_number(x):
    if(x % 2) == 0: 
        print(f'{x} is even')
    else: print(f'{x} is odd')

# don't forget to convert to int when getting the input
number = int(input('Enter a number: '))
is_odd = odd_number(number)
