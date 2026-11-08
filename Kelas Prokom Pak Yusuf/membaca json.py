import json

FILE_NAME = 'Kelas Prokom Pak Yusuf/history_city_list.json'
with open(FILE_NAME, 'r', encoding='Latin1') as jsonfile:
    data = json.load(jsonfile)
    
print(type(data))
print(data[0])
print(len(data))

print(json.dumps(data[764], indent=4))

print(data[764]['city']['coord'][lon])