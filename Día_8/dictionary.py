dog = dict()
dog['name']= 'Tobby'
dog['age']= '5 years'
dog['breed']='Pitbull'
dog['color']='black'
dog['legs']='4'
print(dog)

student_dictionary={
    "First_name":'Mario',
    "Last_name":'Calero',
    "Gender":'Male',
    "Age": '16',
    "Marital_status": 'single',
    "Skills":['run', 'think', 'sleep'],
    "Country": "España",
    "City": 'Jerez de la Frontera',
    "Address":{
        'street':'Calle Polar',
        'zipcode' :'11405'}
}
print(student_dictionary)
print(len(student_dictionary))
print(student_dictionary['Skills'])
print(type(student_dictionary['Skills']))
student_dictionary['Skills'].append('study')
student_dictionary['Skills'].append('eat')
print(student_dictionary)
keys=student_dictionary.keys()
print(keys)
values=student_dictionary.values()
print(values)
print(student_dictionary.items())
del student_dictionary['Marital_status']
print('student dic without marital status' ,student_dictionary)
del student_dictionary