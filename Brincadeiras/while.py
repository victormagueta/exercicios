name = 'Otorrinolaringologista'
vowels = 'ooioaiooia'

for i in vowels:
    if i in name:
        name = name.replace(i, '')

print(name)
