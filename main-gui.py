#cording:utf_8
import csv
import tkinter as tk

file_path = 'libdata.csv'  # CSVファイルのパスを指定
width = 800 #横解像度の選択
height = 800 #縦解像度の選択

#csvの読み込みとレコード数の読み取り
with open(file_path, encoding='utf_8') as f:
    reader = csv.reader(f)
    lines = f.readlines()
endcount = 0

#関数resaltを定義
while endcount == 0:
    #検索関係の処理を行う関数の定義
    def startsearch():
        #startsearch下で検索結果がヒットしなかったときに動作する関数
        def error():
            errorwindow = tk.Tk()
            errorwindow.title('error')
            errorwindow.geometry(f"{300}x{300}")
            errorlab = tk.Label(errorwindow,text='存在しません')
            errorlab.pack()
            retrybtn = tk.Button(errorwindow,text='戻る',command=errorwindow.destroy)
            retrybtn.pack()
            errorwindow.mainloop()
        #startsearch下で結果を出力するときに動作する関数
        def resalt():
            #変数wordentから値を取得
            global wordent
            searchword = wordent.get()
            searchwindow.destroy()
            if searchword == '':
                error()
            else:
                #csvの読み込み
                with open(file_path,encoding='utf_8') as file:
                    reader = csv.reader(file)
                    #各レコードの呼び出し
                    for row in reader:
                        #リストから検索(部分一致)
                        index = ' '.join(row)
                        index = index.lower()
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
                #無駄な文字列を削除
                output = str(listresalt)
                output = output.replace('{','')
                output = output.replace('}','')
                output = output.replace("'","")
                output = output.replace('[','')
                output = output.replace(']','\n')
                output = output.replace(',',' ')
                #ウィンドウ生成
                resaltwindow = tk.Tk()
                resaltwindow.title('結果')
                resaltlab = tk.Label(resaltwindow,text=output)
                resaltlab.pack()
                resaltwindow.geometry(f"{width}x{height}")
                resaltwindow.mainloop()
        #メインウィンドウの削除
        mainwindow.destroy()
        #検索ウィンドウの生成
        searchwindow = tk.Tk()
        searchwindow.title('検索')
        searchwindow.geometry(f"{300}x{300}")
        wordlab = tk.Label(searchwindow,text='検索ワード入力(英数は半角小文字)')
        wordlab.pack()
        global wordent
        wordent = tk.Entry(searchwindow,width=50)
        wordent.pack()
        searchbtn = tk.Button(searchwindow,text='検索',command=resalt)
        searchbtn.pack()
        endbtn = tk.Button(searchwindow,text='戻る',command=searchwindow.destroy)
        endbtn.pack()
        searchwindow.mainloop()
    #追加関係の処理を行う関数を定義
    def startadd():
        #startadd下で追加の処理を行う時に動作する関数
        def addpro():
            #変数呼び出しとaddwindowからの値の取得
            global addtitleent
            title = addtitleent.get()
            global addhiraganaent
            hiragana = addhiraganaent.get()
            global addgenreent
            genre = addgenreent.get()
            global addoptionent
            option = addoptionent.get()
            addwindow.destroy()
            #csvファイルをappendで呼び出し
            with open(file_path,'a',encoding='utf-8',newline='') as afile:
                #csv書き込みのデータ準備
                number = len(lines)
                writer = csv.writer(afile)
                data = [number,title,hiragana,genre,option]
                #csv書き込み
                writer.writerow(data)
            #処理の正常終了を伝えるウィンドウの生成
            compwindow = tk.Tk()
            compwindow.geometry(f"{300}x{300}")
            compwindow.title('出力')
            successlab = tk.Label(compwindow,text='正常に処理を受け付けました')
            successlab.pack()
            endbtn = tk.Button(compwindow,text='戻る',command=compwindow.destroy)
            endbtn.pack

        #addwindowの生成
        addwindow = tk.Tk()
        addwindow.geometry(f"{300}x{300}")
        addwindow.title('追加')
        #変数呼び出し
        global addtitleent
        global addhiraganaent
        global addgenreent
        global addoptionent
        #ボタン類の設定
        addtitlelab = tk.Label(addwindow,text='タイトル')
        addtitlelab.pack()
        addtitleent = tk.Entry(addwindow)
        addtitleent.pack()
        addhiraganalab =tk.Label(addwindow,text='ひらがな名')
        addhiraganalab.pack()
        addhiraganaent = tk.Entry(addwindow)
        addhiraganaent.pack()
        addgenrelab = tk.Label(addwindow,text='ジャンル入力')
        addgenrelab.pack()
        addgenreent = tk.Entry(addwindow)
        addgenreent.pack()
        addoptionlab = tk.Label(addwindow,text='オプション')
        addoptionlab.pack()
        addoptionent = tk.Entry(addwindow)
        addoptionent.pack()
        addbtn = tk.Button(addwindow,text='追加',command=addpro)
        addbtn.pack()
        endbtn = tk.Button(addwindow,text='戻る',command=addwindow.destroy)
        endbtn.pack()
        addwindow.mainloop()
    
    #mainwindow上で終了を選択した時に動作する関数（終了処理）
    def end():
        global endcount
        endcount = endcount+1 
        mainwindow.destroy()
    
    #おまじない
    i = 1
    listresalt = []
    endcount = 0
    resaltcount = 0
    
    #メインウィンドウ生成
    mainwindow = tk.Tk()
    mainwindow.title('HCU-LibSys')
    mainwindow.geometry(f"{300}x{300}")
    sear_btn = tk.Button(mainwindow,text='検索',command=startsearch)
    sear_btn.pack()
    add_btn = tk.Button(mainwindow,text='追加',command=startadd)
    add_btn.pack()
    endbtn = tk.Button(mainwindow,text='終了',command=end)
    endbtn.pack()
    mainwindow.mainloop()
