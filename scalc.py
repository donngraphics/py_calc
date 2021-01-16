import tkinter as tk

root = tk.Tk()

# e = tk.Entry(width=50, bg='white', borderwidth=5)
# e.pack()
# e.get()
# e.insert(0, 'Type your name here')

root.wm_title('Addition Calculator')


def addition():
    hello = 'Hello ' + e.get()
    myLabel = tk.Label(text=hello)
    # myLabel.pack()


def button_add():
    return


answer_window = tk.Entry(width=35, bg='white', borderwidth=5)

answer_window.grid(row=0, column=0, columnspan=3, sticky='nsew')

zero = tk.Button(text='0', padx=10,
                 command=button_add, borderwidth=1)
zero.grid(row=4, column=0, sticky='nsew')

one = tk.Button(text='1', padx=10,
                command=button_add, borderwidth=1)
one.grid(row=3, column=0, sticky='nsew')

two = tk.Button(text='2', padx=10,
                command=button_add, borderwidth=1)
two.grid(row=3, column=1, sticky='nsew')

three = tk.Button(text='3', padx=10,
                  command=button_add, borderwidth=1)
three.grid(row=3, column=2, sticky='nsew')

four = tk.Button(text='4', padx=10,
                 command=button_add, borderwidth=1)
four.grid(row=2, column=0, sticky='nsew')

five = tk.Button(text='5', padx=10,
                 command=button_add, borderwidth=1)
five.grid(row=2, column=1, sticky='nsew')

six = tk.Button(text='6', padx=10,
                command=button_add, borderwidth=1)
six.grid(row=2, column=2, sticky='nsew')

seven = tk.Button(text='7', padx=10,
                  command=button_add, borderwidth=1)
seven.grid(row=1, column=0, sticky='nsew')

eight = tk.Button(text='8', padx=10,
                  command=button_add, borderwidth=1)
eight.grid(row=1, column=1, sticky='nsew')

nine = tk.Button(text='9', padx=10,
                 command=button_add, borderwidth=1)
nine.grid(row=1, column=2, sticky='nsew')

plus = tk.Button(text='+', padx=10,
                 command=addition, borderwidth=1)
plus.grid(row=5, column=0, sticky='nsew')


clear_button = tk.Button(text='Clear', padx=50,
                         command=addition, bg='gold', fg='black')

clear_button.grid(row=4, column=1, columnspan=2, sticky='nsew')


equal_button = tk.Button(text='=', padx=50,
                         command=addition, bg='gold', fg='black')

equal_button.grid(row=5, column=1, columnspan=2, sticky='nsew')

root.mainloop()
