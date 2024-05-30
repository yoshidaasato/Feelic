#cording:utf_8
import csv

file_path = 'libdata.csv'  # CSVファイルのパスを指定してください

searchword = input('入力')
i = 1
resalt = []
endcount = 0
resaltcount = 0
#csvの読み込みとレコード数の読み取り
while endcount == 0:
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
                resaltcount = 1
                continue
            #読み込んでいるレコードとレコード数が一致するとき
            elif len(lines) == i:
                endcount = 1
                break
            #find関数の返り値がdefaultのとき(-1)
            elif searchword == '終了':
                endcount = 1
                break
            else:
                i = i + 1
                continue
    break
#結果があるときだけ表示
if resaltcount == 1:
    output = str(resalt)
    output = output.replace('{','')
    output = output.replace('}','')
    output = output.replace("'","")
    output = output.replace('[','')
    output = output.replace(']','\n')
    output = output.replace(',',' ')
    print('検索結果')
    print(output)
else:
    print('存在しません')
