def masdos(num1,num2):
    num3=num1+num2
    return num3
print(masdos(9,8))

def area_of_circle(radio):
    area=radio**2*3.14159
    return area
print(area_of_circle(4))

def  add_all_nums(*datos):
    total=0
    if not datos:
        print("Necesito datos para mi cálculo")
    else:
        for num in datos:
            total=total+num
    return total
print(add_all_nums(3 ,5 ,6 , 7 ,))