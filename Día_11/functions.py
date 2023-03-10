def masdos(num1,num2):
    num3=num1+num2
    return num3

def area_of_circle(radio):
    area=radio**2*3.14159
    return area

def  add_all_nums(*datos):
    total=0
    datos_tipos=type(datos)
    if not datos:
        print("Necesito datos para mi cálculo")
    else:
        for num in datos:
            if type(num)==str:
                total=("No puedo realizar una suma de strings")
                # break
            else:
                total=total+num
    return total

def convert_celsius_to_fahrenheit(grados):
    fahrenheit=(grados*9/5)+32
    return fahrenheit

def check_season(mes):
    str(mes)
    mes_mayuscula=mes.capitalize()
    if mes_mayuscula=="Diciembre" or mes_mayuscula=="Enero" or mes_mayuscula=="Febrero":
        return "Es invierno"
    elif mes_mayuscula=="Marzo" or mes_mayuscula=="Abril" or mes_mayuscula=="Mayo":
        return "Es primavera"
    elif mes_mayuscula=="Junio" or mes_mayuscula=="Julio" or mes_mayuscula=="Agosto":
        return "Es verano"
    elif mes_mayuscula=="Septiembre" or mes_mayuscula=="Octubre" or mes_mayuscula=="Noviembre":
        return "Es otoño"

def print_list(*lista):
    for element in lista:
        print(element)

def reverse_lista(array):
    list(array)
    array.reverse()
    return array


def capitalize_list_items(items):
    archivo=[]
    list(items)
    for p in items:
        str(p)
        p=p.capitalize()
        archivo.append(p)
    return archivo

def  add_item(lista,objeto):
    list(lista)
    lista.append(objeto)
    return lista
        
def remove_item(lista,objeto):
    list(lista)
    lista.remove(objeto)
    return lista

def sum_of_numbers(numberr):
    joselu=0
    for n in range(numberr+1):
        joselu=joselu+n
    return joselu

def  is_prime(numerito):
    numeros_primos=[2,3,5,7,13]
    for n in numeros_primos:
        if numerito%n==0 and numerito not in numeros_primos:
            return "Su número es primo"
        else:
            return "Su número no es primo"

def check_items(lista):     
    s_e_t=set(lista)   
    if lista==s_e_t:
        return "No se repiten items en la lista" 
    else:
        return "Se repiten items en la lista"

items=["Uno" , "Dos", "Tres" , "Cuatro" , "Dos"]
print(check_items(items))
print(is_prime(169))
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      
print(capitalize_list_items(["manzana" , "melón" , "naranja", "limón"]))
print(reverse_lista([1, 2, 3, 4, 5]))
print(reverse_lista(["A", "B", "C"]))
print(print_list("Zanahoria" , "Arroz" , "Pollo" , "Berza"))
print(masdos(9,8))
print(area_of_circle(4))
print(f"{convert_celsius_to_fahrenheit(30)}º")
print(check_season("enero"))
print(add_all_nums(3 ,5 ,6 , 7 ,"Mario"))
