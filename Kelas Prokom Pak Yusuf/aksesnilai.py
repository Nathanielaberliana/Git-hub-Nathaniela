import pandas as pd

FILE_NAME = 'Kelas Prokom Pak Yusuf/nilaiKuliah.csv'
dfNilai = pd.read_csv(FILE_NAME, delimiter=',', encoding='Latin1')
print(type(dfNilai))
print(dfNilai)

dfNilai.to_csv('Kelas Prokom Pak Yusuf/nilaiKuliah_output.csv', index=False)