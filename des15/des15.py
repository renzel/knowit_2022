
max_liter = 120
max_verdi = 1700
turer = 0
liter = 0
verdi = 0
import csv
with open('des15/data.csv') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    next(data)
    data = list(data)

while not len(data) == 0:
    found = False
    indexes_to_drop = []
    print(len(data))
    i_sekken = []
    for index, row in enumerate(data):
        if verdi + int(row[0]) <= max_verdi:
            if liter + int(row[1]) == max_liter:
                turer += 1
                indexes_to_drop.append(index)
                verdi = 0
                liter = 0
                found = True
                break
            elif liter + int(row[1]) < max_liter:
                verdi += int(row[0])
                liter += int(row[1])
                indexes_to_drop.append(index)

    if not found:
        turer += 1
        verdi = 0
        liter = 0

    if indexes_to_drop:
        i_sekken.append(indexes_to_drop)
        for index in sorted(indexes_to_drop, reverse=True):
            del data[index]
    

print(turer)