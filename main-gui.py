#cording:utf_8
import csv
import tkinter as tk
# CSVファイルを開く

file_path = 'sample.csv'  # CSVファイルのパスを指定してください
#csvの読み込みとレコード数の読み取り
with open(file_path, encoding='utf_8') as f:
    reader = csv.reader(f)
    lines = f.readlines()

i = 1
listresalt = []
endcount = 0

#関数resaltを定義
while endcount == 0:
    def error():
        errorwindow = tk.Tk()
        errorwindow.title('error')
        errorwindow.geometry(f"{200}x{200}")
        errorlab = tk.Label(errorwindow,text='存在しません')
        errorlab.pack()
        retrybtn = tk.Button(errorwindow,text='戻る',command=errorwindow.destroy)
        retrybtn.pack()
        errorwindow.mainloop()

    def end():
         global endcount
         endcount = endcount+1
         searchwindow.destroy()
    def resalt():
        #変数wordentから値を取得
        global wordent
        searchword = wordent.get()
        searchwindow.destroy()
        #csvの読み込み
        with open(file_path,encoding='utf_8') as file:
            reader = csv.reader(file)
            #各レコードの呼び出し
            for row in reader:
                #リストから検索(部分一致)
                index = ','.join(row)
                findcount = index.find(searchword)
                global i
                #find関数の返り値が0より大きいとき
                if findcount >= 0:
                    global resaltcount
                    findcount = -1
                    listresalt.append(row)
                    resaltcount = 1
                    continue
                #読み込んでいるレコードとレコード数が一致するとき
                if i == len(lines):
                    error()
                    break

                #find関数の返り値がdefaultのとき(-1)
                else:
                    i = i + 1
                    continue
        #結果を表示するウィンドウを生成
        if resaltcount == 1:
            resaltcount = 0
            resaltwindow = tk.Tk()
            resaltwindow.title('結果')
            resaltlab = tk.Label(resaltwindow,text=listresalt)
            resaltlab.pack()
            resaltwindow.geometry(f"{200}x{200}")
            resaltwindow.mainloop()

    #スタートのウィンドウ生成
    i = 1
    listresalt = []
    endcount = 0
    resaltcount = 0

    searchwindow = tk.Tk()
    searchwindow.title('検索')
    searchwindow.geometry(f"{200}x{200}")
    wordlab = tk.Label(searchwindow,text='検索ワード入力')
    wordlab.pack()

    wordent = tk.Entry(searchwindow,width=50)
    wordent.pack()
    searchbtn = tk.Button(searchwindow,text='検索',command=resalt)
    searchbtn.pack()
    endbtn = tk.Button(searchwindow,text='終了',command=end)
    endbtn.pack()

    searchwindow.mainloop()
