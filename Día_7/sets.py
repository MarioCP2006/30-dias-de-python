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
