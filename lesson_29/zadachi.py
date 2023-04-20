import tkinter as tk
root = tk.Tk()
# def vyzov():
#     if btn['state'] == "disabled":
#         btn['state'] = "normal"
#         btn['text'] = "Активен!"
#     else:
#         btn['state'] = "disabled"
#         btn['text'] = "Не активен!"



# cb = tk.Checkbutton(root, text="Активировать",
#                     command=vyzov)
# cb.pack()
# # cb.select()

# btn = tk.Button(root, text="Не активен!",
#                 state=tk.DISABLED)
# btn.pack()

def bold():
    if cb1_val.get():  # если cb1_val = True
        lab['font'] += " bold"
    else:
        lab['font'] = lab['font'].replace(" bold", "")

lab = tk.Label(root,
               text="я текст. а кто ты?",
               font="Arial 17")
lab.pack()
cb1_val = tk.BooleanVar()
cb1 = tk.Checkbutton(root,
                     text="Жирный",
                     variable=cb1_val,
                     onvalue=True,
                     offvalue=False,
                     command=bold)
cb1.pack()
def italic():
    if cb2_val.get():
        lab['font'] += " italic"
    else:
        lab['font'] = lab['font'].replace(" italic", "")
cb2_val = tk.BooleanVar()
cb2 = tk.Checkbutton(root,
                     text="Курсив",
                     variable=cb2_val,
                     onvalue=True,
                     offvalue=False,
                     command=italic)
cb2.pack()

def overstrike():
    if cb3_val.get():
        lab['font'] += " overstrike"
    else:
        lab['font'] = lab['font'].replace(" overstrike", "")
cb3_val = tk.BooleanVar()
cb3 = tk.Checkbutton(root,
                     text="Зачёркнутый",
                     variable=cb3_val,
                     onvalue=True,
                     offvalue=False,
                     command=overstrike)
cb3.pack()

def underline():
    if cb4_val.get():
        lab['font'] += " underline"
    else:
        lab['font'] = lab['font'].replace(" underline", "")
cb4_val = tk.BooleanVar()
cb4 = tk.Checkbutton(root,
                     text="Подчёркнутый",
                     variable=cb4_val,
                     onvalue=True,
                     offvalue=False,
                     command=underline)
cb4.pack()








root.mainloop()