from tkinter import *
def clear():
    global expression
    global label_show_cal
    result = "0"
    expression = ""
    label_show_cal.set(result)


def press(number):
    global expression
    global label_show_cal
    expression = expression + number
    label_show_cal.set(expression)

def equal():
    try:
        global expression
        global label_show_cal
        result = str(eval(expression))
        label_show_cal
    except:
        result = "Error"
        expression = ""
    label_show_cal.set(result)

m = Tk()
m.title("Beammie calculator")
m.option_add("*font", "consolas 30")
label_show_cal = StringVar()
label_show_cal.set(0)
expression = ""

Label(m, textvariable=label_show_cal, fg="#FF33FF", bg="#FFCCFF", font="consolas 40").grid(row=0 , column=0, columnspan=4, sticky="news")
Button(m, text="clear", command = clear, fg="#0044FD", bg="#B0DEFF", width=("3")).grid(row=1 , column=0, columnspan=3, sticky="news")
Button(m, text="/", command=lambda: press("/"), fg="#0044FD", bg="#B0DEFF", width=("3")).grid(row=1 , column=3, sticky="news")

Button(m, text="1", command=lambda: press("1"), fg="#8470FF", bg="#FEFCDD", width=("3")).grid(row=2 , column=0, sticky="news")
Button(m, text="2", command=lambda: press("2"), fg="#8470FF", bg="#FEFCDD", width=("3")).grid(row=2 , column=1, sticky="news")
Button(m, text="3", command=lambda: press("3"), fg="#8470FF", bg="#FEFCDD", width=("3")).grid(row=2 , column=2, sticky="news")
Button(m, text="*", command=lambda: press("*"), fg="#0044FD", bg="#B0DEFF", width=("3")).grid(row=2 , column=3, sticky="news")

Button(m, text="4", command=lambda: press("4"), fg="#8470FF", bg="#FEFCDD", width=("3")).grid(row=3 , column=0, sticky="news")
Button(m, text="5", command=lambda: press("5"), fg="#8470FF", bg="#FEFCDD", width=("3")).grid(row=3 , column=1, sticky="news")
Button(m, text="6", command=lambda: press("6"), fg="#8470FF", bg="#FEFCDD", width=("3")).grid(row=3 , column=2, sticky="news")
Button(m, text="-", command=lambda: press("-"), fg="#0044FD", bg="#B0DEFF", width=("3")).grid(row=3 , column=3, sticky="news")

Button(m, text="7", command=lambda: press("7"), fg="#8470FF", bg="#FEFCDD", width=("3")).grid(row=4 , column=0, sticky="news")
Button(m, text="8", command=lambda: press("8"), fg="#8470FF", bg="#FEFCDD", width=("3")).grid(row=4 , column=1, sticky="news")
Button(m, text="9", command=lambda: press("9"), fg="#8470FF", bg="#FEFCDD", width=("3")).grid(row=4 , column=2, sticky="news")
Button(m, text="+", command=lambda: press("+"), fg="#0044FD", bg="#B0DEFF", width=("3")).grid(row=4 , column=3, sticky="news")

Button(m, text="0  ", command=lambda: press("0"), fg="#8470FF", bg="#FEFCDD", width=("3")).grid(row=5 , column=0, columnspan=2, sticky="news")
Button(m, text=".", command=lambda: press("."), fg="#8470FF", bg="#FEFCDD", width=("3")).grid(row=5 , column=2, sticky="news")
Button(m, text="=", command=equal, fg="#0044FD", bg="#B0DEFF", width=("3")).grid(row=5 , column=3, sticky="news")

m.mainloop()