vacio=()
hermanos=("David", "Godofredo", "Asabaneh", "Karim")
hermanas=("Marta", "Angustias",  "Fiona",  "Ambrosia")
siblings=(hermanos  + hermanas)
print(hermanos)
print(hermanas)
print(siblings)
print(len(siblings))
padres= "Carlos", "Cristina"
family_members= siblings + padres
print(family_members)
siblings1=family_members[0:8]
print(siblings1)
parents1=family_members[8:10]
print(parents1)
fruits=("manzana", "naranja", "mango", "platano")
vegetables=("zanahoria", "lechuga", "tomate", "cebolla")
animals=("gato", "perro", "caballo", "vaca")
food_stuff_tp=fruits + vegetables + animals
print(food_stuff_tp)
food_stuff_ls=list(food_stuff_tp)
print(food_stuff_ls)
print(food_stuff_ls[5:7])
print(food_stuff_ls[0:3] + food_stuff_ls[9:12])
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)