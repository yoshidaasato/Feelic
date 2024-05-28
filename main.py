#cording:utf_8
import csv
search = input('入力')
i = 1
resalt = []
file_path = 'sample.csv'  # CSVファイルのパスを指定してください
with open(file_path, encoding='utf_8') as f:
    reader = csv.reader(f)
    lines = f.readlines()

with open(file_path,encoding='utf_8') as f:
    reader = csv.reader(f)   
    for row in reader:
        index = ','.join(row)
        count = index.find(search)
        if count >= 0:
            count = -1
            resalt.append(row)
            continue
        elif len(lines) == i:
            print('存在しません')
            break
        else:
            i = i + 1
            continue
print('検索結果')
print(resalt)