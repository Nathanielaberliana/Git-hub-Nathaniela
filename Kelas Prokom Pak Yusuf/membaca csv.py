import csv

FILE_NAME = 'Kelas Prokom Pak Yusuf/nilaiKuliah.csv'
listNilai = []
kolom = []
with open(FILE_NAME) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    bariske = 0
    for row in readCSV:
        if bariske == 0:
            kolom = row
            bariske += 1
            continue
        listNilai.append(row)
        
print(kolom)
print(listNilai)        