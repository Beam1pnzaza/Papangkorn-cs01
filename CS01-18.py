from tkinter import*

root = Tk()
root.title("First GUI")
myText = Label(text="My name is",fg="blue",font=20).grid(row=0,column=1)
myText = Label(text="Papangkorn",fg="green",font=20).grid(row=1,column=2)
myText = Label(text="Nirawatsuwan",fg="red",font=20).grid(row=2,column=3)
root.geometry("300x300")
root.mainloop()