
import tkinter as tk
import tkinter.messagebox as tkm
import math

# 数字、四則演算、mod、2乗ボタンをクリックしたときの動作
def button_click(event):
    btn = event.widget
    txt = btn["text"]
    n = len(entry.get())
    if n <= 0:
        if (txt == "×") or (txt == "÷"):
            return
        elif (txt == "+") or (txt == "-"):
            entry.insert(tk.END, txt)
            return
    if (txt == "+") or (txt == "-") or (txt == "×") or (txt == "÷"):
        chars = entry.get()
        ch = chars[-1]
        if ((ch == "+") or (ch == "×") or (ch == "÷") or (ch == "-")):
            entry.delete(n-1, tk.END)
    entry.insert(tk.END, txt)

# バックスペースボタンをクリックしたときの動作
def bs_button_click(event):
    siki_len = len(entry.get())
    entry.delete(siki_len-1, tk.END)

# 平方根ボタンをクリックしたときの動作
def root_button_click(event):
    chars = entry.get()
    if len(chars) == 0:
        return
    ch = chars[-1]
    if ((ch == "+") or (ch == "×") or (ch == "÷") or (ch == "-")):
        return
    num = eval(entry.get())
    res = math.sqrt(num)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

# binボタンをクリックしたときの動作
def by_button_click(event):
    chars = entry.get()
    if len(chars) == 0:
        return
    ch = chars[-1]
    if ((ch == "+") or (ch == "×") or (ch == "÷") or (ch == "-")):
        return
    num = eval(entry.get())
    res = bin(num)[2:]
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

# %ボタンをクリックしたときの動作
def per_button_click(event):
    chars = entry.get()
    if len(chars) == 0:
        return
    num = eval(entry.get())
    num *= 100
    res = str(num) + "%"
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

# 消去ボタンをクリックしたときの動作
def del_button_click(event):
    entry.delete(0, tk.END)

# =ボタンをクリックしたときの動作
def eq_button_click(event):
    chars = entry.get()
    if len(chars) == 0:
        return
    ch = chars[-1]
    if ((ch == "+") or (ch == "×") or (ch == "÷") or (ch == "-")):
        return
    s = chars.replace("×", "*")     #掛け算の処理
    sw = s.replace("÷", "/")        #割り算の処理
    swm = sw.replace("mod", "%")    #modの処理
    swm2 = swm.replace("^2", "**2") #2乗の処理
    res = eval(swm2)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

# +/-ボタンをクリックしたときの動作
def pm_button_click(event):
    chars = entry.get()
    len_ch = len(chars)
    if len_ch == 0:
        return
    ch = chars[-1]
    if ((ch == "+") or (ch == "×") or (ch == "÷") or (ch == "-")):
        return
    if eval(chars) == 0:
        return
    i = len_ch - 1
    while not ((chars[i] == "+") or (chars[i] == "×") or (chars[i] == "÷") or (chars[i] == "-") or i <= 0):
        i -= 1
    num = chars[i:]
    if num[0] == "×" or num[0] == "÷":
        ans = int(num[1:]) * -1
    else:
        ans = -1 * int(num)
    if ans > 0:
        res = chars[:i] + "+" +str(ans)
    else:
        if (chars[i] == "×") or (chars[i] == "÷"):
            res = chars[:i+1] + "(" + str(ans) + ")"
        else:
            res = chars[:i] + str(ans)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

# ボタン上にカーソルがある時のボタンの色の設定
def enter_bg(event):
    event.widget['bg'] = "#87cefa"

# ボタン上にカーソルがない時のボタンの色の設定
def leave_bg(event):
    event.widget['bg'] = 'SystemButtonFace'

# 文字サイズの設定
f_size = 20
w = 5
h = 2

root = tk.Tk()
root.geometry("380x510")

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
    e_button = "button"+str(i)+".bind('<Enter>', enter_bg)"
    l_button = "button"+str(i)+".bind('<Leave>', leave_bg)"
    exec(e_button)
    exec(l_button)

# =ボタンの作成
button_eq = tk.Button(root, text="=", width = w, height = h, font=("", f_size))
button_eq.bind("<1>", eq_button_click)
button_eq.grid(column=3, row=6)
button_eq.bind('<Enter>', enter_bg)
button_eq.bind('<Leave>', leave_bg)

# 四則演算, 小数点ボタンの作成
keys = ["+", "-", "×", "÷", "."]
k_cr_list = [[3,5],[3,4],[3,3],[3,2],[2,6]]
for i in range(5):
    button = tk.Button(root, text=keys[i], width = w, height = h, font=("", f_size))
    button.bind("<1>", button_click)
    button.grid(column=k_cr_list[i][0], row=k_cr_list[i][1])
    button.bind('<Enter>', enter_bg)
    button.bind('<Leave>', leave_bg)


# バックスペースボタンの作成
button_bs = tk.Button(root, text="Del", width = w, height = h, font=("", f_size))
button_bs.bind("<1>", bs_button_click)
button_bs.grid(column=3, row=1)
button_bs.bind('<Enter>', enter_bg)
button_bs.bind('<Leave>', leave_bg)

# 消去ボタンの作成
button_del = tk.Button(root, text="C", width = w, height = h, font=("", f_size))
button_del.bind("<1>", del_button_click)
button_del.grid(column=2, row=1)
button_bs.bind('<Enter>', enter_bg)
button_bs.bind('<Leave>', leave_bg)

# %ボタンの作成
button_per = tk.Button(root, text="%", width = w, height = h, font=("", f_size))
button_per.bind("<1>", per_button_click)
button_per.grid(column=0, row=2)
button_per.bind('<Enter>', enter_bg)
button_per.bind('<Leave>', leave_bg)

# 2乗ボタンの作成
button_sqr = tk.Button(root, text="^2", width = w, height = h, font=("", f_size))
button_sqr.bind("<1>", button_click)
button_sqr.grid(column=1, row=2)
button_sqr.bind('<Enter>', enter_bg)
button_sqr.bind('<Leave>', leave_bg)

# 平方根ボタンの作成
button_root = tk.Button(root, text="√", width = w, height = h, font=("", f_size))
button_root.bind("<1>", root_button_click)
button_root.grid(column=2, row=2)
button_root.bind('<Enter>', enter_bg)
button_root.bind('<Leave>', leave_bg)

# binボタンの作成
button_root = tk.Button(root, text="bin", width = w, height = h, font=("", f_size))
button_root.bind("<1>", by_button_click)
button_root.grid(column=1, row=1)
button_root.bind('<Enter>', enter_bg)
button_root.bind('<Leave>', leave_bg)

# modボタンの作成
button_root = tk.Button(root, text="mod", width = w, height = h, font=("", f_size))
button_root.bind("<1>", button_click)
button_root.grid(column=0, row=1)
button_root.bind('<Enter>', enter_bg)
button_root.bind('<Leave>', leave_bg)

# +/-ボタンの作成
button_root = tk.Button(root, text="+/-", width = w, height = h, font=("", f_size))
button_root.bind("<1>", pm_button_click)
button_root.grid(column=0, row=6)
button_root.bind('<Enter>', enter_bg)
button_root.bind('<Leave>', leave_bg)

root.mainloop()