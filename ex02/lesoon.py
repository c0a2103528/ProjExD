import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}]ボタンが押されました")

root = tk.Tk()
root.title("おためしか")
root.geometry("500x200")

label = tk.Label(root,
                text = "らべるを書いてみた件",
                font = ("", 20)
                )
label.pack()

image = tk.PhotoImage(file="tori.PNG")

canvas = tk.Canvas(width = 80, height = 120)

canvas.create_image(30, 40, image=image)
canvas.pack()


entry = tk.Entry(width = 30)
entry.insert(tk.END, "fugapiyo")
entry.pack()

#button = tk.Button(root, text = "押すな")
#button = tk.Button(root, text = "押すな", command=button_click)
button = tk.Button(root, text="押すな")
button.bind("<1>", button_click)
button.pack()


root.mainloop()
