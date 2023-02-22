import copy

d1 = {
    'k1': 1,
    'k2': 2,
    'k3': 3,
    'l1': [0, 1, 2]
}

d2 = d1.copy()

print(d1)
print(d2)

d2['k3'] = 999

print(d1)
print(d2)

d2['l1'][2] = 888  # This will change the both dicts, beacuse "copy" make a shallow copy

print(d1)
print(d2)

d3 = copy.deepcopy(d1)  # Will change only d3, but deepcopy uses more memory and processing
d3['l1'][1] = 777

print(d1)
print(d2)
print(d3)
