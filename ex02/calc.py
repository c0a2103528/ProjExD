
import tkinter as tk
import tkinter.messagebox as tkm
import math

# ボタンをクリックしたときの動作
def button_click(event):
    btn = event.widget
    txt = btn["text"]
    if ((txt == "+") or (txt == "×") or (txt == "÷") or (txt == "-")):
        n = len(entry.get())
        if n <= 0:
            return
        else:
            chars = entry.get()
            ch = chars[-1]
            if ((ch == "+") or (ch == "×") or (ch == "÷") or (ch == "-")):
                entry.delete(n-1, tk.END)
    entry.insert(tk.END, txt)

def bs_button_click(event):
    siki_len = len(entry.get())
    entry.delete(siki_len-1, tk.END)

def sqr_button_click(event):
    num = eval(entry.get())
    res =  num**2
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

def root_button_click(event):
    num = eval(entry.get())
    res = math.sqrt(num)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

def per_button_click(event):
    num = eval(entry.get())
    num *= 100
    res = str(num) + "%"
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

def del_button_click(event):
    entry.delete(0, tk.END)

def eq_button_click(event):
    chars = entry.get()
    ch = chars[-1]
    if ((ch == "+") or (ch == "×") or (ch == "÷") or (ch == "-")):
        return
    s = chars.replace("×", "*")
    sw = s.replace("÷", "/")
    res = eval(sw)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

f_size = 20
w = 6
h = 3

root = tk.Tk()
root.geometry("382x600")

entry = tk.Entry(justify = tk.RIGHT, width = 12, font = ("", 40))
entry.grid(column=0, row=0, columnspan=4)

# 数字(0~9)ボタンの作成
cr_list = [[1,6],[0,5],[1,5],[2,5],[0,4],[1,4],[2,4],[0,3],[1,3],[2,3]]
for i in range(10):
    mk_button = "button"+str(i)+"="+"tk.Button(root, text = "+str(i)+", width = w, height = h, font = ('', f_size))"
    exec(mk_button)
    cl_button = "button"+str(i)+".bind('<1>', button_click)"
    exec(cl_button)
    gr_button = "button"+str(i)+f".grid(column=cr_list[{i}][0], row=cr_list[{i}][1])"
    exec(gr_button)

# +ボタンの作成
button_pl = tk.Button(root, text="+", width = w, height = h, font=("", f_size))
button_pl.bind("<1>", button_click)
button_pl.grid(column=3, row=5)

# =ボタンの作成
button_eq = tk.Button(root, text="=", width = w, height = h, font=("", f_size))
button_eq.bind("<1>", eq_button_click)
button_eq.grid(column=3, row=6)

# -ボタンの作成
button_mn = tk.Button(root, text="-", width = w, height = h, font=("", f_size))
button_mn.bind("<1>", button_click)
button_mn.grid(column=3, row=4)

# ×ボタンの作成
button_kake = tk.Button(root, text="×", width = w, height = h, font=("", f_size))
button_kake.bind("<1>", button_click)
button_kake.grid(column=3, row=3)

# ÷ボタンの作成
button_waru = tk.Button(root, text="÷", width = w, height = h, font=("", f_size))
button_waru.bind("<1>", button_click)
button_waru.grid(column=3, row=2)

# バックスペースボタンの作成
button_bs = tk.Button(root, text="Del", width = w, height = h, font=("", f_size))
button_bs.bind("<1>", bs_button_click)
button_bs.grid(column=3, row=1)

# 消去ボタンの作成
button_del = tk.Button(root, text="C", width = w, height = h, font=("", f_size))
button_del.bind("<1>", del_button_click)
button_del.grid(column=2, row=1)

# 小数点ボタンの作成
button_dot = tk.Button(root, text=".", width = w, height = h, font=("", f_size))
button_dot.bind("<1>", button_click)
button_dot.grid(column=2, row=6)

# %ボタンの作成
button_per = tk.Button(root, text="%", width = w, height = h, font=("", f_size))
button_per.bind("<1>", per_button_click)
button_per.grid(column=0, row=1)

# %ボタンの作成
button_per = tk.Button(root, text="%", width = w, height = h, font=("", f_size))
button_per.bind("<1>", per_button_click)
button_per.grid(column=0, row=1)

# 2乗ボタンの作成
button_sqr = tk.Button(root, text="x^2", width = w, height = h, font=("", f_size))
button_sqr.bind("<1>", sqr_button_click)
button_sqr.grid(column=1, row=2)

# 平方根ボタンの作成
button_root = tk.Button(root, text="√x", width = w, height = h, font=("", f_size))
button_root.bind("<1>", root_button_click)
button_root.grid(column=2, row=2)

root.mainloop()
