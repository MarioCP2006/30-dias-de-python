#Day 2: 30 Days of python programming

from ast import keyword
from distutils.command import build
from itertools import product
from tkinter.messagebox import YES

first_name ='Mario'
last_name ='Calero'
full_name ='Mario Calero'
country= 'España' 
city= 'Jerez'
age= 15
year= 2022
is_married= False
is_true= YES
is_light_on= YES
print(first_name,last_name,full_name)

print(type('Mario'))
print(type('Calero'))
print(type(15))
print(type('España'))
print(type('Jerez'))
print(type('Mario Calero'))
print(type(2022))
print(type('false'))
print(type(YES))
len(first_name)
len(last_name)
check_len_first_and_last_name = first_name==last_name
print(check_len_first_and_last_name)

num_one = 5
num_two =4
cuenta1 = ((num_one + num_two))
print('Suma numeros', cuenta1)
cuenta2= (num_one - num_two)
print('Resta numeros', cuenta2)
cuenta3=(num_one * num_two)
print('Multiplicacion numeros', cuenta3)
cuenta4=(num_one / num_two)
print('Division numeros',cuenta4)
cuenta5=(num_two % num_one)
print('Modulus numeros', cuenta5)
cuenta6=(num_one ** num_two)
print('Elevacion de numeros', cuenta6)
cuenta7=(num_one // num_two)
print('Floor division de numeros', cuenta7)

radio=30
area_of_circle=(radio*3.14159)
print(area_of_circle)
circumference_of_circle=(2*3,14159*radio)
print(circumference_of_circle)
radio2=int(input('Add radio of circle'))
print(radio2)
area_of_circle2= 3.14159 * radio2**2
print('Area del circulo:',area_of_circle2)