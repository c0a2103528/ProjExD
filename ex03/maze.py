import tkinter as tk

root = tk.Tk()
root.title("迷えるこうかとん")
root.geometry("1500x900")

canvas = tk.Canvas(root, width=1500, height=900, bg = "black")

cx = 300
cy = 400
tori = tk.PhotoImage(file="ex03/fig/6.png")
canvas.create_image(cx, cy, image=tori, tag="tori")
canvas.pack()

key=""

root.mainloop()