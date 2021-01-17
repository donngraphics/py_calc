import tkinter as tk

root = tk.Tk()

# e = tk.Entry(width=50, bg='white', borderwidth=5)
# e.pack()
# e.get()
# e.insert(0, 'Type your name here')

root.wm_title('TK Calculator')


answer_window = tk.Entry(width=35, bg='white', borderwidth=5)

answer_window.grid(row=0, column=0, columnspan=3, sticky='nsew')


def button_click(number):
    #answer_window.delete(0, tk.END)
    current = answer_window.get()
    answer_window.delete(0, tk.END)
    answer_window.insert(0, str(current) + str(number))


def button_clear():
    answer_window.delete(0, tk.END)


def addition():
    first_number = answer_window.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    answer_window.delete(0, tk.END)


def subtraction():
    first_number = answer_window.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    answer_window.delete(0, tk.END)


def multiply():
    first_number = answer_window.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    answer_window.delete(0, tk.END)


def divide():
    first_number = answer_window.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    answer_window.delete(0, tk.END)


def button_equal():
    second_number = answer_window.get()
    answer_window.delete(0, tk.END)

    if math == 'addition':
        answer_window.insert(0, f_num + int(second_number))
    elif math == 'subtraction':
        answer_window.insert(0, f_num - int(second_number))
    elif math == 'multiplication':
        answer_window.insert(0, f_num * int(second_number))
    else:
        answer_window.insert(0, f_num / int(second_number))


zero = tk.Button(text='0', padx=10,
                 command=lambda: button_click(0), borderwidth=1)
zero.grid(row=4, column=0, sticky='nsew')

one = tk.Button(text='1', padx=10,
                command=lambda: button_click(1), borderwidth=1)
one.grid(row=3, column=0, sticky='nsew')

two = tk.Button(text='2', padx=10,
                command=lambda: button_click(2), borderwidth=1)
two.grid(row=3, column=1, sticky='nsew')

three = tk.Button(text='3', padx=10,
                  command=lambda: button_click(3), borderwidth=1)
three.grid(row=3, column=2, sticky='nsew')

four = tk.Button(text='4', padx=10,
                 command=lambda: button_click(4), borderwidth=1)
four.grid(row=2, column=0, sticky='nsew')

five = tk.Button(text='5', padx=10,
                 command=lambda: button_click(5), borderwidth=1)
five.grid(row=2, column=1, sticky='nsew')

six = tk.Button(text='6', padx=10,
                command=lambda: button_click(6), borderwidth=1)
six.grid(row=2, column=2, sticky='nsew')

seven = tk.Button(text='7', padx=10,
                  command=lambda: button_click(7), borderwidth=1)
seven.grid(row=1, column=0, sticky='nsew')

eight = tk.Button(text='8', padx=10,
                  command=lambda: button_click(8), borderwidth=1)
eight.grid(row=1, column=1, sticky='nsew')

nine = tk.Button(text='9', padx=10,
                 command=lambda: button_click(9), borderwidth=1)
nine.grid(row=1, column=2, sticky='nsew')

button_add = tk.Button(text='+', padx=10,
                       command=addition, borderwidth=1)
button_add.grid(row=5, column=0, sticky='nsew')

button_subtract = tk.Button(text='-', padx=10,
                            command=subtraction, borderwidth=1)
button_subtract.grid(row=6, column=0, sticky='nsew')

button_multiply = tk.Button(text='*', padx=10,
                            command=multiply, borderwidth=1)
button_multiply.grid(row=6, column=1, sticky='nsew')

button_divide = tk.Button(text='/', padx=10,
                          command=divide, borderwidth=1)
button_divide.grid(row=6, column=2, sticky='nsew')

clear_button = tk.Button(text='Clear', padx=50,
                         command=button_clear, bg='gold', fg='black')

clear_button.grid(row=4, column=1, columnspan=2, sticky='nsew')


equal_button = tk.Button(text='=', padx=50,
                         command=button_equal, bg='green', fg='white')

equal_button.grid(row=5, column=1, columnspan=2, sticky='nsew')


root.mainloop()
