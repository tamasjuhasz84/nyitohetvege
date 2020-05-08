#eredetiCim;   magyarCim;      bemutato;   forgalmazo;   bevel;     latogato
#     0            1               2            3          4           5
#  Allied;   Szövetségesek;   2016.12.01;      UIP;     44341076;    30804

naplopo = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def napszam(datum):
    ev    = int(datum[0:4])
    honap = int(datum[5:7])
    nap   = int(datum[8:])
    gyujto = 0
    for ho in range(1, honap):
        gyujto += naplopo[ho]
    gyujto += nap
    gyujto += (ev-2000) * 365
    return gyujto

class Mozi:
    def __init__(self, sor):
        sor = sor.strip().split(';')
        self.eredetiCim = sor[0]
        self.magyarCim  = sor[1]
        self.bemutato   = sor[2]
        self.forgalmazo = sor[3]
        self.bevel      = int(sor[4])
        self.latogato   = int(sor[5])
        
with open('nyitohetvege.txt', 'r', encoding='UTF-8') as f:
    fejlec = f.readline()
    lista = [Mozi(sor) for sor in f]
    
#3. feladat
print(f'3. feladat: {len(lista)} db')

#4. feladat
bevetel = sum([sor.bevel for sor in lista if sor.forgalmazo == 'UIP'])
print(f'4. feladat: UIP Duna Film forgalmazó 1. hetes bevételeinek összege: {bevetel} Ft')

#5. feladat
print(f'5. feladat: A legtöbb látogató az első héten:')
latogato, sor = max([(sor.latogato, sor) for sor in lista])
print(f'        Eredeti cím: {sor.eredetiCim}')
print(f'        Magyar cím: {sor.magyarCim}')
print(f'        Forgalmató: {sor.forgalmazo}')
print(f'        Bevétel az első héten: {sor.bevel}')
print(f'        Látogatók száma: {sor.latogato}')

#6. feladat
for sor in lista:
    eredeticim = sor.eredetiCim.split()
    magyarcim  = sor.magyarCim.split()
    
    eredetizaszlo = True
    for szo in eredeticim:
        if szo[0] not in ('W', 'w'):
            eredetizaszlo = False
#            print(eredeticim, szo, eredetizaszlo)
            break
        else:
            print(f'---', szo, eredetizaszlo)
    magyarzaszlo = True
    for szo in magyarcim:
        if szo[0] not in ('W', 'w'):
            magyarzaszlo = False
            break
        else:
            print(f'***', szo, magyarzaszlo)
    if eredetizaszlo and magyarzaszlo:
        print(f'Ilyen film volt!')
        break
    
#7. feladat
forgalmazok = [sor.forgalmazo for sor in lista]
forgalmazok_halmaz = set(forgalmazok)
f = open('stat.csv', 'w', encoding='UTF-8')
print(f'forgalmazo;filmekSzama', file=f)
for forgalmazo in forgalmazok_halmaz:
    darab = forgalmazok.count(forgalmazo)
    if darab > 1:
        print(f'{forgalmazo};{darab}', file=f)
f.close()

#8. feladat
bemutatok = [napszam(sor.bemutato) for sor in lista if sor.forgalmazo == 'InterCom']
dif = []
for i in range(len(bemutatok)-1):
    dif.append(bemutatok[i+1] - bemutatok[i])
print(f'8. feladat: A leghoszabb időszak két InterCom-os bemutató között: {max(dif)} nap')
    