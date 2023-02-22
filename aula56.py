p1 = {
    'name': 'Marcelo Gabriel',
    'age': 22,
}

# print(p1['last_name'])
print(p1.get('last_name'))  #Return None as default, without giving an error

print(p1)

p1.update({  # If the key exist, it will update its value, if does not exist, will be created
    'name': 'New name',
    'heigth': 1.82,
    'last_name': 'Last_name_example',
})
# Can be updated using lists or tuples. 

print(p1)

last_value = p1.popitem()

print(p1)
print(last_value)

name = p1.pop('name')
print(p1)
print(name)
