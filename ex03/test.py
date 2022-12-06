import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def timer():
    global tmr 

    if tmr < 0:
        root.after(2000, lambda:root.destroy())
        tkm.showinfo("時間切れ", "残念でした")
    if mx == 13 and my == 7:
        return
    else:
        tmr = tmr - 0.1
        label["text"] = int(tmr)
        #tmr = root.after(1000, timer())


def main_proc():
    global cx, cy, mx, my
    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    if maze_lst [mx][my] == 1:#移動先が壁だったら
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1
    cx, cy = mx*100+50, my*100+50
    canvas.coords("こうかとん",cx, cy)

    if mx == 13 and my == 7:
        root.after(2000, lambda:root.destroy())
        tkm.showinfo("ゴール", "おめでとう")
        exit()
    timer()
    root.after(100, main_proc)

if __name__ == "__main__":

    root = tk.Tk()
    label = tk.Label(root, text="-", font=("", 80))
    label.pack()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_lst)
    tmr = 10
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    #root.after(1000, timer())
    koukaton = tk.PhotoImage(file="ex03/fig/8.png")
    canvas.create_rectangle(100, 100, 200, 200, fill="red")
    canvas.create_rectangle(1300, 700, 1400, 800, fill="red")
    canvas.create_image(cx, cy, image=koukaton, tag="こうかとん")
    
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()