import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker

# ゴールまでにかかる時間のカウントアップ
def count_up():
    global tmr, jid
    label["text"] = tmr
    tmr = tmr+1
    if maze[mx][my] == 3:
        return
    else:
        jid = root.after(1000, count_up)

def goal():
    label["text"] = "Congratulations!!"
    label["fg"] = "red"

# キーを押したときの処理 
def key_down(event):
    global key
    key = event.keysym

# キーを離したときの処理
def key_up(event):
    global key
    key = ""

# 初期設定
def setup():
    global mx, my, cx, cy, key, maze, tori, tmr, jid
    tmr = 0
    jid = None
    mx = 1; my = 1                  # 画像の初期位置の設定
    cx = mx*100+50; cy = my*100+50  # 画像の初期座標の設定
    key = ""
    maze = maze_maker.make_maze(15, 9) #迷路の作成
    maze_maker.show_maze(canvas, maze) #迷路の表示
    tori = tk.PhotoImage(file="ex03/fig/2.png") #画像の読み込み
    canvas.create_image(cx, cy, image=tori, tag="tori") #画像の表示
    count_up()      #カウントの開始

# リアルタイム処理
def main_proc():
    global mx, my, cx, cy, maze, tori
    bx = mx; by = my
    if key == "Up":         #↑キーを入力したときの処理
        my -= 1
    elif key == "Down":     #↓キーを入力したときの処理
        my += 1
    elif key == "Left":     #←キーを入力したときの処理
        mx -= 1
        canvas.delete("tori")
        tori = tk.PhotoImage(file="ex03/fig/5.png")
        canvas.create_image(cx, cy, image=tori, tag="tori") #左向き画像への変更
    elif key == "Right":    #→キーを入力したときの処理
        mx += 1
        canvas.delete("tori")
        tori = tk.PhotoImage(file="ex03/fig/2.png")
        canvas.create_image(cx, cy, image=tori, tag="tori") #右向き画像への変更

    if maze[mx][my] == 1:   #移動先が壁の場合
        mx = bx; my = by    #同じ場所にとどまる
    else:
        cx = mx*100 + 50    #壁以外の場合
        cy = my*100 + 50    #座標を更新する
    canvas.coords("tori", cx, cy) #座標に基づき、画像の位置を更新する

    if maze[mx][my] == 3:   #ゴールした時
        if jid is not None: 
            root.after_cancel(jid) #カウントを止める
        goal()                      #ゴールメッセージの表示
        canvas.delete("tori")
        tori = tk.PhotoImage(file="ex03/fig/6.png")
        canvas.create_image(cx, cy, image=tori, tag="tori") #画像を変更する
        replay = tkm.askyesno("Goal", "Play again?")  #再度プレイするか確認
        if replay == True:          #再度プレイするとき
            canvas.delete("tori")   #画像を消し、
            setup()                 #再度初期設定を行う
        else:
            exit()                  #再度プレイしないとき、ウィンドウを閉じる
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    root.geometry("1500x900")
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    label = tk.Label(root, font=("", 80))
    label.pack()

    canvas = tk.Canvas(root, width=1500, height=1200, bg = "black")
    canvas.pack()

    tmr = 0
    jid = None
    mx = 0; my = 0
    cx = 0; cy = 0
    key = ""; tori = ""
    maze = []
    setup()

    main_proc()
    root.mainloop()