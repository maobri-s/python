from tkinter import *
root = Tk()
root.geometry("550x550")

c = Canvas(root, width=500, height=500, bg="lightgreen")
c.pack(anchor=CENTER, expand=True)

# =============== Текст ===============
# c.create_text(0, 0,
#               text="ликриски",
#               font="Arial 23",
#               fill="indigo",
#               anchor=NW)

# =============== Прямоугольник ===============
# c.create_rectangle(10, 10,
#                    200, 150,
#                    fill="indigo",
#                    width=10,
#                    outline="purple")

# # =============== Многоугольник ===============
# # c.create_polygon(10, 10,
#                  150, 150,
#                  10, 150)

# =============== Окружность ===============
# c.create_oval(10, 10,
#                   150, 150)

# =============== arc ===============
# c.create_oval(10, 10,
#               150, 150,
#               fill="lightblue")
# c.create_arc(10, 10,
#              150, 150,
#              fill="darkred",
#              start=30,
#              extent=-45)
# c.create_arc(10, 10,
#              150, 150,
#              fill="indigo",
#              start=90,
#              extent=135,
#              style=CHORD)
# c.create_arc(10, 10,
#              150, 150,
#              outline="purple",
#              start=110,
#              extent=135,
#              style=ARC,
#              width=10)

# =============== Линии ===============
# c.create_line(10, 10,
#               150, 150,
#               arrow=BOTH,
#               arrowshape=(50, 50, 50),
#               width=20)

# ==============================
c.create_rectangle(10, 10,
                   200, 150,
                   fill="indigo",
                   width=10,
                   outline="purple",
                   dash="-..",
                   activefill="darkred",
                   activewidth=50)

root.mainloop()