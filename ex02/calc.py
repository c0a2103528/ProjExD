
import tkinter as tk
import tkinter.messagebox as tkm

"""
def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"{txt}のボタンが押されました")
"""
def  button_click(event):
    btn = event.widget
    txt = btn["text"]
    entry.insert(tk.END, txt)

def eq_button_click(event):
    res = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(justify = tk.RIGHT, width = 10, font = ("", 40))
entry.get()
entry.grid(column=0, row=0, columnspan=3)

cr_list = [[0,3],[2,2],[1,2],[0,2],[2,1],[1,1],[0,1],[2,0],[1,0],[0,0]]
for i in cr_list:
    i[1] += 1
for i in range(10):
    mk_button = "button"+str(i)+"="+"tk.Button(root, text = "+str(i)+", width = 4, height = 2, font = ('', 30))"
    exec(mk_button)
    cl_button = "button"+str(i)+".bind('<1>', button_click)"
    exec(cl_button)
    gr_button = "button"+str(i)+f".grid(column=cr_list[{i}][0], row=cr_list[{i}][1])"
    exec(gr_button)
button_pl = tk.Button(root, text="+", width = 4, height = 2, font=("",30))
button_pl.bind("<1>", button_click)
button_pl.grid(column=1, row=4)
button_eq = tk.Button(root, text="=", width = 4, height = 2, font=("",30))
button_eq.bind("<1>", eq_button_click)
button_eq.grid(column=2, row=4)



root.mainloop()
