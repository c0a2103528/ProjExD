import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker
from random import randint as rad
import datetime

# 再プレイの確認
def check_replay(rep):
    if rep == True:             #再度プレイするとき
        canvas.delete("tori")   #画像を消し、
        setup()                 #再度初期設定を行う
    else:
        exit()                  #再度プレイしないとき、ウィンドウを閉じる

# 時間による壁と道の変化
# 未実装
"""
def move_wall():
    global maze, times, rx, ry
    for i in range(times):
        if maze[rx[i]][ry[i]] == 0:
            maze[rx[i]][ry[i]] = 1
        else:
            maze[rx[i]][ry[i]] = 0
    rt = rad(1, 2)
    maze_maker.show_maze(canvas, maze)
    canvas.delete("tori")
    canvas.create_image(cx, cy, image=tori, tag="tori")
    root.after(3000*rt, move_wall)
"""

# ゴールまでにかかる時間のカウントダウン
def count_down():
    global tmr, jid
    label["text"] = tmr
    tmr = tmr-1                 #時間を1秒ずつ減少させる
    if maze[mx][my] == 3:       #ゴールについたとき終了する
        return
    elif tmr < 0:               #時間切れになった時
        root.after_cancel(jid)  #再度プレイするか確認
        canvas.delete("tori")
        tori = tk.PhotoImage(file="ex03/fig/8.png")
        canvas.create_image(cx, cy, image=tori, tag="tori")  #泣いている画像に変更
        replay = tkm.askyesno("Time Up", "Game Over...\nTry again?")
        check_replay(replay)
    else:
        jid = root.after(1000, count_down)

# ゴール時のラベルの設定
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
    global mx, my, cx, cy, key, maze, tori, tmr, jid, rx, ry, times
    tmr = 10
    jid = None
    label["fg"] = "black"           #ラベルの色を変更する
    mx = 1; my = 1                  #画像の初期位置の設定
    cx = mx*100+50; cy = my*100+50  #画像の初期座標の設定
    key = ""
    maze = maze_maker.make_maze(15, 9) #迷路の作成
    maze_maker.show_maze(canvas, maze) #迷路の表示
    tori = tk.PhotoImage(file="ex03/fig/9.png") #画像の読み込み
    canvas.create_image(cx, cy, image=tori, tag="tori") #画像の表示
    count_down()      #カウントの開始

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
    #スタート以外で行き止まりに当たった時
    if not(mx == 1 and (my == 1)):
        if ((maze[mx+1][my] == 1 and maze[mx-1][my] == 1) and (maze[mx][my+1] == 1 or maze[mx][my-1] == 1)) or ((maze[mx][my+1] == 1 and maze[mx][my-1] == 1) and (maze[mx+1][my] == 1 or maze[mx-1][my] == 1)):
            canvas.delete("tori")
            tori = tk.PhotoImage(file="ex03/fig/8.png")
            canvas.create_image(cx, cy, image=tori, tag="tori") #泣いている画像に変更する
    if maze[mx][my] == 3:   #ゴールした時
        if jid is not None: 
            root.after_cancel(jid) #カウントを止める
        goal()                      #ゴールメッセージの表示
        canvas.delete("tori")
        tori = tk.PhotoImage(file="ex03/fig/6.png")
        canvas.create_image(cx, cy, image=tori, tag="tori") #画像を変更する
        replay = tkm.askyesno("Goal", "Play again?")  #再度プレイするか確認
        check_replay(replay)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")      #ウィンドウのタイトルを設定
    root.geometry("1500x900")           #ウィンドウサイズの設定
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    label = tk.Label(root, font=("", 80))   #カウントを表示するラベルの設定
    label.pack()

    canvas = tk.Canvas(root, width=1500, height=1200, bg = "black") #キャンバスの設定
    canvas.pack()

    tmr = 0                #グルーバル変数の設定
    jid = None
    mx = 0; my = 0
    cx = 0; cy = 0
    key = ""; tori = ""
    maze = []
    setup()                #初期値の設定
    main_proc()            #リアルタイム処理関数の呼び出し
    root.mainloop()