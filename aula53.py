people = {
    'name': 'Marcelo Gabriel',
    'last_name': 'Ferreira',
    'age': 22,
    'heigth': 1.83,
    'address': [
        {'rua': 'Rua01', 'number': 123},
        {'rua': 'Rua08', 'number': 895},
    ],
}
print(people)

people['new_key'] = 'new value'
print(people)

del people['last_name']
print(people)

if people.get('last_name') is None:
    print('This key does not exist.')
else:
    print(people['last_name'])
