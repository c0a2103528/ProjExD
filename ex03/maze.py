import tkinter as tk
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
    if key == "Up":
        my -= 1
    elif key == "Down":
        my += 1
    elif key == "Left":
        mx -= 1
    elif key == "Right":
        mx += 1
    if maze[mx][my] == 0:
        cx = mx*100 + 50
        cy = my*100 + 50
    else:
        mx = bx; my = by
    canvas.coords("tori", cx, cy)
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
tori = tk.PhotoImage(file="ex03/fig/6.png")
canvas.create_image(cx, cy, image=tori, tag="tori")
key=""
main_proc()
root.mainloop()