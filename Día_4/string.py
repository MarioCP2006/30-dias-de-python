thirty_days_of_python="Thirty" + " " + "Days" + " " + "Of" + " " + "Python"
print(thirty_days_of_python)

coding_for_all="Coding" + " " + "For" + " " + "All"
print(coding_for_all)

company=coding_for_all
print(company)
print(len(company))

print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company.strip("Coding "))
print("Coding" in company)
print(company.replace('Coding', 'Python'))
Python_For_All=company.replace('Coding', 'Python')
print(Python_For_All.replace('All' , 'Everyone'))
print(company.split( ))
marcas="Facebook" + ",  " + "Google" + ", "+"Microsoft" + ", " + "Apple" + ", " + "IBM" + ", " + "Oracle" + ", " + "Amazon"
print(marcas.split(", "))

print(company[0])
print(company[13])
print(company[10])
Pfa=Python_For_All[0] + Python_For_All[7] + Python_For_All [11]
print(Pfa)
Cfa=company[0] + company[7] + company[11]
print(Cfa)
print(company.index("C"))
print(Python_For_All.index("F"))
print(company.rindex("l"))
frase= 'You cannot end a sentence with because because because is a conjunction'
print(frase.find('because'))
print(frase.rfind('because'))
print(frase.replace(' because because because ', ' '))
print(frase.index('because '))