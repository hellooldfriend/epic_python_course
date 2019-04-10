names = ['John', 'Paul', 'George', 'Ringo']
lst = []

for name in names:
    if name == 'John' or name == 'Paul':
        lst.append(name)

print(lst)


##########################

names = ['John', 'Paul', 'George', 'Ringo']
lst2 = [name for name in names if name == 'John' or name == 'Paul']
print(lst2)


###########################

lst3 = list(filter((lambda name: name == 'John' or name == 'Paul'), names))

print(lst3)