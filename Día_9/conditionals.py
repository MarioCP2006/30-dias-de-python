age = int(input("insert your age "))
if age>=18:
    print('You are old enough to drive')
else:
    print(f"You need {18-age} more years to drive")

years=int(input("How old are you? "))    
if years>16:
    print(f"You are {years-16} years older than me")
    if (years-16) <=2:
        print(f"You only have{years-16} more than me")
elif years==16:
    print("We have the same age")
else:
    print(f"I am {16-years}years  older than you")

a=int(input("inserte un numero "))
b=int(input("inserte otro numero "))
if a>b:
    print(f"{a} es mayor que{b}")
elif b>a:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")

mark=int(input("Inserte la nota del estudiante "))
if mark>=80:
    print("La calificación del estudiante es A")
if mark>=70 and mark<80:
    print("La calificación del estudiante es B")
if mark>=60 and mark<70:
    print("La calificación del estudiante es C")
if mark>=50 and mark<60:
    print("La calificación del estudiante es D")
if mark<50:
    print("La calificación del estudiantes es F")

month=str(input("Introduce el mes del año: "))
month_capitalized= month.capitalize()
print(month_capitalized)
if month_capitalized=="Octubre" or month_capitalized=="Noviembre" or month_capitalized=="Septiembre":
    print("Estamos en otoño")
if month_capitalized=="Enero" or month_capitalized=="Diciembre" or month_capitalized=="Febrero":
    print("Estamos en invierno")
if month_capitalized=="Marzo" or month_capitalized=="Abril" or month_capitalized=="Mayo":
    print("Estamos en primavera")
if month_capitalized=="Agosto" or month_capitalized=="Junio" or month_capitalized=="Julio":
    print("Estamos en verano")

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit=input("Inserte una fruta ")
if new_fruit not in fruits:
    fruits.append(new_fruit)
    print(fruits)
else:
    print("Esa fruta ya está en la lista")