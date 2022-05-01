lista = []
while True:
    beker = input('Szavak: ')
    if beker != '':
        lista.append(beker)
    else:
        break
    
print(lista)
maxhossz = max(lista, key=len)
minhossz = min(lista, key=len)
print('Leghosszabb szó: ',maxhossz)
print('Legrövidebb szó: ',minhossz)
