#cording:utf_8
import csv
import tkinter as tk
# CSVファイルを開く

file_path = 'sample.csv'  # CSVファイルのパスを指定してください
with open(file_path, encoding='utf_8') as f:
    reader = csv.reader(f)
    lines = f.readlines()

i = 1
listresalt = []
def resalt():
    global wordent
    searchword = wordent.get()
    print(searchword)
    makewindow.destroy()
    with open(file_path,encoding='utf_8') as f:
        reader = csv.reader(f)
        for row in reader:
            index = ','.join(row)
            count = index.find(searchword)
            global i
            if count >= 0:
                count = -1
                listresalt.append(row)
                continue
            if i == len(lines):
                    errorwindow = tk.Tk()
                    errorwindow.title('error')
                    errorwindow.geometry(f"{200}x{200}")
                    errorlab = tk.Label(errorwindow,text='存在しません')
                    errorlab.pack()
                    errorwindow.mainloop()
                    break
            else:
                i = i + 1
                continue
    resaltwindow = tk.Tk()
    resaltwindow.title('結果')
    resaltlab = tk.Label(resaltwindow,text=listresalt)
    resaltlab.pack()
    resaltwindow.geometry(f"{200}x{200}")
    resaltwindow.mainloop()


makewindow = tk.Tk()
makewindow.title('検索')
makewindow.geometry(f"{200}x{200}")
wordlab = tk.Label(makewindow,text='検索ワード入力')
wordlab.pack()

wordent = tk.Entry(makewindow,width=50)
wordent.pack()
searchbtn = tk.Button(makewindow,text='検索',command=resalt)
searchbtn.pack()

makewindow.mainloop()
