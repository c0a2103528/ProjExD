import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global mx, my, cx, cy
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
        tkm.showinfo("Goal", "Congraturarions!!")
    else:
        root.after(100, main_proc)

root = tk.Tk()
root.title("迷えるこうかとん")
root.geometry("1500x900")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

canvas = tk.Canvas(root, width=1500, height=900, bg = "black")
canvas.pack()

maze = maze_maker.make_maze(15, 9)
maze_maker.show_maze(canvas, maze)

mx = 1; my = 1
cx = mx*100 + 50; cy = my*100 + 50
tori = tk.PhotoImage(file="ex03/fig/2.png")
IoC = canvas.create_image(cx, cy, image=tori, tag="tori")
key=""
main_proc()
root.mainloop()