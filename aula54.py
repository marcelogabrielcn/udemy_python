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

print(len(people))  # Return the number of keys
print(people)
print(list(people))  # Return only the keys
print(list(people.keys()))  # Same thing
print(list(people.values()))  # Return only the values

for value in people.values():
    print(value)

print(list(people.items()))  # Return keys and values
for keys, values in people.items():
    print(keys, values)

people.setdefault('new_value', 987)  # if it has the "new_value" key, it uses whatever value it has, but if it doesn't have it, it will use the defined default value (987)
print(people['new_value'])

