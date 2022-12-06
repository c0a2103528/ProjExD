import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def setup():
    global mx, my, cx, cy, key
    mx = 1; my = 1
    cx = mx*100+50; cy = my*100+50
    key = ""

def main_proc():
    global mx, my, cx, cy, maze, tori
    bx = mx; by = my
    if key == "Up":         #↑キーを入力したときの処理
        my -= 1
    elif key == "Down":     #↓キーを入力したときの処理
        my += 1
    elif key == "Left":     #←キーを入力したときの処理
        mx -= 1
    elif key == "Right":    #→キーを入力したときの処理
        mx += 1
    if maze[mx][my] == 1:
        mx = bx; my = by
    else:
        cx = mx*100 + 50
        cy = my*100 + 50
    canvas.coords("tori", cx, cy)
    if maze[mx][my] == 3:
        replay = tkm.askyesno("Goal", "Congraturarions!!\nDo you want to Play again?")  #ゴール判定
        if replay == True:
            setup()
        else:
            exit()
    root.after(100, main_proc)

root = tk.Tk()
root.title("迷えるこうかとん")
root.geometry("1500x900")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

canvas = tk.Canvas(root, width=1500, height=900, bg = "black")
canvas.pack()

mx = 0; my = 0
cx = 0; cy = 0
key = ""
setup()
maze = maze_maker.make_maze(15, 9)
maze_maker.show_maze(canvas, maze)
tori = tk.PhotoImage(file="ex03/fig/2.png")
canvas.create_image(cx, cy, image=tori, tag="tori")
main_proc()
root.mainloop()