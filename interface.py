import socket, time, threading


from tkinter import *
from polinom import Polinom
from complex import Complex


shutdown = False
join = False




window = Tk()
polinom = None
window.title("Polinom")

window.geometry('700x200')

#lbl = Label(window, text="Hello")
def clicked_polinom_button():
    global polinom
    c1, c2, c3 = complex(coefficient1.get()), complex(coefficient2.get()), complex(coefficient3.get())
    coeffs = [Complex(i.real, i.imag) for i in (c1,c2,c3)]
    polinom = Polinom(*coeffs)
    polinom_output.configure(text = polinom)


def clicked_roots_button():

    global polinom
    #c1, c2, c3 = (coefficient1.get()), (coefficient2.get()), (coefficient3.get())
    roots.configure(text=polinom.roots())
def clicked_value_button():
    global polinom
    val = complex(value_form.get())
    val = Complex(val.real, val.imag)
    print(val)
    value.configure(text=polinom.value(val))
#lbl.grid(column=0, row=0)

coefficient1 = Entry(window, width=10)
coefficient1.grid(column=0, row=0)
coefficient2 = Entry(window, width=10)
coefficient2.grid(column=2, row=0)
coefficient3 = Entry(window, width=10)
coefficient3.grid(column=3, row=0)
polinom_output = Label(window, text='here is your polinom', width=45)
polinom_output.grid(column=3, row=3)
polinom_button = Button(window, text='show polinom', command = clicked_polinom_button)
polinom_button.grid(column=0,row=3)

roots_button = Button(window, text='roots', command=clicked_roots_button)
roots_button.grid(row = 5, column = 0)
roots = Label(window, text='roots', width=45)
roots.grid(row = 5, column=3)


value_button = Button(window, text='value', command=clicked_value_button)
value_button.grid(row = 7, column = 0)


value = Label(window, text='value', width=25)
value_form = Entry(window, width = 10)
value_form.grid(column = 2, row=7)
value.grid(row = 7, column=3)

window.mainloop()