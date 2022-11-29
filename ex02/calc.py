
import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"{txt}のボタンが押されました")

root = tk.Tk()
root.geometry("300x500")

cr_list = [[0,3],[2,2],[1,2],[0,2],[2,1],[1,1],[0,1],[2,0],[1,0],[0,0]]
for i in range(10):
    mk_button = "button" + str(i) + "=" + "tk.Button(root, text = " + str(i) + ", width = 4, height = 2, font = ('', 30))"
    exec(mk_button)
    cl_button = "button" + str(i) + ".bind('<1>', button_click)"
    exec(cl_button)
    gr_button = "button" + str(i) + f".grid(column=cr_list[{i}][0], row=cr_list[{i}][1])"
    exec(gr_button)

root.mainloop()
