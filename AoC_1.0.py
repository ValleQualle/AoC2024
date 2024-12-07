dateipfad = 'AoC_1.0_InputListe'

# Datei öffnen und den Inhalt lesen
with open(dateipfad, 'r', encoding='utf-8') as datei:
    list = datei.read().strip()  # strip entfernt führende/trailing Leerzeichen und Zeilenumbrüche

listIn = []
listIn = list.split()

intList = [int(i) for i in listIn]

listA = []
listB = []

i = 0
while i < len(intList):
    if i % 2 != 0:
        listB.append(intList[i])
        i += 1
    else:
        listA.append(intList[i])
        i += 1

print(listA)
print(listB)

listA.sort()
listB.sort()



distance = 0
count = 0
if len(listA) > len(listB):
    for i in listB:
        distance += abs(i - listA[count])
        count += 1
else:
    for i in listA:
        distance += abs(i - listB[count])
        count += 1

print(distance)