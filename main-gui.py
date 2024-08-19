#cording:utf_8
import csv
import tkinter as tk
import pandas as pd

file_path = 'libdata.csv'  # CSVファイルのパスを指定
width = 800 #横解像度の選択
height = 800 #縦解像度の選択

#loop処理用の変数定義
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

        #メインウィンドウの削除
        mainwindow.destroy()
        #検索ウィンドウの生成
        def allwordsearch():  
            searchmodewindow.destroy()      
            def resalt():
                #変数wordentから値を取得
                global wordent
                searchword = wordent.get()
                allwordwindow.destroy()
                if searchword == '':
                    error()
                else:
                    #csvの読み込み
                    with open(file_path,encoding='utf_8') as file:
                        data = [x for x in csv.reader(file)]
                        resaltid = []
                        resalttitle = []
                        #各レコードの呼び出し
                        for i in range(1,len(data)):
                            #リストから検索(部分一致)
                            index = ''.join(data[i])
                            index = index.lower()
                            findcount = index.find(searchword)
                            #find関数の返り値が0より大きいとき
                            if findcount >= 0:
                                global resaltcount
                                findcount = -1
                                resaltid.append(data[i][0])
                                resalttitle.append(data[i][1])
                                resaltcount = 1

                            #find関数の返り値がdefaultのとき(-1)
                            else:
                                i = i + 1
                                continue

                #検索結果がヒットした時に表示するウィンドウを生成
                if resaltcount == 1:
                    resaltcount = 0
                    idoutput = ''
                    titleoutput = ''


                    #検索結果が20以下の時の処理
                    if len(resaltid) <= 20:
                        resaltwindow = tk.Tk()
                        resaltwindow.title('結果')
                        resaltwindow.overrideredirect(True)
                        #結果を変数に格納
                        for i in range(len(resaltid)):
                            idoutput = idoutput + str(resaltid[i]) + '\n'
                        
                        for i in range(len(resalttitle)):
                            titleoutput = titleoutput + str(resalttitle[i]) + '\n'
                        #結果をウィンドウに表示する
                        idresaltlab = tk.Label(resaltwindow,text=idoutput,font=(10))
                        idresaltlab.grid(row=0,column=0)
                        titleresaltlab = tk.Label(resaltwindow,text=titleoutput,font=(10))
                        titleresaltlab.grid(row=0,column=1)
                        endbtn = tk.Button(resaltwindow,text='終了',command=resaltwindow.destroy)
                        endbtn.grid(row=1,column=1)
                        resaltwindow.geometry(f"{width}x{height}")
                        resaltwindow.mainloop()
                    #検索結果が21以上の時の処理
                    else:
                        #ページを保存する変数
                        global page
                        page = 1
                        global resaltendcount
                        resaltendcount = 0
                        #終了処理を行うまでloop
                        while resaltendcount == 0:
                            #次のページへの処理を行う関数
                            def next():
                                resaltwindow.destroy()
                                global page
                                page = page + 1
                            #前のページへの処理を行う関数
                            def pre():
                                resaltwindow.destroy()
                                global page
                                page = page - 1
                            #終了処理を行う関数
                            def resaltend():
                                resaltwindow.destroy()
                                global resaltendcount
                                resaltendcount = 1
                            #検索結果のウィンドウを表示
                            resaltwindow = tk.Tk()
                            resaltwindow.title('結果')
                            resaltwindow.overrideredirect(True)
                            idoutput = ''
                            titleoutput = ''
                            #最後のページ用の処理
                            if page > len(resaltid)//20:
                                for i in range(0+(page-1)*20,len(resaltid)):
                                    titleoutput = titleoutput + str(resalttitle[i]) + '\n'     
                                for i in range(0+(page-1)*20,len(resaltid)):
                                    idoutput = idoutput + str(resaltid[i]) + '\n'
                            #通常時の処理
                            else:
                                for i in range(0+(page-1)*20,20+(page-1)*20):
                                    titleoutput = titleoutput + str(resalttitle[i]) + '\n'     
                                for i in range(0+(page-1)*20,20+(page-1)*20):
                                    idoutput = idoutput + str(resaltid[i]) + '\n'   
                            #検索結果をウィンドウに表示
                            idresaltlab = tk.Label(resaltwindow,text=idoutput,font=(15))
                            idresaltlab.grid(row=0,column=0)
                            titleresaltlab = tk.Label(resaltwindow,text=titleoutput,font=(15))
                            titleresaltlab.grid(row=0,column=1)
                            #ページごとにボタンの配置を変更
                            if page > 1:
                                returnbtn = tk.Button(resaltwindow,text='前のページ',command=pre,font=(15))
                                returnbtn.grid(row=1,column=0)
                            
                            if  page <= len(resaltid)//20:
                                nextbtn = tk.Button(resaltwindow,text='次のページ',command=next,font=(15))
                                nextbtn.grid(row=1,column=2)
                            #終了ボタン
                            endbtn = tk.Button(resaltwindow,text='終了',command=resaltend,font=(15))
                            endbtn.grid(row=2,column=1)

                            resaltwindow.geometry(f"{width}x{height}")
                            resaltwindow.mainloop()    
              
                    
            #全文検索選択時のウィンドウ生成
            allwordwindow = tk.Tk()
            allwordwindow.title('検索')
            allwordwindow.geometry(f"{500}x{500}")
            wordlab = tk.Label(allwordwindow,text='検索ワード入力(英数は半角小文字)',font=(10))
            wordlab.pack()
            global wordent
            wordent = tk.Entry(allwordwindow,width=50,font=('',40))
            wordent.pack(ipady=16)
            searchbtn = tk.Button(allwordwindow,text='検索',font=('Helvetica',20),width=20,height=2,command=resalt)
            searchbtn.pack(anchor='center')
            endbtn = tk.Button(allwordwindow,text='戻る',font=('Helvetica',20),width=20,height=2,command=allwordwindow.destroy)
            endbtn.pack(anchor='center')
            allwordwindow.mainloop()
        #楽器パート選択時の処理を行う関数
        def instsearch():
            searchmodewindow.destroy()
            instlist = []
            #結果を処理する関数
            def resalt():
                #選択した楽器をlistに格納
                if selectfl.get() == 1:
                    instlist.append('fl')
                if selectcl.get() == 1:
                    instlist.append('cl')
                if selectob.get() == 1:
                    instlist.append('ob')
                if selectasax.get() == 1:
                    instlist.append('asax')
                if selecttsax.get() == 1:
                    instlist.append('tsax')
                if selectbsax.get() == 1:
                    instlist.append('bsax')
                if selecttp.get() == 1:
                    instlist.append('tp')
                if selecthr.get() == 1:
                    instlist.append('hr')
                if selecttrb.get() == 1:
                    instlist.append('trb')
                if selecteup.get() == 1:
                    instlist.append('eup')
                if selecttub.get() == 1:
                    instlist.append('tub')
                if selectperc.get() == 1:
                    instlist.append('perc')
                if selectdr.get() == 1:
                    instlist.append('dr')
                if selectmar.get() == 1:
                    instlist.append('mar')
                if selectglo.get() == 1:
                    instlist.append('glo')
                #csvの読み込み
                with open(file_path,'r',encoding='utf-8') as rfile:
                    rdata = [x for x in csv.reader(rfile)]
                    resaltcount = 0
                    resaltid = []
                    resalttitle = []
                    #すべてのデータをloopで照合
                    for i in range(1,len(rdata)):
                        instdata = rdata[i][5]
                        instdata = instdata.split(" ")
                        y = 0
                        #選択したパートと取り出したデータとの一致を確認
                        for x in range(len(instlist)):
                            if instlist[x] in instdata:
                                y = y + 1
                                resaltcount = 1
                            else:
                                break
                            if len(instlist) == y:
                                resaltid.append(rdata[i][0])
                                resalttitle.append(rdata[i][1])
                
                instwindow.destroy()                
                #検索結果がヒットした時の処理
                if resaltcount == 1:
                    #変数定義
                    resaltcount = 0
                    idoutput = ''
                    titleoutput = ''

                    #検索結果が20以下で1ページで表示できる場合
                    if len(resaltid) <= 20:
                        resaltwindow = tk.Tk()
                        resaltwindow.title('結果')
                        resaltwindow.overrideredirect(True)
                        for i in range(len(resaltid)):
                            idoutput = idoutput + str(resaltid[i]) + '\n'
                        
                        for i in range(len(resalttitle)):
                            titleoutput = titleoutput + str(resalttitle[i]) + '\n'
                        idresaltlab = tk.Label(resaltwindow,text=idoutput,font=(10))
                        idresaltlab.grid(row=0,column=0)
                        titleresaltlab = tk.Label(resaltwindow,text=titleoutput,font=(10))
                        titleresaltlab.grid(row=0,column=1)
                        endbtn = tk.Button(resaltwindow,text='終了',command=resaltwindow.destroy)
                        endbtn.grid(row=1,column=1)
                        resaltwindow.geometry(f"{width}x{height}")
                        resaltwindow.mainloop()
                    #検索結果が21以上で複数ページに結果がわたる場合
                    else:
                        #page数を保存する変数
                        global page
                        page = 1
                        global resaltendcount
                        resaltendcount = 0
                        #終了処理をするまでloop
                        while resaltendcount == 0:
                            #次のページを表示する処理を行う関数定義
                            def next():
                                resaltwindow.destroy()
                                global page
                                page = page + 1
                            #前のページを表示する処理を行う関数定義
                            def pre():
                                resaltwindow.destroy()
                                global page
                                page = page - 1
                            #終了処理を行う関数定義
                            def resaltend():
                                resaltwindow.destroy()
                                global resaltendcount
                                resaltendcount = 1
                            #検索結果を表示するウィンドウを生成
                            resaltwindow = tk.Tk()
                            resaltwindow.title('結果')
                            resaltwindow.overrideredirect(True)
                            idoutput = ''
                            titleoutput = ''
                            #最後のページにおけるインデックスエラー回避用プログラム
                            if page > len(resaltid)//20:
                                for i in range(0+(page-1)*20,len(resaltid)):
                                    titleoutput = titleoutput + str(resalttitle[i]) + '\n'     
                                for i in range(0+(page-1)*20,len(resaltid)):
                                    idoutput = idoutput + str(resaltid[i]) + '\n'
                            #通常時の結果表示プログラム
                            else:
                                for i in range(0+(page-1)*20,20+(page-1)*20):
                                    print(resalttitle)
                                    titleoutput = titleoutput + str(resalttitle[i]) + '\n'     
                                for i in range(0+(page-1)*20,20+(page-1)*20):
                                    idoutput = idoutput + str(resaltid[i]) + '\n'   
                            #ウィンドウに結果を表示
                            idresaltlab = tk.Label(resaltwindow,text=idoutput,font=(15))
                            idresaltlab.grid(row=0,column=0)
                            titleresaltlab = tk.Label(resaltwindow,text=titleoutput,font=(15))
                            titleresaltlab.grid(row=0,column=1)
                            #ページごとにボタン変更
                            if page > 1:
                                returnbtn = tk.Button(resaltwindow,text='前のページ',command=pre,font=(15))
                                returnbtn.grid(row=1,column=0)
                            
                            if  page <= len(resaltid)//20:
                                nextbtn = tk.Button(resaltwindow,text='次のページ',command=next,font=(15))
                                nextbtn.grid(row=1,column=2)
                            #終了ボタン
                            endbtn = tk.Button(resaltwindow,text='終了',command=resaltend,font=(15))
                            endbtn.grid(row=2,column=1)

                            resaltwindow.geometry(f"{width}x{height}")
                            resaltwindow.mainloop()  
                #合致する楽器パートが存在しない場合errorを出す分岐
                else:
                    resaltwindow =tk.Tk()
                    resaltwindow.title('検索結果')
                    resaltwindow.geometry(f"{300}x{300}")
                    nulllab = tk.Label(resaltwindow,text='存在しません')
                    nulllab.pack()
                    returnbtn = tk.Button(resaltwindow,text='終了',command=resaltwindow.destroy)
                    returnbtn.pack()
                    resaltwindow.mainloop()
            #楽器パート検索用のウィンドウを生成
            instwindow = tk.Tk()
            instwindow.title('楽器パート検索')
            instwindow.geometry(f"{500}x{500}")
            wordlab = tk.Label(instwindow,text='楽器パート選択',font=(10))
            wordlab.grid(row=0,column=1,columnspan=3)
            #チェックボックスの値を取得する変数群
            selectfl = tk.IntVar()
            selectcl = tk.IntVar()
            selectob = tk.IntVar()
            selectasax = tk.IntVar()
            selecttsax = tk.IntVar()
            selectbsax = tk.IntVar()
            selecttp = tk.IntVar()
            selecthr = tk.IntVar()
            selecttrb = tk.IntVar()
            selecteup = tk.IntVar()
            selecttub = tk.IntVar()
            selectperc = tk.IntVar()
            selectdr = tk.IntVar()
            selectmar = tk.IntVar()
            selectglo = tk.IntVar()
            #各楽器のチェックボックスを生成
            flcb = tk.Checkbutton(instwindow,text='フルート',variable=selectfl)
            flcb.grid(row=1,column=0)
            clcb = tk.Checkbutton(instwindow,text='クラリネット',variable=selectcl)
            clcb.grid(row=1,column=1)
            obcb = tk.Checkbutton(instwindow,text='オーボエ',variable=selectob)
            obcb.grid(row=1,column=2)
            asaxcb = tk.Checkbutton(instwindow,text='アルトサックス',variable=selectasax)
            asaxcb.grid(row=1,column=3)
            tsaxcb = tk.Checkbutton(instwindow,text='テナーサックス',variable=selecttsax)
            tsaxcb.grid(row=1,column=4)
            bsaxcb = tk.Checkbutton(instwindow,text='バリトンサックス',variable=selectbsax)
            bsaxcb.grid(row=2,column=0)
            tpcb = tk.Checkbutton(instwindow,text='トランペット',variable=selecttp)
            tpcb.grid(row=2,column=1)
            hrcb = tk.Checkbutton(instwindow,text='ホルン',variable=selecthr)
            hrcb.grid(row=2,column=2)
            trbcb = tk.Checkbutton(instwindow,text='トロンボーン',variable=selecttrb)
            trbcb.grid(row=2,column=3)
            eupcb = tk.Checkbutton(instwindow,text='ユーフォニアム',variable=selecteup)
            eupcb.grid(row=2,column=4)
            tubcb = tk.Checkbutton(instwindow,text='チューバ',variable=selecttub)
            tubcb.grid(row=3,column=0)
            perccb = tk.Checkbutton(instwindow,text='パーカッション',variable=selectperc)
            perccb.grid(row=3,column=1)
            drcb = tk.Checkbutton(instwindow,text='ドラム',variable=selectdr)
            drcb.grid(row=3,column=2)
            marcb = tk.Checkbutton(instwindow,text='マリンバ',variable=selectmar)
            marcb.grid(row=3,column=3)
            grocb = tk.Checkbutton(instwindow,text='グロッケン',variable=selectglo)
            grocb.grid(row=3,column=4)
            #検索処理を実行するボタン
            searchbtn = tk.Button(instwindow,text='検索',font=('Helvetica',20),width=6,height=1,command=resalt)
            searchbtn.grid(row=4,column=2)
            #戻る処理を実行するボタン
            endbtn = tk.Button(instwindow,text='戻る',font=('Helvatica',20),width=7,height=1,command=instwindow.destroy)
            endbtn.grid(row=5,column=2)
            instwindow.mainloop()

        #id検索の処理を行う関数定義
        def idsearch():
            searchmodewindow.destroy()
            #検索結果の処理を行う関数定義
            def resalt():
                global count
                count = 0
                global ident
                searchid = ident.get()
                idwindow.destroy()
                resaltwindow = tk.Tk()
                resaltwindow.title('検索結果')
                resaltlab = tk.Label(resaltwindow,text='検索結果',font=(20))
                resaltlab.pack()
                #csvの読み込み
                with open('libdata.csv',encoding='utf8') as file:
                    data = [x for x in csv.reader(file)]
                    #入力したidとデータにあるidを照合
                    for i in range(len(data)):
                        index = str(data[i][0])                      
                        if index == searchid:
                            idresaltlab = tk.Label(resaltwindow,text=str(data[i][0])+str(data[i][1]),font=(10))
                            idresaltlab.pack()
                            count = 1
                            break #合うidがあればloop処理を終了
                        else:
                            continue #合うidが見つかるまでloop
                #見つからなかったときerrorlabを表示
                if count == 0:
                    errorlab = tk.Label(resaltwindow,text='存在しません',font=(10))
                    errorlab.pack()
                #その他のUI
                returnbtn = tk.Button(resaltwindow,text='戻る',command=resaltwindow.destroy,font=(10))
                returnbtn.pack()
                resaltwindow.geometry(f"{500}x{500}")
                resaltwindow.mainloop()
            #id検索用のウィンドウを生成
            idwindow = tk.Tk()
            idwindow.title('id検索')
            idwindow.geometry(f"{500}x{500}")
            idlab = tk.Label(idwindow,text='検索したいIDを入力してください(算用数字　整数)',font=(10))
            idlab.pack()
            global ident
            ident = tk.Entry(idwindow,width=50,font=('',40))
            ident.pack(ipady=16)
            searchbtn = tk.Button(idwindow,text='検索',font=('Helvetica',20),width=20,height=2,command=resalt)
            searchbtn.pack(anchor='center')
            endbtn = tk.Button(idwindow,text='戻る',font=('Helvetica',20),width=20,height=2,command=idwindow.destroy)
            endbtn.pack(anchor='center')
            idwindow.mainloop()
        #検索設定のウィンドウを生成
        searchmodewindow = tk.Tk()
        searchmodewindow.title('検索設定')
        searchmodewindow.geometry(f"{500}x{500}")
        allwordbtn = tk.Button(searchmodewindow,text='全文検索',font=('Helvetica',20),width=20,height=2,command=allwordsearch,)
        allwordbtn.pack(expand=True)
        instbtn = tk.Button(searchmodewindow,text='楽器パート検索',font=('Helvetica',20),width=20,height=2,command=instsearch)
        instbtn.pack(expand=True)
        idsearchbtn = tk.Button(searchmodewindow,text='id検索',font=('Helvetica',20),width=20,height=2,command=idsearch)
        idsearchbtn.pack(expand=True)
        returnbtn = tk.Button(searchmodewindow,text='戻る',font=('Helvetica',20),width=20,height=2,command=searchmodewindow.destroy)
        returnbtn.pack(expand=True)
        searchmodewindow.mainloop()
    #追加関係の処理を行う関数を定義
    def startadd():
        #startadd下で追加の処理を行う時に動作する関数
        mainwindow.destroy()
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
            instlist = []
            if selectfl.get() == 1:
                instlist.append('fl')
            if selectcl.get() == 1:
                instlist.append('cl')
            if selectob.get() == 1:
                instlist.append('ob')
            if selectasax.get() == 1:
                instlist.append('asax')
            if selecttsax.get() == 1:
                instlist.append('tsax')
            if selectbsax.get() == 1:
                instlist.append('bsax')
            if selecttp.get() == 1:
                instlist.append('tp')
            if selecthr.get() == 1:
                instlist.append('hr')
            if selecttrb.get() == 1:
                instlist.append('trb')
            if selecteup.get() == 1:
                instlist.append('eup')
            if selecttub.get() == 1:
                instlist.append('tub')
            if selectperc.get() == 1:
                instlist.append('perc')
            if selectdr.get() == 1:
                instlist.append('dr')
            if selectmar.get() == 1:
                instlist.append('mar')
            if selectglo.get() == 1:
                instlist.append('glo')
            instruments = ' '.join(instlist)
            #csvファイルをappendで呼び出し
            with open(file_path,'a',encoding='utf-8',newline='') as afile:
                #csv書き込みのデータ準備
                with open(file_path,'r',encoding='utf=8',newline='') as rfile:
                    rdata = [x for x in csv.reader(rfile)]
                number = str(int(rdata[len(rdata)-1][0]) + 1)
                writer = csv.writer(afile)
                data = [number,title,hiragana,genre,option,instruments]
                #csv書き込み
                writer.writerow(data)
            #処理の正常終了を伝えるウィンドウの生成
            compwindow = tk.Tk()
            compwindow.geometry(f"{300}x{300}")
            compwindow.title('出力')
            successlab = tk.Label(compwindow,text='正常に処理を受け付けました')
            successlab.pack()
            endbtn = tk.Button(compwindow,text='戻る',command=compwindow.destroy)
            endbtn.pack()

        #addwindowの生成
        addwindow = tk.Tk()
        addwindow.geometry(f"{500}x{500}")
        addwindow.title('追加')
        #変数呼び出し
        global addtitleent
        global addhiraganaent
        global addgenreent
        global addoptionent
        #ボタン類の設定
        addlab = tk.Label(addwindow,text='追加設定',font=('',20))
        addlab.grid(row=0,column=1,columnspan=3)
        addtitlelab = tk.Label(addwindow,text='タイトル',font=(10))
        addtitlelab.grid(row=1,column=1,columnspan=3)
        addtitleent = tk.Entry(addwindow,font=(10))
        addtitleent.grid(row=2,column=1,columnspan=3)
        addhiraganalab =tk.Label(addwindow,text='ひらがな名',font=(10))
        addhiraganalab.grid(row=3,column=1,columnspan=3)
        addhiraganaent = tk.Entry(addwindow,font=(10))
        addhiraganaent.grid(row=4,column=1,columnspan=3)
        addgenrelab = tk.Label(addwindow,text='ジャンル入力',font=(10))
        addgenrelab.grid(row=5,column=1,columnspan=3)
        addgenreent = tk.Entry(addwindow,font=(10))
        addgenreent.grid(row=6,column=1,columnspan=3)
        addoptionlab = tk.Label(addwindow,text='オプション',font=(10))
        addoptionlab.grid(row=7,column=1,columnspan=3)
        addoptionent = tk.Entry(addwindow,font=(10))
        addoptionent.grid(row=8,column=1,columnspan=3)
        addinstlab = tk.Label(addwindow,text='楽器パート選択',font=(10))
        addinstlab.grid(row=9,column=1,columnspan=3)  
        #選択した楽器を取得する変数
        selectfl = tk.IntVar()
        selectcl = tk.IntVar()
        selectob = tk.IntVar()
        selectasax = tk.IntVar()
        selecttsax = tk.IntVar()
        selectbsax = tk.IntVar()
        selecttp = tk.IntVar()
        selecthr = tk.IntVar()
        selecttrb = tk.IntVar()
        selecteup = tk.IntVar()
        selecttub = tk.IntVar()
        selectperc = tk.IntVar()
        selectdr = tk.IntVar()
        selectmar = tk.IntVar()
        selectglo = tk.IntVar()
        #楽器の選択用チェックボックス
        flcb = tk.Checkbutton(addwindow,text='フルート',variable=selectfl)
        flcb.grid(row=10,column=0)
        clcb = tk.Checkbutton(addwindow,text='クラリネット',variable=selectcl)
        clcb.grid(row=10,column=1)
        obcb = tk.Checkbutton(addwindow,text='オーボエ',variable=selectob)
        obcb.grid(row=10,column=2)
        asaxcb = tk.Checkbutton(addwindow,text='アルトサックス',variable=selectasax)
        asaxcb.grid(row=10,column=3)
        tsaxcb = tk.Checkbutton(addwindow,text='テナーサックス',variable=selecttsax)
        tsaxcb.grid(row=10,column=4)
        bsaxcb = tk.Checkbutton(addwindow,text='バリトンサックス',variable=selectbsax)
        bsaxcb.grid(row=11,column=0)
        tpcb = tk.Checkbutton(addwindow,text='トランペット',variable=selecttp)
        tpcb.grid(row=11,column=1)
        hrcb = tk.Checkbutton(addwindow,text='ホルン',variable=selecthr)
        hrcb.grid(row=11,column=2)
        trbcb = tk.Checkbutton(addwindow,text='トロンボーン',variable=selecttrb)
        trbcb.grid(row=11,column=3)
        eupcb = tk.Checkbutton(addwindow,text='ユーフォニアム',variable=selecteup)
        eupcb.grid(row=11,column=4)
        tubcb = tk.Checkbutton(addwindow,text='チューバ',variable=selecttub)
        tubcb.grid(row=12,column=0)
        perccb = tk.Checkbutton(addwindow,text='パーカッション',variable=selectperc)
        perccb.grid(row=12,column=1)
        drcb = tk.Checkbutton(addwindow,text='ドラム',variable=selectdr)
        drcb.grid(row=12,column=2)
        marcb = tk.Checkbutton(addwindow,text='マリンバ',variable=selectmar)
        marcb.grid(row=12,column=3)
        grocb = tk.Checkbutton(addwindow,text='グロッケン',variable=selectglo)
        grocb.grid(row=12,column=4)
        #その他のUI
        addbtn = tk.Button(addwindow,text='追加',command=addpro,font=(10))
        addbtn.grid(row=13,column=1,columnspan=3)
        endbtn = tk.Button(addwindow,text='戻る',command=addwindow.destroy,font=(10))
        endbtn.grid(row=14,column=1,columnspan=3)
        addwindow.mainloop()
    #削除処理の関数
    def remove():
        mainwindow.destroy()
        #確認するウィンドウ用の関数
        def check():                
            global removeident
            removeid = removeident.get()
            removewindow.destroy()
            #削除用の処理
            def removepro():      
                checkwindow.destroy()          
                with open(file_path,'r',encoding='utf-8') as rfile:
                    rdata = [x for x in csv.reader(rfile)]
                    for i in range(len(rdata)):
                        if rdata[i][0] == removeid:
                            removetitle = rdata[i][1]
                            break
                #csvの読み込み
                df = pd.read_csv(file_path)
                df = df.drop(i-1,axis=0)
                df.to_csv(file_path,index=False)
                #ウィンドウを生成
                resaltwindow = tk.Tk()
                resaltwindow.title('処理結果')
                resaltwindow.geometry(f"{300}x{300}")
                resaltlab = tk.Label(resaltwindow,text='以下の楽譜データを削除しました')
                resaltlab.grid(row=0,column=1)
                idlab = tk.Label(resaltwindow,text=removeid)
                idlab.grid(row=1,column=0)
                titlelab = tk.Label(resaltwindow,text=removetitle)
                titlelab.grid(row=1,column=1,columnspan=2)
                returnbtn = tk.Button(resaltwindow,text='終了',command=resaltwindow.destroy)
                returnbtn.grid(row=2,column=1)
                resaltwindow.mainloop()
            #確認用ウィンドウを生成
            checkwindow = tk.Tk()
            checkwindow.title('確認')
            checklab = tk.Label(checkwindow,text='削除してもいいですか')
            checklab.pack()
            applybtn = tk.Button(checkwindow,text='はい',command=removepro)
            applybtn.pack()
            ignorebtn = tk.Button(checkwindow,text='いいえ',command=checkwindow.destroy)
            ignorebtn.pack()
            checkwindow.mainloop()
        #削除設定用のウィンドウを生成
        removewindow = tk.Tk()
        removewindow.title('削除設定')
        removewindow.geometry(f"{500}x{500}")
        removelab = tk.Label(removewindow,text='削除設定',font=('',20))
        removelab.pack(ipady=5)
        removeidlab = tk.Label(removewindow,text='削除したい楽譜のidを入力してください',font=(10))
        removeidlab.pack()
        global removeident
        removeident = tk.Entry(removewindow,font=(10))
        removeident.pack()
        removebtn = tk.Button(removewindow,text='削除',command=check,font=(10))
        removebtn.pack()
        endbtn = tk.Button(removewindow,text='戻る',command=removewindow.destroy,font=(10))
        endbtn.pack(side='bottom',pady=10)        
    
    #mainwindow上で終了を選択した時に動作する関数（終了処理）
    def end():
        global endcount
        endcount = endcount+1 
        mainwindow.destroy()
    
    #変数定義
    i = 1
    listresalt = []
    endcount = 0
    resaltcount = 0
    
    #メインウィンドウ生成
    mainwindow = tk.Tk()
    mainwindow.title('Feelic')
    iconfile = 'feelic.ico'
    mainwindow.iconbitmap(default=iconfile)
    mainwindow.geometry(f"{500}x{500}")
    mainlab = tk.Label(mainwindow,text='Feelic',font=('times',40,'italic'))
    mainlab.pack(side='top',pady=20)
    sear_btn = tk.Button(mainwindow,text='検索',font=('Helvetica',20),command=startsearch,width=20,height=2)
    sear_btn.pack(expand=True)
    add_btn = tk.Button(mainwindow,text='追加',font=('Helvetica',20),command=startadd,width=20,height=2)
    add_btn.pack(expand=True)
    rem_btn = tk.Button(mainwindow,text=('削除'),font=('courier',20),command=remove,width=20,height=2)
    rem_btn.pack(expand=True)
    endbtn = tk.Button(mainwindow,text='終了',font=('courier',20),command=end,width=20,height=2)
    endbtn.pack(expand=True)
    rightslab = tk.Label(text='© 2024 Uwajima East Brass Band')
    rightslab.pack(side='bottom')
    mainwindow.mainloop()