import tkinter as tk

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, key
    if key == "Up":
        cy -= 20
    elif key == "Down":
        cy += 20
    elif key == "Left":
        cx -= 20
    elif key == "Right":
        cx += 20
    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)

root = tk.Tk()
root.title("迷えるこうかとん")
root.geometry("1500x900")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

canvas = tk.Canvas(root, width=1500, height=900, bg = "black")
canvas.pack()
cx = 300; cy = 400
tori = tk.PhotoImage(file="ex03/fig/6.png")
canvas.create_image(cx, cy, image=tori, tag="tori")
key=""
main_proc()
root.mainloop()