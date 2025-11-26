"""
A csoport
Szimuláljuk egy 20 oldalú D&D kocka 100 db dobását! A dobásokat egy listában tároljuk! Majd oldjuk meg a következő feladatokat!
Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e 6-os a dobások között?
2. Hányadikra sikerült először 18-nál nagyobbat dobni?
3. Hány darab 1-est dobtak?
4. Melyik volt a legnagyobb dobás a 10-nél kisebbek közül, és hányadik dobás volt?
5. Mennyi a 4-es dobások szorzata?
"""

import random as r

#szimmulálás:

dobasok = [[r.randint(1, 20) for i in range(100)]]
print("Dobások:", dobasok)
print()

#1.Volt-e 6-os a dobások között:
print("1. Volt-e 6-os a dobások között?")

try:
    hatos_dobas = dobasok[0].index(6)
    print("Igen, volt 6-os a dobások között.")
except ValueError as e:
    print(f"{e} \nNem, nem volt 6-os a dobások között.")
print()

#2.Hányadikra sikerült először 18-nál nagyobbat dobni:
print("2. Hányadikra sikerült először 18-nál nagyobbat dobni?")

tznyoc_nagyobb = [num for num in dobasok[0] if num > 18]
min_tznyoc = min(tznyoc_nagyobb)
print(f"Nagyobb számok, mint 18: {tznyoc_nagyobb}")

try:
    elso_tznyoc = dobasok[0].index(19) + 1 #+1 mert az indexelés 1-től kezdődik
    print(f"Az első 18-nál nagyobb dobás a(z) a {elso_tznyoc}. dobás volt, ami a(z) {min_tznyoc} volt.")
except ValueError as e:
    print(f"{e} \nNem volt ilyen dobás.")
print()

#3.Hány darab 1-est dobtak:
print("3. Hány darab 1-est dobtak?")

try:
    egyesek = [num for num in dobasok[0] if num == 1]
    print(f"Egyesek száma: {len(egyesek)}")
except ValueError as e:
    print(f"{e} \nNem voltak egyes dobások.")
print()

#4.Melyik volt a legnagyobb dobás a 10-nél kisebbek közül, és hányadik dobás volt:
print("4. Melyik volt a legnagyobb dobás a 10-nél kisebbek közül, és hányadik dobás volt?")

legagy_bef_ten = [num for num in dobasok[0] if num < 10]
print(f"Dobások amik kisebbek, mint 10: {legagy_bef_ten}")

try:
    min_kisten = max(legagy_bef_ten)
    max_ten = dobasok[0].index(min_kisten) + 1 #+1 mert az indexelés 1-től kezdődik
    print(f"A legnagyobb dobás ami kisebb, mint tíz az a(z) {min_kisten}, ami a {max_ten}. dobás volt.")
except ValueError as e:
    print(f"{e} \nNem volt 10-mél kisebb dobás.")
print()

#5.Mennyi a 4-es dobások szorzata:
print("5. Mennyi a 4-es dobások szorzata?")

negyesek = [num for num in dobasok[0] if num == 4]
print(f"Négyes dobások: {len(negyesek)}db {negyesek}")

try:
    negy_dbszam = len(negyesek)
    negy_szorzat = 4 * negy_dbszam
    print(f"A 4-es dobások szorzata: {negy_szorzat}")
except ValueError as e:
    print(f"{e} \nNincs négyes dobás.")
print()

#Vége