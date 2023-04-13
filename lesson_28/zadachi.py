import tkinter as tk
def show_message(event):
    # приём значения из Entry
    message = ent.get()  #  получить значение с поля ввода
    ent.delete(0, 'end')  # очистка поля для ввода полностью
    lab['text'] = message
    print(message)

    # приём значение из Text
    message2 = txt.get(2.4, 'end')  # отсчёт от 1.0
    txt.delete(0.0, 'end')  # очистка Text
    print(message2)


window = tk.Tk()
window.geometry("300x400")
lab = tk.Label(window, text="ликриски",
               font="Verdana 18",
               bg="indigo", fg="pink2",
               width=50)  # надпись
lab.pack()
ent = tk.Entry(bd=7, width=10)  # поле для ввода
ent.pack()

btn = tk.Button()
btn.pack()
btn['text'] = "Отправить"
btn['font'] = ("Verdana 18", 15)
btn['fg'] = "pink2"
btn['bg'] = "purple3"
btn.bind("<Button-1>", show_message)

txt = tk.Text(window, width=20, height=5)  #многострочный ввод
txt.pack()

window.mainloop()