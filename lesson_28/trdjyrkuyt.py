import tkinter as tk
def show_message(e):
    message = ent.get()
    ent.delete(0, 'end')  # очистка поля для ввода полностью
    print(message)

    message2 = txt.get(0.0, 'end')  # отсчёт от 1.0
    txt.delete(0.0, 'end')  # очистка Text
    print(message2)


window = tk.Tk()
window.geometry("300x400")
window.configure(background='wheat')

lab = tk.Label(window, text="Ваш адрес:",
               font=("Arial Black", 11),
               bg="wheat")
lab.pack()

ent = tk.Entry(bd=10, width=20)
ent.pack()
lab = tk.Label(window, text="Комментарии:",
               font=("Arial Black", 11),
               bg="wheat")
lab.pack()
txt = tk.Text(window, width=20, height=5)
txt.pack()
btn = tk.Button()
btn.pack()
btn['text'] = "Отправить"
btn['font'] = ("Arial Black", 11)
btn['bg'] = "lightblue"
btn.bind("<Button-1>", show_message)


window.mainloop()