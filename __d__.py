from tkinter import *

root = Tk()
root.title("ВОВА.com")
root.geometry("1500x809")
root.resizable(width=False, height=False)


def outText():
    label.configure(text="HELLO WORLD")


btn1 = Button(root, command=outText, text="кнопка", background="#008000", foreground="#fff", pady="2", font="12",
              width=30)
btn1.place(x=30, y=50)

label = Label(root)
label.place(x=700, y=20)

root.mainloop()