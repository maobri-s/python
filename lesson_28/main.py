import tkinter as tk

def baget(event):
    print("я круассан")

window = tk.Tk()  # инициализация, создание В НАЧАЛЕ
window.geometry("500x400")  # размеры окна
window.title("Моё первое окошечко с:")

btn = tk.Button(window, text="Моя первая кнопочка с:")  # создание кнопки
btn.pack()  # размещение кнопки
btn['text'] = "Ы"  # изменение конфигурации
btn['font'] = ("Arial Black",
               15,
               "bold",  # жирный
               "underline", #подчёркнуто
               "italic",  # курсив
                "overstrike"  # зачёркнуто
                )

# btn['background'] = "purple3"
btn['bg'] = "purple3"
# btn['foreground'] = "green1"
btn['fg'] = "green1"
btn['width'] = 10  # width - ширина
btn['height'] = 3  # height - высота
# btn['borderwidth'] = 10  # borderwidth - ширина рамки
btn['bd'] = 10
# btn['command'] = baget  # нажатие на кнопку левой кнопкой мыши
btn.bind("<Double-Button-1>", baget)





window.mainloop()