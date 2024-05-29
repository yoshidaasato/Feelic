#cording:utf_8
import csv

file_path = 'sample.csv'  # CSVファイルのパスを指定してください

searchword = input('入力')
i = 1
resalt = []
#csvの読み込みとレコード数の読み取り
with open(file_path, encoding='utf_8') as f:
    reader = csv.reader(f)
    lines = f.readlines()
#csvの読み込み
with open(file_path,encoding='utf_8') as f:
    reader = csv.reader(f)
    #各レコードを呼び出し
    for row in reader:
        #リストから検索(部分一致)
        index = ','.join(row)
        findcount = index.find(searchword)
        #find関数の返り値が0より大きいとき
        if findcount >= 0:
            findcount = -1
            resalt.append(row)
            continue
        #読み込んでいるレコードとレコード数が一致するとき
        elif len(lines) == i:
            print('存在しません')
            break
        #find関数の返り値がdefaultのとき(-1)
        else:
            i = i + 1
            continue
print('検索結果')
print(resalt)
