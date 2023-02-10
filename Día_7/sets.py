it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add("Twitter")
print(it_companies)
new_it_companies=("xiaomi", "hp", "acer")
it_companies.update(new_it_companies)
print(it_companies)
it_companies.remove("IBM")
print(it_companies)
print("La diferencia es que si el elemento no existe , remove da error y discard no")
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
C=(A.union(B))
D=(B.union(A))
print(C)
print(D)
print(A.symmetric_difference(B))
del A
del B
del C
del D
ages_set=set(age)
print(len(age))
print(len(ages_set))
print(len(ages_set) > len(age))
print('''la diferencia entre list, string , tuples y set es que una string es un conjunto de caracteres que se declaran entre doble comilla y son invariables,
las listas son un conjunto de lo que sea , pueden abarcar string , integers, etc además son mutables es decir una vez declaradas no se pueden modificar,
las tuples son exactamente igual a las listas pero con la única diferencia de que una vez declarados no se pueden variar y los sets no tienen orden.''')
profe="I am a teacher and I love to inspire and teach people."
Words_profe=set(profe.split())
print(Words_profe)
print(len(Words_profe))