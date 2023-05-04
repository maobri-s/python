
from tkinter import *
root = Tk()
root.geometry("1000x1000")
c = Canvas(root, width=900, height=200, bg="lightgreen")
c.pack(anchor=CENTER, expand=True)


# def likris():
#     global timer
#     c.delete("all")
#     timer += 1
#     c.create_text(300, 250,
#                   text=timer,
#                   font="Arial 25")
#     c.create_image(295, 245,
#                    image=img)
#     c.after(1000, likris)
#     if timer == 16:
#         root.destroy()
#
#
# img = PhotoImage(file="watch.png").subsample(2,2)
#
#
#
#
#
#
# timer = 0
#
# c.create_text(300, 250,
#               text=timer,
#               font="Arial 25")
# c.create_image(300, 250,
#                image=img)
#
# likris()

# ПЛАНЫ НА ЖИЗНЬ

c.create_text(10, 10,
              anchor=NW,
              text="школа",
              font="Arial 20")
c.create_line(150, 25,
              250, 25, arrow=LAST)

c.create_text(300, 10,
              anchor=NW,
              text="туда-сюда",
              font="Arial 20")
c.create_line(500, 25,
              600, 25, arrow=LAST)
c.create_text(650, 10,
              anchor=NW,
              text="успех 100%",
              font="Arial 20")




root.mainloop()