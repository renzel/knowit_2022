import pandas as pd
# data = pd.read_csv("/home/tostby/random/knowit_2022/des15/data.csv")

max_liter = 120
max_verdi = 1700
turer = 0
liter = 0
verdi = 0
import csv
with open('/home/tostby/random/knowit_2022/des15/test.csv') as csv_file:
    data = list(csv.reader(csv_file, delimiter=','))

while not len(data) == 0:
    found = False
    # print(data)
    indexes_to_drop = []
    print(data)
    #print(verdi)
    print(turer)
    for index, row in enumerate(data):
        if verdi + int(row[0]) < 1700:
            if liter + int(row[1]) == 120:
                turer += 1
                indexes_to_drop.append(index)
                verdi = 0
                liter = 0
                found = True
                break
            elif liter + int(row[1]) < 120:
                verdi += int(row[0])
                liter += int(row[1])
                last_index = index
                print(liter + int(row[1]))
                indexes_to_drop.append(index)
            #else:
                #find_correct_package(data)
        else:
            turer += 1
            indexes_to_drop.append(index)
            #print(last_index)
            verdi = int(row[0])
            liter = int(row[1])
            found = True
            break
            
    if not found:
        turer += 1
        #indexes_to_drop.append(index)
        verdi = 0
        liter = 0
    if len(data) == 1:
        turer += 1
        data = []
    if indexes_to_drop:
        for index in sorted(indexes_to_drop, reverse=True):
            del data[index]
    

print(turer)