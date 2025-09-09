names = []

for i in range(5):
    name = input(f'Enter name {i+1}: ')
    names.append(name.capitalize())

names.sort()
print('Sorted Names:', names)