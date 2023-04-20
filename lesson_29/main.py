import tkinter as tk  # импорт


root = tk.Tk()  # создать окно

root.geometry("400x400")

#=========CHECKBUTTON=========
# def check():
#     print(val_cb.get())
# val_cb = tk.BooleanVar()  # переменная для хранения True/False
# cb = tk.Checkbutton(root, text="Подписка",
#                     font=15,
#                     bg="purple",
#                     variable=val_cb,  # хранение значения в
#                     onvalue=True,
#                     offvalue=False,
#                     command=check)  # создали переключатель
# cb.pack()

#=========RADIOBUTTON=========
# def get_rb():
#     print(val_rb.get())
# val_rb = tk.IntVar()
# rb1 = tk.Radiobutton(root, text="бархатные тяги",
#                      variable=val_rb,
#                      value=1,
#                      command=get_rb)
# rb1.pack()
#
# rb2 = tk.Radiobutton(root, text="подкрадуля",
#                      variable=val_rb,
#                      value=2,
#                      command=get_rb)
# rb2.pack()
#
# rb3 = tk.Radiobutton(root, text="подкракадуля",
#                      variable=val_rb,
#                      value=3,
#                      command=get_rb)
# rb3.pack()

#=========SCALE=========
# def get_skala(lalala):
#     print(skala.get())  # значение либо так
#     print(lalala)  # либо так
#
# skala = tk.Scale(root,
#                  from_=500,  # откудова
#                  to=1000,  # докудова
#                  width=50,  # толщина полоски
#                  length=300,  # длина полоски
#                  orient=tk.HORIZONTAL,  # ориентация(север)
#                  tickinterval=100,  # подпись
#                  resolution=50,  # шаг
#                  command=get_skala)
# skala.pack()

#=========PICTURES=========
# img = tk.PhotoImage(file="b.png")  # объект изображения
# # img = img.subsample(3, 3)  # уменьшение
# # img = img.zoom(2, 2)  # увеличение
# lab = tk.Label(root, image=img)
# lab.pack()

#=========СОСТОЯНИЯ=========
# def switch():
#     if btn1['state'] == "disabled":  # если неактивна кнопка
#         btn1['state'] = "normal"
#     else:
#         btn1['state'] = "disabled"
# btn1 = tk.Button(root, text="активируй меня",
#                  state=tk.DISABLED,
#                  fg="pink",
#                  disabledforeground="lightblue3",
#                  width=30)
# btn1.pack(pady=10, ipady=5)
# btn2 = tk.Button(root, text="активатор2023_без_вирусов",
#                  command=switch)
# btn2.pack()
#=========ЗНАЧЕНИЕ ПО УМОЛЧАНИЮ В ENTRY=========
# ent = tk.Entry(root)
# ent.pack()
# ent.insert(tk.END, "перекус таксиста ...")


root.mainloop()