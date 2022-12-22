age=15
height=float=1.73
ecuación1=complex= 3 + 3j
base=int(input('Base'))
print(base)
altura=int(input('Altura'))
print(altura)
print('el perímetro es',(0,5*base*altura))

ladoa=int(input('Lado a'))
ladob=int(input('Lado b'))
ladoc=int(input('Lado c'))
perimeter=(ladoa + ladob + ladoc)
print(perimeter)

length= int(input('Largo de su rectangulo'))
print(length)
wide= int(input('Ancho de su rectangulo'))
areaofrectangle=length * wide
print(areaofrectangle)
perimetrofrectangle=2*(length+wide)
print(perimetrofrectangle)

pi=3,14
radioofcircle=int(input('Radio de su circulo'))
print(radioofcircle)
areaofcircle=pi*radioofcircle**2
print(areaofcircle)
circumferenceofcircle=2*pi *radioofcircle
print(circumferenceofcircle)

function1="y=2x-2"
print("La formula es:"+function1)
m_de_function1=str(2)
print("La pendiente es igual a:"+m_de_function1)
ejex=str(2^0 -2)
print("el intercepto de x es igual a:")
print(0,ejex)
ejey=str((0+2)/2)
print("el intercepto de y es igual a:")
print(ejey,0)

punto1=(2,2)
punto2=(6,10)
x1=2 in punto1
x2=6 in punto2
y1=2 in punto1
y2=10 in punto2
m=(y2-y1)/(x2-x1)
print(f"La m es:{m}")
euclideandist=(x2-x1)**2+(y2-y1)**2
print(f"La distancia euclidiana es de:{euclideandist})

print(m_de_function1==m)

test_numbers=(2,3,-3,5,6)
for n in test_numbers:
    print(n**2+6*n+9)

print(len("python"))
print(len("dragon"))
print(len("python")!=len("dragon"))

print("on"in "python")
print("on"in "dragon")

print("jargon"in"I hope this course is not full of jargon")

print("on" not in "dragon")
print("on"not in "python")